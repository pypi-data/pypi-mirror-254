import prometheus_client


class Counter:
    child: prometheus_client.Counter

    def __init__(self, c: prometheus_client.Counter, labels: list[str]) -> None:
        if len(labels) != 0:
            self.child = c.labels(*labels)
        else:
            self.child = c

    def inc(self, value=1) -> None:
        self.child.inc(value)
