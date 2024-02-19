# Home

Smart Mixin is a Python library for Clash configuration file manipulation.

## Prerequisites

Python >= 3.10.0

## Installation

To install Smart Mixin, run the following command in your terminal:

```
pip3 install smartmixin
```

Alternatively, you can clone the repository and install it manually:

```
git clone https://github.com/UFervor/SmartMixin.git
cd SmartMixin
pip3 install .
```

## Usage Examples

Here's a quick example to get you started. This script downloads a configuration from `https://example.com/abc`, removes all proxies whose names match the regex expression `Official Website|Expire`, and then dumps the modified YAML configuration to `config.yaml`.

```python
from SmartMixin import Config, select_all, ClashforWindows

# Initialize the configuration
conf = Config("https://example.com/abc", UA=ClashforWindows("0.20.39"))

# Select and delete the specified proxies
select_all(conf.Proxies, False, re_name="Official Website|Expire").delete(globally=True)

# Dump the modified configuration to a file
with open("config.yaml", "w") as f:
    f.write(conf.YAML)
```

## Documentation

For more detailed information about Smart-Mixin's features and usage, please refer to [the documentation](https://ufervor.github.io/SmartMixin/).
