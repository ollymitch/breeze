from flask import Flask
app = Flask(__name__)

@app.route("/")
def advice():
    return "Don't cycle in between two red buses!"

print('damn')
if __name__ == 'main':
    print('ayo')
    app.run(debug=True, host='0.0.0.0')


app.run(debug=True, host='0.0.0.0', port=2418)