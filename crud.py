from database import get_connection

def cadastrar_cliente(nome,telefone,email):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM pacientes WHERE nome = %s AND telefone = %s AND email = %s',(nome,telefone,email))
        paciente_existe = cur.fetchone() is not None
        if paciente_existe:
            return{"mensagem" : "Esse Paciente já está cadastrado"}
        else:
            cur.execute('INSERT INTO pacientes (nome,telefone,email) VALUES (%s,%s,%s) RETURNING id',(nome,telefone,email))
            row = cur.fetchone()
            conn.commit()
            return{"mensagem" : "Paciente Cadastrado"}
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cur.close()
        conn.close()

def procurar_cliente(nome,telefone):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM pacientes WHERE nome = %s OR telefone = %s',(nome,telefone))
        row = cur.fetchone()
        if row is None:
            return{"mensagem" : "Nnehum Usuário Encontrado"}
        else:
            cur.execute('SELECT * FROM pacientes WHERE nome = %s OR telefone = %s',(nome,telefone))
            conn.commit()
            return{"paciente": row}
    except Exception:
        conn.rollback()
        
