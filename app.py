from flask import Flask, request, jsonify
from models import db, Note
from utils import check_api_key, log_request
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Use absolute path for production (Render needs this)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'notes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
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
            if not note:
                return jsonify({"error": "Note not found"}), 404
            note.content = data['content']
            db.session.commit()
            return jsonify(note.serialize()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    if request.method == 'DELETE':
        try:
            note = Note.query.get(data['id'])
            if not note:
                return jsonify({"error": "Note not found"}), 404
            db.session.delete(note)
            db.session.commit()
            return jsonify({"message": "Deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

@app.route('/agent-config', methods=['GET'])
def config():
    return jsonify({
        "language": "en",
        "mode": "assistant",
        "version": "1.0"
    }), 200

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Makes Render use its port
    app.run(host='0.0.0.0', port=port)
