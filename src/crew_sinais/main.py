#!/usr/bin/env python
import sys
from crew_sinais.crew import InsightsCrewCrew
from datetime import datetime


def run():
    inputs = {
        'context': 'Car insurance',
        'current_year': datetime.now().year
    }
    InsightsCrewCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'context': 'Car insurance',
        'current_year': datetime.now().year
    }
    try:
        InsightsCrewCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
