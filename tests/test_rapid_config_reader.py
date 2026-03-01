"""Tests for rapid-config-reader."""

import os
import tempfile
import pytest
from rapid_config_reader import reader


class TestReader:
    """Test suite for reader."""

    def test_basic(self):
        """Test basic usage with a real temp directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a sample file inside
            sample = os.path.join(tmpdir, "sample.txt")
            with open(sample, "w") as f:
                f.write("hello world")
            result = reader(tmpdir)
            assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            reader("")
        except (ValueError, TypeError, FileNotFoundError, OSError):
            pass  # Expected for path-based utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = reader(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
