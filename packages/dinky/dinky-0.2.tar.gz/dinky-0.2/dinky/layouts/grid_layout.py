from dinky.display_configuration import DisplayConfiguration
from dinky.layouts.layout_configuration import BaseLayoutConfiguration, Zone

class GridLayout(BaseLayoutConfiguration):
    def __init__(self, padding: int = 5):
        display_configuration = DisplayConfiguration()
        title = "Grid"
        zone_width = display_configuration.width / 2
        zone_height = display_configuration.height / 2
        zones = [
            Zone(id="A", x=0, y=0, width=zone_width, height=zone_height, padding=padding),
            Zone(id="B", x=zone_width, y=0, width=zone_width, height=zone_height, padding=padding),
            Zone(id="C", x=0, y=zone_height, width=zone_width, height=zone_height, padding=padding),
            Zone(id="D", x=zone_width, y=zone_height, width=zone_width, height=zone_height, padding=padding)
        ]
        super().__init__(display_configuration=display_configuration, title=title, zones=zones)

    def is_valid(self) -> bool:
        if sum(zone.width for zone in self.zones) > self.display_configuration.width * 2:
            return False
        if sum(zone.height for zone in self.zones) > self.display_configuration.height * 2:
            return False
        if any(zone.x > self.display_configuration.width for zone in self.zones):
            return False
        if any(zone.y > self.display_configuration.height for zone in self.zones):
            return False
        return True
