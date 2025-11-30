# Vandana_JEE_Mentor — JEE Multi-Agent AI Mentor

**Capstone Project — AI Agents Intensive with Google**

Vandana is an intelligent multi-agent system designed to support JEE aspirants with:

-  Personalised study plans
-  Topic explanations
-  Practice questions
-  Performance evaluation with progress tracking

Built using Google **ADK (Agent Development Kit)**  
and **Gemini 2.5** models.

---

## Team Information

    
   | Team Name   | Anagha_Vandana                                                                |
   |-------------|-------------------------------------------------------------------------------|
   | Project     | Vandana_JEE_Mentor                                                            |
   | Competition | AI Agents Intensive with Google – Capstone Project                            |
   | Members     | DHRUVIN NARENDRA BAROT *(Lead Developer)*<br>VARDHAN PATEL<br>ANUPKUMAR SINGH |


---
## Problem Statement

### JEE (Joint Entrance Examination) is one of the most competitive exams in India.  

Students often struggle with:
* Not knowing **what to study** and **how much to study**
* Poor time allocation across Physics, Chemistry, and Maths
* Identifying and recovering from **weak topics**
* Getting **quality practice** questions at the right level
* Lack of constant evaluation and **feedback loops**
* No personalised guidance outside coaching

This results in:
* Low confidence  
* Inefficient learning  
* Underperformance in exams despite efforts  

There is a strong need for a **personal AI mentor** that supports every step of preparation.

---

## Solution Overview

**Vandana_JEE_Mentor** introduces a **multi-agent AI system** that acts as a personalized JEE mentor.

Powered by Google **ADK** and **Gemini 2.5**, Vandana:

* Creates adaptive daily study plans  
* Teaches concepts using a tutor agent  
* Generates exam-style questions instantly  
* Evaluates answers and tracks progress  
* Improves strategy based on performance  

Students get a **24x7 intelligent coaching companion** without needing paid coaching support.

---

## System Architecture

```mermaid
flowchart TD
    User -->|asks| Vandana_Root
    Vandana_Root -->|study plan| Planner_Agent
    Vandana_Root -->|explain topics| Tutor_Agent
    Vandana_Root -->|generate questions| Question_Agent
    Vandana_Root -->|evaluate answers| Evaluator_Agent
    Planner_Agent -->|get syllabus| Syllabus_Tool
    Evaluator_Agent -->|update mastery| Progress_Tool
````

---

## Workflow of the System

```mermaid
sequenceDiagram
    User->>Vandana_Root: Request (plan, explanation, questions, evaluation)
    Vandana_Root->>Planner_Agent: Study Plan Request
    Planner_Agent->>Syllabus_Tool: Fetch topics
    Planner_Agent->>Progress_Tool: Check mastery
    Planner_Agent-->>Vandana_Root: Personalized Plan

    Vandana_Root->>Tutor_Agent: Explain Topic
    Tutor_Agent-->>Vandana_Root: Simplified Explanation

    Vandana_Root->>Question_Agent: Generate Practice
    Question_Agent-->>Vandana_Root: Questions + Solutions

    User->>Evaluator_Agent: Submit Answers
    Evaluator_Agent->>Progress_Tool: Update Progress
    Evaluator_Agent-->>Vandana_Root: Feedback + Tips

    Vandana_Root-->>User: Final response
```

---

## Project Structure

```text
Vandana_JEE_Mentor/
│
├─ app.py                 # CLI runner (local chat interface)
├─ adk.yaml               # Used for ADK Web deployment
│
├─ agents/
│   ├─ agent.py           # Bridge file for ADK (exposes root_agent)
│   ├─ Vandana_root/
│   │   └─ agent.py       # MAIN orchestrator (Vandana)
│   ├─ planner_agent/
│   │   └─ agent.py
│   ├─ tutor_agent/
│   │   └─ agent.py
│   ├─ question_agent/
│   │   └─ agent.py
│   └─ evaluator_agent/
│       └─ agent.py
│
├─ tools/
│   ├─ syllabus_tools.py
│   └─ progress_tools.py
│
└─ data/
|   └─ progress.json      # Auto-generated progress tracking
└─ tests/
   ├─ __init__.py
   └─ test_vandana_agents.py
```

---

## Run Project (Local CLI)

### Install dependencies first:

```bash
pip install google-generativeai-agents google-generativeai
```

### Add your API key:

Create `.env` file in project root:

 ```bash  
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Start chat:

```bash
python app.py
```

---

## Run on ADK Web (Browser UI)

Start server inside project root:

```bash
adk web .
```

Open:

[http://localhost:8000](http://localhost:8000)

Select app: **agents**

A web chat UI will appear

> Note: First message is user-triggered in ADK Web.

---

## Features Supported


* Personalised daily JEE study planner
  
* Weak/strong topic consideration

* Syllabus-aware schedule generation

* Concept tutoring for PCM

* Question generator (JEE Mains/Adv)

* Short answers + key steps

* Answer evaluation

* Progress tracking & update

* Modular multi-agent architecture

* Auto greeting (CLI mode)

* ADK Web UI chat

---

## Future Enhancements

* Voice-based interaction

* Weekly/monthly plan visualisation dashboard

* Adaptive difficulty system based on performance analytics

* User login & multi-user support

* Notification system (daily task reminders)

---

## Key Learning Outcomes

* Practical usage of LLM Agents & tool orchestration

* Multi-agent autonomy with clear responsibility separation

* JSON-based state management for adaptive learning

* Hands-on experience with Google ADK & Gemini models

* Scalable AI architecture for real-world education

---

## Demo Use Cases

### Try asking Vandana:

> "Help me make a 1-month JEE Main plan."

> "Explain Newton’s laws at JEE Main level."

> "Give 5 medium calculus questions."

> "Check if my answer is correct: Work = F × d = 200 J?"

---

## Tests

This project includes a minimal integration test to verify that the **Vandana root agent**
can be loaded and produce a reasonable response via `InMemoryRunner`.

Test files are located in:

```text
Vandana_JEE_Mentor/
└─ tests/
   ├─ __init__.py
   └─ test_vandana_agents.py
```

## Run the tests

### Install pytest if not already installed:

```bash
pip install pytest
```

### From the project root (Vandana_JEE_Mentor), run:

```bash
pytest
```

>Note: The integration test calls the real Gemini model via Google ADK,
>so it requires a valid GOOGLE_API_KEY in your .env file.

---

## License

> Internal academic project. All rights reserved by authors.
