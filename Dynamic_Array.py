def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for q, x, y in queries:
        idx = (x ^ lastAnswer) % n

        if q == 1:
            arr[idx].append(y)

        elif q == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


first = input().split()
n = int(first[0])
q = int(first[1])

queries = []

for i in range(q):
    queries.append(list(map(int, input().split())))

result = dynamicArray(n, queries)

for answer in result:
    print(answer)