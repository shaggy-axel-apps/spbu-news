from spbu_api import SpbuApi


class StudyDivisionsApi(SpbuApi):
    def __init__(self):
        self.API = f"{self.API}study/divisions/"

    def get_all(self):
        return self.send_query(self.API)
