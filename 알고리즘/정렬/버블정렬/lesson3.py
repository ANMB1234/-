#알고리즘 개선 방법1 정렬이 완료된 후의 불필요한 계산을 줄인다.
#정렬이 완료되었다는 뜻은 안에있는 교환 횟수가 한번도 일어나지않았다는 말과 같다.
#따라서 한 패스안에서 scnt가 0이 라면 그이후의 작업들은 불필요하다.(개선방법)
from typing import MutableSequence

def bubble_sort_verbose(a:MutableSequence)->None:
    #버블 정렬(정렬과정 출력)
    ccnt=0#비교 횟수
    pcnt=0#패스 횟수
    total_s=0#총 교환횟수
    n=len(a)
    for i in range(n-1):  
        scnt=0#한 패스안의 교환횟수 이게 0이라면 불필요한 정렬은 필요없다.
        pcnt+=1
        print(f'패스 {pcnt}')
        for j in range(n-1,i,-1):
            ccnt+=1
            if a[j-1]>a[j]:
                total_s+=1
                scnt+=1
                a[j-1],a[j]=a[j],a[j-1]
        if scnt==0:
            break
        for m in range(0,n-1):
            print(f'{a[m]:2}',end='')
        print(f'{a[n-1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {total_s}번 했습니다.')
    
x=int(input("정수를 입력해주세요 :"))
n=[None]*x

for i in range(x):
    n[i]=int(input(f'x[{i}]: '))

bubble_sort_verbose(n)
