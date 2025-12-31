# Days Since

A simple program to show time elapsed since past events.

```
Met my friend Anna --------------- 11mo 11d
Last time I ate sushi ------------ 2y 11mo 23d
Started playing the clarinet ----- 8mo
Bought my PC --------------------- 5y 11mo
Skyrim came out ------------------ 14y 1mo 19d
```

The program was tested only with Python 3.12, but it's probably also compatible with older versions.

## Clone and run

```sh
git clone https://github.com/Atomk/days_since.git
cd days_since
python3 src/days_since/main.py
```

## Configure

Data is loaded from a `events.json` file located in the `data` directory. When you first clone the repo this file does not exist. You can copy or rename the existing sample file.

Or you can run this command from the project's root:
```sh
cp data/events_sample.json data/events.json
```

## Tests

If you have `uv` installed:
```sh
uv run pytest
```

Otherwise:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
```
