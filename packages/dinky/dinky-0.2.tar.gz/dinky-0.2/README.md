# dinky

Dashboard generator for e-ink devices such as the [Inky Frame](https://shop.pimoroni.com/products/inky-frame-7-3).

## Installation

Install this library using `pip`:

```bash
pip install dinky
```

dinky is only a dashboard manager. It relies on widgets that fill the dashboard. Install your first widget also using `pip`:

```bash
pip install dinky-calendar
```

## Usage

A small Python script is enough to generate your dashboard.

Start by instantiating the DashboardManager with a layout of your choice:

```python
from dinky.dashboard_manager import DashboardManager
from dinky.layouts.column_grid_layout import ColumnGridLayout

dm = DashboardManager(layout_configuration=ColumnGridLayout(padding=5))
```

Then register your first widget and specify the zone in which you want it displayed:

```python
from dinky_calendar import DinkyCalendarPlugin

dm.register(DinkyCalendarPlugin(), name="A")
```

Finally, draw your dashboard:

```python
dm.draw_dashboard()
```

The dashboard can now be displayed on your e-ink device.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd dinky
python -m venv .venv
source .venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
pytest
```