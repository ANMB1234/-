#알고리즘 개선 방법2 각 패스안에서 어느 특정 원소이후에 교환하지않는다면 그원소보다 앞쪽에 있는 원소는 정렬을 마친거다.
#따라서 그 이후로 나오는 비교 연산은 불필요한 연산이기때문에 줄인다면 알고리즘이 개선된다.

from typing import MutableSequence

def bubble_sort_verbose(a:MutableSequence)->None:
    n=len(a)
    passing=0
    k=0
    ccnt=0#비교횟수
    scnt=0#교환횟수
    while k<n-1:
        last=n-1
        passing+=1
        print(f'pass : {passing}')
        for j in range(n-1,k,-1):
            ccnt+=1
            for m in range(0,n-1):
                print(f'{a[m]:2}'+(' ' if m!=j-1 else
                                   '+' if a[j-1]>a[j]else '-'),
                      end='')
            print(f'{a[n-1]:2}')
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                scnt+=1
                last=j
        k=last
        for m in range(0,n-1):
            print(f'{a[m]:2}',end='')
        print(f'{a[n-1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
    
x=int(input("정수를 입력해주세요 :"))
n=[None]*x

for i in range(x):
    n[i]=int(input(f'x[{i}]: '))

bubble_sort_verbose(n)
