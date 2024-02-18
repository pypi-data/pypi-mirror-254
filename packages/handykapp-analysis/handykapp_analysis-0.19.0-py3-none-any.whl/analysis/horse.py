from horsetalk import HorseAge, RaceDesignation

from .race_conditions import RaceConditions
from .race_performance import RacePerformance


class Horse:
    def __init__(
        self,
        name: str,
        country: str | None = None,
        age: HorseAge | None = None,
        race_career: dict[RaceConditions, RacePerformance] = {},
    ):
        self.name = name
        self.country = country
        self.age = age
        self.race_career = race_career

    @property
    def race_career(self):
        return self._race_career

    @race_career.setter
    def race_career(self, value: dict[RaceConditions, RacePerformance]):
        self._race_career = dict(sorted(value.items(), key=lambda x: x[0].datetime))

    @property
    def is_handicap_debutant(self):
        return not any(
            race.race_designation == RaceDesignation.HANDICAP
            for race in self.race_career
        )

    @property
    def is_lto_winner(self):
        return self.performances[-1].is_win

    @property
    def is_maiden(self):
        return not any(run.is_win for run in self.performances)

    @property
    def is_unbeaten(self):
        return all(run.is_win for run in self.performances)

    @property
    def performances(self):
        return list(self.race_career.values())
