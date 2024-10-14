from flask import Flask, request, jsonify

app = Flask(__name__)

middleware = []

TOKEN = "apipass123"

books = []

#Authentication
@app.before_request
def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401



#Routes
#Get /books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

#Post /books
@app.route("/books", methods=["POST"])
def create_book():
    book = {
        "id": len(books) + 1,
        "title": request.json.get("title"),
        "price": request.json.get("price"),
        "quantity": request.json.get("quantity", 0),
    }
    books.append(book)
    return jsonify(book), 201


#Put 
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["price"] = request.json.get("price", book["price"])
    book["quantity"] = request.json.get("quantity", book["quantity"])
    return jsonify(book)

#Delete
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return '', 204

#Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

#Run
if __name__ == "__main__":
    app.run(port=3000)
