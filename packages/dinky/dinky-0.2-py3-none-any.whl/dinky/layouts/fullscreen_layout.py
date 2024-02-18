from dinky.display_configuration import DisplayConfiguration
from dinky.layouts.layout_configuration import BaseLayoutConfiguration, Zone

class FullscreenLayout(BaseLayoutConfiguration):
    def __init__(self, padding: int = 5):
        display_configuration = DisplayConfiguration()
        title = "Fullscreen"
        zone_width = display_configuration.width
        zone_height = display_configuration.height
        zones = [
            Zone(id="A", x=0, y=0, width=zone_width, height=zone_height, padding=padding)
        ]
        super().__init__(display_configuration=display_configuration, title=title, zones=zones)

    def is_valid(self) -> bool:
        if self.zones[0].width > self.display_configuration.width:
            return False
        if self.zones[0].height > self.display_configuration.height:
            return False
        if self.zones[0].x > self.display_configuration.width:
            return False
        if self.zones[0].y > self.display_configuration.height:
            return False
        return True
