Bem vindo ao nosso projeto do Hackaton
<h1>Sumário</h1>
        <ul>
            <li><a href="#tratamento">Tratamento Corpo Solution</a>
                <ul>
                    <li><a href="#dependencias">Dependências necessárias</a>
                        <ul>
                            <li><a href="#passoapasso">Passo a Passo</a></li>
                            <li><a href="#bancodedados">Banco de Dados</a></li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
 
 
<h2 id="tratamento">Tratamento_Corp_Solutions</h1>
## Primeiros Passos Sobre o Projeto

<h2 id="dependencias"> Dependências necessárias</h2>
Para este projeto, vamos estar trabalhando usando linguagem Python em conjunto com suas ferramentas integradas. Portanto, recomendamos seguir as tecnologias indicadas nesta seção para conseguir compreender e ter uma experiência agradável neste projeto.

<h2 id="passoapasso"> Passo a Passo</h2>
- Instale o <a href="https://www.python.org/downloads/">Python</a> em sua versão 3.10 ou superior.
- Instale o Gerenciar de Pacotes Python Poetry atraves do tutorial feito pelo <a href="https://github.com/mauriciobenjamin700/Poetry-Learning">Mauricio Benjamin</a> ou apartir da <a href="https://python-poetry.org/docs/#installation">documentação oficial</a>.


- Instale as dependencias necessárias
```bash
poetry install
```

<h2 id="bancodedados"> Banco de Dados</h2>
Para acessar os dados processados, acesse nosso banco de dados postgreeSQL mantido na nuvem por meio do serviço <a href="https://www.elephantsql.com/">Elephant SQL</a>

Credenciais do Banco de dados (Copie apenas o conteúdo dentro das **aspas**):
- **database:** "ydgyztao",
- **host:** "isabelle.db.elephantsql.com",
- **user:** "ydgyztao",
- **password:** "6NrXuPaXhvTxfhXLd3xbXtb_VAaqtL3t",
- **port:** "5432".

Script SQL para gerar a tabela central com os registros
```sql
employee 
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(20),
    age INTEGER,
    race VARCHAR(20),
    study VARCHAR(20),
    state VARCHAR(20),
    time NUMERIC(5, 2),
    department VARCHAR(40),
    seniority VARCHAR(20),
    entry_age NUMERIC(5, 2)
)
```

Visualização previa (10 primeiras linhas) visando entender de como está a tabela central do banco de dados:

| id | name                                   | gender | age | race  | study           | state         | time | department                 | seniority       | entry_age |
|----|----------------------------------------|--------|-----|-------|-----------------|---------------|------|----------------------------|-----------------|-----------|
| 1  | Eleonora Arilda Penedo Gomes de Padilha | Fem    | 34  | pardo | Ensino Médio    | Santa Catarina | 12.0 | Compras                    | Analista Pleno | 22.0      |
| 2  | Elisângela Gabrielle de Osório        | Fem    | 26  | pardo | Ensino Médio    | Pará          | 6.0  | Contabilidade              | Analista Júnior| 20.0      |
| 3  | José Túlio de Cabral                  | Masc   | 35  | pardo | Ensino Médio    | Santa Catarina | 5.0  | Vendas                     | Analista Pleno | 30.0      |
| 4  | Ezequiel Edivaldo de Medeiros Sonao   | Masc   | 24  | pardo | Ensino Superior | Tocantins     | 4.0  | Administrativo             | Gerente         | 20.0      |
| 5  | Fagner Josiel dos Santos              | Masc   | 21  | pardo | Ensino Superior | Ceará         | 5.0  | Recursos Humanos           | Analista Júnior| 16.0      |
| 6  | Magali Luzimara da Silva              | Fem    | 49  | pardo | Ensino Superior | São Paulo     | 3.0  | Contabilidade              | Analista Pleno | 46.0      |
| 7  | Victor Plínio Shufrouze               | Masc   | 29  | pardo | Pós graduação   | Ceará         | 9.0  | Compras                    | Analista Sênior| 20.0      |
| 8  | Laércio Rossi                          | Masc   | 35  | pardo | Ensino Superior | Rondônia      | 8.0  | Operações                  | Analista Júnior| 27.0      |
| 9  | Francisco Ângelo de Toledo Seixas      | Masc   | 40  | pardo | Mestrado        | Amapá         | 1.0  | Administrativo             | Analista Pleno | 39.0      |
| 10 | Fabrício Rangel de Gonçalves dos Santos| Masc  | 33  | pardo | Ensino Superior | Minas Gerais  | 3.0  | Desenvolvimento de Produtos| Analista Pleno | 30.0      |

