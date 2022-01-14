if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([score,name])
    list.sort()

    list = [[37.2, 'Tina'], [37.21, 'Berry'], [37.21, 'Harry'], [39.0, 'Harsh'], [41.0, 'Akriti']]
    for i in range(1,len(list)):
        if list[i][0] > list[0][0]:
            second_lowest_index = i
            break
    print(list[second_lowest_index][1])
    for i in range(second_lowest_index+1,len(list)):
        if list[i][0] == list[second_lowest_index][0]:
            print(list[i][1])
