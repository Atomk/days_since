## Setup and run

```sh
git clone https://github.com/Atomk/days_since.git
cd days_since
```

The program needs an `events.json` file, which defines the events to show. As a quickstart you can rename or copy the existing sample json in the `data` directory, either manually or with the following command:
```sh
cp data/events_sample.json data/events.json
```

Now you can run the app:
```sh
python3 src/days_since/main.py
```
