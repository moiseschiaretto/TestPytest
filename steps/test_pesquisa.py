from pytest_bdd import scenarios, scenario, given, when, then, parsers
import time

# scenarios('pesquisa.feature')

# @scenario('pesquisa.feature', 'Pesquisa válida')
# def test_pesquisa_existente():
#     print('starting bdd test...')
#     assert True


@given('que o usuário esteja no blogdoagi')
def test_user_acessar_blog(browser):
    page = browser
    url = 'https://blogdoagi.com.br/'
    page.goto(url)
    time.sleep(2)
    screenshot_path = "./evidencias/01_img_bloagi.png"
    page.screenshot(path=screenshot_path)
    assert page.url == url
    assert page.title() == "Blog do Agi | Tudo sobre empréstimo e educação financeira"


@when('o usuário clicar no botão de pesquisar')
def test_user_clicar_botao_pesquisar(browser):
    page = browser
    botao_pesquisa = page.query_selector(
        'xpath=/html/body/div[1]/header/div[1]/div[1]/div/div/div/div[3]/div[2]/div/div/a/span[2]')
    botao_pesquisa.click()
    assert True


@when('clicar e limpar o campo de pesquisa')
def test_user_clicar_limpar_campo_pesquisa(browser):
    page = browser
    campo_pesquisa = page.query_selector('//*[@id="search-field"]')
    time.sleep(1)
    campo_pesquisa.click()
    campo_pesquisa.fill('')
    assert True


@when('digitar o conteúdo existente, texto teste')
def test_user_digitar_texto_pesquisa(browser):
    page = browser
    input_pesquisa = page.query_selector('//*[@id="search-field"]')
    input_pesquisa.fill('teste')
    time.sleep(2)
    screenshot_path = "./evidencias/02_img_pesquisa_teste.png"
    page.screenshot(path=screenshot_path)
    assert True


@when('teclar ENTER')
def test_user_teclar_enter(browser):
    page = browser
    page.keyboard.press("Enter")
    time.sleep(3)
    screenshot_path = "./evidencias/03_img_resultado_pesquisa_teste.png"
    page.screenshot(path=screenshot_path)
    assert True


@then('o blog deverá retornar os resultados referentes ao texto teste informado')
def test_verificar_resultados_pesquisa(browser):
    page = browser
    result_pesquisa = page.query_selector('//h1[contains(., " Resultados encontrados para: ")]')
    result1 = ' Resultados encontrados para: ' in result_pesquisa.inner_html()
    span_element = page.wait_for_selector('section h1:first-child span', state='visible')
    result2 = 'teste' in span_element.text_content()
    assert result1 and result2
    time.sleep(5)


# @scenario('pesquisa.feature', 'Pesquisa inválida')
@when('digitar o conteúdo inexistente, texto python')
def test_user_digitar_texto_pesquisa(browser):
    page = browser
    input_pesquisa = page.query_selector('//*[@id="search-field"]')
    input_pesquisa.fill('python')
    time.sleep(2)
    screenshot_path = "./evidencias/04_img_pesquisa_python.png"
    page.screenshot(path=screenshot_path)
    assert True


@when('teclar ENTER')
def test_user_teclar_enter(browser):
    page = browser
    page.keyboard.press("Enter")
    time.sleep(2)
    screenshot_path = "./evidencias/05_img_resultado_pesquisa_python.png"
    page.screenshot(path=screenshot_path)
    assert True
    time.sleep(5)


@then('o blog deverá retornar os resultados referentes ao texto python informado')
def test_verificar_resultados_pesquisa(browser):
    page = browser
    result_pesquisa = page.query_selector('//h1[contains(., " Resultados encontrados para: ")]')
    result1 = ' Resultados encontrados para: ' in result_pesquisa.inner_html()
    span_element = page.wait_for_selector('section h1:first-child span', state='visible')
    result2 = 'python' in span_element.text_content()
    assert result1 and result2
    time.sleep(5)
