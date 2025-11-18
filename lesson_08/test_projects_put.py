from projects_api import ProjectsAPI
import uuid


def test_update_project_positive():
    api = ProjectsAPI()

    # создаем проект
    name = "Project Before " + str(uuid.uuid4())
    created = api.create_project(name).json()

    # обновляем
    new_name = "Project After " + str(uuid.uuid4())
    response = api.update_project(created["id"], new_name)

    assert response.status_code == 200
    assert response.json()["name"] == new_name


def test_update_project_negative_wrong_id():
    api = ProjectsAPI()

    response = api.update_project("wrong123", "New Name")

    assert response.status_code in (400, 404)