import octoprint.plugin

class PhysicalButtonPSUControlPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        physicalbutton_helpers = self._plugin_manager.get_helpers("physicalbutton", "register_button_actions")
        psucontrol_helpers = self._plugin_manager.get_helpers("psucontrol", "get_psu_state", "turn_psu_on", "turn_psu_off")

        if physicalbutton_helpers and all(map(lambda x: x in physicalbutton_helpers, ["register_button_actions"])) \
            and psucontrol_helpers and all(map(lambda x: x in psucontrol_helpers, ["get_psu_state", "turn_psu_on", "turn_psu_off"])):

            self._logger.info("Registering toggle_psu action")
            physicalbutton_helpers["register_button_actions"](self, {
                "toggle_psu": self.toggle_psu
            })

    def toggle_psu(self):
        helpers = self._plugin_manager.get_helpers("psucontrol", "get_psu_state", "turn_psu_on", "turn_psu_off")

        if helpers["get_psu_state"]():
            helpers["turn_psu_off"]()
        else:
            helpers["turn_psu_on"]()




__plugin_name__ = "Physical Buttons - PSU Control"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A bridge between PSU control and physical button plugin"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = PhysicalButtonPSUControlPlugin()
