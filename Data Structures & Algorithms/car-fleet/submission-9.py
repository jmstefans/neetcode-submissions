class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # array can be the highway
        # no car starts at the target
        # helpful to order descending position so we can calculate if cars finish together based on their time to target
        # helpful to use a stack for the current fleet leader's speed
        
        # start at one because we will always have 1 car on the road and that way we can just leave stuff in the stack at the end
        carFleets = 1 
        roadArray = [] # position and time to target of all cars still on the road
        stack = [] # keep track of the current car fleet leader's time

        # initialize the road array and calculate time it takes each car to get to the target
        for i in range(len(position)): # O(n)
            roadArray.append([position[i], (target - position[i]) / speed[i]])

        # sort this array descending position as cars drive
        roadArray.sort(key=lambda x: x[0], reverse=True) # O(n log n)

        # Go through the array 
        for i in range(len(roadArray)):

            # if stack is empty push a new fleet leader's time
            if not stack:
                stack.append(roadArray[i][1])

            # if there's a fleet leader in the stack and it's faster
            # then we have a new fleet leader and we need to pop and increment
            elif stack[-1] < roadArray[i][1]:
                stack.pop()
                carFleets += 1
                stack.append(roadArray[i][1])

            # Else there's a fleet leader and it's slower, this car joins the fleet
            # and there's nothing to do
            
        
            # if car to the left has a greater time then the current car we know it's a fleet
            #if i > 0 and roadArray[i][1] <= roadArray[i - 1][1]:
             #   newFleet = False
              #  continue
            #else:
             #   newFleet = True

            #if newFleet:
             #   carFleets += 1



        # loop until no more cars 
        #while roadArray:

            # update positions and speeds after an hour goes by
           # for i in len(roadArray):

                # move the car by it's speed if no cars ahead of it
            #    newPotentialPosition = roadArray[i][0] + roadArray[i][1] 
             #   if i - 1 >= 0 and roadArray[i - 1][0] > newPotentialPosition:
              #      roadArray[i][0] = newPotentialPosition
               # else:
                                    

            # check if any cars have reached the target and pop them and update carFleets







        return carFleets