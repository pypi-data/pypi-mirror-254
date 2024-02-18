"""

Notes
----------------

Inspired from nox-poetry

---

MIT License

Copyright © 2020 Claudio Jolowicz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""
import functools
import hashlib
from typing import Any

from pathlib import Path


import nox


def session(*args, **kwargs):
    """Drop-in replacement for the :func:`nox.session` decorator.

    Use this decorator instead of ``@nox.session``. Session functions are passed
    :class:`Session` instead of :class:`nox.sessions.Session`; otherwise, the
    decorators work exactly the same.

    Args:
        args: Positional arguments are forwarded to ``nox.session``.
        kwargs: Keyword arguments are forwarded to ``nox.session``.

    Returns:
        The decorated session function.
    """
    if not args:
        return functools.partial(session, **kwargs)

    [function] = args

    @functools.wraps(function)
    def wrapper(session: nox.Session, *_args, **_kwargs) -> None:
        proxy = Session(session)
        function(proxy, *_args, **_kwargs)

    return nox.session(wrapper, **kwargs)  # type: ignore[call-overload]


class Session:
    def __init__(self, session: nox.Session) -> None:
        """Initialize."""
        self._session = session
        self.pdm_session = _PDMSession(session)

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to nox.Session."""
        return getattr(self._session, name)

    def install(self, *args: str, **kwargs) -> None:
        """Install packages into a Nox session using PDM."""
        return self.pdm_session.install(*args, **kwargs)


class _PDMSession:
    """PDM-related utilities for session functions."""

    def __init__(self, session: nox.Session) -> None:
        """Initialize."""
        self.session = session
        self.pdm = _PDM(session)

    def install(self, *args: str, **kwargs: Any) -> None:
        try:
            requirements = self.export_requirements()
        except CommandSkippedError:
            return
        else:
            self.session.install(f"--constraint={requirements}", *args, **kwargs)

    def export_requirements(self) -> Path:
        """Export a requirements file from PDM.

        This function uses
        `pdm export <https://pdm-project.org/2.12/usage/advanced/#export-requirementstxt>`_
        to generate a :ref:`requirements file <Requirements Files>` containing the
        project dependencies at the versions specified in ``pdm.lock``. The
        requirements file includes both core and development dependencies.

        The requirements file is stored in a per-session temporary directory,
        together with a hash digest over ``pdm.lock`` to avoid generating the
        file when the dependencies have not changed since the last run.

        Returns:
            The path to the requirements file.
        """
        # Avoid ``session.virtualenv.location`` because PassthroughEnv does not
        # have it. We'll just create a fake virtualenv directory in this case.

        tmpdir = Path(self.session._runner.envdir) / "tmp"
        tmpdir.mkdir(exist_ok=True, parents=True)

        path = tmpdir / "requirements.txt"
        hashfile = tmpdir / f"{path.name}.hash"

        lockdata = Path("pdm.lock").read_bytes()
        digest = hashlib.blake2b(lockdata).hexdigest()

        if not hashfile.is_file() or hashfile.read_text() != digest:
            constraints = to_constraints(self.pdm.export())
            path.write_text(constraints)
            hashfile.write_text(digest)

        return path


def to_constraints(pdm_export: str) -> str:
    return pdm_export


class _PDM:

    def __init__(self, session: Session) -> None:
        """Initialize."""
        self.session = session
        # self._config: Optional[Config] = None
        # self._version: Optional[str] = None

    def export(self) -> str:
        """Export the lock file to requirements format.

        Returns:
            The generated requirements as text.

        Raises:
            CommandSkippedError: The command `pdm export` was not executed.
        """
        # dependency_groups = (
        #     [f"--group={group}" for group in self.config.dependency_groups]
        #     if self.has_dependency_groups
        #     else ["--dev"]
        # )

        output = self.session.run_always(
            "pdm",
            "export",
            "--format=requirements",
            # *dependency_groups,
            "--without-hashes",
            external=True,
            silent=True,
            stderr=None,
        )

        if output is None:
            raise CommandSkippedError(  # pragma: no cover
                "The command `pdm export` was not executed"
                " (a possible cause is specifying `--no-install`)"
            )

        return output


class CommandSkippedError(Exception):
    """The command was not executed by Nox."""
