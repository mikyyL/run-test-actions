import allure


@allure.feature('test numbers')
class TestNumbers:
    @allure.story('Тест номер 1')
    def test_number_one(self):
        with allure.step('Шаг 1 подготовка данных'):
            x = 3
            assert x == 3

    @allure.story('Тест номер 2')
    def test_number_two(self):
        with allure.step('Шаг 1 подготовка данных'):
            x = 2
            assert x == 2
