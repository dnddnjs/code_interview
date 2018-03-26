""" hash table : ransom note
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-ransom-note/problem
output :  Print Yes if he can use the magazine to create an untraceable replica
of his ransom note; otherwise, print No.
"""

def ransom_note(magazine, ransom):
    dic_magazine = {}
    for word in magazine:
        if word in dic_magazine:
            dic_magazine[word] += 1
        else:
            dic_magazine[word] = 1

    for word in ransom:
        if word in dic_magazine and dic_magazine[word] != 0:
            dic_magazine[word] -= 1
        else:
            return False
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")