'''
A plane can maximum cover a distance of k units. There are multiple airports on x- axis 
represented by 1 and if there are no airports it is represented by 0 . 

What is the minimum number of stops that must be taken by the plane to reach destination 
(x,0) on x-axis. 

Return -1 is the destination is unreachable. Start of plane [0,0] i.e. origin
'''

def glider(maxDistance, destination, airports):
    destination = destination[0]
    stops = 0
    i, n = 0, len(airports)
    # we use shrinking window technique
    while i + maxDistance < n:
        j = i + maxDistance
        while j > i and airports[j] == 0:
            # shrink the window if not airport
            j-=1

        if j == i:  # we are back at origins so dest cannot be reached
            return -1

        stops+=1
        # set new beginning for a new window begins
        i = j
    return stops


maxDistance = 5
destination = [4,0]
airports = [1, 0, 1, 1, 1]
print(glider(maxDistance, destination, airports))


maxDistance = 5
destination = [8, 0]
airports = [1, 0, 0, 0, 0, 0, 0, 1, 1]
print(glider(maxDistance, destination, airports))


maxDistance = 3
destination = [8, 0]
airports = [1, 0, 0, 1, 1, 1, 1, 1, 1]
print(glider(maxDistance, destination, airports))
