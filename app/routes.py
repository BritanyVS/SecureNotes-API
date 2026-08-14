from flask import Blueprint, request, render_template_string
from app.database import get_db_connection

bp = Blueprint('main', __name__)

# SQL Injection por concatenación directa
@bp.route('/notes', methods=['GET'])
def get_notes():
    search_term = request.args.get('search', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Consulta vulnerable
    query = f"SELECT id, title, content FROM Notes WHERE title LIKE '%{search_term}%'"
    cursor.execute(query)
    notes = cursor.fetchall()
    conn.close()
    
    return {"notes": [str(note) for note in notes]}

# XSS / Improper Input Validation
@bp.route('/feedback', methods=['POST'])
def submit_feedback():
    comment = request.form.get('comment', '')
    template = f"<h1>Gracias por tu comentario:</h1><p>{comment}</p>"
    return render_template_string(template)