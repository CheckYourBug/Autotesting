import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
#перечень настроенных опций
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru")
# создаем фикстуру browser (request)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    #добавлена возмодность тестирования разноязычных веб приложений через параметр --language
    #для Chrome
    languages = Options()
    languages.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    #для Firefox
    languages_fifefox = OptionsFirefox()
    languages_fifefox.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        browser = webdriver.Chrome(options=languages)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        browser = webdriver.Firefox(options=languages_fifefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser")
    browser.quit()






