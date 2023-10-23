import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Vitalii Sharov")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка названия Issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps(config_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s('#query-builder-test').send_keys("Sharpei88/qa_guru_python_8_9").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("Sharpei88/qa_guru_python_8_9")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с именем 'Test issue'"):
        s(by.partial_text("Test issue")).should(be.visible)
