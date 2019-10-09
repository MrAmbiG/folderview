from flask import Flask, abort, send_file, render_template
import os

app = Flask(__name__)

ppath = "/home/gaambi11/Documents/reports" # update your own parent directory here

from flask_autoindex import AutoIndex

app = Flask(__name__)
AutoIndex(app, browse_root=ppath)    


if __name__ == "__main__":
    app.run()

    