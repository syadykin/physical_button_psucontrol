import octoprint.plugin

class PhysicalButtonPSUControlPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        helpers = self._plugin_manager.get_helpers("physicalbutton", "register_button_actions")
        if helpers and all(map(lambda x: x in helpers, ["register_button_actions", "get_psu_state", "turn_psu_on", "turn_psu_off"])):
            helpers["register_button_actions"]("toggle_psu", "Toggle PSU", "Toggle the power supply unit (PSU) on or off.", self.toggle_psu)

    def toggle_psu(self):
        psu_state = self._plugin_manager.get_helpers("psucontrol", "get_psu_state")
        if psu_state:
            if psu_state == "on":
                self._plugin_manager.get_helpers("psucontrol", "turn_psu_off")()
            else:
                self._plugin_manager.get_helpers("psucontrol", "turn_psu_on")()




__plugin_name__ = "Physical Buttons - PSU Control"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A bridge between PSU control and physical buttons plugin"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = PhysicalButtonPSUControlPlugin()
