# src/utils.py
def format_message(sender, message):
    """Formatea el mensaje con Markdown y emojis."""
    if sender == "Bot":
        return f"🤖 **ChatMate:** {message}"
    else:
        return f"🧑 **Tú:** {message}"