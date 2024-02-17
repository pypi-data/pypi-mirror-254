# MUMiChasPy

**Mondragon Unibertsitatea**'s *Microservice Chassis* pattern implementation in *Python* (MuMiChasPy).

## Developers

- [Alain PEREZ RIAÑO](https://github.com/draperez)

## Testing

- Create virtual environment:

```bash
python -m venv env
source env/bin/activate
```

- Install dependencies:

```bash
python -m pip install .[test]
```

- Execute tests:

```bash
pytest
```

## Style guide with flake8

```bash
pip install flake8 flake8-html
flake8 --max-line-length=100 --format=html --htmldir=flake-report **/*.py
```

Open flake-report/index.html with your browser.


## License

MIT license (see LICENSE), provided WITHOUT WARRANTY.