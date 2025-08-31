from tools.env import prepare_env, prepare_project

# Set up the web server
from flask import Flask, jsonify, send_from_directory

from flask_cors import CORS

import os
import json
import webbrowser

default_web_porting = 1688
if os.getenv("CCROOT_WEB_PORT"):
    default_web_porting = os.getenv("CCROOT_WEB_PORT")

prepare_env()
prepare_project(os.getcwd())

def has_local_web_domain():
    with open("/etc/hosts", "r") as f:
        hosts_content = f.read()
    return "ccroot.local" in hosts_content

def check_local_web_domain():
    # get /etc/hosts content
    hosts_content = ""

    if not has_local_web_domain():

        print("Do you want use ccroot.local to access the web server? (y/n): ", end="")
        choice = input().strip().lower()

        if choice == 'y':
            # add ccroot.local to /etc/hosts with sudo
            command = "echo '127.0.0.1 ccroot.local' | sudo tee -a /etc/hosts"
            os.system(command)

    else:
        print("ccroot.local already exists in /etc/hosts")
    # add ccroot.local to 127.0.0.1

def web_build():

    web_static_dir = os.environ.get("CC_ROOT_WEB_DIR")
    web_src_dir = web_static_dir+'/src'

    if not os.path.exists(web_src_dir):
        print("Web source dir not found: " + web_src_dir)
        return
    print("Building web static files...")
    os.system(f"cd {web_src_dir} && npm run build && cp -r {web_src_dir}/dist/* {web_static_dir}/app/")


def web_server():

    global default_web_porting

    web_static_dir = os.environ.get("CC_ROOT_WEB_DIR")

    app = Flask("cc_root_web_server")
    CORS(app)  # 允许所有跨域请求

    @app.route('/assets/<path:filename>')
    def custom_static(filename):
        print("Request for image: " + filename + " path is " + f"{web_static_dir}/assets/app/{filename}")
        return send_from_directory(f"{web_static_dir}/app/assets", filename)

    @app.route('/')
    def index():
        return send_from_directory(f"{web_static_dir}/app", 'index.html')

    @app.route('/status')
    def status():
        return jsonify({"status": "Running", "project_dir": os.environ.get("CC_ROOT_TARGET_DIR", "Not set")})

    @app.route('/toolchains')
    def toolchains():
        toolchains_config_dir = os.environ.get("CC_ROOT_CONFIGS_DIR") + "/toolchains"
        _toolchains = {}

        # toolchain dir tree is   chipset/target/version
        if os.path.exists(toolchains_config_dir):
            for chipset in os.listdir(toolchains_config_dir):
                chipset_path = os.path.join(toolchains_config_dir, chipset)
                if os.path.isdir(chipset_path):
                    _toolchains[chipset] = {}
                    for target in os.listdir(chipset_path):
                        target_path = os.path.join(chipset_path, target)
                        if os.path.isdir(target_path):
                            _toolchains[chipset][target] = {}
                            for version in os.listdir(target_path):
                                version_path = os.path.join(target_path, version)
                                if os.path.isdir(version_path):
                                    _toolchain_file = version_path+'/toolchains.json'
                                    if os.path.exists(_toolchain_file):
                                        with open(_toolchain_file, 'r') as file:
                                            _toolchains[chipset][target][version] = json.load(file)
                                    else:
                                        _toolchains[chipset][target][version] = "No toolchain file found"
        else:
            return jsonify({"error": "Toolchains directory not found"}), 404
        return jsonify(_toolchains)

    @app.route('/api/getToolchains')
    def get_toolchains():
        return toolchains()

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

    check_local_web_domain()

    # open home page on web browser
    # cc_domain = "ccroot.local" if has_local_web_domain() else "127.0.0.1"
    cc_domain = "127.0.0.1"
    webbrowser.open(f"http://{cc_domain}:{default_web_porting}")

    app.run(debug=True,port=default_web_porting)
