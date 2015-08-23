__author__ = 'jeet'

def 
if __name__ == '__main__':
    list = []
    listLower = []
    listUpper = []
    list.append([-10, -1])
    list.append([-10, -4])
    list.append([0, 2])
    list.append([4, 10])

    list.sort()

    for i in list:
        listLower.append(i[0])
        listUpper.append(i[1])


    print list
    print listLower
    print listUpper