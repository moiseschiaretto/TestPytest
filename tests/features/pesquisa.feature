Feature: Pesquisar
    O usuário realizar duas pesquisas no blog "https://blogdoagi.com.br"

    Background: Acessar o blogdoagi e o botão de pesquisa
        Given que o usuário esteja no blogdoagi
        When o usuário clicar no botão de pesquisar
        And clicar e limpar o campo de pesquisa

    Scenario: Pesquisa válida
        And digitar o conteúdo existente, texto teste
        And teclar ENTER
        Then o blog deverá retornar os resultados referentes ao texto teste informado

    Scenario: Pesquisa inválida
       And digitar o conteúdo inexistente, texto python
       And teclar ENTER
       Then o blog deverá retornar os resultados referentes ao texto python informado
