from flask import Flask

app = Flask(__name__)


@app.route("/bot", methods=['POST'])
def bot():
    # add webhook logic here and return a response
    pass


if __name__ == '__main__':
    app.run()