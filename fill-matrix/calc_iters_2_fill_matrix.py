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
  cells_to_update = set()
  for row in range(rows):
    for column in range(columns):
      if grid[row][column]:
        for adj in get_outdated_adjacents((row, column), maxPosition, grid):
          cells_to_update.add(adj)

  for row, column in cells_to_update:
    grid[row][column] = 1

  return len(cells_to_update)

def number_of_iterations(rows, columns, grid):
  print('calculating interations for {} x {} grid'.format(rows, columns))
  iterations = 0
  
  while update_grid(rows, columns, grid):
    iterations += 1

  return iterations

if __name__ == '__main__':
  from sys import stdin

  test_cases = int(stdin.readline().rstrip())
  for test in range(1, test_cases + 1):
    rows, columns, expected = [int(x) for x in stdin.readline().rstrip().split(' ')]
    # print(rows, columns, expected)
    grid = []
    for row in range(rows):
      grid.append([int(x) for x in stdin.readline().rstrip().split(' ')])

    print(len(grid[0]))

    # print(grid)
    actual = number_of_iterations(rows, columns, grid)
    status = "passed" if expected == actual else "failed"
    print("Test case #{}:\n\tExpected: {}. Got: {}. {}".format(test, expected, actual, status))
    
    # read empty line
    stdin.readline()
  