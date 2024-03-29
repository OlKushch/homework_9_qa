import allure
from selene import browser, by, be


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open('/')

    with allure.step("Ищем репозитория"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s(".ActionListItem-label").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)


