

def create_table(conn: object,cursor: object, sql:str) -> bool:
    result = False
    #try:
        # Executando a consulta SQL para criar uma tabela
        
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {sql}")
    conn.commit()
    result = True
    #except:
    #    pass
    
    return result


def delete_table(conn: object,cursor: object, table_name:str) -> bool:
    result = False
    try:
        # Executando a consulta SQL para deletar a tabela
        
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        conn.commit()
        result = True
    except:
        pass
    
    return result


def insert_value(conn: object, cursor: object, table:str, values:tuple)-> bool:
    result = False
    #try:
        # Executando a consulta SQL para deletar a tabela
    query = f"""
    INSERT INTO {table} (id, name, gender, age, race, study, state, time, department, seniority, entry_age)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, values)
    conn.commit()
    result = True
    #except:
    #    pass
    
    return result

def remove_value(conn: object, cursor: object, table: str, condition: str)-> bool:
    #DELETE FROM employee WHERE age < 18;
    
    query = f"DELETE FROM  {table} WHERE {condition}"
    cursor.execute(query)
    conn.commit()
    
def count_values(cursor: object, table: str)-> bool:
    #DELETE FROM employee WHERE age < 18;
    
    query = f"SELECT COUNT(*) FROM {table};"
    cursor.execute(query)
    return cursor.fetchone()[0]
    
def get_value(cursor: object, table: str, condition: str) -> tuple:
    query = f"SELECT * FROM {table} WHERE {condition}"
    cursor.execute(query)
    return cursor.fetchall()