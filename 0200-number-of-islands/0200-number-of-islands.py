class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def depthsearch(grid,row,col,rows,cols,visted):
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                ur=row+r
                uc=col+c
                if (ur>=0 and ur<rows and uc>=0 and uc<cols and grid[ur][uc]=='1' and visited[ur][uc]==0):
                    visited[ur][uc]=1
                    depthsearch(grid,ur,uc,rows,cols,visited)
                
        rows=len(grid)
        cols=len(grid[0])
        visited=[]
        for i in range(rows):
            visited.append([0]*cols)
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and visited[row][col]==0:
                    visited[row][col]=1
                    depthsearch(grid,row,col,rows,cols,visited)
                    count+=1
        return count
                    