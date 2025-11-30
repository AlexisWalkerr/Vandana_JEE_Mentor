"""
====================================================================================
    Project     : Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor
    Competition : AI Agents Intensive with Google — Capstone Project

    Team Name   : Anagha_Vandana
    Members     : DHRUVIN NARENDRA BAROT
                  VARDHAN PATEL
                  ANUPKUMAR SINGH

------------------------------------------------------------------------------------
    File        : test_vandana_agents.py
    Role        : Basic integration tests for Vandana root agent using InMemoryRunner.
                  Ensures that the system can load the root agent and produce a
                  non-empty response to a simple user query.
------------------------------------------------------------------------------------
    How to Run  : 
        1) Install pytest:
               pip install pytest

        2) Run tests from project root:
               pytest
====================================================================================
"""

import asyncio

import pytest
from google.adk.runners import InMemoryRunner
from google.genai import types

from agents.agent import root_agent 


APP_NAME = "vandana_test_app"
USER_ID = "test_user"


def _run_one_message(message: str) -> str:
    """
    Helper to create a session and send a single user message
    to the root_agent via InMemoryRunner. Returns final text reply.
    """
    runner = InMemoryRunner(
        agent=root_agent,
        app_name=APP_NAME,
    )

    # Create async session
    session = asyncio.run(
        runner.session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
        )
    )

    content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)],
    )

    final_text = ""

    for event in runner.run(
        user_id=USER_ID,
        session_id=session.id,
        new_message=content,
    ):
        if event.content and event.content.parts and event.content.parts[0].text:
            final_text = event.content.parts[0].text

    return final_text.strip()


@pytest.mark.integration
def test_root_agent_basic_response():
    """
    Verify that the Vandana root agent can:
    - Load correctly through agents.agent.root_agent
    - Produce a non-empty reply to a simple message.
    """
    reply = _run_one_message("Hi, I want help with my JEE study plan.")
    assert reply, "Root agent returned an empty reply."
    assert any(
        keyword in reply.lower()
        for keyword in ["plan", "study", "jee", "physics", "chemistry", "maths"]
    ), f"Reply does not look like a JEE mentoring response: {reply!r}"
