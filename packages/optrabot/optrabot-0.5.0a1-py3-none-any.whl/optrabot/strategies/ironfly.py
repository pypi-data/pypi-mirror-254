from optrabot.strategies.strategy import *

class IronFly(Strategy):
	def __init__(self, name: str) -> None:
		super().__init__(name=name)
		self._type = StrategyType.IronFly