#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The punch prometheus context makes it easier to correctly name the metrics,
in particular the usage of the namespace and subsystem, and the
right use of labels.

Using the plain prometheus client API, each metric user must
go through a child metric to publish values with the right labels.

Besides, the punch API uses a light facade API which makes it
future-proof to accommodate other metric back ends.
"""

__author__ = "RT"

import threading
from copy import copy

import prometheus_client
import punch_api.metrics.counter
import punch_api.metrics.gauge
import punch_api.metrics.histogram
from prometheus_client.exposition import pushadd_to_gateway, basic_auth_handler
from prometheus_client.registry import CollectorRegistry
from punch_api.logger import print_warning


class MetricContext:
    # Singleton
    _instance = None

    __subsystem: str
    __namespace: str
    __labels: dict[str, str]

    __registered_metrics: dict[
        str, punch_api.metrics.counter.Counter | punch_api.metrics.gauge.Gauge | punch_api.metrics.histogram.Histogram]

    def __new__(cls, *args, **kwargs):
        """
        Singleton class to hold the metrics context.
        """
        if not cls._instance:
            cls._instance = super(MetricContext, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, namespace: str = None, subsystem: str = None, labels: dict[str, str] = None,
                 pushgateway_url: str = None, push_metric_interval_seconds=None, credentials: str = None) -> None:

        # Only initialize once
        if self._initialized:
            return

        self.__subsystem = "" if subsystem is None else subsystem
        self.__namespace = "" if namespace is None else namespace
        self.__labels = {} if labels is None else labels

        self.__registered_metrics = {}

        self._pushgateway_url = pushgateway_url
        self._push_metric_interval_seconds = None if not push_metric_interval_seconds else int(
            push_metric_interval_seconds)
        self._registry = CollectorRegistry()

        self._credentials = credentials

        # run the push metrics thread
        self._stop_event = threading.Event()
        self.start_push_gateway()

        self._initialized = True

    def get_new_subsystem_context(self, subsystem: str) -> "MetricContext":
        """
        Derive a context from a parent to add some specific tags for a subsystem.
        :param subsystem: the subsystem, typically netty, kafka, elasticsearch
        :return: a new context instance
        """
        metric_context = copy(self)
        metric_context.__subsystem = subsystem
        return metric_context

    def add_tag(self, key: str, value: str) -> None:
        """
        Update the tag if it exists, otherwise add it
        """
        self.__labels[key] = value

    def __get_labels(self) -> list[str]:
        return list(self.__labels.keys())

    def __get_label_values(self) -> list[str]:
        return list(self.__labels.values())

    def start(self, scrape: str, port: int) -> "MetricContext":
        """
        Start the metrics server
        """
        if scrape and scrape.upper() == "TRUE":
            if 0 < int(port) < 65536:
                prometheus_client.start_http_server(int(port))
            else:
                raise ValueError(
                    f"Start metrics server failed : bad port value: got {port}, expected value between 1 and 65535."
                )
        return self

    def get_counter(self, name: str, doc: str, unit: str,
                    labels: dict[str, str] = {}) -> punch_api.metrics.counter.Counter:
        """
        Create a counter metric
        """
        return punch_api.metrics.counter.Counter(
            self.__get_create_registered_counter(name, doc, unit, list(labels.keys())),
            self.__get_label_values() + list(labels.values()),
        )

    def get_histogram(self, name: str, doc: str, unit: str,
                      labels: dict[str, str] = {}) -> punch_api.metrics.histogram.Histogram:
        """
        Create a histogram metric
        """
        return punch_api.metrics.histogram.Histogram(
            self.__get_create_registered_histogram(name, doc, unit, list(labels.keys())),
            self.__get_label_values() + list(labels.values()),
        )

    def get_gauge(self, name: str, doc: str, unit: str, labels: dict[str, str] = {}) -> punch_api.metrics.gauge.Gauge:
        """
        Create a counter metric
        """
        return punch_api.metrics.gauge.Gauge(
            self.__get_create_registered_gauge(name, doc, unit, list(labels.keys())),
            self.__get_label_values() + list(labels.values()),
        )

    def __get_create_registered_counter(self, name: str, doc: str, unit: str,
                                        labels: list[str]) -> prometheus_client.Counter:
        if name not in self.__registered_metrics:
            self.__registered_metrics[name] = prometheus_client.Counter(
                name=name,
                subsystem=self.__subsystem,
                namespace=self.__namespace,
                unit=unit,
                labelnames=self.__get_labels() + labels,
                documentation=doc,
                registry=self._registry
            )
        return self.__registered_metrics[name]

    def __get_create_registered_gauge(self, name: str, doc: str, unit: str,
                                      labels: list[str]) -> prometheus_client.Gauge:
        if name not in self.__registered_metrics:
            self.__registered_metrics[name] = prometheus_client.Gauge(
                name=name,
                subsystem=self.__subsystem,
                namespace=self.__namespace,
                unit=unit,
                labelnames=self.__get_labels() + labels,
                documentation=doc,
                registry=self._registry
            )
        return self.__registered_metrics[name]

    def __get_create_registered_histogram(self, name: str, doc: str, unit: str,
                                          labels: list[str]) -> prometheus_client.Histogram:
        if name not in self.__registered_metrics:
            self.__registered_metrics[name] = prometheus_client.Histogram(
                name=name,
                subsystem=self.__subsystem,
                namespace=self.__namespace,
                unit=unit,
                labelnames=self.__get_labels() + labels,
                documentation=doc,
                registry=self._registry
            )
        return self.__registered_metrics[name]

    def __get_metric_name(self, name: str, unit: str) -> str:
        sb: str = self.__namespace
        if len(self.__subsystem) > 0:
            sb += "_" + self.__subsystem
        sb += "_" + name
        if len(unit) > 0:
            sb += "_" + unit
        return sb

    def push_metrics(self):
        """
        Push the metrics to the pushgateway POST method.
        """
        if self._pushgateway_url:
            self._registry.collect()
            # Push metrics if registry have metrics
            if self._registry._collector_to_names:
                try:
                    if self._credentials:
                        credentials = self._credentials.split(":")
                        pushadd_to_gateway(self._pushgateway_url, job=self.__labels.get("app_name", None),
                                           registry=self._registry,
                                           handler=basic_auth_handler(credentials[0], credentials[1]))
                    else:
                        pushadd_to_gateway(self._pushgateway_url, job=self.__labels.get("app_name", None),
                                           registry=self._registry)
                except Exception as e:
                    print_warning(f"Pushing metrics to pushgateway failed : {e}")
        # else:
        # print_warning("Pushing metrics to pushgateway failed : no pushgateway url provided.")

    def start_push_gateway(self):
        """
        Start the push metrics scheduler.
        """
        if self._push_metric_interval_seconds and self._pushgateway_url and not self._stop_event.is_set():
            threading.Timer(self._push_metric_interval_seconds, self.start_push_gateway).start()
            self.push_metrics()

    def stop_push_gateway(self):
        """
        Stop the push metrics scheduler.
        """
        self._stop_event.set()
