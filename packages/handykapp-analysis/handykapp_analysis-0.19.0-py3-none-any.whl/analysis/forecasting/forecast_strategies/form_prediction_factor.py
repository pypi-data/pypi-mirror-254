from decimal import Decimal
from typing import Self

from analysis.horse import Horse
from analysis.race_conditions import RaceConditions


class FormPredictionFactor(Decimal):
    def __init__(self, horse: Horse, race_conditions: RaceConditions):
        self.horse = horse
        self.race_conditions = race_conditions
        self._value = self._calc()

    def __new__(cls, *args, **kwargs) -> Self:
        instance = super().__new__(cls)
        instance.__init__(*args, **kwargs) # type: ignore
        return super().__new__(cls, instance._value)

    def _calc(self) -> Decimal:
        raise NotImplementedError
