from typing import MutableSequence

def bubble_sort_verbose(a:MutableSequence)->None:
    #버블 정렬(정렬과정 출력)
    ccnt=0#비교 횟수
    scnt=0#교환 횟수
    pcnt=0#패스 횟수
    n=len(a)
    for i in range(n-1):
        pcnt+=1
        print(f'패스 {pcnt}')
        for j in range(n-1,i,-1):
            for m in range(0,n-1):
                print(f'{a[m]:2}'+(' ' if m!=j-1 else
                                   '+' if a[j-1]>a[j]else '-'),
                      end='')
            print(f'{a[n-1]:2}')
            ccnt+=1
            if a[j-1]>a[j]:
                scnt+=1
                a[j-1],a[j]=a[j],a[j-1]
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
