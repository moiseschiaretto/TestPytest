# Projeto TestBlogAgi
- Autor Moisés Ademir Chiaretto
- Descrição das explicações de cada item da 'estrutura do projeto "TestBlogAgi" desenvolvido'.
- Python, Pytest, Playwright

## Estrutura do Projeto "TestBlogAgi"

```     .
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
Constam o caminho dos arquivos '.feature' referente a funcionalidade e cenários do BDD.
E o caminho dos arquivos 'test_*.py' de execução dos métodos da 'feature do BDD'.

```
[pytest]
python_files = test_*.py
bdd_features_base_dir = tests\features\
```

## Arquivo '.gitignore'
Constam todos os diretórios e arquivos que devem serem ignorados ao subir o código para o git (controle de versão).

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
Constam os arquivos '*.feature' que contém as 'funcionalidades e cenários do BDD', **arquivo [pesquisa.feature]**

## Diretório './steps/' 
Constam os arquivos 'test_*.py' que contém em cada arquivo os métodos (código) relacionados a 'funcionalidade e os cenários do BDD', **arquivo [test_pesquisa.py]**

## Arquivo 'conftest.py' 
Contém as configurações de acesso ao 'browser' com a biblioteca 'Playwright' da Microsoft.
Com esta biblioteca não há necessidade de uso da biblioteca do 'selenium.webdriver' com os arquivos:
- chromedriver.exe (Navegador Google Chrome)
- geckodriver.exe (Navegador Mozilla Firefox)
  
**Por exemplo, e tendo que substituir estes arquivos no projeto a cada nova versão liberada do navegador Web.**

## Diretório './steps/evidencias/' 
Contém os 'screenshot', ou seja, as capturas de telas para evidenciar os testes realizados de forma automática, arquivos de evidências:
- 01_img_bloagi.png
- 02_img_pesquisa_teste.png
- 03_img_resultado_pesquisa_teste.png
- 04_img_pesquisa_python.png
- 05_img_resultado_pesquisa_python.png

## Diretório './steps/assets' 
Será criado ao gerar o relatório 'report.html' da execução dos testes com o arquivo 'style.css', referente ao estilo do arquivo '*.html'.

## Arquivo 'report.html' 
Contém o relatório do resultado da execução dos testes, para abrir este arquivo:
- Clicar com o botão direito do mouses sobre o arquivo 'report.html'.
- Opção 'Open in' (IDE PyCharm)
- Selecionar:
- "Explorer" para visualizar o arquivo 'report.html' no diretório gerado.
- "Browser" para visualizar o arquivo 'report.html' direto em um dos navegadores: Chrome, Firefox, Edge (por exemplo).

## Passos para gerar o relatório 'report.html'
A biblioteca 'pytest-html' informada no arquivo 'requeriments.txt' para a instalação.

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
- 
```
x mod 3 = Fizz
x mod 5 = Buzz
x mod 15 = FizzBuzz
```
