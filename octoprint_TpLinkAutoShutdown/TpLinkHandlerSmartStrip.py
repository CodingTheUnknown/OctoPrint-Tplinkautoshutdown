import asyncio
from kasa import SmartStrip, SmartDeviceException


class TpLinkHandlerSmartStrip(SmartDeviceException):
	def __init__(self):
		pass

	def turn_on(self, plugNumber):
		pass

	def shutdown(self, plugNumber):
		pass

	def get_plug_information(self):
		pass

	def __repr__(self):
		pass
