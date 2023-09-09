myDict = {}
while (True):
    iname2 = input()
    if not iname2:
        break
    isal2 = input()
    myDict[iname2] = int(isal2)
for key in myDict.keys():
    if key.lower() == 'brad':
        myDict[key] = 8500
print(myDict.get('brad'))
# swapping in 2ways
# 1
num1 = input()
num2 = input()
(num1, num2) = (num2, num1)
print(num1, num2)
# 2
temp = num1
num1 = num2
num2 = temp
print(num1, num2)
# reversing a list
myList = [1, 2, 3, 4, 6, 7, 8]
myList.reverse()
print(myList)
myList2 = [6, 7, 8, 7, 6, 4, 3, 3]
reversedList = myList2[::-1]
print(reversedList)
mylist3 = [7, 7, 9]
reversed_list = list(reversed(mylist3))
print(reversed_list)
###################
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = [x + y for x, y in zip(list1, list2)]
print(result)
#########################
list8 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list9 = ["h", "i", "j"]
list8[2][1][2].extend(list9)
print(list8)
tuple2 = (1, 50, 80, 90, 50, 50)
cnt = tuple2.count(50)
print(cnt)
