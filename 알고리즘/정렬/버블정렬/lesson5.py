#셰이커 정렬 칵테일 정렬 칵테일 셰이커 정렬 양방향 버블 정렬
#lesson4.py 와같은 알고리즘 개선 사항을 한쪽만이아닌 양쪽을 넣어 개선
from typing import MutableSequence


def shaker_sort(n:MutableSequence)->None:
    left=0
    right=len(n)-1
    last=right
    passing=0#패스횟수
    scnt=0 #교환횟수
    ccnt=0 #비교횟수
    while left<right:
        passing+=1
        print(f'pass : {passing}')
        for j in range(right,left,-1):
            ccnt+=1
            if n[j-1]>n[j]:
                n[j-1],n[j]=n[j],n[j-1]
                scnt+=1
                last = j
            print(n)
            print()
        left=last# 좌방향 알고리즘 개선1
        for j in range(left,right):
            ccnt+=1
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
                last=j
                scnt+=1
            print(n)
            print()
        right = last
        print()
    print(f'total ccnt : {ccnt}')
    print(f'total scnt : {scnt}')
x=int(input("정수를 입력해주세요 :"))
n=[None]*x

for i in range(x):
    n[i]=int(input(f'x[{i}]: '))

shaker_sort(n)

print(n)