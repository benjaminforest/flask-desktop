from flask import Flask
from flask import request
from webui import WebUI
app = Flask(__name__,
            static_url_path='/static',
            static_folder='',
            template_folder='')

ui = WebUI(app, debug=True, app_name="Salut")

@app.route('/post_form', methods=['POST'])
def return_form():
    info = request.data
    return f"Got {request.data}"

@app.route("/")
def home():
    return app.send_static_file('static/index.html'), 200
if __name__ == "__main__":
    ui.run()