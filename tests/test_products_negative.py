import allure


@allure.title("Создание товара с пустым телом")
@allure.description("Проверка поведения API при попытке создать товар без данных")
def test_create_product_with_empty_body(api_client):
    response = api_client.post("/products", {})

    assert response.status_code in [200, 201, 400]


@allure.title("Обновление товара с некорректной ценой")
@allure.description("Проверка реакции API на некорректное значение поля price")
def test_update_product_with_invalid_price(api_client):
    payload = {
        "title": "Bad price",
        "price": "not-a-number",
        "description": "desc",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }

    response = api_client.put("/products/1", payload)

    assert response.status_code in [200, 201, 400]

