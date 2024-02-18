import pluggy

from dinky.layouts.layout_configuration import Zone
from dinky.display_configuration import DisplayConfiguration

hookspec = pluggy.HookspecMarker("dinky")

@hookspec
def dinky_draw(zone: Zone, fullscreen: DisplayConfiguration):
    """Take a zone and display to fill.

    :param zone: the zone to draw on
    :param fullscreen: the full screen configuration
    :return: two images
    """
