from dinky.display_configuration import DisplayConfiguration
from dinky.layouts.layout_configuration import BaseLayoutConfiguration, Zone

class ColumnGridLayout(BaseLayoutConfiguration):
    def __init__(self, padding: int = 5):
        display_configuration = DisplayConfiguration()
        title = "ColumnGrid"
        zones = [
            Zone(id="A", x=0, y=0, width=200, height=480, padding=padding),
            Zone(id="B", x=200, y=0, width=300, height=240, padding=padding),
            Zone(id="C", x=500, y=0, width=300, height=240, padding=padding),
            Zone(id="D", x=200, y=240, width=300, height=240, padding=padding),
            Zone(id="E", x=500, y=240, width=300, height=240, padding=padding)
        ]
        super().__init__(display_configuration=display_configuration, title=title, zones=zones)

    def is_valid(self) -> bool:
        if sum(zone.width for zone in self.zones) > self.display_configuration.width * 2:
            return False
        if sum(zone.height for zone in self.zones) > self.display_configuration.height * 3:
            return False
        if any(zone.x > self.display_configuration.width for zone in self.zones):
            return False
        if any(zone.y > self.display_configuration.height for zone in self.zones):
            return False
        return True
