# dinky-onthisday

_"OnThisDay"_ widget for the [dinky](https://github.com/get-dinky/dinky) dashboard generator

## Installation

Install this plugin using `pip`:

```bash
pip install dinky-onthisday
```

## Usage

`dinky-onthisday` is a plugin for the `dinky` dashboard generator. You can simply register the _"OnThisDay"_ widget with your DashboardManager:

```python
from dinky_onthisday import DinkyOnThisDayPlugin

dm.register(
    DinkyOnThisDayPlugin(), zone="A")
```

Then draw your dashboard as usual:

```python
dm.draw_dashboard()
```

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd dinky-onthisday
python -m venv .venv
source .venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
python -m pytest
```