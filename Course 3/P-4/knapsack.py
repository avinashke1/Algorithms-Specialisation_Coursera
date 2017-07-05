def knapsack(items, Weight):
  n = len(items)
  ranging = range(0, Weight + 1)

  last = [0 for x in ranging]

  for i in range(1, n + 1):
    print(100 * i / n)

    crow = []
    (v, w) = items[i - 1]

    for x in ranging:
      if x < w:
        crow.append(last[x])
      else:
        crow.append(max(last[x], last[x - w] + v))

    last = crow

  return last[Weight]

if __name__ == '__main__':
  filename = 'k2.txt'

  Weight = 0
  items = []

  with open(filename) as f:
    Weight = int(f.readline().rstrip().split(' ')[0])

    for line in f:
      [value, weight] = [int(x) for x in line.rstrip().split(' ')]

      items.append((value, weight))

  optimal_value = knapsack(items, Weight)

  print("Answer: ",optimal_value)
