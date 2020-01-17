from itertools import product
from functools import reduce

def main():
  test_cases = int(input())
  for _ in range(test_cases):
    rows, columns = [int(i) for i in  input().split()]
    total_blocked_rows, total_blocked_columns, grid_size =  [int(i) for i in input().split()]
    available_rows = []
    available_columns = []

    if total_blocked_rows:
      available_rows.append(rows // grid_size)
    else:
      available_rows.append(rows // grid_size)
    if total_blocked_columns:
      available_columns.append(columns // grid_size)
    else:
      available_rows.append(rows // grid_size)

    available_columns = [int(i) for i in input().split()] if total_blocked_columns else [columns]

    total = reduce(lambda i, j: i[0] * i[1] + j[0] + j[1] , product(available_rows, available_columns))
    print(total)
if __name__ == '__main__':
  main()