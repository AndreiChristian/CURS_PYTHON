students = [1, 2, 3, 4, 5, 6, 7, 8,]


# functie cu O(1)
def first(students):
    print("Aceasta este o functie cu 0(1)")
    print(students)


# logarithmic -> O(log(n))
def binary_search(lista, target):

    low = 0
    high = len(lista) - 1

    while low <= high:
        mid = (low + high)//2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def second(students):
    # pentru 8 studenti -> 8 iterari
    for student in students:
        print(student)
        print("Buna ziua")
        print('La reveredere')
        print("Complexitate O(n)")


def third(students):
    # complexitate 0(n2)
    for s1 in students:
        for s2 in students:
            print(s1, s2)


input = [2, 7, 9, 10, 14]
target = 9


def suma_target():

    vector = [2, 7, 11, 15]
    sol = []
    target = 9
    dict = {}
    for index in range(len(vector)):
        dict[index] = vector[index]
    for cheie in dict:
        if target-dict[cheie] in vector:
            sol.append(cheie)
    print(sol)


suma_target()


def suma_target_2(nums, target):
    dictionar = {}
    for i in range(len(nums)):
        numar = nums[i]
        valoarea_cautata = target - numar
        if valoarea_cautata in dictionar:
            return [dictionar[numar], i]  # TODO
        dictionar[numar] = i
    return None
