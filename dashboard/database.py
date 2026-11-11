
from pathlib import Path
import sys

# Identify the project root directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Add project root to Python path
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

# Reuse the existing PostgreSQL connection
from database_connection import get_connection


def fetch_data(query, params=None):
    """
    Execute a read-only SQL query and return results as a Pandas DataFrame.
    """
    import pandas as pd

    with get_connection() as connection:
        return pd.read_sql_query(query, connection, params=params)
