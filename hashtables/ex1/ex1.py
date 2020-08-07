def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    indiciesDict = {}

    for i in range(length):
        if weights[i] in indiciesDict:
            returnArray = [i, indiciesDict[weights[i]]]
            returnArray.sort(reverse=True)
            return returnArray
            # if weights[i] >= weights[indiciesDict[weights[i]]]:
            #     print("if")
            #     print([i, indiciesDict[weights[i]]])
            #     return [i, indiciesDict[weights[i]]]
            # else:
            #     print("else")
            #     print([indiciesDict[weights[i]], i])
            #     return [indiciesDict[weights[i]], i]

        else:
            indiciesDict[limit - weights[i]] = i

    return None
