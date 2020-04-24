
def is_fuzzy_match(first, second, match_per):
    similarity = 0
    for i in range(len(first)):
        if i == 0:
            if first[i] == second[i] or first[i] == second[i + 1]:
                similarity += 1
                print(similarity)
        elif i == (len(first) - 1):
            if first[i] == second[i] or first[i] == second[i - 1]:
                similarity += 1
                print(similarity)
        else:
            if first[i] == second[i] or first[i] == second[i - 1] or first[i] == second[i + 1]:
                similarity += 1
                print(similarity)

    similarity_perc = round(float(similarity / len(first)), 2)
    print(similarity_perc)
    if similarity_perc > match_per:
        return True
    return False

def same_leng(short, long):
    i = 0
    while len(short) != len(long):
        if (i % 2) == 0:
            short.append(None)
        else:
            short.insert(len(short), None)
    return short, long

############################################

match = 0.75
total_corr = 0

############################################
with open('common_misspellings.txt') as f:
    lines = [line.rstrip() for line in f]

for i in range(len(lines)):
    if (i % 2) == 0:
        word1 = (list(lines[i]))
        word2 = (list(lines[i+1]))
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        print(word1)
        print(word2)

        word1, word2 = same_leng(word1, word2)

        print(word1)
        print(word2)
        if is_fuzzy_match(word1, word2, match):
            total_corr +=1
            print('Słowa są podobne!')

print(total_corr)
print(total_corr/189)
