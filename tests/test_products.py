import allure
from utils.schema import validate_schema


@allure.title("Получение списка товаров")
@allure.description("Проверка получения списка товаров через FakeStore API")
def test_get_all_products(api_client):
    with allure.step("Отправить GET запрос /products"):
        response = api_client.get("/products")

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить, что ответ содержит список товаров"):
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@allure.title("Получение товара по ID")
@allure.description("Проверка получения одного товара по его идентификатору")
def test_get_single_product_by_id(api_client):
    with allure.step("Отправить GET запрос /products/1"):
        response = api_client.get("/products/1")

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить структуру ответа"):
        product = response.json()
        validate_schema(product, "schemas/product_schema.json")
        assert product["id"] == 1


@allure.title("Получение несуществующего товара")
@allure.description("Проверка поведения API при запросе несуществующего товара")
def test_get_single_product_not_found(api_client):
    with allure.step("Отправить GET запрос /products/9999"):
        response = api_client.get("/products/9999")

    with allure.step("Проверить статус код"):
        assert response.status_code in [200, 404]

    with allure.step("Проверить тело ответа (если есть)"):
        if response.text:
            try:
                data = response.json()
                assert isinstance(data, dict)
            except ValueError:
                pass


@allure.title("Создание нового товара")
@allure.description("Проверка создания товара через POST запрос")
def test_create_product(api_client):
    payload = {
        "title": "Test product",
        "price": 13.5,
        "description": "Test description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    with allure.step("Отправить POST запрос /products"):
        response = api_client.post("/products", payload)

    with allure.step("Проверить статус код"):
        assert response.status_code in [200, 201]

    with allure.step("Проверить данные созданного товара"):
        created = response.json()
        assert "id" in created
        assert created["title"] == payload["title"]
        assert float(created["price"]) == float(payload["price"])


@allure.title("Обновление товара")
@allure.description("Проверка обновления данных товара")
def test_update_product(api_client):
    payload = {
        "title": "Updated title",
        "price": 99.99,
        "description": "Updated description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    with allure.step("Отправить PUT запрос /products/1"):
        response = api_client.put("/products/1", payload)

    with allure.step("Проверить статус код"):
        assert response.status_code in [200, 201]

    with allure.step("Проверить обновлённые данные"):
        updated = response.json()
        assert updated["title"] == payload["title"]
        assert float(updated["price"]) == float(payload["price"])


@allure.title("Удаление товара")
@allure.description("Проверка удаления товара")
def test_delete_product(api_client):
    with allure.step("Отправить DELETE запрос /products/1"):
        response = api_client.delete("/products/1")

    with allure.step("Проверить статус код"):
        assert response.status_code in [200, 201]

    with allure.step("Проверить ответ"):
        deleted = response.json()
        assert isinstance(deleted, dict)
        assert "id" in deleted
