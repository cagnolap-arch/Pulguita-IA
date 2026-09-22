import json
import os
import threading
import urllib.parse
import urllib.request

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


APP_NAME = "Pulguita IA"
MEMORY_FILE = "pulguita_memory.json"


class PulguitaIA:
    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):
        try:
            path = os.path.join(
                App.get_running_app().user_data_dir,
                MEMORY_FILE
            )

            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)

        except Exception:
            pass

        return {
            "nombre": "Pulguita IA",
            "version": "0.1",
            "personalidad": "educada, natural, elegante y útil"
        }

    def save_memory(self):
        try:
            path = os.path.join(
                App.get_running_app().user_data_dir,
                MEMORY_FILE
            )

            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.memory, f, ensure_ascii=False, indent=2)

        except Exception:
            pass

    def remember(self, text):
        lower = text.lower().strip()

        if lower.startswith("recuerda que "):
            dato = text[12:].strip()

            if dato:
                key = "dato_" + str(len(self.memory))
                self.memory[key] = dato
                self.save_memory()
                return "Perfecto. Lo guardaré en mi memoria."

        if lower.startswith("recuerda:"):
            dato = text[9:].strip()

            if dato:
                key = "dato_" + str(len(self.memory))
                self.memory[key] = dato
                self.save_memory()
                return "Perfecto. Lo guardaré en mi memoria."

        return None

    def memory_answer(self, text):
        lower = text
