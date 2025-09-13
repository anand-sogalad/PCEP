"""
lab1:
Scenario
There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).
Ready for this challenge?
"""


def list_modification():
    _list = [1, 2, 3, 4, 5]
    number = int(input("Enter a number to replace the middle element: "))
    # step1: replace middle element
    _list[2] = number

    # step2: remove last element
    _list.pop()

    # step3: print length of list
    print(len(_list))


"""
lab2:
Scenario
The Beatles were one of the most popular music group of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?)
"""


def beatles_list():
    beatels = list()
    beatels.append("John Lennon")
    beatels.append("paul McCartney")
    beatels.append("George Harrison")
    for word in "Stu Sutcliffe", "Pete Best":
        beatels.append(word)
    del beatels[3:]
    beatels.insert(0, "Ringo Starr")

    print(beatels)


"""
lab3:
scenario:
Implement a bubble sort
"""


def bubble_sort(_list):
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(_list) - 1):
            if _list[index] > _list[index + 1]:
                _list[index], _list[index + 1] = _list[index + 1], _list[index]
                swapped = True
    return _list


"""
lab4:
remove duplication in a list
"""


def remove_duplication(_list):
    new_list = list()
    for item in _list:
        if item not in new_list:
            new_list.append(item)
    return new_list


# alternative with built in data structures
def remove_duplication_set(_list):
    return list(set(_list))


"""
lab5:
scenario:
create two dimentionnal array using nested loop and loop comprehension
"""


def two_dimensional_array(l, w):
    _list = list()
    for i in range(l):
        row = []
        for j in range(w):
            row.append(j)
        _list.append(row)
    return _list


def two_dimensional_array_comprehension(l, w):
    return [[i for i in range(w)] for j in range(l)]


def main():
    list_modification()
    beatles_list()
    print(bubble_sort([10, 8, 6, 11, 5, 1, 2]))
    print(remove_duplication([10, 12, 15, 1, 2, 2, 10, 1, 2, 5, 6, 7, 5, 6, 10, 11, 2, 3, 4, 5]))
    print(remove_duplication_set([10, 12, 15, 1, 2, 2, 10, 1, 2, 5, 6, 7, 5, 6, 10, 11, 2, 3, 4, 5]))
    print(two_dimensional_array(5, 5))
    print(two_dimensional_array_comprehension(5, 5))


if __name__ == "__main__":
    main()
