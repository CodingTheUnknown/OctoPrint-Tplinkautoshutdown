# coding=utf-8
from __future__ import absolute_import
from .TpLinkHandler import TpLinkHandler as wallPlug
import octoprint.plugin
import flask


class TpLinkAutoShutdown(octoprint.plugin.StartupPlugin, octoprint.plugin.SettingsPlugin,
						 octoprint.plugin.EventHandlerPlugin, octoprint.plugin.TemplatePlugin,
						 octoprint.plugin.AssetPlugin, octoprint.plugin.SimpleApiPlugin):

	def on_after_startup(self):
		self._logger.info("Plugin TpLinkHandler has started")

	def on_event(self, event, payload):
		if event == "PrintDone":
			self._logger.info("Print has completed")
			self.conn.shutdown()
		elif event == "PrintStarted":
			self._logger.info("Print has PrintStarted")
			self.conn = wallPlug(self._settings.get(["url"]))
			self.conn.update()
		elif event == "PrintPaused":
			self._logger.info("Print paused")

	def get_api_commands(self):
		return dict(
			turnOn=[],
			turnOff=[]
		)

	def on_api_command(self, command, data):
		_conn = wallPlug(self._settings.get(["url"]))
		_conn.update()
		if command == "turnOn":
			self._logger.info("Turning the printer ON")
			_conn.turnOn_btn()
			return flask.jsonify(res="Turining the 3D printer on. Please wait ... ")
		elif command == "turnOff":
			self._logger.info("Turning the printer OFF")
			_conn.shutdown_btn()
			return flask.jsonify(res="Turning the 3D printer off. 3 ... 2 ... 1 ...")

	def get_settings_defaults(self):
		return dict(url="Testing")

	def get_template_configs(self):
		return [
			dict(type="navbar", template="TpNavigation_navbar.jinja2"),
			dict(type="settings", template="TpNavigation_settings.jinja2", custom_bindings=False),
		]

	def get_assets(self):
		return dict(
			js=['js/navbarControll.js']
		)

	def get_update_infomation(self):
		return dict(
			TpLinkAutoShutdown=dict(
				display_name=self._plugin_name,
				display_version=self._plugin_version,

				type="github_release",
				current=self._plugin_version,
				user="jamesmccannon02",
				pip="https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/archive/v{target_version}.zip"
			)
		)


__plugin_name__ = "TpLinkHandler"
__plugin_pythoncompat__ = ">=3.0,<4"
__plugin_implementation__ = TpLinkAutoShutdown()
__plugin_hooks__ = {
"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_infomation
}
