"""
Debate Prep Agent — A multi-agent system that helps users prepare for
negotiations, interviews, or debates by simulating the opposition.

Architecture:
  root_agent (Coordinator) — routes conversation and manages the debate flow
    ├── debate_round (SequentialAgent) — runs one round of debate prep
    │     ├── interrogator — attacks the user's argument
    │     ├── fact_checker — verifies claims from both sides
    │     └── coach — gives private strategic advice
"""

import os
from google.adk.agents import LlmAgent, SequentialAgent

MODEL_ID = os.getenv("MODEL_ID", "gemini-2.5-flash")

from debate_prep_agent.agents.interrogator import interrogator_agent
from debate_prep_agent.agents.fact_checker import fact_checker_agent
from debate_prep_agent.agents.coach import coach_agent


# Sequential pipeline: Interrogator → Fact-Checker → Coach
debate_round = SequentialAgent(
    name="debate_round",
    description="Runs one full round of debate prep: attack, verify, then coach.",
    sub_agents=[interrogator_agent, fact_checker_agent, coach_agent],
)


ROOT_INSTRUCTION = """You are the Debate Prep Coordinator — a system that helps users prepare for
negotiations, interviews, and debates by simulating the opposition.

## How you work:

1. **Setup phase**: When the user first arrives, ask them:
   - What is the debate/negotiation topic?
   - What is their position or argument?
   Save the topic to state key `debate_topic` and their argument to state key `user_argument`.

2. **Debate round**: Once you have both the topic and argument, transfer to the
   `debate_round` agent. This will run the Interrogator, Fact-Checker, and Coach
   in sequence.

3. **After the round**: Present the results to the user in this order:
   - The Interrogator's critique (from state `interrogator_response`)
   - The Fact-Checker's report (from state `fact_checker_response`)
   - The Coach's private advice (from state `coach_response`)

4. **Next round**: Ask the user if they want to refine their argument and go again.
   If they provide a new/updated argument, update state `user_argument` and run
   another debate round.

## Rules:
- Always be encouraging. This is a training tool, not a judgment system.
- Keep the flow clear: setup → round → results → iterate.
- If the user seems confused, explain how the system works.
- You can handle casual conversation, but always steer back to debate prep.
"""


root_agent = LlmAgent(
    name="debate_prep_coordinator",
    model=MODEL_ID,
    description="Main coordinator for the debate prep system. Manages the flow between setup, debate rounds, and results.",
    instruction=ROOT_INSTRUCTION,
    sub_agents=[debate_round],
)
