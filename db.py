import sqlite3


def get_connection():
    conn = sqlite3.connect("agencia.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT,
        telefone TEXT,
        documento TEXT UNIQUE,
        criado_em TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS viagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        destino TEXT NOT NULL,
        data_ida TEXT,
        data_volta TEXT,
        qtd_viajantes INTEGER DEFAULT 1,
        passagem INTEGER DEFAULT 0,
        hospedagem INTEGER DEFAULT 0,
        carro INTEGER DEFAULT 0,
        seguro INTEGER DEFAULT 0,
        status TEXT DEFAULT 'RASCUNHO',
        criado_em TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );
    """
    )
    conn.commit()
    conn.close()


import sqlite3


def insert_client(name, email=None, phone=None, document=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone, documento) VALUES (?, ?, ?, ?)",
            (name, email, phone, document),
        )

        conn.commit()
        new_id = cursor.lastrowid
        return new_id

    except sqlite3.IntegrityError as e:
        raise ValueError(
            "Não foi possível inserir: documento já cadastrado (ou violação de integridade)."
        ) from e

    finally:
        conn.close()


def list_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, nome, email, telefone, documento FROM clientes ORDER BY id;"""
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_clients_name(term):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, nome, email, telefone, documento FROM clientes WHERE nome LIKE ?""",
        (f"%{term}%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_clients_email(term):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, nome, email, telefone, documento FROM clientes WHERE email LIKE ?""",
        (f"%{term}%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_clients_document(term):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, nome, email, telefone, documento FROM clientes WHERE documento LIKE ?""",
        (f"%{term}%",),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def get_client(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, nome, email, telefone, documento FROM clientes WHERE id = ?""",
        (client_id,),
    )
    result = cursor.fetchone()
    conn.close()
    return result


def get_trip(trip_id) -> tuple | None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT id, cliente_id, destino, status FROM viagens WHERE id = ?""",
            (trip_id,),
        )
        result = cursor.fetchone()
        return result
    finally:
        conn.close()


def get_trip_full(trip_id) -> tuple | None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, cliente_id, destino, data_ida, data_volta, qtd_viajantes, passagem, hospedagem, carro, seguro, status 
            FROM viagens WHERE id = ?;
            """,
            (trip_id,),
        )
        result = cursor.fetchone()
        return result
    finally:
        conn.close()


def update_trip(
    trip_id,
    destino,
    data_ida,
    data_volta,
    qtd_viajantes,
    passagem,
    hospedagem,
    carro,
    seguro,
):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE viagens SET destino = ?, data_ida = ?, data_volta = ?, qtd_viajantes = ?, passagem = ?, hospedagem = ?,
            carro = ?, seguro = ? WHERE id = ?""",
            (
                destino,
                data_ida,
                data_volta,
                qtd_viajantes,
                passagem,
                hospedagem,
                carro,
                seguro,
                trip_id,
            ),
        )
        conn.commit()
        updated_rows = cursor.rowcount
        return updated_rows
    finally:
        conn.close()


def update_trip_status(trip_id, new_status):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE viagens SET status = ? WHERE id = ?""",
            (
                new_status,
                trip_id,
            ),
        )
        conn.commit()
        updated_rows = cursor.rowcount
        return updated_rows
    finally:
        conn.close()


def insert_trip(
    client_id,
    destination,
    start_date,
    end_date,
    travelers_qty,
    flight,
    hotel,
    car,
    insurance,
    status="RASCUNHO",
):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO viagens
            (cliente_id, destino, data_ida, data_volta, qtd_viajantes,
             passagem, hospedagem, carro, seguro, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                client_id,
                destination,
                start_date,
                end_date,
                travelers_qty,
                flight,
                hotel,
                car,
                insurance,
                status,
            ),
        )

        conn.commit()
        return cursor.lastrowid

    except sqlite3.IntegrityError as e:
        raise ValueError("Cliente não encontrado ou erro de integridade.") from e

    finally:
        conn.close()


def list_trips_by_client(client_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """ 
            SELECT id, destino, data_ida, data_volta, qtd_viajantes, passagem, hospedagem, carro, seguro, status 
            FROM viagens WHERE cliente_id = ? ORDER BY id DESC;
            """,
            (client_id,),
        )
        result = cursor.fetchall()
        return result
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print(get_client(1))
