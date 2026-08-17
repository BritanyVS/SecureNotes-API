from flask import Blueprint, request
from app.database import get_db_connection

bp = Blueprint('main', __name__)


# SQL Injection - vulnerabilidad intencional para el laboratorio
@bp.route('/notes', methods=['GET'])
def get_notes():
    search_term = request.args.get('search', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta vulnerable: SQL Injection
    query = f"SELECT id, title, content FROM Notes WHERE title LIKE '%{search_term}%'"

    cursor.execute(query)
    notes = cursor.fetchall()

    conn.close()

    return {"notes": [str(note) for note in notes]}