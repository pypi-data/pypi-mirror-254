from horsetalk import RaceDistance as HorsetalkRaceDistance

from .likeness import LikenessMixin, discount


class RaceDistance(LikenessMixin, HorsetalkRaceDistance):
    _likeness_functions = {
        "furlong": lambda a, b: discount((float(abs(a - b) / min(a, b)) / 1.5) ** 0.5)
    }

    def __getattr__(self, name):
        if name == "like":
            return self.like

        return super().__getattr__(name)
