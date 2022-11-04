# list_pull_requests

<h2>Desafio de listagem de Pull Requests</h2>

<p>
Times de desenvolvimento adotam processos de code review em suas rotinas para
garantir a qualidade do código desenvolvido. Como DevOps, precisamos trabalhar
em soluções que facilitem o time a fazer tal processo.
O desafio de desenvolvimento consiste em criar um código executável na linguagem
de programação de seu preferência que deve atender aos seguintes requisitos:
</p>

1. O código deverá consultar a API do GitHub e retornar todos os Pull Requests(PR) que estejam em aberto;
2. Caso não tenha nenhum Pull Request em aberto, o código não deve fazer
nenhuma ação;
3. Caso existam Pull Requests em aberto, o código deverá imprimir o título e o Link do Pull Request concatenado em uma string de forma paginada, respeitando o limite de 10 PR’s;
4. Utilize docker e docker-compose para a criação de um ambiente que tenha todos os requisitos necessários para a execução do código.

<h4>Observações:</h4>
- O uso de bibliotecas está liberado para facilidade o desenvolvimento da
funcionalidade;
- De preferência para o uso de linguagens mais comuns de serem usadas na
área de DevOps (Ex: Python, Shell Script, JavaScript...);
- Junto com o código desenvolvido, devem ser enviadas (respeitando a LGPD)
as instruções de como executá-lo e os requerimentos necessários para tal.


---
> Buildar a imagem docker: docker build -t gt-api .
> Rodar a app com o dockar: docker run -t gt-api --project_path=Diulia/list_pulll_requests

Argumentos da app:
- --project_path: Caminho do projeto no Github (usuário/repo)
- page: Indexação da listagem
- per_page: Quantidade de itens por página