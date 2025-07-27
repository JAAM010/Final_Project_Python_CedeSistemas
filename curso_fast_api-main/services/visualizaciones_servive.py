from database.connection import ConnectionFactory
from schemas.visualizacion import VisualizacionOut

def obtener_visualizacion():
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre,titulo,fecha_visualizacion FROM VISUALIZACIONES V JOIN USUARIOS U ON V.USUARIO_ID = U.ID JOIN CONTENIDOS C ON V.CONTENIDO_ID = C.ID "
    )
    rows = cursor.fetchall()
    return [
        VisualizacionOut(
            nombre=row[0],
            titulo=row[1],
            fecha_visualizacion=str(row[2]) if row[2] else None,
        )
        for row in rows
    ]

