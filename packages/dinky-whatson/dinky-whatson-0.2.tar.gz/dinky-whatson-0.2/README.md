# dinky-whatson

_"What's On"_ widget for the [dinky](https://github.com/get-dinky/dinky) dashboard generator using data from the [What's On City of Sydney](https://whatson.cityofsydney.nsw.gov.au/) website

## Installation

Install this plugin using `pip`:

```bash
pip install dinky-whatson
```

## Usage

`dinky-whatson` is a plugin for the `dinky` dashboard generator. You can simply register the _"What's On"_ widget with your DashboardManager:

```python
from dinky_whatson import DinkyWhatsOnPlugin

dm.register(DinkyWhatsOnPlugin(suburb="Suburb in Sydney"), zone="A")
```

Then draw your dashboard as usual:

```python
dm.draw_dashboard()
```

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd dinky-whatson
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