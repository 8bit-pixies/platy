# Platy

Platy (named after platypus - weird, functional, and confusing to explain) is a qr code generator application written in Python with the goal to provide a single binary with a UI that is privacy perserving and does not require internet access to use.

This project is setup using `uv`

To start the app run:

```sh
uv run app.py
```

To build app

```sh
uv run pyinstaller -w --onefile --name="platy" --icon="icon.ico" app.py
```