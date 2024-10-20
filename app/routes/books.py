from flask import Blueprint, request, jsonify
from middleware.Authorization import authenticate_token

book_ro = Blueprint("books", __name__)

books = []

#Authentication check before request
@book_ro.before_request
def before_request():
    authenticate_token()


#Routes
#Get /books
@book_ro.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

#Get by id/books
@book_ro.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

#Post /books
@book_ro.route("/books", methods=["POST"])
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
@book_ro.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = next((b for b in books if b["id"] == id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["price"] = request.json.get("price", book["price"])
    book["quantity"] = request.json.get("quantity", book["quantity"])
    return jsonify(book)

#Delete
@book_ro.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return '', 204

#Error handling
@book_ro.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404
