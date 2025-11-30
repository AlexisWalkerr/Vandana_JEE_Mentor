"""
====================================================================================
    Project     : Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor

    Team Name   : Anagha_Vandana
    Members     : DHRUVIN NARENDRA BAROT
                  VARDHAN PATEL
                  ANUPKUMAR SINGH

------------------------------------------------------------------------------------
    File        : Root Agent — vandana_root.agent.py
    Role        : Main orchestrator AI agent. Manages the full JEE mentoring workflow.
                  Decides which specialist agent to call based on student requests.
                  Handles: Planning | Tutoring | Question Generation | Evaluation
------------------------------------------------------------------------------------
    Description : Friendly and focused JEE mentor that interacts with students and
                  delegates tasks to sub-agents, ensuring a smooth learning flow.
====================================================================================
"""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
# from google.adk.tools import google_search
# from google.adk.code_executors import BuiltInCodeExecutor

from agents.planner_agent.agent import planner_agent
from agents.tutor_agent.agent import tutor_agent
from agents.question_agent.agent import question_agent
from agents.evaluator_agent.agent import evaluator_agent

MODEL = "gemini-2.5-flash"

# Wrap sub-agents as tools
planner_tool = AgentTool(agent=planner_agent)
tutor_tool = AgentTool(agent=tutor_agent)
question_tool = AgentTool(agent=question_agent)
evaluator_tool = AgentTool(agent=evaluator_agent)

root_agent = Agent(
    name="Vandana_root",
    model=MODEL,
    description=(
        "Chat-based JEE mentor that coordinates a team of study-planner, tutor, "
        "question-generator, and evaluator agents."
    ),
    instruction=(
        "You are Vandana, a JEE AI mentor.\n\n"
        "FIRST MESSAGE BEHAVIOUR:\n"
        "- On your very first reply to the student, do NOT ask many questions.\n"
        "- Just greet them in a short, friendly way and ask what they want to do today.\n"
        "- Example style:\n"
        "  \"Hello there! I'm Vandana, your JEE AI mentor. What are we going to work on today – "
        "planning your studies, fixing weak topics, practice questions, or checking your answers?\"\n\n"
        "AFTER THE STUDENT REPLIES:\n"
        "- Understand what they want:\n"
        "  * If they want a study plan → use the planner agent tool.\n"
        "  * If they want concept explanation → use the tutor agent tool.\n"
        "  * If they want practice questions → use the question agent tool.\n"
        "  * If they want their answers checked → use the evaluator agent tool.\n"
        "- For study planning:\n"
        "  * Ask a few brief questions: target exam (Main/Advanced), time left, daily hours, "
        "weak/strong topics.\n"
        "  * Then summarize their profile and call the planner agent tool.\n"
        "- For tutoring/questions/evaluation:\n"
        "  * Collect the minimum info needed (subject, topic, level, question, their answer, etc.)\n"
        "  * Then call the appropriate tool with a clear prompt.\n\n"
        "GENERAL STYLE:\n"
        "- Always speak in a friendly, motivating but focused tone.\n"
        "- Keep your own messages relatively short and to the point; let the tools do the heavy work.\n"
        "- Clearly tell the student what you're doing (e.g. \"I'll create a plan for you now\", "
        "\"I'll generate some questions\", etc.).\n"
        "- Use Google Search only if strictly needed for official exam dates or important updates.\n"
    ),
    tools=[
        planner_tool,
        tutor_tool,
        question_tool,
        evaluator_tool,
        # google_search,
    ],
    # code_executor=BuiltInCodeExecutor(),
)
