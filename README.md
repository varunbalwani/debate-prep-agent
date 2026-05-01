# Debate Prep Agent

A multi-agent system built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) that helps you prepare for debates, negotiations, and interviews by simulating the opposition.

**Live Demo:** [https://debate-prep-735254737103.us-central1.run.app](https://debate-prep-735254737103.us-central1.run.app)

## How It Works

You provide a topic and your argument. The system then runs a three-stage pipeline that stress-tests your position and coaches you on how to improve it.

```
Coordinator (root agent)
  └── debate_round (SequentialAgent)
        ├── Interrogator — attacks your argument, finds logical gaps
        ├── Fact-Checker — verifies claims from both sides using Google Search
        └── Coach — gives you private strategic advice on how to respond
```

### The Agents

**Coordinator** — Manages the overall flow. Collects your topic and argument, kicks off debate rounds, presents results, and asks if you want to iterate.

**Interrogator** — An adversarial opponent that identifies logical fallacies, weak assumptions, and unsupported claims. Presents counterarguments and pointed questions to expose gaps in your reasoning.

**Fact-Checker** — An impartial verification agent that extracts every factual claim from both your argument and the Interrogator's critique, then uses Google Search to rate each claim as VERIFIED, PARTIALLY TRUE, UNVERIFIED, or DEBUNKED.

**Coach** — A supportive strategic advisor that synthesizes everything (your argument, the attack, and the fact-check report) into actionable advice: what worked, how to counter each attack, suggested talking points, and rhetorical tips.

## Setup

### Prerequisites

- Python 3.10+
- A Google API key with access to Gemini models

### Installation

```bash
# Clone the repo
git clone <repo-url>
cd debate-prep-agent

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your-api-key-here
```

Optionally set a different model:

```
MODEL_ID=gemini-2.5-flash
```

The default model is `gemini-2.5-flash`.

## Usage

Run the agent using the ADK CLI:

```bash
adk run debate_prep_agent
```

Or launch the ADK web UI for a chat interface:

```bash
adk web
```

### Example Flow

1. The Coordinator asks for your debate topic and position.
2. You provide your argument.
3. The system runs a debate round:
   - The **Interrogator** tears apart your argument.
   - The **Fact-Checker** verifies every claim.
   - The **Coach** tells you how to come back stronger.
4. You refine your argument and go again.

## Project Structure

```
debate_prep_agent/
├── __init__.py              # Package entry point
├── agent.py                 # Root agent and sequential pipeline
├── agents/
│   ├── interrogator.py      # Adversarial debate opponent
│   ├── fact_checker.py      # Claim verification with Google Search
│   └── coach.py             # Strategic coaching advisor
└── tools/
    ├── __init__.py
    └── search.py            # Google Search tool wrapper
```

## License

This project is provided as-is for educational and personal use.
