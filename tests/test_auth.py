import allure

@allure.title("Авторизация пользователя")
@allure.description("Проверка успешной авторизации пользователя")
def test_login_success(api_client):
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }

    with allure.step("Отправить POST запрос /auth/login"):
        response = api_client.post("/auth/login", payload)

    with allure.step("Проверить статус код"):
        assert response.status_code in [200, 201]

    with allure.step("Проверить наличие токена"):
        assert "token" in response.json()