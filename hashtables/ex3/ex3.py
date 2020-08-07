def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # print(len(arrays))

    foundNumbers = {}

    result = []

    for k in range(len(arrays[0])):
        foundNumbers[arrays[0][k]] = 1

    for i in range(1, len(arrays)):
        for j in range(len(arrays[i])):
            if arrays[i][j] in foundNumbers:
                foundNumbers[arrays[i][j]] += 1

    for l in range(len(arrays[0])):
        if foundNumbers[arrays[0][l]] == len(arrays):
            result.append(arrays[0][l])

    # for j in range(len(arrays[0])):
    #     for i in range(1, len(arrays)):
    #         if arrays[i][j] in foundNumbers:
    #             foundNumbers[arrays[i][j]] += 1
    #         else:
    #             i = len(arrays[i]) * 2

    # for i in range(len(arrays[0])):
    #     for j in range(len(arrays)):
    #         # print(j)
    #         if arrays[0][i] not in arrays[j]:
    #             j = len(arrays) * 2
    #             # print("j went up?")
    #             # print(j)
    #     if j <= len(arrays):
    #         result.append(arrays[0][i])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
