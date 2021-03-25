import csv
import sys

sys.setrecursionlimit(1000000)
# key: cost, value: number of sequences (cycles*10)
m = {}
cost_matrix = []
visited = [False] * 10


def calculate_cost(arr):
    c = 0
    n = len(arr)
    for i in range(n):
        c += cost_matrix[arr[i % n]][arr[(i + 1) % n]]
    return c


def permutations(A, i, n, seq):
    if i == n:
        cost = calculate_cost(seq)
        if cost in m.keys():
            m[cost] += 1
        else:
            m[cost] = 1
        return

    for j in range(len(A)):
        if not visited[j]:
            seq[i] = A[j]
            visited[j] = True
            permutations(A, i + 1, n, seq)
            visited[j] = False


def print_cost_matrix():
    print("Cost Matrix:")
    for i in range(0, 10):
        cost_matrix.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    nums = [
        [1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1]
    ]

    for i in range(0, 10):
        num1 = nums[i]
        for j in range(0, 10):
            num2 = nums[j]
            cost = 0
            for bit in range(0, 7):
                if num1[bit] != num2[bit]:
                    cost += 1
            cost_matrix[i][j] = cost
            cost_matrix[j][i] = cost

    for i in range(0, 10):
        print(cost_matrix[i])


def print_csv():
    print("Cost.csv file generated!")
    with open('cost.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for key in sorted(m):
            writer.writerow([key, int(m[key] / 10)])
    print("\n")


def evaluate_cycle_cost(n):
    print("\n")
    arr = [None] * n
    for i in range(n):
        for j in range(n):
            arr[j] = (j + i) % n
        print(arr, ": cost = ", calculate_cost(arr))
    print("For the given cycles, all costs are equal!\n")


def print_best_worst():
    best_cost = -1
    worst_cost = 71 # cost cannot cross 70
    for i in m.keys():
        best_cost = max(i, best_cost)
        worst_cost = min(i, worst_cost)
    print("Best cost =", best_cost, ", Worst cost =", worst_cost, "\n")


def print_cycle_count():
    print("Cost, Number of cycles")
    # every cycle will be repeated 10 times in permutation
    for i in m.keys():
        print(i, ",", int(m[i] / 10))


if __name__ == '__main__':
    # main algorithm
    print_cost_matrix()
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    seq = [None] * 10
    # number of permutations = 3628800
    permutations(A, 0, len(A), seq)

    h = 0
    for i in sorted(m):
        h += m[i]
    print(h)

    # Stage D: Evaluating the Cost of a Counting Cycle
    evaluate_cycle_cost(10)
    # Stage C: Best and Worst Cycles
    print_best_worst()
    # Stage B: Counting Cycles of Each Cost
    print_cycle_count()
    # Stage B+: File Output and Displays
    print_csv()
