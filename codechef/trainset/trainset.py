from functools import reduce

def main():
  test_cases = int(input())
  for _ in range(test_cases):
    words = {}
    samples = int(input())
    for _ in range(samples):
      word, mark = input().split()
      if word not in words:
        words[word] = {'0': 0, '1': 0}
      words[word][mark] += 1

    print(reduce(lambda acc, item: acc + max(item.values()), words.values(), 0))

if __name__ == '__main__':
  main()