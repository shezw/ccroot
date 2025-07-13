from tools.env import prepare_env, prepare_project

# Set up the web server
from flask import Flask, jsonify

import os
import json

def web_server():

    prepare_env()
    prepare_project(os.getcwd())

    app = Flask("cc_root_web_server")

    @app.route('/')
    def index():
        return 'Welcome to the CC Root Web Server!<br>' \
                '<a href="/status">Status</a><br>' \
                '<a href="/docs">Documentation</a>'

    @app.route('/status')
    def status():
        return jsonify({"status": "Running", "project_dir": os.environ.get("CC_ROOT_TARGET_DIR", "Not set")})

    @app.route('/docs')
    def docs():
        docs_path = os.path.join(os.environ.get("CC_ROOT_DIR", ""), "README.md")
        if os.path.exists(docs_path):
            with open(docs_path, 'r') as file:
                content = file.read()

            # Convert Markdown to HTML or return as plain text
            html_content = f"<pre>{content}</pre>"
            return html_content
        else:
            return jsonify({"error": "Documentation not found"}), 404

    app.run(debug=True)