from projects_api import ProjectsAPI
import uuid


def test_get_project_positive():
    api = ProjectsAPI()

    # создаём проект
    name = "ProjectForGet " + str(uuid.uuid4())
    created = api.create_project(name).json()

    # получаем
    response = api.get_project(created["id"])

    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["id"] == created["id"]


def test_get_project_negative_not_found():
    api = ProjectsAPI()

    response = api.get_project("notExist123")

    assert response.status_code in (400, 404)