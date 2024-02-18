def test_constraints_versions_match():
    # TODO: read expected versions using tomli and pdm.lock
    import pytest

    assert pytest.__version__ == "8.0.0"

    import urllib3

    assert urllib3.__version__ == "2.1.0"
