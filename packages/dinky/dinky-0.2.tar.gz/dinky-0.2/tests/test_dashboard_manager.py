import pluggy
from PIL import Image
from dinky.dashboard_manager import DashboardManager
from dinky.layouts.column_grid_layout import ColumnGridLayout
from dinky.display_configuration import DisplayConfiguration

hookimpl = pluggy.HookimplMarker("dinky")

class TestPlugin:
    @hookimpl
    def dinky_draw(self, zone, fullscreen):
        return Image.new("RGB", (zone.width, zone.height), (255, 255, 255)), Image.new("RGB", (fullscreen.width, fullscreen.height), (255, 255, 255))

def test_dashboard_manager_initialization():
    dashboard_manager = DashboardManager(ColumnGridLayout())
    assert isinstance(dashboard_manager.display_configuration, DisplayConfiguration)
    assert isinstance(dashboard_manager.layout_configuration, ColumnGridLayout)

def test_dashboard_manager_register():
    dashboard_manager = DashboardManager(ColumnGridLayout())
    dashboard_manager.register(TestPlugin(), "A")
    assert any(name == "A" for name, _ in dashboard_manager.pm.list_name_plugin())

def test_dashboard_manager_draw_dashboard(mocker):
    dashboard_manager = DashboardManager(ColumnGridLayout())
    dashboard_manager.register(TestPlugin(), "A")
    mock_image = mocker.Mock()
    mocker.patch('PIL.Image.new', return_value=mock_image)
    dashboard_manager.draw()
    assert mock_image.save.called