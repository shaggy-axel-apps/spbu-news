from datetime import date

from spbu_api import SpbuApi
from spbu_api.models import Event, GroupEvent, Day, EventLocation, Educator


class EventApi(SpbuApi):
    def __init__(self):
        super().__init__()
        self.API = f"{self.API}groups/""{id}/events/"

    async def get_all_events_for_group(self, group_id: int) -> list[Event]:
        """ Gets a given student group's events for the current week """
        response = await self.send_query(self.API, id=group_id)
        group = await response.response
        return self.parse_events(group)

    def parse_events(group: dict) -> GroupEvent:
        events = GroupEvent(
            student_group_id=group["StudentGroupId"],
            student_group_display_name=group["StudentGroupDisplayName"],
            timetable_display_name=group["TimeTableDisplayName"],
            previous_week_monday=group["PreviousWeekMonday"],
            next_week_monday=group["NextWeekMonday"],
            is_previous_week_reference_available=group["IsPreviousWeekReferenceAvailable"],
            is_next_week_reference_available=group["IsNextWeekReferenceAvailable"],
            is_current_week_reference_available=group["IsCurrentWeekReferenceAvailable"],
            week_display_text=group["WeekDisplayText"],
            week_monday=group["WeekMonday"],
            days=[
                Day(
                    day=date(),
                    day_string=day["DayString"],
                    day_study_events=[
                        Event(
                            study_events_timetable_kind_code=event[
                                "StudyEventsTimeTableKindCode"],
                            start=event["Start"],
                            end=event["End"],
                            subject=event["Subject"],
                            time_interval_string=event["TimeIntervalString"],
                            date_with_time_interval_string=event[
                                "DateWithTimeIntervalString"],
                            display_date_and_time_interval_string=event[
                                "DisplayDateAndTimeIntervalString"],
                            locations_display_text=event[
                                "LocationsDisplayText"],
                            educators_display_text=event[
                                "EducatorsDisplayText"],
                            has_educators=event["HasEducators"],
                            is_cancelled=event["IsCancelled"],
                            contingent_unit_name=event["ContingentUnitName"],
                            division_and_course=event["DivisionAndCourse"],
                            is_assigned=event["IsAssigned"],
                            time_was_changed=event["TimeWasChanged"],
                            locations_were_changed=event[
                                "LocationsWereChanged"],
                            educators_were_reassigned=event[
                                "EducatorsWereReassigned"],
                            elective_disciplines_count=event[
                                "ElectiveDisciplinesCount"],
                            is_elective=event["IsElective"],
                            has_the_same_time_as_previous_item=event[
                                "HasTheSameTimeAsPreviousItem"],
                            contingent_units_display_test=event[
                                "ContingentUnitsDisplayTest"],
                            is_study=event["IsStudy"],
                            all_day=event["AllDay"],
                            within_the_same_day=event["WithinTheSameDay"],
                            event_locations=[
                                EventLocation(
                                    is_empty=location["IsEmpty"],
                                    display_name=location["DisplayName"],
                                    has_geographic_coordinates=location[
                                        "HasGeographicCoordinates"],
                                    latitude=location["Latitude"],
                                    longitude=location["Longitude"],
                                    latitude_value=location[
                                        "LatitudeValue"],
                                    longitude_value=location[
                                        "LongitudeValue"],
                                    educators_display_text=location[
                                        "EducatorsDisplayText"],
                                    has_educators=location["HasEducators"],
                                    educators=[
                                        Educator(
                                            educator_id=educator["Item1"],
                                            educator_name=educator["Item2"],
                                        )
                                        for educator in location["EducatorIds"]
                                    ],
                                )
                                for location in event["EventLocations"]
                            ],
                            educators=[
                                Educator(
                                    educator_id=educator["Item1"],
                                    educator_name=educator["Item2"],
                                )
                                for educator in event["EducatorIds"]
                            ]
                        )
                        for event in day["DayStudyEvents"]
                    ]
                )
                for day in group["Days"]
            ],
        )
        return events
