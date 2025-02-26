from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from .services import create_thread, send_message
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class DetectIntentWithGPT(Action):
    def name(self):
        return "action_detect_intent_gpt"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        user_message = tracker.latest_message.get("text")

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=user_message
        )
        print(response.text)

        dispatcher.utter_message(response.text)

        # Guardar el thread_id en los slots para futuras interacciones
        return []