def print_cost_matrix():

    cost_matrix = []
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_cost_matrix()
