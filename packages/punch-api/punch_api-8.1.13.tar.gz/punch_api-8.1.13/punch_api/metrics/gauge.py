import prometheus_client


class Gauge:
    child: prometheus_client.Gauge

    def __init__(self, g: prometheus_client.Gauge, labels: list[str]) -> None:
        if len(labels) != 0:
            self.child = g.labels(*labels)
        else:
            self.child = g

    def inc(self, value=1) -> None:
        self.child.inc(value)

    def dec(self, value=1) -> None:
        self.child.dec(-value)

    def set(self, value: float) -> None:
        self.child.set(value)
