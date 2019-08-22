def combinations(a,b):
    word_1 = list(a)
    word_2 = list(b)
    combo = []
    longest_word = 0

    if  len(word_1)>len(word_2):
        longest_word = len(word_1)
    else:
        longest_word = len(word_2)

    for i in range(1, longest_word):
        combi = "".join(word_1[:i]+word_2[i:])
        combo.append(combi)

    for i in range(1, longest_word):
        combi = "".join(word_2[:i]+word_1[i:])
        combo.append(combi)

    print(*combo, sep='\n')

name_1 = input("Enter name #1:")
name_2 = input("Enter name #2:")


combinations(name_1,name_2)