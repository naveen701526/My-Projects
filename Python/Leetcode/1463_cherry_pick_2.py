class Solution:
	def cherryPickup(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])

		@lru_cache(None)
		def dfs(r,c1,c2):
			if r==m:
				return 0

			ch = grid[r][c1] if c1==c2 else grid[r][c1]+grid[r][c2]            
			res = 0
			for p in range(c1-1,c1+2):
				for q in range(c2-1,c2+2):
					if 0<=p<n and 0<=q<n:
						res = max(res,dfs(r+1,p,q))
			return ch+res

		return dfs(0,0,n-1)
