import asyncio
from kasa import SmartStrip, SmartDeviceException


class TpLinkHandlerSmartStrip(SmartDeviceException):
	def __init__(self, address):
		self.device = SmartStrip(address)

	def update(self):
		asyncio.run(self.device.update())

	def update_two(self):
		asyncio.create_task(self.device.update())

	def turn_on(self, plugNumber):
		asyncio.run(self.device.children[plugNumber].turn_on())

	def shutdown(self, plugNumber):
		asyncio.run(self.device.children[plugNumber].turn_on())

	def get_plug_information(self):
		return self.device.children

	def __repr__(self):
		pass
