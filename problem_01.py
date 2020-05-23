import string

origArray = []

inputValue = int(input())


def solution(inputVal: string) -> object:
    if inputVal == 1:
        origArray.append(int(inputVal))
    elif inputVal % 2 == 0:
        origArray.append(int(inputVal))
        solution(inputVal / 2)
    else:
        origArray.append(int(inputVal))
        solution((inputVal * 3) + 1)


solution(inputValue)

print(*origArray)
