from pathlib import Path

import pytest

THIS_DIR = Path(__file__).parent
mesa_run_path = THIS_DIR / "mesa_run"


# need to load MESA-Web run output, for test loading
@pytest.fixture
def history_fname():
    return mesa_run_path / "trimmed_history.data"


@pytest.fixture
def index_fname():
    return mesa_run_path / "profiles.index"


@pytest.fixture
def profile_fname():
    return mesa_run_path / "profile123.data"
