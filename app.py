from flask import Flask, request, jsonify
from models import db, Note
from utils import check_api_key, log_request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def before():
    log_request(request)
    check_api_key(request)

@app.route('/notes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def notes():
    if request.method == 'GET':
        notes = Note.query.all()
        return jsonify([n.serialize() for n in notes]), 200

    data = request.json
    if request.method == 'POST':
        try:
            new_note = Note(content=data['content'])
            db.session.add(new_note)
            db.session.commit()
            return jsonify(new_note.serialize()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    if request.method == 'PUT':
        try:
            note = Note.query.get(data['id'])
            note.content = data['content']
            db.session.commit()
            return jsonify(note.serialize()), 200
        except:
            return jsonify({"error": "Note not found or update failed"}), 400

    if request.method == 'DELETE':
        try:
            note = Note.query.get(data['id'])
            db.session.delete(note)
            db.session.commit()
            return jsonify({"message": "Deleted"}), 200
        except:
            return jsonify({"error": "Delete failed"}), 400

@app.route('/agent-config', methods=['GET'])
def config():
    return jsonify({
        "language": "en",
        "mode": "assistant",
        "version": "1.0"
    }), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
