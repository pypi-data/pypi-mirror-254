from decimal import Decimal

from .form_prediction_factor import FormPredictionFactor


class ThreeYearOldVsOlderBonus(FormPredictionFactor):
    def _calc(self) -> Decimal:
        return Decimal(10 if self.horse.age == 3 else 0)
