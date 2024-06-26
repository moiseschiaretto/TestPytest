# Projeto TestBlogAgi
- Autor Moisés Ademir Chiaretto
- Descrição das explicações de cada item da 'estrutura do projeto "TestBlogAgi" desenvolvido'.
- Python, Pytest, Playwright
<br>

|QA - Tester      |Python         |IDE PyCharm         |Playwright          |Cucumber          |HTML / CSS / JS    	|XPATH		|
|-----------------|---------------|--------------------|--------------------|------------------|--------------------|-----------|
| ![14_QA_TESTER](https://github.com/moiseschiaretto/TestPytest/assets/84775466/17b2e3d0-6a8b-4442-aa5d-5d0b295de871) | ![04_Python](https://github.com/moiseschiaretto/TestPytest/assets/84775466/2138c001-029a-4072-8150-be8bc4055411) | <img width="194" alt="PyCharm" src="https://github.com/moiseschiaretto/TestPytest/assets/84775466/a8eae923-fcb5-4ccf-b516-9ea9fd136945"> | ![05_Playwrigth](https://github.com/moiseschiaretto/TestPytest/assets/84775466/a06619a2-ffc6-4213-b808-35fcb44f75fc) | <img width="198" alt="Cucumber" src="https://github.com/moiseschiaretto/TestPytest/assets/84775466/0de732a5-242c-4707-a3a2-94aab6c354b0"> | <img width="236" alt="00_HTML_CSS_JS" src="https://github.com/moiseschiaretto/TestPytest/assets/84775466/76f91713-7691-4797-b255-6a6030cf1492"> | <img width="142" alt="00_XPATH" src="https://github.com/moiseschiaretto/TestPytest/assets/84775466/91fab5a5-0325-4ec0-be3d-7570f931caae"> |



<br>

## Estrutura do Projeto "TestBlogAgi"

```

TestBlogAgi
|
|-----requeriments.txt
|-----.venv
|-----pytest.ini
|-----.gitgnore
|-----README.md
|
|_____steps
|       |____assets
|       |____evidencias
|       |____conftest.py
|       |____test_pesquisa.py
|       |____report.html
|       
|-----tests
|       |____features
|               |____pesquisa.feature
|
|-----teste1_numeros_multiplos_3_5_15.py


```

## Arquivo 'requeriments.txt'
Constam todas as 'bibliotecas' do projeto para serem instaladas.

```
pytest>=8.2.0
pytest-bdd>=7.1.2
pytest-playwright>=0.4.4
playwright>=1.43.0
pytest-html>=4.1.1
```

## Diretório virtual '.venv' do ambiente virtual 
Projeto que contém todas informações do projeto, e consta o diretório 'Lib' com todas as dependências / bilioteclas udadas no projeto, para facilitar a manutenção ou uso do projeto por outro DEV/QA temos consta o arquivo 'requeriments.txt' com as bibliotecas necessárias para serem instaladas referente ao projeto. 

## Arquivo 'pytest.ini'
Constam os caminhos dos arquivos '.feature' referente a funcionalidade e os cenários do BDD.
E o caminho dos arquivos 'test_*.py' de execução dos métodos da 'feature do BDD'.

```
[pytest]
python_files = test_*.py
bdd_features_base_dir = tests\features\
```

## Arquivo '.gitignore'
Constam todos os diretórios e os arquivos que devem serem ignorados ao subir o código para o git (controle de versão).

```
/.venv/
/.pytest_cache/
/.idea/
/steps/__pycache__/
/steps/assets/
/steps/evidencias/
/steps/report.html
```

## Diretórios './tests/features/' 
Constam os arquivos '*.feature' que contém as **'funcionalidades e os cenários do BDD', arquivo [pesquisa.feature]**

```

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

```

- Escreve um cenário que passe **"Green"** e um cenário que falhe **"Red"**.


![BDD_SEM_E_COM_FALHA](https://github.com/moiseschiaretto/TestPytest/assets/84775466/7c384207-7d94-4b27-9b08-ed2866e56d31)


## Diretório './steps/' 
Constam os arquivos 'test_*.py' que contém em cada arquivo os métodos (código) relacionados a 'funcionalidade e os cenários do BDD', **arquivo [test_pesquisa.py]**

## Arquivo 'conftest.py' 
Contém as configurações de acesso ao 'browser' com a biblioteca 'Playwright' da Microsoft.
Com esta biblioteca não há necessidade de uso da biblioteca do 'selenium.webdriver' com os arquivos:
- chromedriver.exe (Navegador Google Chrome)
- geckodriver.exe (Navegador Mozilla Firefox)
  
**Por exemplo, e tendo que substituir estes arquivos no projeto a cada nova versão liberada do navegador Web.**

## Diretório './steps/evidencias/' 
Contém os 'screenshots', ou seja, as capturas de telas para evidenciar os testes realizados de forma automática, os arquivos de evidências:
- 01_img_bloagi.png
- 02_img_pesquisa_teste.png
- 03_img_resultado_pesquisa_teste.png
- 04_img_pesquisa_python.png
- 05_img_resultado_pesquisa_python.png

## Diretório './steps/assets' 
Será criado ao gerar o relatório 'report.html' da execução dos testes com o arquivo 'style.css', referente ao estilo do arquivo '*.html'.

## Arquivo 'report.html' 
Contém o relatório do resultado da execução dos testes, para abrir este arquivo:
- Clicar com o botão direito do mouse sobre o arquivo 'report.html'.
- Opção 'Open in' (IDE PyCharm)
- Selecionar:
- "Explorer" para visualizar o arquivo 'report.html' no diretório gerado.
- "Browser" para visualizar o arquivo 'report.html' direto em um dos navegadores: Chrome, Firefox, Edge (por exemplo).

## Passos para gerar o relatório 'report.html'
A biblioteca 'pytest-html' é informada no arquivo 'requeriments.txt' para a instalação, digitar os seguintes comandos no terminal da IDE PyCharm para a geração do relatório, **arquivo 'report.html:** 

```
pip install pytest-html
pytest test_pesquisa.py
pytest --html=report.html
```

## Teste 1 (um) do site
Corrigir a sintaxe do código 'Python', no arquivo **[teste1_numeros_multiplos_3_5_15.py].**
- Escreva um programa que imprima os números de 1 a 100.
- Mas para múltiplos de três imprima "Fizz", em vez do número.
- E para múltiplos de cinco imprima "Buzz".
- Para números múltiplos de três e cinco, imprima "FizzBuzz".

```
x mod 3 = Fizz
x mod 5 = Buzz
x mod 15 = FizzBuzz
```
