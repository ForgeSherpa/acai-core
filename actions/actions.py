from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime

def build_response(tracker: Tracker) -> dict:
    # Get slot values
    year_start = tracker.get_slot('year_start')
    year_end = tracker.get_slot('year_end')
    year = tracker.get_slot('year')
    major = tracker.get_slot('major')
    period = tracker.get_slot('period')
    faculty = tracker.get_slot('faculty')

    # Value of period_years
    period_years = None
    if period == "dari tahun lalu":
        period_years = 1
    elif period:
        period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

    # Construct the response data
    response = {}
    if year_start and year_end:
        year_starts = int(year_start.split()[1])
        year_ends = int(year_end.split()[1])
        response["year_range"] = calculate_years_range(year_starts, year_ends)
    if year:
        response["year"] = year
    if major:
        response["major"] = major
    if faculty:
        response["faculty"] = faculty
    if period_years:
        response["period"] = calculate_period_range(period_years)

    return response

def reset_slots(slot_names: list) -> list:
    return [SlotSet(slot, None) for slot in slot_names]


def calculate_period_range(period_years: int) -> str:
    current_year = datetime.now().year
    if period_years == 1: 
        start_year = current_year - 1
    else:
        start_year = current_year - period_years
    return f"{start_year} - {current_year}"

def calculate_years_range(year_start: int, year_end: int) -> str:
    return f"{year_start} - {year_end}"

class ActionShowGraduationData(Action):
    def name(self) -> str:
        return "action_show_graduation_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_kelulusan"
        
        response = build_response(tracker)

        # Prepare data to be sent to backend
        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)

        return reset_slots([
                    "year_start",
                    "year_end",
                    "year_range",
                    "year",
                    "major",
                    "period",
                    "faculty"
                ])


class ActionShowResearchData(Action):
    def name(self) -> str:
        return "action_show_research_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_penelitian"
        
        # Get slot values
        response = build_response(tracker)
        
        # Build final response including intent and entities
        final_response = {
            "intent": intent,
            "entities": response
        }

        # Send the response as a JSON message
        dispatcher.utter_message(json_message=final_response)

        # Reset slots after sending response
        return reset_slots([
                    "year_start",
                    "year_end",
                    "year_range",
                    "year",
                    "major",
                    "period",
                    "faculty"
                ])

class ActionShowActivityData(Action):
    def name(self) -> str:
        return "action_show_activity_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_aktivitas"
        
        # Get slot values
        activity_level = tracker.get_slot('activity_level')

        response = build_response(tracker)
        if activity_level:
            response["activity_level"] = activity_level

        # Build final response including intent and entities
        final_response = {
            "intent": intent,
            "entities": response
        }

        # Send the response as a JSON message
        dispatcher.utter_message(json_message=final_response)

        # Reset slots after sending response
        return reset_slots([
                    "year_start",
                    "year_end",
                    "year_range",
                    "year",
                    "major",
                    "period",
                    "faculty",
                    "activity_level"
                ])

class ActionShowIPKData(Action):
    def name(self) -> str:
        return "action_show_ipk_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_ipk"
        
        # Get slot values
        cohort = tracker.get_slot('cohort')

        response = build_response(tracker)
        if cohort:
            response["cohort"] = int(cohort.split()[1])

        # Build final response including intent and entities
        final_response = {
            "intent": intent,
            "entities": response
        }

        # Send the response as a JSON message
        dispatcher.utter_message(json_message=final_response)

        # Reset slots after sending response
        return reset_slots([
                    "year_start",
                    "year_end",
                    "year_range",
                    "year",
                    "major",
                    "period",
                    "faculty",
                    "activity_level",
                    "cohort"
                ])

class ActionShowLecturerData(Action):
    def name(self) -> str:
        return "action_show_lecturer_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_dosen"
        
        # Get slot values
        lecturer = tracker.get_slot('lecturer')

        response = build_response(tracker)
        if lecturer:
            response["lecturer"] = lecturer

        # Build final response including intent and entities
        final_response = {
            "intent": intent,
            "entities": response
        }

        # Send the response as a JSON message
        dispatcher.utter_message(json_message=final_response)

        # Reset slots after sending response
        return reset_slots([
                    "major",
                    "faculty",
                    "lecturer"
                ])