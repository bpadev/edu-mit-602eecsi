# A robot might try to move forward without hitting something by defining a procedure:
def step():
    distToFront = min(frontSonarReadings)
    motorOutput(gain * (distToFront - desiredDistance), 0.0)