from typing import Union

from spbu_api import SpbuApi
from spbu_api.models import ApiResponse, Division, Program


class StudyDivisionsApi(SpbuApi):
    def __init__(self):
        super().__init__()
        self.API = f"{self.API}study/divisions/"

    async def get_all(self) -> Union[list[Division], str]:
        """ Gets study divisions """
        response = await self.send_query(self.API)
        if 200 <= response.code and response.code < 400:
            divisions = []
            for division in await response.response:
                divisions.append(Division(
                    oid=division.get("Oid", None),
                    alias=division.get("Alias", None),
                    name=division.get("Name", None)
                ))
            return divisions
        return response.status

    async def get_programs(self, alias: str) -> list[Program]:
        """ Gets study programs with levels for a given study division """
        response: ApiResponse = await self.send_query(
            f"{self.API}{alias}/programs/levels/"
        )
        if 200 <= response.code and response.code < 400:
            programs = []
            for level in await response.response:
                study_level_name = level["StudyLevelName"]
                has_courses = level["HasCourse6"]
                for program in level["StudyProgramCombinations"]:
                    program_name = program["Name"]
                    program_name_english = program["NameEnglish"]
                    programs += [
                        Program(
                            program_id=year["StudyProgramId"],
                            name=program_name,
                            name_english=program_name_english,
                            year=year["YearNumber"],
                            is_empty=year["IsEmpty"],
                            division_alias=year["PublicDivisionAlias"],
                            study_level=study_level_name,
                            has_courses=has_courses,
                        )
                        for year in program["AdmissionYears"]
                    ]
            return programs
        response.status
