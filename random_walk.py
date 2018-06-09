#!/usr/bin/python

import random

def random_walk(n):
	x = y = 0
	for i in range(n):
		(dx, dy) = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
		x += dx
		y += dy
	return (x, y)


total_walks = 30000
threshold = 4

for steps in range(1, 51):
	acceptable = 0
	for i in range(total_walks):
		x, y = random_walk(steps)
		distance = abs(x) + abs(y)
		if distance <= threshold:
			acceptable += 1
	acceptable_percentage = float(acceptable) / total_walks * 100
	if acceptable_percentage >= 50:
		longest_acceptable = steps
	print "Walked: {} steps, less than threshold: {}, {}% of the time".format(steps, threshold, acceptable_percentage)

print "Longest acceptable walk: {} steps".format(longest_acceptable)
