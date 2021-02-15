import asyncio
from kasa import SmartPlug


class TpLinkHandler():
	def __init__(self, address):
		self.device = SmartPlug(address)

	async def update(self):
		await self.device.update()

	def shutdown(self):
		asyncio.create_task(self.device.turn_off())
		return "shutdown"

	def turnOn(self):
		asyncio.create_task(self.device.turn_on())
		return "Turning on"

	def __repr__(self):
		pass
