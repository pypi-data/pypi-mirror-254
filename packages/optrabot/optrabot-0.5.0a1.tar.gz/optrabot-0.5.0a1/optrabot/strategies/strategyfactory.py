from typing import OrderedDict
from loguru import logger
from optrabot.strategies.ironfly import *
from optrabot.strategies.putspread import *
from optrabot.strategies.strategy import *

class StrategyFactory:

	@staticmethod
	def createStrategy(name: str, data) -> Strategy:
		""" Erzeugt aus der übergebenen Strategy Konfiguration aus der config.yaml das entprechende Strategy Objekt
		"""
		strategy = None
		stratType = data['type']
		match stratType:
			case 'Iron Fly':
				logger.debug('Creating Iron Fly strategy from config')
				strategy = IronFly(name)
			case 'Put Spread':
				logger.debug('Creating Put Spread strategy from config')
				strategy = PutSpread(name)
			case _:
				logger.error('Strategy type {} is unknown!', stratType)
				return None

		# Trigger configuration
		triggerinfo = data['trigger']
		trigger = StrategyTrigger(triggerinfo)
		strategy.setTrigger(trigger)

		try:
			account = data['account']
			strategy.setAccount(account)
		except KeyError:
			pass

		try:
			takeProfit = data['takeprofit']
			strategy.setTakeProfit(takeProfit)
		except KeyError:
			pass

		try:
			stopLoss = data['stoploss']
			strategy.setStopLoss(stopLoss)
		except KeyError:
			pass

		try:
			amount = data['amount']
			strategy.setAmount(amount)
		except KeyError:
			pass

		try:
			minPremium = data['minpremium']
			strategy.setMinPremium(minPremium)
		except KeyError:
			pass

		try:
			adjustmentStep = data['adjustmentstep']
			strategy.setAdjustmentStep(adjustmentStep)
		except KeyError:
			pass

		# Stop Loss Adjuster
		try:
			stoplossadjustment = OrderedDict(data['adjuststop'])
		except KeyError as keyErr:
			stoplossadjustment = None
			pass

		if stoplossadjustment:
			try:
				trigger = stoplossadjustment['trigger']
				stop = stoplossadjustment['stop']
				offset = float(stoplossadjustment['offset'])
				adjuster = StopLossAdjuster(reverse=True, trigger=trigger, stop=stop, offset=offset)
				strategy.setStopLossAdjuster(adjuster)
			except KeyError:
				pass

		return strategy
			
