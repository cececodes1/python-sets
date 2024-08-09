'''
1. Python Sets Adventure
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

'''

#  the sets of routes
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#  the common routes
common_routes = set()
for route in our_routes:
    if route in competitor_routes:
        common_routes.add(route)

print("Destinations that both airlines fly to:", common_routes)

#  our unique routes
our_unique_routes = our_routes - competitor_routes
print("Destinations unique to our airline:", our_unique_routes)

#  competitor's unique routes
competitor_unique_routes = competitor_routes - our_routes
print("Destinations unique to competitor's airline:", competitor_unique_routes)

#  routes that neither airline shares
all_routes = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK", "AMS", "FRA",}
neither_routes = all_routes - (our_routes | competitor_routes)
print("Destinations that neither airline shares:", neither_routes)