import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime

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
        
        # Get slot values
        year_start = tracker.get_slot('year_start')
        year_end = tracker.get_slot('year_end')
        year = tracker.get_slot('year')
        major = tracker.get_slot('major')
        faculty = tracker.get_slot('faculty')
        period = tracker.get_slot('period')
        cohort = tracker.get_slot('cohort')

        # value of period_years
        period_years = None
        if period == "dari tahun lalu":
            period_years = 1
        elif period:
            period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

        # Construct the response data
        response = {}
        if year_start and year_end:
            year_starts = int(year_start.split()[2])
            year_ends = int(year_end.split()[1])
            response ["year_range"] = calculate_years_range(year_starts, year_ends)
        if year:
            response["year"] = year
        if major:
            response["major"] = major
        if faculty:
            response["faculty"] = faculty
        if period_years:
            response["period"] = calculate_period_range(period_years)
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
        return [
            SlotSet("year_start", None),
            SlotSet("year_end", None),
            SlotSet("year_range", None),
            SlotSet("year", None),
            SlotSet("major", None),
            SlotSet("faculty", None),
            SlotSet("period", None),
            SlotSet("cohort", None)
        ]

class ActionShowResearchData(Action):
    def name(self) -> str:
        return "action_show_research_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_penelitian"
        
        # Get slot values
        year_start = tracker.get_slot('year_start')
        year_end = tracker.get_slot('year_end')
        year = tracker.get_slot('year')
        major = tracker.get_slot('major')
        faculty = tracker.get_slot('faculty')
        period = tracker.get_slot('period')
        cohort = tracker.get_slot('cohort')

        # value of period_years
        period_years = None
        if period == "dari tahun lalu":
            period_years = 1
        elif period:
            period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

        # Construct the response data
        response = {}
        if year_start and year_end:
            year_starts = int(year_start.split()[2])
            year_ends = int(year_end.split()[1])
            response ["year_range"] = calculate_years_range(year_starts, year_ends)
        if year:
            response["year"] = year
        if major:
            response["major"] = major
        if faculty:
            response["faculty"] = faculty
        if period_years:
            response["period"] = calculate_period_range(period_years)
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
        return [
            SlotSet("year_start", None),
            SlotSet("year_end", None),
            SlotSet("year_range", None),
            SlotSet("year", None),
            SlotSet("major", None),
            SlotSet("faculty", None),
            SlotSet("period", None),
            SlotSet("cohort", None)
        ]

class ActionShowActivityData(Action):
    def name(self) -> str:
        return "action_show_activity_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_aktivitas"
        
        # Get slot values
        year_start = tracker.get_slot('year_start')
        year_end = tracker.get_slot('year_end')
        year = tracker.get_slot('year')
        major = tracker.get_slot('major')
        faculty = tracker.get_slot('faculty')
        period = tracker.get_slot('period')
        cohort = tracker.get_slot('cohort')

        # value of period_years
        period_years = None
        if period == "dari tahun lalu":
            period_years = 1
        elif period:
            period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

        # Construct the response data
        response = {}
        if year_start and year_end:
            year_starts = int(year_start.split()[2])
            year_ends = int(year_end.split()[1])
            response ["year_range"] = calculate_years_range(year_starts, year_ends)
        if year:
            response["year"] = year
        if major:
            response["major"] = major
        if faculty:
            response["faculty"] = faculty
        if period_years:
            response["period"] = calculate_period_range(period_years)
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
        return [
            SlotSet("year_start", None),
            SlotSet("year_end", None),
            SlotSet("year_range", None),
            SlotSet("year", None),
            SlotSet("major", None),
            SlotSet("faculty", None),
            SlotSet("period", None),
            SlotSet("cohort", None)
        ]

class ActionShowIPKData(Action):
    def name(self) -> str:
        return "action_show_ipk_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
        # Set the intent for this action
        intent = "permintaan_data_ipk"
        
        # Get slot values
        year_start = tracker.get_slot('year_start')
        year_end = tracker.get_slot('year_end')
        year = tracker.get_slot('year')
        major = tracker.get_slot('major')
        faculty = tracker.get_slot('faculty')
        period = tracker.get_slot('period')
        cohort = tracker.get_slot('cohort')

        # value of period_years
        period_years = None
        if period == "dari tahun lalu":
            period_years = 1
        elif period:
            period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

        # Construct the response data
        response = {}
        if year_start and year_end:
            year_starts = int(year_start.split()[2])
            year_ends = int(year_end.split()[1])
            response ["year_range"] = calculate_years_range(year_starts, year_ends)
        if year:
            response["year"] = year
        if major:
            response["major"] = major
        if faculty:
            response["faculty"] = faculty
        if period_years:
            response["period"] = calculate_period_range(period_years)
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
        return [
            SlotSet("year_start", None),
            SlotSet("year_end", None),
            SlotSet("year_range", None),
            SlotSet("year", None),
            SlotSet("major", None),
            SlotSet("faculty", None),
            SlotSet("period", None),
            SlotSet("cohort", None)
        ]
