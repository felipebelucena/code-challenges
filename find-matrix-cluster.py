from collections import deque

def get_adjacents(currentPosition, maxPosition):
  row, column = currentPosition
  maxRow, maxColumn = maxPosition
  adj_positions = []
  
  if row > 0:
      adj_positions.append((row - 1, column))
  if row < maxRow:
      adj_positions.append((row + 1, column))
  if column > 0:
      adj_positions.append((row, column - 1))
  if column < maxColumn:
      adj_positions.append((row, column + 1))
  
  return adj_positions

def find_clusters(graph):
  visited = set()
  clusters = 0
  
  for pos in graph.keys():
    if pos not in visited:
      clusters += 1
      visited.add(pos)
      queue = deque([pos])
      while len(queue):
        node = queue.popleft()
        for edge in graph[node]:
          if edge not in visited:
            visited.add(edge)
            queue.append(edge)

  return clusters

def number_of_clusters(rows, columns, grid):
  graph = {}
  maxPos = (rows - 1, columns - 1)
  for row in range(rows):
    for column in range(columns):
      if grid[row][column]:
        pos = (row, column)
        graph[pos] = [(i, j) for i, j in get_adjacents(pos, maxPos) if grid[i][j]]
  
  return find_clusters(graph)

if __name__ == '__main__':
   # no clusters
  assert number_of_clusters(3, 3, [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
  ]) == 0

  # 1 cluster
  assert number_of_clusters(3, 5, [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
  ]) == 1

  assert number_of_clusters(5, 4, [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
  ]) == 3

  assert number_of_clusters(4, 4, [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
  ]) == 4

  assert number_of_clusters(5, 7, [
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1],
  ]) == 5

  assert number_of_clusters(5, 5, [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
  ]) == 5

  assert number_of_clusters(4, 6, [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
  ]) == 2

  assert number_of_clusters(4, 6, [
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
  ]) == 3