""" tries : contacts
author : Woongwon Lee
problem : https://www.hackerrank.com/challenges/ctci-contacts/problem
output : For each find partial operation, print the number of contact names
starting with  on a new line.
"""

def all_word(contact):
    all_word = []
    for idx in range(1, len(contact) + 1):
        all_word.append(contact[0:idx])
    return all_word


contacts = {}


def add(contact):
    for word in all_word(contact):
        contacts[word] = contacts.get(word, 0) + 1


def find(name):
    return contacts.get(name, 0)


n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        print(find(contact))
