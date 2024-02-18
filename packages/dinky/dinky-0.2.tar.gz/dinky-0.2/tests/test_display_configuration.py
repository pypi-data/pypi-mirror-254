import pytest
from pydantic import ValidationError
from dinky.display_configuration import DisplayConfiguration

def test_display_configuration_creation():
    config = DisplayConfiguration(width=800, height=480, colors=7)
    assert config.width == 800
    assert config.height == 480
    assert config.colors == 7

def test_display_configuration_validation():
    with pytest.raises(ValidationError):
        config = DisplayConfiguration(width='test', height=480, colors=7)

    with pytest.raises(ValidationError):
        config = DisplayConfiguration(width=800, height='test', colors=7)

    with pytest.raises(ValidationError):
        config = DisplayConfiguration(width=800, height=480, colors='test')