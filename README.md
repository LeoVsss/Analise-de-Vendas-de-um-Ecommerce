Este projeto possui finalidade de estudos para a análise de dados. 
- Nenhum dado verídico foi utilizado

/Funcionalidades/

Esse programa conta com o processo de ETL (Extract, Transform, Load) que seria Extrair, Transformar, Carregar.

Com o objetivo de extrair dados de um arquivo .CSV, utilizei a biblioteca **Pandas** para criação de um dataframe contendo esses dados, 
para posteriormente ser possível limpar os dados. Durante o processo de Transform realizei a limpeza dos dados, trazendo 
o nome das colunas para português visando a acessibilidade de outras pessoas que consumirão essas análises. 
Para o armazenamento desses dados, realizei a inserção deles em um banco PostgreSQL, criando de forma automática as colunas no banco, por meio
da biblioteca **SQLAlchemy**.

O arquivo jupyter notebook foi utilizado como teste de chamada, para verificar as funções construídas.

/Resultados/

Os dados foram carregados no **PostgreSQL** com o objetivo de serem consumidos posteriormente pelo **Power BI**, assim criando análises inteligentes 
e relações entre as informações fornecidas.

Dados do .CSV inseridos no **PostgreSQL**:
<img width="1511" height="864" alt="image" src="https://github.com/user-attachments/assets/588dce65-828f-4b4b-a66e-a5a19aabb2a1" />

Dashboard interativo para Análise de métricas utilizando o **Power BI**:
<img width="1458" height="816" alt="image" src="https://github.com/user-attachments/assets/3b433a94-db99-42ad-a782-70b4f0c58ebd" />


