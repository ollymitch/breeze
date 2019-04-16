from flask import Flask
app = Flask(__name__)

@app.route("/")
def advice():
    return "Don't cycle in between two red buses, and remember to charge your lights.\n\n:-) heyyy"

print('damn')
if __name__ == 'main':
    print('ayo')
    app.run(debug=True, host='localhost')


app.run(debug=True, host='localhost', port=8080)
