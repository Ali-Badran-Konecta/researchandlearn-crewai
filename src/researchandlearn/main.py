#!/usr/bin/env python
import warnings
# Filter warnings before any other imports
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
warnings.filterwarnings("ignore", category=UserWarning, message=".*shadows an attribute in parent.*")
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic.*")

from researchandlearn.crew import Researchandlearn

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the Roadmap Factory crew to generate a concise learning roadmap
    """
    
    topic = "Backend"
    
    inputs = {
        'topic': topic
    }
    
    try:
        Researchandlearn().crew().kickoff(inputs=inputs)
        
        print("\n✅ Roadmap generation complete!")
        print(f"📄 Output saved to: {topic.replace(' ', '-')}-Learning-Roadmap.md")

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
