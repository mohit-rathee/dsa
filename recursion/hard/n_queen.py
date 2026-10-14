def printgrid(mat):
    for i in mat:
        print(i)

def clone(mat):
    cloned_mat = []
    for row in mat:
        cloned_mat.append(row[:])
    return cloned_mat

dirs= [
        [1,0],      # down
        [-1,0],     # up
        [0,1],      # right
        [0,-1],     # left
        [1,1],      # down-right diagnol
        [-1,-1],    # anti-down-right diagnol
        [-1,1],      # up-right diagnol
        [1,-1],    # anti-up-right diagnol
        ]

class Solution:
    def is_valid_move(self,x,y):
        if (self.n>x and x>=0) and (self.n>y and y>=0):
            return True
        return False

    def is_another_queen_in_way(self,x,y,mat):
        for dx,dy in dirs:
            nx=x+dx
            ny=y+dy
            while self.is_valid_move(nx,ny):
                # print(x,y,nx,ny)
                # printgrid(mat)
                if mat[nx][ny] == 'Q':
                    return True
                nx+=dx
                ny+=dy
        return False

    def is_valid_placement(self,mat):
        for x in range(self.n):
            for y in range(self.n):
                if mat[x][y] == 'Q':
                    if self.is_another_queen_in_way(x,y,mat):
                        return False
        return True



    def place_and_check_n_queen(self,x,y,mat,queens):
        # marks queen's position
        mat[x][y] = 'Q'
        queens+=1
        if self.is_another_queen_in_way(x,y,mat):
            # un-marks it
            mat[x][y] = '.'
            # print('invalid move')
            return
        if queens == self.n:
            # printgrid(mat)
            # print('valid placement')
            mat_clone = clone(mat)
            self.result.append(mat_clone)
        # printgrid(mat)
        # try out all other possibitlities
        for nx in range(self.n):
            for ny in range(self.n):
                if ((x==nx and y<ny) or x<nx):
                    # print('placing at',nx,ny,'with',queens,'queens')
                    self.place_and_check_n_queen(nx,ny,mat,queens)
        # print('------end------')
        # un-marks it
        mat[x][y] = '.'

    def n_queen(self,n):
        self.n = n
        # build matrix
        mat = [['.' for i in range(n)] for i in range(n)]
        print(n)
        queens=0
        self.result = []
        for x in range(self.n):
            for y in range(self.n):
                self.place_and_check_n_queen(x,y,mat,queens)
        # return self.result
        result = []
        for placement in self.result:
            p=[]
            for row in placement:
                p.append(''.join(row))
            printgrid(placement)
            print()
            result.append(p)
        
        # print(result)
        return result


sol = Solution()
sol.n_queen(4)
