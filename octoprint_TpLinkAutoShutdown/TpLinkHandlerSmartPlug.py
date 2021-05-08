import asyncio
from kasa import SmartPlug, SmartDeviceException
from .ThreadedWorker import ThreadedWorker


class TpLinkHandlerSmartPlug(SmartDeviceException):
	def __init__(self, address):
		self.device = SmartPlug(address)

	def update(self):
		asyncio.run(self.device.update())

	def update_two(self):
		asyncio.create_task(self.device.update())

	def update_three(self):
		future = asyncio.run_coroutine_threadsafe(self.device.update(), self.worker.loop)
		result = future.result()

	def shutdown_btn(self, settings):
		asyncio.create_task(self.device.turn_off())
		return "shutdown"

	def turnOn_btn(self, settings):
		asyncio.create_task(self.device.turn_on())
		return "Turning on"

	def shutdown(self):
		asyncio.run(self.device.turn_off())
		return "shutdown"

	def turnOn(self):
		asyncio.run(self.device.turn_on())
		return "Turning on"

	def get_plug_information(self):
		return self.device.hw_info

	def __repr__(self):
		pass
