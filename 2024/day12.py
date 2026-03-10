
# f = open("day12testinput.txt", "r")
f = open("day12input.txt", "r")

IS_PART_ONE = True

class Grid:
	grid: list
	grid_width: int
	grid_height: int

	def __init__(self):
		self.grid = []
		self.grid_width = 0
		self.grid_height = 0
	
	def calculate_dimensions(self):
		self.grid_width = len(self.grid[0])
		self.grid_height = len(self.grid)
	
	def get_tile(self, x, y):
		if x >= 0 and y >= 0 and x < self.grid_width and y < self.grid_height:
			return self.grid[y][x]
		return None
	
	def print(self):
		for y in range(self.grid_height):
			line = ""
			for x in range(self.grid_width):
				line += self.grid[y][x].plant
			print(line)


main_grid = Grid()
zones = []

class Tile:
	x: int
	y: int
	index: int
	plant: str
	zone_id: int

	def __init__(self, x, y, plant, grid):
		self.x = x
		self.y = y
		self.index = grid.grid_width * y + x
		self.plant = plant
		self.zone_id = -1
		

class Zone:
	tiles: list
	zone_id: int
	dimensions: list
	tile_min_x: int
	tile_min_y: int

	def __init__(self, zone_id):
		self.zone_id = zone_id
		self.tiles = []
		self.dimensions = [0, 0]
		self.tile_min_x = -1
		self.tile_min_y = -1

	def add_tile(self, tile):
		self.tiles.append(tile)
		tile.zone_id = self.zone_id
	
	def get_dimensions(self):
		if len(self.tiles) == 0:
			dimensions = [0, 0]
			return dimensions
		min_x = self.tiles[0].x
		max_x = self.tiles[0].x
		min_y = self.tiles[0].y
		max_y = self.tiles[0].y

		for tile in self.tiles:
			if tile.x < min_x:
				min_x = tile.x
			if tile.x > max_x:
				max_x = tile.x
			if tile.y < min_y:
				min_y = tile.y
			if tile.y > max_y:
				max_y = tile.y

		self.tile_min_x = min_x
		self.tile_min_y = min_y
		dimensions = [max_x + 1 - min_x, max_y + 1 - min_y]
		return dimensions





# build grid
lines = f.readlines()

for y in range(len(lines)):
	main_grid.grid.append([])
	for x in range(len(lines[y])):
		if lines[y][x] != '\n':
			main_grid.grid[y].append(Tile(x, y, lines[y][x], main_grid))

main_grid.calculate_dimensions()


# build zones
DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def add_adjacent_tiles_to_zone(tile, zone):
	for dir in DIRECTIONS:
		adj_tile = main_grid.get_tile(tile.x + dir[0], tile.y + dir[1])
		if adj_tile != None and adj_tile.zone_id == -1 and adj_tile.plant == tile.plant:
			zone.add_tile(adj_tile)
			add_adjacent_tiles_to_zone(adj_tile, zone)
	

for x in range(main_grid.grid_width):
	for y in range(main_grid.grid_height):
		tile = main_grid.get_tile(x, y)
		if tile.zone_id == -1:
			new_zone = Zone(len(zones))
			zones.append(new_zone)
			new_zone.add_tile(tile)
			add_adjacent_tiles_to_zone(tile, new_zone)

# calculate fences
total_price = 0

for zone in zones:
	zone_dim = zone.get_dimensions()
	zone_grid = Grid()
	for y in range(zone_dim[1] + 2):
		zone_grid.grid.append([])
		for x in range (zone_dim[0] + 2):
			tile_found = False
			for tile in zone.tiles:
				if tile.x - zone.tile_min_x + 1 == x and tile.y - zone.tile_min_y + 1 == y:
					zone_grid.grid[y].append(Tile(x, y, "P", zone_grid))
					tile_found = True
					break
			if not tile_found:
				zone_grid.grid[y].append(Tile(x, y, "-", zone_grid))

	zone_grid.calculate_dimensions()
	zone_perimeter = 0

	if IS_PART_ONE:
		for y in range(zone_grid.grid_height):
			for x in range(zone_grid.grid_width):
				zone_tile = zone_grid.get_tile(x, y)
				if zone_tile.plant == "P":
					for dir in DIRECTIONS:
						adj_tile = zone_grid.get_tile(zone_tile.x + dir[0], zone_tile.y + dir[1])
						if adj_tile != None and adj_tile.plant == "-":
							zone_perimeter += 1
	else:
		# todo
		zone_perimeter = 0
	
	# print(f"Zone {zone.zone_id} - growing {zone.tiles[0].plant} - {len(zone.tiles)} plants - dimensions: {zone_dim}, perimeter: {zone_perimeter}")
	# zone_grid.print()
	total_price += zone_perimeter * len(zone.tiles)

print(f"Total fence prince: {total_price}")