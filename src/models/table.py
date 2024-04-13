

def create_table(conn: object,cursor: object, sql:str) -> bool:
    result = False
    try:
        # Executando a consulta SQL para criar uma tabela
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {sql}")
        conn.commit()
        result = True
    except:
        pass
    
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


def insert_table(conn: object, cursor: object, table_name:str, values:str)-> bool:
    result = False
    try:
        # Executando a consulta SQL para deletar a tabela
        delete_table_query = f'INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(delete_table_query, values)
        conn.commit()
        result = True
    except:
        pass
    
    return result
