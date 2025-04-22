from mysql.connector import Error
from fastapi import APIRouter

from db.DatabaseConnector import DatabaseConnector

router = APIRouter(prefix="/content", tags=["Content"])
db = DatabaseConnector()

@router.get("/")
async def get_all_content():
    try:
        data = db.get_connection()
        cursor = data.cursor()

        if cursor:
            cursor.execute("SELECT * FROM contents")
            return cursor.fetchall()

    except Error as e:
        print(f'Verbindung Fehlgeschlagen: {e}')

@router.get("/{content_id}")
async def get_content_by_id(content_id: int):
    try:
        data = db.get_connection()
        cursor = data.cursor()

        sql = f"SELECT * FROM contents WHERE id={content_id}"
        if cursor:
            cursor.execute(sql)
            return cursor.fetchone()

    except Error as e:
        print(f'Verbindung Fehlgeschlagen: {e}')