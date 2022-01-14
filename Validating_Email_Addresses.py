def fun(s):
    # return True if s is a valid email, else return False
    if s.count('@') == 1 and s.count('.')==1:
        first,second = s.split("@")
        second, third = second.split(".")
        if not (len(second)>0 and len(first)>0 and len(third)>0):
            return False
        for i in first:
            if not (i.isalpha() or str(i).isnumeric() or i == '_' or i == '-'): 
                return False
        for i in second:
            if not (i.isalpha() or str(i).isnumeric()): 
                return False
        if not len(third) <= 3 or not third.isalpha:
            return False              
    else:
        return False
    return True 

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
