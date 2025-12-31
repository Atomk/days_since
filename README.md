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

## Web

Python on the frontend! Talk about using the wrong tool for the job. This repo provides a web version of the program, reusing much of its code by using [PyScript](https://pyscript.net/). Like its terminal counterpart, the web page provides a read-only visual representation of data in `events.json`.

Launch a local server:
```sh
python3 -m http.server 8080
```

Assuming you launched the server in the project's root, navigate your browser to: http://localhost:8080/web/

The interpreter will take a few seconds to load, this is unfortunate but expected.
