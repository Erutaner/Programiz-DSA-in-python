"""
Author: Erutaner
Date: 2022.11.06
Knuth–Morris–Pratt Algorithm
"""

def next(p):
    nxt = []
    now = 0
    nxt.append(0)   #nxt[0]按定义，是零 nxt[x]代表p[0]到p[x]这x+1个元素前面等于后面的最大子串长度
    x = 1           #next数组元素个数和len(p)是一致的
    while x < len(p): #这个地方不能用for循环，两者区别在于while不会自动自增
        if p[x] == p[now]:
            x += 1
            now += 1
            nxt.append(now)
        elif now:
            now = nxt[now-1]
        else:
            nxt.append(now)
            x += 1
    return nxt

def kmp(s,p):
    nxt = next(p)
    tar = 0
    pos = 0
    matching = []
    while tar < len(s):
        if s[tar] == p[pos]:
            tar += 1
            pos += 1
        elif pos:
            pos = nxt[pos-1]
        else:
            tar += 1
        if pos == len(p):
            matching.append(tar-pos)
            pos = nxt[pos-1]
    return matching



def main():
    while True:
        choice = input("Please make a choice, c for continue, e for exit:")
        if choice == 'e':
            print("Exit successfully")
            break
        else:
            s = input("Please input the longer string:")
            p = input("Please input the pattern string:")
            lst = kmp(s,p)
            if lst:
                for i in lst:
                    print("s[{} : {}] = ".format(i,i+len(p)),s[i : i + len(p)])
            else:
                print("Pattern string not found or it's longer then the main string.")

main()