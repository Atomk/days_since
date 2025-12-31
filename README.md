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

## About and Q&A

I made this mainly for the "personal project" requirement on Boot.dev, but I genuinely find it useful as there are in fact some things I'm interested in tracking. Sometimes it's useful to see or remember how long you've been practicing a craft, how far in the past an important event happened, how long you avoided a bad habit, how close you are to a friendship/work/something anniversary.

My guiding principles are that I like simple, minimal things that are easy to use and setup. So while this project is pretty barebones, that's in part laziness but mostly intentional.

#### Why no add/edit/remove capabilities?
This project is supposed to be evaluated by people who follow the *backend* curriculum on Boot.dev and may not know HTML/CSS/JS. Up until this point the course only taught Python and C so I wanted to stick to Python, and implementing those features in the way I want requires JavaScript. But again, this is not a frontend course, so...

What about implementing them as CLI commands? I certainly don't see myself using the CLI to add/edit/remove stuff when editing the JSON directly is much easier and doesn't require knowing what the commands are.

It sucks that the projects I want to make and use are full-stack and not just Python, I could not come up with other project ideas simple enough to fit the requirements, and that I actually found interesting, ideally I would have made a fully functional web UI and used Python just for a proper backend (REST API + database) or maybe not.

#### Why is the web page loading so slow?
- PyScript and the Python interpreter are loaded from an external server which is perhaps intentionally not super fast
- The Python interpreter is loaded from within PyScript's code and I haven't found an obvious to cache it, so it's downloaded again at each refresh
- I'm using the [Pyodide](https://pyodide.com/) interpreter (`<script type="py">`) instead of the [MicroPython](https://micropython.org/) interpreter (`<script type="mpy">`). Pyodide has the best support for Python's features and standard library, at the cost of size. MicroPython is much smaller but also supports less Python features and standard modules, and I cannot use it without making some adjustments to the code, which I don't want to do since I'll rewrite this in JavaScript anyway (the right tool for this project)
    - For reference, MicroPython does not support the "typing" module and the "dataclasses" module
- This was just a silly experiment and I'm not familiar yet with PyScript so there may be something obvious I missed

#### This looks too simple. Have you actually learned anything?
It's very simple in functionality, it wasn't simple in terms of deciding what to make, how to make it, and what "good enough" would look like. When you see the final product everything seems obvious in hindsight and if I hade a precise plan I would have made this in an afternoon and not over multiple days.

That said, I didn't learn much in the "hard skills" sense but I have some takeaways:
- Tests give me such peace of mind!
- I've heard about PyScript before but it's the first time I try it, it's an interesting project and the authors did a great job at documenting it, despite it feeling pretty niche and perhaps a bit cursed...
- I've heard about Pyodide and MicroPython in the past, now I know a little bit more about them
- I haven't done anything web in a while so it was nice to get my hands dirty again
- I tend to get stuck on wanting to get things perfect at first try, and then doubt my skills if I can't decide on the best path forward or feeling like I wasted time by trying something that turned out to be a bad idea. It might help to experiment more and allow myself to make a mess sometimes, if only to spend more time "doing" rather than thinking. Not that thinking is bad but in my particular case it gets to a point where it has diminishing returns. I've found it surprisingly helpful to express my doubts to an LLM (the one and only time I used AI for this project) but I feel it would be better to talk about stuff I'm working on with friends or other learners, I feel even just checking in on each other from time to time and asking for opinions would help significantly
