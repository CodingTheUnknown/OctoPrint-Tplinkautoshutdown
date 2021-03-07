import asyncio
import threading


class ThreadedWorker():
	def __init__(self):
		self.thread = threading.Thread(target=self.run, daemon=True)
		self.loop = None
		self.thread.start()

	def run(self):
		self.loop = asyncio.new_event_loop()
		asyncio.set_event_loop(self.loop)
		return self.loop.run_forever()
