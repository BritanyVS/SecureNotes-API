from flask import Blueprint, request
from app.database import get_db_connection

bp = Blueprint('main', __name__)



@bp.route('/notes', methods=['GET'])
def get_notes():
    search_term = request.args.get('search', '')

    conn = get_db_connection()
    cursor = conn.cursor()


    query = f"SELECT id, title, content FROM Notes WHERE title LIKE '%{search_term}%'"

    cursor.execute(query)
    notes = cursor.fetchall()

    conn.close()

    return {"notes": [str(note) for note in notes]}