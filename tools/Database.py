
# Database class is used to interact with the database.
# Main functions are saving projects configurations. or some lib info

import os
import json
import sqlite3
from sqlite3 import Error
from rich.console import Console
from tools.i18n import i18n
from tools.env import prepare_env, prepare_project
from tools.config import cc_root_config

CC_ROOT_SQLITE_DB_FILE = "ccroot.db"

class Database:

    def __init__(self):
        global CC_ROOT_SQLITE_DB_FILE
        self.db_file = os.getenv("CC_ROOT_CONFIGS_DIR") + '/' + CC_ROOT_SQLITE_DB_FILE
        self.conn = self.create_connection()
        self.console = Console()
        self.initialize_database()

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            return self.conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def initialize_database(self):
        """ create tables if they do not exist """
        print("Initializing database...")

        # check if the tables exist
        tables = {
            "projects": """
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    path TEXT NOT NULL,
                    options TEXT,
                    libs TEXT,
                    configs TEXT,
                    version TEXT NOT NULL DEFAULT '0.0.1',
                    auto_version INTEGER DEFAULT 1
                );
            """,
            "libs": """
                CREATE TABLE IF NOT EXISTS libs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    version TEXT,
                    source TEXT,
                    build_commands TEXT,
                    install_commands TEXT
                );
            """
        }
        try:
            c = self.conn.cursor()
            for table_name, create_table_sql in tables.items():
                c.execute(create_table_sql)
            self.conn.commit()
            print("Database initialized.")
        except Error as e:
            self.console.print(f"Error initializing database: {e}", style="bold red")


    def execute_query(self, query, params=()):
        """ Execute a query with optional parameters """
        try:
            c = self.conn.cursor()
            c.execute(query, params)
            self.conn.commit()
            return c
        except Error as e:
            self.console.print(f"Error executing query: {e}", style="bold red")
            return None


def get_cc_db():
    return Database()