Bem vindo ao nosso projeto do Hackaton
<h1>Sumário</h1>
        <ul>
            <li><a href="#tratamento">Tratamento Corpo Solution</a>
                <ul>
                    <li><a href="#etl">Extração, Transformação e Carregamento(ETL) dos Dados</a>
                        <ul>
                            <li><a href="#dsbasededados">Base de Dados</a></li>
                            <li><a href="#dsstateofdata">State of Data</a></li>
                            <li><a href="#dsibge">IBGE</a></li>
                        </ul>
                    </li>
                    <li><a href="#dependencias">Dependências necessárias</a>
                        <ul>
                            <li><a href="#passoapasso">Passo a Passo</a></li>
                            <li><a href="#bancodedados">Banco de Dados</a></li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
 
 
<h2 id="etl">Extração, Transformação e Carregamento(ETL) dos Dados</h1>
O processo de ETL é fundamental na gestão e análise de dados. Ele compreende três etapas principais:

1. <b>Extração</b>: Nesta etapa, os dados são coletados de suas fontes de origem, que podem incluir bancos de dados, arquivos, APIs ou outras fontes de dados. A extração envolve acessar e capturar os dados brutos de suas fontes e transferi-los para um ambiente de armazenamento centralizado.

2. <b>Transformação</b>: Após a extração, os dados brutos passam por processos de transformação para prepará-los para análise. Isso pode incluir limpeza de dados, padronização de formatos, remoção de duplicatas, correção de erros e agregação de informações. A transformação visa garantir que os dados estejam consistentes, precisos e prontos para serem utilizados nas análises.

3. <b>Carregamento</b>: Por fim, os dados transformados são carregados em um destino final, como um data warehouse, um banco de dados ou uma ferramenta de análise. Nesta etapa, os dados são organizados e estruturados de forma adequada para facilitar o acesso e a consulta posterior. O carregamento pode ser realizado de forma incremental, adicionando novos dados aos já existentes, ou de forma completa, substituindo os dados antigos pelos novos.

O processo de ETL é essencial para garantir a qualidade e a integridade dos dados, preparando-os para serem utilizados em análises e tomadas de decisão. Ele proporciona uma base sólida para a realização de análises de dados eficazes e ajuda a garantir que as informações obtidas sejam confiáveis e relevantes para os objetivos do negócio.

<h3 id="dsbasededados"> Base de Dados</h3>
<h3 id="dsstateofdata"> State of Data</h3>

O segundo conjunto de dados com o qual vamos trabalhar neste projeto é originado da comunidade _Data Hackers_, denominado **State_of_data_2022.csv**. Essa pesquisa foi conduzida em 2022 e seus dados foram divulgados em 2023, fornecendo informações sobre pessoas ligadas à área de dados. Uma observação importante é que uma pesquisa mais recente foi realizada em 2023, porém o conjunto de dados completo ainda não foi divulgado até a presente data. Utilizaremos este conjunto de dados para fazer uma comparação com os dados da Corp Solutions, a fim de obtermos um ponto de comparação e identificar insights.

O arquivo conta com 4271 registros distribuídos em 353 colunas. Devido à complexidade e ao tamanho do arquivo, optamos por realizar o processo de limpeza dos dados diretamente pelo Excel. Para isso, transformamos o arquivo de **CSV** para **XLXS**, desta forma retirando a separação dos registros por vírgula. Para deixar o arquivo o mais próximo possível da base de dados da Corp Solutions, excluímos 347 colunas, deixando apenas as que iríamos necessitar para análise, conforme abaixo:

|id|Gênero|Idade|Raça|Formação|Estado|Senioridade|
|---|---|---|---|---|---|---|
|1|Masc|39|Parda|Pós-graduação|Distrito Federal|Analista Júnior|
|2|Masc|32|Parda|Ensino Superior|Pará|Gerente|
|3|Masc|53|Branca|Pós-graduação|Distrito Federal|Analista Pleno|
|4|Masc|27|Branca|Doutorado|Minas Gerais|Analista Sênior|
|5|Fem|46|Branca|Pós-graduação|Pará|Analista Pleno|

Além da exclusão das colunas que diferenciavam este conjunto de dados do da Corp Solutions, modificamos os títulos para que ficassem condizentes com os títulos do conjunto de dados da Corp Solutions. Também realizamos o processo de alteração de alguns dados que estavam fora do padrão _UTF-8_, utilizando a função de localizar/substituir do próprio Excel. O arquivo foi salvo com o nome de **State of Data 2022 - Modificada.xlsx** para melhor compreensão em relação ao processo de limpeza dos dados do dataset.

<h3 id="dsibge"> IBGE</h3>

O terceiro conjunto de dados que utilizaremos em nossa análise é um conjunto de dados sobre o censo de 2022. Ele será empregado para identificar correlações entre os padrões de cor/raça dos funcionários da Corp Solutions e os dados do censo coletados no ano de 2022. Nosso objetivo é identificar padrões e possíveis disparidades em relação à cor e raça dentro da empresa, em comparação com os dados do Brasil. O conjunto de dados do censo mostra a quantidade de pessoas por estado, classificadas de acordo com sua cor/raça, divididas em Branco, Preto, Amarelo, Pardo e Indígena.

Assim como fizemos com os dados do conjunto de dados da comunidade _Data Hackers_, optamos por realizar o processo de limpeza diretamente no arquivo deste dataset. Removemos as somatórias dos valores totais e as macrorregiões do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste e Sul). Também eliminamos as variações e os dados do censo realizados no ano de 2010, mantendo apenas os dados do ano de 2022. Adicionamos uma coluna com as macrorregiões do Brasil para facilitar a obtenção de insights futuros.

<img src="src/img/img1.png" alt="Dataset antes da ETL">
<b><i><small>Dataset antes da limpeza dos dados</small></b></i>

<img src="src/img/img2.png" alt="Dataset depois do processo de ETL">
<b><i><small>Dataset após a limpeza dos dados</small></b></i>

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

