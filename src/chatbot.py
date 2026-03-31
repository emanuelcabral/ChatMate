# src/chatbot.py
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from src.memory import MemoryManager

class ChatMate:
    def __init__(self):
        # Memoria de la sesión
        self.memory = ConversationBufferMemory()
        self.model = ChatOpenAI(temperature=0.7)
        self.chain = ConversationChain(
            llm=self.model,
            memory=self.memory
        )
        # Memoria persistente
        self.memory_manager = MemoryManager("data/memory.json")
        self.memory_manager.load_memory()

    def get_response(self, user_input: str) -> str:
        # Agrega datos importantes a memoria persistente
        response = self.chain.run(user_input)
        self.memory_manager.update_memory(user_input, response)
        return response