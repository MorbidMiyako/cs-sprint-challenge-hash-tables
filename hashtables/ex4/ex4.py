def has_negatives(numbersArray):
    """
    YOUR CODE HERE
    """
    # Your code here

    indiciesDict = {}

    limit = 0

    result = []

    for i in range(len(numbersArray)):
        if numbersArray[i] in indiciesDict:
            if numbersArray[i] >= numbersArray[indiciesDict[numbersArray[i]]]:
                result.append(numbersArray[i])
            else:
                result.append(numbersArray[indiciesDict[numbersArray[i]]])
            # returnArray = [i, indiciesDict[numbersArray[i]]]
            # returnArray.sort(reverse=True)
            # return returnArray
            # if numbersArray[i] >= numbersArray[indiciesDict[numbersArray[i]]]:
            #     print("if")
            #     print([i, indiciesDict[numbersArray[i]]])
            #     return [i, indiciesDict[numbersArray[i]]]
            # else:
            #     print("else")
            #     print([indiciesDict[numbersArray[i]], i])
            #     return [indiciesDict[numbersArray[i]], i]

        else:
            indiciesDict[limit - numbersArray[i]] = i

    result.sort()
    print(result)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
