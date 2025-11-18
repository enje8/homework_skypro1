from projects_api import ProjectsAPI
import uuid


def test_create_project_positive():
    api = ProjectsAPI()
    name = "AutoTest Project " + str(uuid.uuid4())

    response = api.create_project(name)

    assert response.status_code == 200
    assert response.json()["name"] == name
    assert "id" in response.json()


def test_create_project_negative_empty_name():
    api = ProjectsAPI()

    response = api.create_project("")

    # если в документации будет другой код — поменяйте
    assert response.status_code in (400, 422)