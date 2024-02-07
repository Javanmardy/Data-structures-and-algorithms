def min_edit(word1, word2):
    len_word1, len_word2 = len(word1), len(word2)
    costs = {"delete": 1, "insert": 1.5, "replace": 2.5}

    matrix = [[0 for i in range(len_word2 + 1)] for i in range(len_word1 + 1)]

    for i in range(len_word1 + 1):
        matrix[i][0] = i * costs["delete"]
    for j in range(len_word2 + 1):
        matrix[0][j] = j * costs["insert"]

    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            if word1[i - 1] == word2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + costs["delete"],
                    matrix[i][j - 1] + costs["insert"],
                    matrix[i - 1][j - 1] + costs["replace"],
                )

    i, j = len_word1, len_word2
    transformations = []

    while i > 0 and j > 0:
        current_cost = matrix[i][j]
        if word1[i - 1] == word2[j - 1]:
            transformations.append(f"'{word1[i - 1]}' unchanged")
            i, j = i - 1, j - 1
        elif current_cost == matrix[i - 1][j - 1] + costs["replace"]:
            transformations.append(f"replace '{word1[i - 1]}' with '{word2[j - 1]}'")
            i, j = i - 1, j - 1
        elif current_cost == matrix[i - 1][j] + costs["delete"]:
            transformations.append(f"delete '{word1[i - 1]}'")
            i -= 1
        elif current_cost == matrix[i][j - 1] + costs["insert"]:
            transformations.append(f"insert '{word2[j - 1]}'")
            j -= 1

    while i > 0:
        transformations.append(f"delete '{word1[i - 1]}'")
        i -= 1
    while j > 0:
        transformations.append(f"insert '{word2[j - 1]}'")
        j -= 1

    return transformations[::-1], matrix[len_word1][len_word2]


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
transformations, total_cost = min_edit(word1, word2)

print("Transformations:")
for transformation in transformations:
    print(transformation)
print(f"Total cost: {total_cost}")
