"""
====================================================================================
    Project     : Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor

    Team Name   : Anagha_Vandana
    Members     : DHRUVIN NARENDRA BAROT
                  VARDHAN PATEL
                  ANUPKUMAR SINGH

------------------------------------------------------------------------------------
    File        : question_agent.agent.py
    Role        : Generates exam-oriented practice questions with answer keys and
                  short solutions, based on subject, topic, and difficulty.
------------------------------------------------------------------------------------
    Description : Creates customized question sets similar to JEE Main/Advanced,
                  helping students strengthen conceptual problem-solving skills.
====================================================================================
"""

from google.adk.agents.llm_agent import Agent

MODEL = "gemini-2.5-flash"

question_agent = Agent(
    name="question_agent",
    model=MODEL,
    description=(
        "A JEE question-generator agent that creates practice questions for "
        "Physics, Chemistry and Maths, with answers and brief solutions."
    ),
    instruction=(
        "You are a JEE practice question generator.\n\n"
        "Your job:\n"
        "- Generate exam-style questions for JEE Main/Advanced.\n"
        "- Support Physics, Chemistry and Maths.\n"
        "- For each question, also provide the final answer.\n"
        "- When appropriate, provide a short solution or key steps (not very long).\n\n"
        "Output format:\n"
        "- When the student asks for questions, first clarify:\n"
        "  * subject\n"
        "  * topic or chapter\n"
        "  * level (easy / medium / hard, Main / Advanced)\n"
        "  * how many questions (default 5 if not specified).\n"
        "- Then output questions in this structure:\n"
        "  Q1) <question>\n"
        "      Answer: <final answer>\n"
        "      Solution (short): <2–5 lines> (optional if user wants)\n"
        "  Q2) ...\n\n"
        "Constraints:\n"
        "- Keep questions relevant, not too trivial and not absurdly difficult.\n"
        "- If user only wants questions (no solutions), respect that.\n"
    ),
)
