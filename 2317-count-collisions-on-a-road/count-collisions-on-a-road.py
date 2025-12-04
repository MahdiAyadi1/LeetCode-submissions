class Solution:
    def countCollisions(self, directions: str) -> int:
        # original solution, didn't finish in time
        # collision = 0
        # for index in range(len(directions)):
        #     if directions[index] == "L" and ("R" in directions[:index] or "S" in directions[:index]):
        #         collision+=1
        #         directions=directions[:index]+"S"+directions[index+1:]
        #     elif directions[index] == "R" and ("L" in directions[index+1:] or "S" in directions[index+1:]):
        #         collision+=1
        #         directions= directions[:index]+"S"+directions[index+1:]
        # return collision
        # optimized
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        return directions.count("R") + directions.count("L")
