# OctoPrint-Tplinkautoshutdown

!!! THIS PLUGIN WILL NO LOGER RECIEVE UPDATES !!!

This plugin is designed to help you integrate your IoT TP-Link Kasa wireless plug into OctoPrint. The basis of the plug-in is to enable you to automatically switch-off your 3D printer
once a print has successfully completed.

## Requirements
* Python >=3.7, <4.0

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/CodingTheUnknown/OctoPrint-Tplinkautoshutdown.git

#### Simple installation

Installation can be achieved through two options. The first and simplest option is to use the plugin manager within OctoPrint and search for TpLinkHandler. Then upon installation all you need to do is re-start you device and the plugin will be installed and ready for use.

#### Manual installation

To manually install your plugin, follow these steps:

1.	Open settings,
2.	Click on ‘Plugin Manager’
3.	Now click ‘Get More’
4.	A window will then pop-up. There will be a text box with ‘Enter URL…’. Paste the URL from above. This URL must be the URL from this README.md file not the URL of the webpage within your browser.
5.	Finally click install
6.	Restart OctoPrint and you are ready.

#### Connection to a device
To connect to your smart device, simply download the plugin and navigate to 'settings > TpLinkHandler'

#### Current features
1. Manually switch your Tp-Link socket on and off.
2. Automatically switch your Tp-Link socket on and off.
3. choose if you want your timelapse to render before the plug is turned off automatically (great if you use the same plug for OctoPrint and the printer).
4. When using the smart strip KP303 you can manually decide what each socket does.

## compatibility

Although, this plugin may work with a number of other Kasa devices, this plugin has been designed to definitively work with the following devices.

#### Smart Plugs:

* HS100
* HS103
* HS105
* HS107
* HS110

#### Smart Strips:
* HS300
* KP303

## Authors

- James D. McCannon

## Contributions
Contributions (be it adding missing features, fixing bugs or improving documentation) are more than welcome, feel free to submit pull requests!

## Screenshots
Top navigation buttons to allow simple manual controll over the Tp-Link device

![navigation bar image](https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/blob/master/assets/Buttons_navigation.png?raw=true)

Views from within the settings

![Smart plug settings](https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/blob/master/assets/smartPlug_settings.png?raw=true)

![Smart strip settings](https://github.com/jamesmccannon02/OctoPrint-Tplinkautoshutdown/blob/master/assets/smartStrip_settings.png?raw=true)

