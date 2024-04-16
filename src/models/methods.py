def create_employee()-> tuple | None:
    """
    Pega os Dados necessários para um novo usuário ser cadastrado
    
    Retorna uma tupla no seguinte formato:
        (id, name, gender, age, race, study, state, time, departament, seniority, entry_age)
    
    Caso haja dados invalidos, retorna:
        None
    
    """
    
    id = input("ID: ")
    name = input("Nome: ")
    gender = input("Gênero: ")
    age = input("Idade: ")
    race = input("Raça: ")
    study = input("Grau de Escolaridade: ")
    state = input("Estado: ")
    time = input("Tempo de Casa: ")
    departament = input("Departamento: ")
    seniority = input("Senioridade: ")
    entry_age = input("Ingressou na Empresa com Qual IDade: ")
    
    result = None
    
    
    if (id.isnumeric() and 
        len(name) > 0 and
        len(gender) == 3 and
        age.isnumeric() and
        len(race) > 0 and
        len(study) > 0 and
        len(state) > 0 and
        time.isnumeric() and
        len(departament) > 0 and
        len(seniority) > 0 and
        entry_age.isnumeric()) :
        result = (id, name, gender, age, race, study, state, time, departament, seniority, entry_age)
    
    return result