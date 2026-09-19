from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {"id": 1, "title": "Firewall", "content": "Controls network traffic"},
    {"id": 2, "title": "IDS", "content": "Detects suspicious activity"}
]

@app.route("/")
def home():
    return "Cybersecurity Notes API"

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    for note in notes:
        if note["id"] == id:
            return jsonify(note)

    return jsonify({"error": "Note not found"}), 404

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()

    new_note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }

    notes.append(new_note)

    return jsonify(new_note), 201

if __name__ == "__main__":
    app.run(debug=True)