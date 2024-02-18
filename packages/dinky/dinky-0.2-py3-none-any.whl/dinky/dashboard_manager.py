from PIL import Image
import pluggy

from dinky import hookspecs
from dinky.display_configuration import DisplayConfiguration
from dinky.layouts.layout_configuration import BaseLayoutConfiguration

class DashboardManager():
    def __init__(self, layout_configuration: BaseLayoutConfiguration):
        self.pm = pluggy.PluginManager("dinky")
        self.pm.add_hookspecs(hookspecs)
        self.display_configuration: DisplayConfiguration = DisplayConfiguration()
        self.layout_configuration: BaseLayoutConfiguration = layout_configuration

    def register(self, plugin: object, zone: str):
        self.pm.register(plugin, name=zone)

    def draw(self):
        dashboard = Image.new("RGB", (self.display_configuration.width, self.display_configuration.height), (255, 255, 255))
        for plugin in self.pm.get_plugins():
            zone = next(filter(lambda zone: zone.id == self.pm.get_name(plugin), self.layout_configuration.zones))
            panel, fullscreen = plugin.dinky_draw(zone=zone, fullscreen=self.display_configuration)
            dashboard.paste(panel, (zone.x, zone.y))
            fullscreen.save(f"panel_{self.pm.get_name(plugin).lower()}.jpg")
        dashboard.save("dashboard.jpg")
