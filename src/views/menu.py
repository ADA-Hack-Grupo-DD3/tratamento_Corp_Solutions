def main_menu():
    """
    Retorna uma funcionalidade de 1 a 5
    
    Erros:
         0 - Caso informe texto ao inves de número
        -1 - Caso informe um valor menor que 1 ou maior que 5 
    """
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Alterar")
    print("4 - Deletar")
    print("5 - Sair")
    
    result = input("Digite a opção desejada: ")
    
    if result.isnumeric():
        result = int(result)
        if result < 1 or result > 5:
            result = -1
            
    else:
        result = 0
    
    return result