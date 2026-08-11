"""
Handles the MySQL connection.
Edit the values below to match your local MySQL setup,
or set them as environment variables instead.
"""

import os
import sys
import mysql.connector as sql
from mysql.connector import Error

DB_CONFIG = {
    "host": os.getenv("FIT_DB_HOST", "localhost"),
    "user": os.getenv("FIT_DB_USER", "root"),
    "password": os.getenv("FIT_DB_PASSWORD", ""),
    "database": os.getenv("FIT_DB_NAME", "fit_project"),
}


def get_connection():
    """Returns a live MySQL connection, or exits with a clear error."""
    try:
        conn = sql.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print("\n[!] Could not connect to MySQL.")
        print(f"    Reason: {e}")
        print("    Check db_config.py (host/user/password) and that")
        print("    MySQL is running and schema.sql has been executed.\n")
        sys.exit(1)
