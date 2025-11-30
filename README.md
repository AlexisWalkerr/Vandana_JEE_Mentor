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
    └─ progress.json      # Auto-generated progress tracking
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

* Weekly/monthly plan visualization dashboard

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

> "Help me make a 1 month JEE Main plan."

> "Explain Newton’s laws at JEE Main level."

> "Give 5 medium calculus questions."

> "Check if my answer is correct: Work = F × d = 200 J?"

---

## License

> Internal academic project. All rights reserved by authors.
