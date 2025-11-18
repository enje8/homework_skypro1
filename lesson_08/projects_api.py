from api_client import APIClient


class ProjectsAPI(APIClient):

    def create_project(self, name):
        payload = {"name": name}
        return self.post("/projects", payload)

    def update_project(self, project_id, new_name):
        payload = {"name": new_name}
        return self.put(f"/projects/{project_id}", payload)

    def get_project(self, project_id):
        return self.get(f"/projects/{project_id}")