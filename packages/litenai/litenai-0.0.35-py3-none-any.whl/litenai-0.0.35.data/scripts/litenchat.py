"""
Chat app for LitenAI
"""
import sys
import os
import panel as pn

import litenai as tenai

class ChatApp():
    """
    Chat app for LitenAI
    """
    def start(self):
        """
        Start chat app
        """
        pn.extension('bokeh')
        config = tenai.Config()
        session = tenai.Session.get_or_create('chatsession', config)
        chatbot = tenai.ChatBot(session=session)
        chat_panel = chatbot.start()
        chat_panel.servable(title="LitenAI")

def print_usage():
    """
    Print usage
    """
    print(f"""
Usage: python litenchat.py
Example: python litenchat.py
Received: f{sys.argv}
""")

ChatApp().start()
