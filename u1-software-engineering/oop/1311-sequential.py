# Moving an idealized robot in a square, if there is space in front of it.
if noObstacleInFront:
    moveDistance(1)
    turnAngle(90)
    moveDistance(1)
    turnAngle(90)
    moveDistance(1)
    turnAngle(90)
    moveDistance(1)
    turnAngle(90)

# A better program would probably be...
while lightValue < desiredValue:
    moveDistance(0.1)