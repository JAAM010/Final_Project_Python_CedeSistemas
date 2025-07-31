from database.connection import ConnectionFactory
from schemas.contenido import ContenidoOut, ContenidoCreate

def obtener_contenidos():
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, titulo, descripcion, fecha_lanzamiento, tipo_contenido FROM contenidos"
    )
    rows = cursor.fetchall()
    return [
        ContenidoOut(
            id=row[0],
            titulo=row[1],
            descripcion=row[2],
            fecha_lanzamiento=str(row[3]) if row[3] else None,
            tipo_contenido=row[4],
        )
        for row in rows
    ]

def crear_contenido(contenido: ContenidoCreate) -> ContenidoOut:
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contenidos (titulo, descripcion, fecha_lanzamiento, tipo_contenido)
        OUTPUT INSERTED.id, INSERTED.titulo, INSERTED.descripcion, INSERTED.fecha_lanzamiento, INSERTED.tipo_contenido
        VALUES (?, ?, ?, ?)
    """, (contenido.titulo, contenido.descripcion, contenido.fecha_lanzamiento, contenido.tipo_contenido))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return ContenidoOut(
        id = row.id,
        titulo = row.titulo,
        descripcion = row.descripcion,
        fecha_lanzamiento = row.fecha_lanzamiento,
        tipo_contenido = row.tipo_contenido
    )
        
    
