from app.core.enums import Strategies
from app.strategies import NuggetV1, NuggetV2, NuggetV3, NuggetV4, NuggetV5

selector = {
    Strategies.NUGGET_V1: NuggetV1,
    Strategies.NUGGET_V2: NuggetV2,
    Strategies.NUGGET_V3: NuggetV3,
    Strategies.NUGGET_V4: NuggetV4,
    Strategies.NUGGET_V5: NuggetV5
}


class StrategySelector:

    @staticmethod
    def get_strategy_class(strategy: Strategies):
        return selector.get(strategy)