# This is the main class for managing projects in the tool.
import os
import json

from tools.Database import get_cc_db


class ProjectConfig:
    def __init__(self):
        self.Target = ""
        self.Toolchain = ""
        self.Host = ""


class Project:
    def __init__(self):
        self.Name = ""
        self.Path = ""
        self.Options:[ProjectConfig] = []
        self.Libs = []
        self.Configs = []


def has_project():
    _current_dir = os.getcwd()
    db = get_cc_db()
    cursor = db.conn.cursor()
    cursor.execute("SELECT * FROM projects WHERE path=?", (_current_dir,))
    row = cursor.fetchone()
    return row is not None

def init_project(project_dir):
    db = get_cc_db()
    cursor = db.conn.cursor()

    project = Project()
    project.Name = os.path.basename(project_dir)
    project.Path = project_dir
    project.Options = []
    project.Libs = []
    project.Configs = []

    # insert the project into the database
    cursor.execute(
        "INSERT INTO projects (name, path, options, libs, configs) VALUES (?, ?, ?, ?, ?)",
        (
            project.Name,
            project.Path,
            json.dumps([vars(opt) for opt in project.Options]),
            json.dumps(project.Libs),
            json.dumps(project.Configs)
        )
    )
    db.conn.commit()
    print(f"Project {project.Name} initialized at {project.Path}")