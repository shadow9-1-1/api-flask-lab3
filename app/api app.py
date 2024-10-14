from flask import Flask, request, jsonify
from routes.books import book_ro
app = Flask(__name__)


#Register blueprint
app.register_blueprint(book_ro)

#Run
if __name__ == "__main__":
    app.run(port=3000, debug=True)
