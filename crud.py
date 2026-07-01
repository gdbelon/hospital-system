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
            cur.execute('INSERT INTO pacientes (nome,telefone,email) VALUES (%s,%s,%s)',(nome,telefone,email))
            conn.commit()
            return{"mensagem" : "Paciente Cadastrado"}
    except Exception as e:
        conn.rollback()
        return{"erro" : str(e)}
    finally:
        cur.close()
        conn.close()

def procurar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM pacientes WHERE id = %s', (id,))
        row = cur.fetchone()
        if row is None:
            return {"mensagem": "Nenhum usuário encontrado"}
        
        colunas = []
        for desc in cur.description:
            colunas.append(desc[0])
        return dict(zip(colunas, row))
    except Exception as e:
        conn.rollback()
        return {"erro": str(e)}
    finally:
        cur.close()
        conn.close()

def alterar_dados_paciente(nome,telefone,email,id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('UPDATE pacientes SET nome = %s, telefone = %s, email = %s WHERE id = %s',(nome,telefone,email,id))
        conn.commit()
        return {"mensagem" : "Atualização feita com sucesso"}
        
    except Exception as e:
        conn.rollback()
        return {"erro" : str(e) }
    finally:
        conn.close()
        cur.close()
        
def deletar_paciente(id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM pacientes WHERE id = %s',(id,))
        row = cur.fetchone()
        if row is None:
            return{"mensagem":"Nnehum Usuário Encontrado"}
        cur.execute('DELETE FROM pacientes WHERE id = %s',(id,))
        conn.commit()
        return{"sistema" : f"Usuário {row} Deletado"}
    except Exception as e:
        conn.rollback()
        return{"erro" : str(e)}
    finally:
        conn.close()
        cur.close()
        
