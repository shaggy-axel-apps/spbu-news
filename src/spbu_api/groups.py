from spbu_api import SpbuApi
from spbu_api.models import Group


class GroupApi(SpbuApi):
    def __init__(self):
        super().__init__()
        self.API = f"{self.API}progams""/{id}/groups/"

    async def get_groups_of_program(self, program_id: int) -> list[Group]:
        """ Gets a given study program's student groups for the current study year """
        groups = []
        response = await self.send_query(self.API, id=program_id)
        for group in await response.response["Groups"]:
            groups.append(Group(
                group_id=group["StudentGroupId"],
                name=group["StudentGroupName"],
                form=group["StudentGroupStudyForm"],
                profiles=group["StudentGroupProfiles"]
            ))
        return groups
