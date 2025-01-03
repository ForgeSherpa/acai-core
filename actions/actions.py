from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from rapidfuzz import process
import re
from typing import Any, Text, Dict, List


faculty_patterns = [
    "Fakultas Bisnis dan Manajemen",
    "Fakultas Ilmu Pendidikan",
    "Fakultas Ilmu Komputer",
    "Fakultas Teknik Sipil dan Perencanaan",
    "Fakultas Hukum",
]
major_patterns = [
    "Manajemen",
    "Akuntansi",
    "Pariwisata",
    "Pendidikan Bahasa Inggris",
    "Teknik Sipil",
    "Arsitektur",
    "Ilmu Hukum",
    "Sistem Informasi",
    "Teknologi Informasi",
]

def word_match(input_text: str, patterns: list, threshold: int = 85) -> str:
    result = process.extractOne(input_text, patterns)
    if result and result[1] >= threshold:
        return result[0]
    return input_text

def extract_number(text: str) -> int:
    text = re.sub(r"\D", "", text) 
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    else:
        return None

def build_response(tracker: Tracker) -> dict:
    start = tracker.get_slot('start')
    end = tracker.get_slot('end')
    year = tracker.get_slot('year')
    major = tracker.get_slot('major')
    period = tracker.get_slot('period')
    faculty = tracker.get_slot('faculty')
    range = tracker.get_slot('range')

    entities = tracker.latest_message.get('entities', [])

    if isinstance(entities, dict):  
        entities = [entities]
    elif isinstance(entities, str):  
        entities = [] 

    if faculty:
        faculty = word_match(faculty, faculty_patterns)
    if major:
        major = word_match(major, major_patterns)

    period_years = None
    if period == "dari tahun lalu":
        period_years = 1
    elif period:
        period_years = int(period.split()[0]) if period.split()[0].isdigit() else None

    response = {}
    mode = "list"

    message = tracker.latest_message.get("text", "").lower()
    if "rata-rata" in message:
        mode = "avg"

    if start:
        response['start'] = start

    if end:
        response['end'] = end

    if year:
        year_number = extract_number(year)
        if year_number: 
            response["year"] = year_number

    if major:
        response["major"] = major

    if faculty:
        response["faculty"] = faculty


    if period_years:
        response["year_range"] = calculate_period_range(period_years)
        mode = "sum" 

    if range:
        # response["range"] = range
        mode = "sum" 
        current_year = datetime.now().year
        year = int(year)
        response["year_range"] = f"{year} - {current_year}"
        del response["year"]

    response["mode"] = mode
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

def calculate_years_range(start: int, end: int) -> str:
    return f"{start} - {end}"

class ActionShowGraduationData(Action):
    def name(self) -> str:
        return "action_show_graduation_data"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = "ask_graduation_data"
        response = build_response(tracker)

        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)

        return reset_slots([
            "start",
            "end", 
            "year_range", 
            "year", 
            "major",
            "faculty",
            "period",
            "range"
        ])



class ActionShowResearchData(Action):
    def name(self) -> str:
        return "action_show_research_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _domain) -> list:
        intent = "ask_research_data"

        publication_type = tracker.get_slot('publication_type')
        
        publication_type_patterns = ["Nasional non-sinta", "Scopus", "Sinta", "international"]

        if publication_type:
            publication_type = word_match(publication_type.lower(), publication_type_patterns)

        response = build_response(tracker)
        if publication_type:
            response["publication_type"] = publication_type
        
        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)
        
        return reset_slots([
            "start",
            "end",
            "year_range",
            "year",
            "major",
            "faculty",
            "period",
            "range"
        ])



class ActionShowActivityData(Action):
    def name(self) -> str:
        return "action_show_activity_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _domain) -> list:
        intent = "ask_activity_data"

        activity_level = tracker.get_slot('activity_level')

        activity_level_patterns = ["internasional", "lokal", "nasional"]

        if activity_level:
            activity_level = word_match(activity_level.lower(), activity_level_patterns)

        response = build_response(tracker)
        if activity_level:
            response["activity_level"] = activity_level

        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)

        return reset_slots([
            "start",
            "end",
            "year_range",
            "year",
            "major",
            "faculty",
            "period",
            "activity_level",
            "range"
        ])


class ActionShowIPKData(Action):
    def name(self) -> str:
        return "action_show_ipk_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _domain) -> list:
        intent = "ask_ipk_data"
        
        cohort = tracker.get_slot('cohort')

        response = build_response(tracker)
        
        if cohort:
            cohort_number = extract_number(cohort)
            if cohort_number:
                response["cohort"] = cohort_number

        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)

        return reset_slots([
            "start",
            "end",
            "year_range",
            "year",
            "major",
            "faculty",
            "period",
            "cohort",
            "range"
        ])

class ActionShowLecturerData(Action):
    def name(self) -> str:
        return "action_show_lecturer_data"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, _domain) -> list:
        intent = "ask_lecturer_data"
        
        response = build_response(tracker)

        final_response = {
            "intent": intent,
            "entities": response
        }

        dispatcher.utter_message(json_message=final_response)
    
        return reset_slots([
            "major",
            "faculty"
        ])