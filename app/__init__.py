#import bibliotek
from flask import Flask

#utowrzenie instancji(obiektu) klasy Flask reprezentującej aplikację
app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True, host = '127.0.0.1', port=5000)