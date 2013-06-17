# each square in a 3x3 grid tells you how many of its edges should be filled in, to make a closed shape
# are any patterns ambiguous?

from itertools import product

# generate every possible pattern of filled-in squares in a 3x3 grid
grids = [[g[0:3],g[3:6],g[6:9]] for g in product([True,False],repeat=9)]

# given a pattern of filled-in squares, count the edges for each square
def detect_edges(grid):
	out=[[0,0,0],[0,0,0],[0,0,0]]
	for x in range(3):
		# there's an edge if two adjacent squares are different

		# do a row
		a = grid[x][0] != grid[x][1]
		b = grid[x][1] != grid[x][2]
		out[x][0] += a + grid[x][0]
		out[x][1] += a+b
		out[x][2] += b + grid[x][2]

		# do a column
		a = grid[0][x] != grid[1][x]
		b = grid[1][x] != grid[2][x]
		out[0][x] += a + grid[0][x]
		out[1][x] += a+b
		out[2][x] += b + grid[2][x]
	return out

#represent a grid as a single-line string
def grid_string(grid):
	return ','.join(','.join(str(x) for x in y) for y in grid)

#represent a grid as a 2d picture
def grid_dots(grid):
	return '_________\n'+'\n'.join(''.join(' # ' if x else ' - ' for x in y) for y in grid)

# for each shape-grid, work out its edge pattern, and store it in a dictionary
# shape-grids with the same edge pattern will be under the same key in the dictionary
edge_dict = {}
for grid in grids:
	s = grid_string(detect_edges(grid))
	l=edge_dict.setdefault(s,[])
	l.append(grid)

# print out the edge patterns that have more than one corresponding shape
for s,l in edge_dict.items():
	if len(l)>1:
		print(s)
		for grid in l:
			print(grid_dots(grid))
