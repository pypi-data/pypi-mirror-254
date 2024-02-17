import threading


class ColorCycle:
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls) -> "ColorCycle":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ColorCycle, cls).__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if not self._initialized:
            self.index = 0
            self.colors = [
                "red",
                "green",
                "blue",
                "yellow",
                "magenta",
                "cyan",
                "orange",
                "purple",
                "pink",
                "lime",
                "olive",
                "navy",
                "gold",
                "orchid",
                "coral",
                "salmon",
                "chocolate",
                "steel_blue",
                "seagreen",
                "sky_blue",
            ]
        self._initialized = True

    def current_color(self) -> str:
        with self._lock:
            return self.colors[self.index]

    def next_color(self) -> str:
        with self._lock:
            if self.index >= len(self.colors):
                self.index = 0

            color = self.colors[self.index]
            self.index += 1

        return color

    def reset(self) -> None:
        with self._lock:
            self.index = 0
