from optrabot.stoplossadjuster import StopLossAdjuster
from optrabot.strategies.strategytrigger import StrategyTrigger

class StrategyType:
	IronFly = "IF"
	PutSpread = "PS"

class Strategy:
	def __init__(self, name: str) -> None:
		self._type = None
		self.name = name
		self._trigger = None
		self.account = None
		self.takeProfit = None
		self.stopLoss = None
		self.amount = 1
		self.minPremium = None
		self.adjustmentStep = 0.05
		self.stopLossAdjuster = None

	def setTrigger(self, trigger: StrategyTrigger):
		""" Definiert den Trigger für diese Strategie.
		"""
		self._trigger = trigger

	def getTrigger(self) -> StrategyTrigger:
		""" Returns the trigger of the strategy
		"""
		return self._trigger
	
	def setAccount(self, account: str):
		""" Sets the account which the strategy is traded on 
		"""
		self.account = account
	
	def setTakeProfit(self, takeprofit: int):
		""" Sets the take profit level in % of the strategy 
		"""
		self.takeProfit = takeprofit

	def setStopLoss(self, stoploss: int):
		""" Sets the stop loss level in % of the strategy
		"""
		self.stopLoss = stoploss

	def setAmount(self, amount: int):
		""" Sets the amount of contracts to be traded with this strategy
		"""
		self.amount = amount
	
	def setMinPremium(self, minPremium: float):
		""" Sets the minimum premium which must be received from broker in order to execute a trade
		of this strategy.
		"""
		self.minPremium = minPremium

	def setAdjustmentStep(self, adjustmentStep: float):
		""" Sets the price adjustment step size for the entry order adjustment
		"""
		self.adjustmentStep = adjustmentStep
	
	def setStopLossAdjuster(self, stopLossAdjuster: StopLossAdjuster):
		""" Sets the Stop Loss Adjuster for this strategy, if configured
		"""
		self.stopLossAdjuster = stopLossAdjuster
	
	def __str__(self) -> str:
		""" Returns a string representation of the strategy
		"""
		strategyString = ('Name: ' + self.name + ' Type: ' + self._type + ' Trigger: (' + self._trigger.type + ', ' + str(self._trigger.value) + ')' +
		' Account: ' + self.account + ' Amount: ' + str(self.amount) + ' Take Profit (%): ' + str(self.takeProfit) + ' Stop Loss (%): ' + str(self.stopLoss) +
		' Min. Premium: ' + str(self.minPremium) + ' Entry Adjustment Step: ' + str(self.adjustmentStep) + ' Stop Loss Adjuster: ()' + 
		str(self.stopLossAdjuster) + ')')
		return strategyString