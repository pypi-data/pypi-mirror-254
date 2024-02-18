import pytest
from pydantic import ValidationError
from dinky.layouts.layout_configuration import BaseLayoutConfiguration, Zone
from dinky.display_configuration import DisplayConfiguration

def test_zone_creation():
    zone = Zone(id="A", x=0, y=0, width=100, height=100, padding=5)
    assert zone.id == "A"
    assert zone.x == 0
    assert zone.y == 0
    assert zone.width == 100
    assert zone.height == 100
    assert zone.padding == 5

def test_zone_validation():
    with pytest.raises(ValidationError):
        zone = Zone(id=1, x=0, y=0, width=100, height=100)

    with pytest.raises(ValidationError):
        zone = Zone(id="A", x="test", y=0, width=100, height=100)

    with pytest.raises(ValidationError):
        zone = Zone(id="A", x=0, y="test", width=100, height=100)

    with pytest.raises(ValidationError):
        zone = Zone(id="A", x=0, y=0, width="test", height=100)

    with pytest.raises(ValidationError):
        zone = Zone(id="A", x=0, y=0, width=100, height="test")

def test_base_layout_configuration_creation():
    display_config = DisplayConfiguration(width=800, height=480, colors=7)
    zones = [Zone(id="A", x=0, y=0, width=100, height=100, padding=5)]
    config = BaseLayoutConfiguration(display_configuration=display_config, title="Columns", zones=zones)
    assert config.display_configuration == display_config
    assert config.title == "Columns"
    assert config.zones == zones

def test_base_layout_configuration_validation():
    display_config = DisplayConfiguration(width=800, height=480, colors=7)
    zones = [Zone(id="A", x=0, y=0, width=100, height=100, padding=5)]

    with pytest.raises(ValidationError):
        config = BaseLayoutConfiguration(display_configuration="display_config", title="Columns", zones=zones)

    with pytest.raises(ValidationError):
        config = BaseLayoutConfiguration(display_configuration=display_config, title=123, zones=zones)

    with pytest.raises(ValidationError):
        config = BaseLayoutConfiguration(display_configuration=display_config, title="Columns", zones="test")

def test_base_layout_configuration_is_valid():
    display_config = DisplayConfiguration(width=800, height=480, colors=7)
    zones = [Zone(id="A", x=0, y=0, width=100, height=100, padding=5)]
    config = BaseLayoutConfiguration(display_configuration=display_config, title="Columns", zones=zones)

    with pytest.raises(Exception) as e:
        config.is_valid()
    assert str(e.value) == f"'is_valid' not implemented for {config.__module__}"