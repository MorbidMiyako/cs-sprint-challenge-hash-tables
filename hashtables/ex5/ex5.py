# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    files_dict = {}

    result = []

    for filePath in files:
        fileExtension = filePath.split("/")

        fileExtension = ""
        l = len(filePath) - 1
        while filePath[l] != "/":
            fileExtension = filePath[l] + fileExtension
            l -= 1

        if fileExtension in files_dict:
            files_dict[fileExtension].append(filePath)
        else:
            files_dict[fileExtension] = [filePath]

        # if fileExtension[-1] in files_dict:
        #     files_dict[fileExtension[-1]].append(filePath)
        # else:
        #     files_dict[fileExtension[-1]] = [filePath]

    for query in queries:
        if query in files_dict:
            result += files_dict[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
