# src/memory.py
import json
import os

class MemoryManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.memory = {}

    def load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.memory = json.load(f)
        else:
            self.memory = {}

    def update_memory(self, user_input, bot_response):
        # Guardar la conversación en memoria persistente
        self.memory[user_input] = bot_response
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)