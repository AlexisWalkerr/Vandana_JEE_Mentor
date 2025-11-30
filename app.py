"""
====================================================================================
    Project     : Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor

    Team Name   : Anagha_Vandana
    Members     : DHRUVIN NARENDRA BAROT
                  VARDHAN PATEL
                  ANUPKUMAR SINGH

------------------------------------------------------------------------------------
    File        : app.py
    Role        : CLI Interface — Launches Vandana AI chat locally using 
                  InMemoryRunner and session-based chat flow.

    Use         : Run this file to interact with Vandana in a command-line chat.
                  Auto-greets user on startup and maintains chat session.
------------------------------------------------------------------------------------
    Command     : python app.py
====================================================================================
"""

import asyncio
from google.adk.runners import InMemoryRunner
from google.genai import types
from agents.Vandana_root.agent import root_agent

APP_NAME = "vandana_app"
USER_ID = "student"

runner = InMemoryRunner(
    agent=root_agent,
    app_name=APP_NAME,
)

def create_session():
    session = asyncio.run(
        runner.session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
        )
    )
    return session
def run_agent(session_id: str, user_message: str) -> str:
    content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_message)],
    )
    final_text = ""
    for event in runner.run(
        user_id=USER_ID,
        session_id=session_id,
        new_message=content,
    ):
        if event.content and event.content.parts and event.content.parts[0].text:
            # keep updating final_text; last non-empty becomes final reply
            final_text = event.content.parts[0].text

    return final_text.strip()
def main():
    print("Vandana AI, Your JEE Mentor")
    print("Type 'exit' or 'quit' to end the chat.\n")

    session = create_session() # Create session for this chat

    first_reply = run_agent(session.id, "start")
    print("Vandana:", first_reply) # Greeting message

    while True:
        user_msg = input("You: ")

        if user_msg.strip().lower() in {"exit", "quit"}:
            print("Vandana: All the best for your JEE prep!")
            break

        try:
            reply = run_agent(session.id, user_msg)
            print("Vandana:", reply)
        except Exception as e:
            print("Error:", e)
            print("Vandana: Sorry, something went wrong. Can you try again?") #error handeler


if __name__ == "__main__":
    main()
