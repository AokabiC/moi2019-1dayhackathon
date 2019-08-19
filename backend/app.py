from flask import Flask, render_template, jsonify
from twitcasting_api import getUserInfo

DEBUG = True
app = Flask(__name__,
            static_folder='../frontend/dist/static',     
            template_folder='../frontend/dist'                      
)
app.config.from_object(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/userinfo/<userid>')
def userinfo(userid):
    return jsonify(getUserInfo(userid))


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run()