import allure
from allure_commons.types import Severity
from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Vitalii Sharov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка названия Issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_checking_title_of_issue_in_repository_with_decorators(config_browser):
    open_main_page()
    find_repository()
    open_repository()
    open_issues_tab()
    find_issue_with_name()


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def find_repository():
    s(".header-search-button").click()
    s('#query-builder-test').send_keys("Sharpei88/qa_guru_python_8_9").press_enter()


@allure.step('Переходим в репозиторий')
def open_repository():
    s(by.link_text("Sharpei88/qa_guru_python_8_9")).click()


@allure.step('Переходим во вкладку Issues')
def open_issues_tab():
    s("#issues-tab").click()


@allure.step('Проверяем название Issue')
def find_issue_with_name():
    s(by.partial_text("Test issue")).should(be.visible)
