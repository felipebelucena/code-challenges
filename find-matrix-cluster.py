def get_adjacent_positions(currentPosition, maxPosition):
  row, column = currentPosition
  maxRow, maxColumn = maxPosition
  adj_positions = []
  
  if row > 0:
      adj_positions.append((row - 1, column))
  if row < maxRow - 1:
      adj_positions.append((row + 1, column))
  if column > 0:
      adj_positions.append((row, column - 1))
  if column < maxColumn - 1:
      adj_positions.append((row, column + 1))
  
  return adj_positions

def find_clusters(graph):
  visited = { position: False for position in graph.keys()}
  clusters = 0
  
  for pos in graph.keys():
    print(pos, " ", visited[pos])
    if not visited[pos]:
      clusters += 1
      visited[pos] = True
      queue = [pos]
      while len(queue):
        node = queue.pop(0) # dequeue
        for edge in graph[node]:
          if not visited[edge]:
            visited[edge] = True
            queue.append(edge)

  return clusters

def number_of_clusters(rows, columns, grid):
  graph = {}
  maxPosition = (rows, columns)
  for row in range(rows):
    for column in range(columns):
      position = (row, column)
      adj_positions = get_adjacent_positions(position, maxPosition)
      graph[position] = [(i, j) for i, j in adj_positions if grid[i][j]]
  
  return find_clusters(graph)

if __name__ == '__main__':
  # test case 1
  assert number_of_clusters(5, 4, [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1]
  ]) == 3

  # # test case 1
  # assert number_of_clusters(4, 4, [
  #   [1, 0, 0, 0],
  #   [0, 1, 0, 0],
  #   [0, 0, 1, 0],
  #   [0, 0, 0, 1],
  # ]) == 4