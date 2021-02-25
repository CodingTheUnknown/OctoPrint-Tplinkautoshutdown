# coding=utf-8
from __future__ import absolute_import
from .TpLinkHandlerSmartPlug import TpLinkHandlerSmartPlug as wallPlug
from .TpLinkHandlerSmartStrip import TpLinkHandlerSmartStrip as wallStrip
import octoprint.plugin
import flask


class TpLinkAutoShutdown(octoprint.plugin.StartupPlugin, octoprint.plugin.SettingsPlugin,
						 octoprint.plugin.EventHandlerPlugin, octoprint.plugin.TemplatePlugin,
						 octoprint.plugin.AssetPlugin, octoprint.plugin.SimpleApiPlugin):

	def on_after_startup(self):
		self._logger.info("Plugin TpLinkHandler has started")
		# todo Check the type of plug used
		# todo If Else dependent on the type of plug being used.
		if self._settings.get(["type"]) == "smartPlug":
			try:
				self.conn = wallPlug(self._settings.get(["url"]))
				self.conn.update()
				self._logger.info(self.conn.get_plug_information())
			except:
				self._logger.info("+++++++++++ Can't connect to plug +++++++++++++")
		elif self._settings.get(["type"]) == "smartStrip":
			try:
				self.conn = wallStrip(self._settings.get(["url"]))
				self.conn.update()
				self._logger.info(self.conn.get_plug_information())
			except:
				self._logger.info("+++++++++++ Can't connect to strip +++++++++++++")
		else:
			self._logger("+++++++++++Aborted onStartup connection+++++++++++")

	# Triggered through system events wihtin the octoprint server
	def on_event(self, event, payload):
		if event == "PrintDone":
			# If the plug being used is a smartPlug
			if self._settings.get(["type"]) == "smartPlug":
				self._logger.info(f"The print has completed. Auto-shutdown is set to {str(self._settings.get(['smartPlug', 'auto']))}")
				if self._settings.get(["smartPlug", "auto"]) and self._settings.get(["smartPlug", "movieDone"]) == False:
					self._logger.info("Printer is being shutdown")
					self.conn.shutdown()
			# If the plug being used is a smartStrip
			elif self._settings.get(["type"]) == "smartStrip":
				# check the setting Preferences of each socket
				if self._settings.get(["smartStrip", "deviceOne", "auto"]) and self._settings.get(["smartStrip", "deviceOne", "movieDone"] == False):
					self._logger.info("Printer is being shutdown")
					self.conn.shutdown(1)
				elif self._settings.get(["smartStrip", "deviceTwo", "auto"]) and self._settings.get(["smartStrip", "deviceTwo", "movieDone"] == False):
					self._logger.info("Printer is being shutdown")
					self.conn.shutdown(2)
				elif self._settings.get(["smartStrip", "deviceThree", "auto"]) and self._settings.get(["smartStrip", "deviceThree", "movieDone"] == False):
					self._logger.info("Printer is being shutdown")
					self.conn.shutdown(3)
		elif event == "PrintStarted":
			if self._settings.get(["type"]) == "smartPlug":
				self._logger.info(str(self._settings.get(["smartPlug", "auto"])))
				self._logger.info("Print has been started")
				self.conn = wallPlug(self._settings.get(["url"]))
				self.conn.update()
			elif self._settings.get(["type"]) == "smartStrip":
				self._logger.info(str(self._settings.get(["smartStrip", "auto"])))
				self._logger.info("Print has been started")
				self.conn = wallStrip(self._settings.get(["url"]))
				self.conn.update()
		elif event == "MovieDone":
			if self._settings.get(["type"]) == "smartPlug":
				if self._settings.get(["smartPlug", "movieDone"]) and self._settings.get(["smartPlug", "auto"]):
					self.conn.shutdown()
			elif self._settings.get(["type"]) == "smartStrip":
				if self._settings.get(["smartStrip", "deviceOne", "movieDone"]) and self._settings.get(["smartStrip", "deviceOne", "auto"]):
					self.conn.shutdown(1)
				elif self._settings.get(["smartStrip", "deviceTwo", "movieDone"]) and self._settings.get(["smartStrip", "deviceTwo", "auto"]):
					self.conn.shutdown(2)
				elif self._settings.get(["smartStrip", "deviceThree", "movieDone"]) and self._settings.get(["smartStrip", "deviceThree", "auto"]):
					self.conn.shutdown(3)
		elif event == "PrintPaused":
			self._logger.info("Print paused")

	# Defining the expected incoming data
	def get_api_commands(self):
		return dict(
			turnOn=[],
			turnOff=[],
			update=["url", "type"]
		)

	# Handling the requests sent from javascript
	def on_api_command(self, command, data):
		if command == "turnOn":
			# todo Check the type of plug used
			# todo If Else dependent on the type of plug being used.
			self._logger.info("Turning the printer ON")
			self.conn.turnOn_btn()
			return flask.jsonify(res="Turning the 3D printer on. Please wait ... ")
		elif command == "turnOff":
			# todo Check the type of plug used
			# todo If Else dependent on the type of plug being used.
			self._logger.info("Turning the printer OFF")
			self.conn.shutdown_btn()
			return flask.jsonify(res="Turning the 3D printer off. 3 ... 2 ... 1 ....")
		# Triggered when the user clicks to 'update connection' within the settings interface
		elif command == "update":
			try:
				self.on_settings_save(data)
				returnData = self.conn.get_plug_information()
				self._logger.info(returnData)
				return flask.jsonify(res=self.conn.get_plug_information())
			except:
				return flask.jsonify(res="Error Occurred")

	def get_settings_defaults(self):
		return dict(
			url="0.0.0.0",
			device="Unavailable",
			firmwareVersion="Unavailable",
			type="None",
			plugType="None",
			smartPlug=dict(
				auto=True,
				movieDone=False,
			),
			smartStrip=dict(
				deviceOne=dict(
					light=False,
					printer=False,
					custom=False,
					auto=False,
					movieDone=False,
				),
				deviceTwo=dict(
					light=False,
					printer=False,
					custom=False,
					auto=False,
					movieDone=False,
				),
				deviceThree=dict(
					light=False,
					printer=False,
					custom=False,
					auto=False,
					movieDone=False,
				),
			),
		)

	def on_settings_save(self, data):
		try:
			self._logger.info(data)
			if data["url"] != self._settings.get(["url"]):
				self.conn.__init__(data["url"])
				self.conn.update_two()
		except:
			pass
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

	def get_template_configs(self):
		return [
			dict(type="navbar", template="TpNavigation_navbar.jinja2"),
			dict(type="settings", template="TpNavigation_settings.jinja2", custom_bindings=False),
		]

	# Setting the location of the assets such as javascript
	def get_assets(self):
		return dict(
			js=["js/navbarControll.js", "js/settingsControll.js"],
			css=["css/settingsControll.css"]
		)

	# This is being used to distribute updates
	def get_update_information(self):
		return dict(
			TpLinkHandler=dict(
				display_name="TpLinkHandler",
				display_version=self._plugin_version,

				type="github_release",
				user="jamesmccannon02",
				repo="OctoPrint-Tplinkautoshutdown",
				current=self._plugin_version,

				pip="https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "TpLinkHandler"
__plugin_pythoncompat__ = ">=3.0,<4"
__plugin_implementation__ = TpLinkAutoShutdown()
__plugin_hooks__ = {
	"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
}
