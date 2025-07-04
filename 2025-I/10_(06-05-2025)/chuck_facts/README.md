# Chuck Facts

A Python package that fetches random Chuck Norris facts from the Chuck Norris API.

## Installation

You can install the package using pip:

```bash
pip install .
```

## Usage

### Command Line Interface

After installation, you can use the `FACTS` command to get random Chuck Norris facts:

```bash
# Get a single fact
FACTS

# Get multiple facts
FACTS -n 3
```

### Python API

You can also use the package in your Python code:

```python
from chuck_facts.facts import give_me_facts

# Get a random fact
fact = give_me_facts()
print(fact)
```

## Requirements

- Python 3.8 or higher
- requests library

## License

MIT License 