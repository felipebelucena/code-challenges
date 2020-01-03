def get_outdated_adjacents(currentPosition, maxPosition, grid):
  row, column = currentPosition
  maxRow, maxColumn = maxPosition
  adjacents = []
  
  if row > 0 and not grid[row - 1][column]:
      adjacents.append((row - 1, column))
  if row < maxRow and not grid[row + 1][column]:
      adjacents.append((row + 1, column))
  if column > 0 and not grid[row][column - 1]:
      adjacents.append((row, column - 1))
  if column < maxColumn and not grid[row][column + 1]:
      adjacents.append((row, column + 1))
  
  return adjacents

def update_grid(rows, columns, grid):
  maxPosition = (rows - 1, columns - 1)
  cells_to_update = []
  for row in range(rows):
    for column in range(columns):
      if grid[row][column]:
        adjacents = get_outdated_adjacents((row, column), maxPosition, grid)
        cells_to_update.extend(adjacents)

  for row, column in cells_to_update:
    grid[row][column] = 1

def has_zero_values(grid):
  for row in grid:
    for value in row:
      if not value:
        return True
  return False

def number_of_iterations(rows, columns, grid):
  iterations = 0
  
  while has_zero_values(grid):
    iterations += 1
    update_grid(rows, columns, grid)
  
  return iterations

if __name__ == '__main__':
  # test case 1
  assert number_of_iterations(3, 3, [
    [1, 0, 1],
    [0, 0, 0],
    [0, 1, 0],
  ]) == 1

 # test case 2
  assert number_of_iterations(5, 5, [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
  ]) == 4

  # test case 3
  assert number_of_iterations(5, 6, [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
  ]) == 3

  # test case 4
  assert number_of_iterations(4, 2, [
    [1, 1],
    [1, 1],
    [1, 1],
    [1, 1],
  ]) == 0