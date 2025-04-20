# coding=utf-8

########################################################################################################################
### Do not forget to adjust the following variables to your own plugin.

import sys

plugin_identifier = "physical_button_psucontrol"

plugin_package = "octoprint_physical_button_psucontrol"

plugin_name = "Physical Button PSU Control Bridge"

plugin_version = "1.0.0"

plugin_description = """A bridge between PSU control and physical buttons plugin"""

plugin_author = "Stanyslav Yadykin"

plugin_author_email = "syadykin@gmail.com"

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data via __plugin_url__ in the plugin module
plugin_url = "https://github.com/syadykin/physical_button_psucontrol"

plugin_license = "AGPLv3"

plugin_additional_data = []

plugin_additional_packages = []

plugin_ignored_packages = []

additional_setup_parameters = {"python_requires": ">=3, <4"}

########################################################################################################################

from setuptools import setup

try:
    import octoprint_setuptools
except:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    import sys

    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    requires=[],
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge

    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
