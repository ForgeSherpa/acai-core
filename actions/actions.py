import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime

def calculate_period_range(period_years: int) -> str:
    current_year = datetime.now().year
    start_year = current_year - period_years
    return f"{start_year} - {current_year}"

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

        # Construct the response data
        response = {}
        if year_start and year_end:
            response["year_start"] = year_start
            response["year_end"] = year_end
        if year:
            response["year"] = year
        if major:
            response["major"] = major
        if faculty:
            response["faculty"] = faculty
        if period:
            period_years = int(period.split()[0]) if period else None
            if period_years:
                response["period"] = calculate_period_range(period_years)

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
            SlotSet("year", None),
            SlotSet("major", None),
            SlotSet("faculty", None),
            SlotSet("period", None)
        ]
