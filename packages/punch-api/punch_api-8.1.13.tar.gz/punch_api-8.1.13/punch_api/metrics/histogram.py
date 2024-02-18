import prometheus_client


class Histogram:
    child: prometheus_client.Histogram

    def __init__(self, h: prometheus_client.Histogram, labels: list[str]) -> None:
        if len(labels) != 0:
            self.child = h.labels(*labels)
        else:
            self.child = h

    def observe(self, o: float) -> None:
        self.child.observe(o)

    def time(self) -> prometheus_client.context_managers.Timer:
        return self.child.time()
