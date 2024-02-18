# nox-pdm

Use [PDM] inside [Nox] sessions

This package provides a drop-in replacement for the `nox.session` decorator,
and for the `nox.Session` object passed to user-defined session functions.
This enables `session.install` to install packages at the versions specified in the `pdm.lock` file.

```py
from nox_pdm import session, Session

@session(python=["3.10", "3.9"])
def tests(session: Session):
    # To install all packages in dependency group `tests` while using pdm.lock as constraint
    session.install(".[tests]")
    session.run("pytest")

```

## Installation

Install `nox-pdm` from the Python Package Index:

```sh
pip install nox-pdm
```

**Important:**
This package must be installed into the same environment that Nox is run from.
If you installed Nox using [pipx],
use the following command to install this package into the same environment:

```sh
pipx inject nox nox-pdm
```

## Requirements

- Python 3.9+
- PDM >= 2.12.0

You need to have a [PDM] installation on your system. It does not have to be in the
same environment, but at the very least running the command `pdm` should work.
`nox-pdm` uses PDM via its command-line interface.


## Credits

This project was inspired by Claudio Jolowicz's  <https://pypi.org/project/nox-poetry>.


[nox]: https://nox.thea.codes/
[pdm]: https://pdm-project.org/
[constraints file]: https://pip.pypa.io/en/stable/user_guide/#constraints-files
[file an issue]: https://codeberg.org/ashwinvis/nox-pdm/issues
[keyword-only parameter]: https://docs.python.org/3/glossary.html#keyword-only-parameter
[nox.sessions.session.install]: https://nox.thea.codes/en/stable/config.html#nox.sessions.Session.install
[nox.sessions.session.run]: https://nox.thea.codes/en/stable/config.html#nox.sessions.Session.run
[pip install]: https://pip.pypa.io/en/stable/reference/pip_install/
[pip]: https://pip.pypa.io/
[pipx]: https://pipxproject.github.io/pipx/
