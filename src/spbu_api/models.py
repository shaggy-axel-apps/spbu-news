from datetime import date
from typing import NamedTuple, Optional


class ApiResponse(NamedTuple):
    code: int
    status: str
    response: list[dict]


class Event(NamedTuple):
    study_events_timetable_kind_code: int
    start: date
    end: date
    subject: str
    time_interval_string: str
    date_with_time_interval_string: str
    display_date_and_time_interval_string: str
    locations_display_text: str
    educators_display_text: str
    has_educators: bool
    is_cancelled: bool
    contingent_unit_name: str
    division_and_course: str
    is_assigned: bool
    time_was_changed: bool
    locations_were_changed: bool
    educators_were_reassigned: bool
    elective_disciplines_count: int
    is_elective: bool
    has_the_same_time_as_previous_item: bool
    contingent_units_display_test: Optional[str]
    is_study: bool
    all_day: bool
    within_the_same_day: bool
    event_locations: list


class Day(NamedTuple):
    day: date
    day_string: str
    day_study_events: list[Event]


class GroupEvent(NamedTuple):
  student_group_id: int
  student_group_display_name: str
  timetable_display_name: str
  previous_week_monday: date
  next_week_monday: date
  is_previous_week_reference_available: bool
  is_next_week_reference_available: bool
  is_current_week_reference_available: bool
  week_display_text: str
  week_monday: date
  days: list[Day]


class Group(NamedTuple):
    group_id: int
    name: str
    form: str
    profiles: str


class Division(NamedTuple):
    oid: int
    alias: str
    name: str


class Program(NamedTuple):
    program_id: int
    name: str
    name_english: str
    year: int
    is_empty: bool
    division_alias: str
    study_level: str
    has_courses: bool
