from dinky.layouts.grid_layout import GridLayout

def test_grid_layout_is_valid():
    layout = GridLayout()
    assert layout.is_valid() == True

    # Test case where sum of widths of zones + border width is greater than display width
    layout = GridLayout()
    layout.zones[0].width = 801
    assert layout.is_valid() == False

    # Test case where sum of heights of zones + border width is greater than display height
    layout = GridLayout()
    layout.zones[0].height = 481
    assert layout.is_valid() == False

    # Test case where x coordinate of a zone is greater than display width
    layout = GridLayout()
    layout.zones[0].x = 801
    assert layout.is_valid() == False

    # Test case where y coordinate of a zone is greater than display height
    layout = GridLayout()
    layout.zones[0].y = 481
    assert layout.is_valid() == False