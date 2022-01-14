# Problem's Link:  https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N): 
        line = input().split()
        
        if line[0] == "insert": 
            my_list.insert(int(line[1]),int(line[2]))
        elif line[0] == "print": 
            print(my_list)
        elif line[0] == "remove": 
            my_list.remove(int(line[1]))
        elif line[0] == "append": 
            my_list.append(int(line[1])) 
        elif line[0] == "sort": 
            my_list.sort()
        elif line[0] == "pop": 
            my_list.pop()
        elif line[0] == "reverse": 
            my_list.reverse()