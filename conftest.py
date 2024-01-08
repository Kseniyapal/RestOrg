"""Base conftesr"""

import pytest


@pytest.fixture(autouse=True)
def create_data_base_connection(db):
    """Create database connection"""
    pass
