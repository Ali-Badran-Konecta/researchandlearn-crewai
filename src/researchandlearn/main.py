#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from researchandlearn.crew import Researchandlearn

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the Roadmap Factory crew to generate a concise learning roadmap
    """
    import os
    
    # Get topic from environment variable or command line
    # topic = os.getenv('TOPIC')
    # if not topic and len(sys.argv) > 1:
    #     topic = " ".join(sys.argv[1:])
    # if not topic:
    #     topic = input("Enter the topic to research: ").strip() or "claude opus 4.5"
    
    # print(f"\n🚀 Starting Roadmap Factory for topic: '{topic}'")
    # print(f"📝 This will generate: {topic.replace(' ', '-')}-Learning-Roadmap.md")
    # print(f"⏱️  Estimated time: 5-10 minutes\n")
    topic = "AI LLMs"
    
    inputs = {
        'topic': topic
    }
    
    try:
        result = Researchandlearn().crew().kickoff(inputs=inputs)
        
        print("\n✅ Roadmap generation complete!")
        print(f"📄 Output saved to: {topic.replace(' ', '-')}-Learning-Roadmap.md")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Researchandlearn().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Researchandlearn().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        Researchandlearn().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = Researchandlearn().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
