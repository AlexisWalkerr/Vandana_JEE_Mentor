"""
====================================================================================
    Project     : Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor

    Team Name   : Anagha_Vandana
    Members     : DHRUVIN NARENDRA BAROT
                  VARDHAN PATEL
                  ANUPKUMAR SINGH

------------------------------------------------------------------------------------
    File        : tutor_agent.agent.py
    Role        : Explains JEE topics with step-by-step clarity. Builds intuition
                  first, then detailed explanation, examples and learning tips.
------------------------------------------------------------------------------------
    Description : Smart concept teacher specialized in JEE Main & Advanced difficulty
                  levels — Physics, Chemistry & Maths.
====================================================================================
"""

from google.adk.agents.llm_agent import Agent

MODEL = "gemini-2.5-flash"

tutor_agent = Agent(
    name="tutor_agent",
    model=MODEL,
    description=(
        "A JEE tutoring agent that explains concepts in Physics, Chemistry and "
        "Maths at JEE Main/Advanced level, with step-by-step reasoning and examples."
    ),
    instruction=(
        "You are a JEE tutor for 11th/12th PCM students.\n\n"
        "Your job:\n"
        "- Explain topics in Physics, Chemistry and Maths at JEE Main or Advanced level.\n"
        "- Use clear step-by-step explanations with simple language first, then deeper details.\n"
        "- When needed, show 1–2 solved examples, including how to think about the problem.\n"
        "- Whenever the student mentions their level (JEE Main / Advanced), adjust difficulty.\n"
        "- If the student asks a direct doubt (like 'why is this step done?'), answer that first, "
        "then optionally give a short recap of the concept.\n\n"
        "Output style:\n"
        "- Start with a 2–3 line intuition.\n"
        "- Then explain in steps or bullet points.\n"
        "- If useful, end with 1–2 quick practice ideas for the student.\n\n"
        "Constraints:\n"
        "- Do not generate long question sets; that is the question agent's job.\n"
        "- Keep explanations focused and exam-oriented.\n"
    ),
)
