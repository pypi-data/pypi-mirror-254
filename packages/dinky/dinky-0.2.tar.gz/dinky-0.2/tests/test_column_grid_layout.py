from dinky.layouts.column_grid_layout import ColumnGridLayout

def test_column_grid_layout_initialization():
    layout = ColumnGridLayout()
    assert layout.title == "ColumnGrid"
    assert len(layout.zones) == 5
    assert layout.zones[0].id == "A"
    assert layout.zones[0].x == 0
    assert layout.zones[0].y == 0
    assert layout.zones[0].width == 200
    assert layout.zones[0].height == 480

def test_column_grid_layout_is_valid():
    layout = ColumnGridLayout()
    assert layout.is_valid() == True

    # Test case where sum of widths of zones is greater than double the display width
    layout = ColumnGridLayout()
    layout.zones[0].width = 801
    assert layout.is_valid() == False

    # Test case where sum of heights of zones is greater than double the display height
    layout = ColumnGridLayout()
    layout.zones[0].height = 481
    assert layout.is_valid() == False

    # Test case where x coordinate of a zone is greater than display width
    layout = ColumnGridLayout()
    layout.zones[0].x = 801
    assert layout.is_valid() == False

    # Test case where y coordinate of a zone is greater than display height
    layout = ColumnGridLayout()
    layout.zones[0].y = 481
    assert layout.is_valid() == False