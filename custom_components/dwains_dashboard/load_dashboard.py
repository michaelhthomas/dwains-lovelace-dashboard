import logging

from homeassistant.components.lovelace.dashboard import LovelaceYAML
from homeassistant.components.lovelace import _register_panel

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

def load_dashboard(hass, config_entry):

    #_LOGGER.warning(config_entry.options)
    #_LOGGER.warning(config_entry.options["sidepanel_title"])

    sidepanel_title = "Dwains Dashboard"
    sidepanel_icon = "mdi:alpha-d-box"
    enable_sidepanel = True

    if("sidepanel_title" in config_entry.options):
        sidepanel_title = config_entry.options["sidepanel_title"]

    if("sidepanel_icon" in config_entry.options):
        sidepanel_icon = config_entry.options["sidepanel_icon"]

    if("enable_sidepanel" in config_entry.options):
        enable_sidepanel = config_entry.options["enable_sidepanel"]

    dashboard_url = "dwains-dashboard"
    dashboard_config = {
        "mode": "yaml",
        "icon": sidepanel_icon,
        "title": sidepanel_title,
        "filename": "custom_components/dwains_dashboard/lovelace/ui-lovelace.yaml",
        "show_in_sidebar": enable_sidepanel,
        "require_admin": False,
    }

    hass.data["lovelace"]["dashboards"][dashboard_url] = LovelaceYAML(hass, dashboard_url, dashboard_config)

    _register_panel(hass, dashboard_url, "yaml", dashboard_config, False)