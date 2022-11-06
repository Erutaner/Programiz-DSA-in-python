"""
Author: Erutaner
Date: 2022.11.06
"""

def brute_force(s,p):  #主串为s, 模式串为p, 即s是那个长的
    if len(s) < len(p):
        return False
    else:
        lst = []
        for i in range(0,len(s)-len(p)+1):
            if s[i : i + len(p)] == p:
                lst.append(i)
        return lst

def main():
    while True:
        choice = input("Please make a choice, c for continue, e for exit:")
        if choice == 'q':
            print("Exit successfully")
            break
        else:
            s = input("Please input the longer string:")
            p = input("Please input the pattern string:")
            lst = brute_force(s,p)
            if lst:
                for i in lst:
                    print("s[{} : {}] = ".format(i,i+len(p)),s[i : i + len(p)])
            else:
                print("Pattern string not found or it's longer then the main string.")
main()