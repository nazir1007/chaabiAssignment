# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]


list1 = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
list2 = ["Full Metal Alchemist", "Code Geass", "Death Note","Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]
full_list = list1 + list2
common = []
non_common = []

for i in full_list:
    if i in list1 and i in list2:
        if i not in common:
            common.append(i)
    else:
        if i not in non_common:
            non_common.append(i)

print(common, non_common)