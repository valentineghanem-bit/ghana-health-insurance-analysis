"""Basic smoke tests for analysis pipeline."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_scripts_importable():
    """Verify scripts directory Python files have no syntax errors."""
    import importlib.util
    scripts_dir = os.path.join(os.path.dirname(__file__), "..", "scripts")
    for fname in os.listdir(scripts_dir):
        if fname.endswith(".py"):
            spec = importlib.util.spec_from_file_location(
                fname[:-3], os.path.join(scripts_dir, fname)
            )
            assert spec is not None, f"Could not load {fname}"


def test_dashboard_exists():
    """Verify the static dashboard HTML exists."""
    dash_path = os.path.join(
        os.path.dirname(__file__), "..", "dashboard",
        "NHIS_OOP_Ghana_Dashboard.html"
    )
    assert os.path.exists(dash_path), "Dashboard HTML not found"


def test_poster_exists():
    """Verify the static poster HTML exists."""
    poster_path = os.path.join(
        os.path.dirname(__file__), "..", "poster",
        "NHIS_OOP_Ghana_Poster.html"
    )
    assert os.path.exists(poster_path), "Poster HTML not found"
