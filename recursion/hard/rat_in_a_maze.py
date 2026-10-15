from utils.matrix import printgrid


class Solution:
    directions = {
            'U':[-1,0], # up
            'D':[1,0],  # down
            'L':[0,-1], # left
            'R':[0,1],  # right
            }

    def is_valid(self,x,y,maze):
        if x<0 or y<0:
            return False
        if x>=len(maze) or y>=len(maze[0]):
            return False
        return True

    def mark_and_move(self,x,y,maze,path):
        if not self.is_valid(x,y,maze):
            return
        if maze[x][y] == 0:     # movement is not allowed
            return
        if maze[x][y] == '*':   # cell already visited
            return
        if x == len(maze)-1 and y == len(maze[0])-1:
            #done
            result = ''.join(path)
            self.result.append(result)
            return
        # mark rat if possible
        maze[x][y] = '*'
        #move in next direction
        for dir, dir_vec in self.directions.items():
            dx,dy = dir_vec
            nx = x+dx
            ny = y+dy
            path.append(dir)
            self.mark_and_move(nx,ny,maze,path)
            path.pop()

        # unmark rat
        maze[x][y] = 1


    def rat_in_a_maze(self,maze):
        # mouse at (0,0)
        printgrid(maze)
        if maze[0][0] == 0 or maze[-1][-1] == 0:
            # early exit
            return []
        # THINK:
            # YES : mark each cell we visited in a path with '*'
        self.result = []
        path = []
        self.mark_and_move(0,0,maze,path)
        print(self.result)
        return self.result

sol = Solution()
maze = [ 
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0], 
        [0, 1, 1, 1],
        ]
sol.rat_in_a_maze(maze)
