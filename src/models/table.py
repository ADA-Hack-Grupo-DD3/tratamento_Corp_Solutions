

def create_table(conn: object,cursor: object, sql:str):
    """
    Cria uma tabela se não existir uma com o mesmo nome
    """
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {sql}")
    conn.commit()




def delete_table(conn: object,cursor: object, table_name:str) -> None:
    """
    Deleta a tabela passada caso ela exista
    """
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    conn.commit()




def insert_value(conn: object, cursor: object, table:str, values:tuple)-> None:

    query = f"""
    INSERT INTO {table} (id, name, gender, age, race, study, state, time, department, seniority, entry_age)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, values)
    conn.commit()


def remove_value(conn: object, cursor: object, table: str, condition: str)-> None:
    """
    Remove do BD os itens que condizem com a condição passada
    """
    
    query = f"DELETE FROM  {table} WHERE {condition}"
    cursor.execute(query)
    conn.commit()
    
def count_values(conn: object, cursor: object, table: str)-> int:
    """
    Conta quantos itens tem na coluna passada
    """
    
    query = f"SELECT COUNT(*) FROM {table};"
    cursor.execute(query)
    return cursor.fetchone()[0]
    
def get_value(cursor: object, table: str, condition: str) -> tuple:
    query = f"SELECT * FROM {table} WHERE {condition}"
    cursor.execute(query)
    return cursor.fetchall()