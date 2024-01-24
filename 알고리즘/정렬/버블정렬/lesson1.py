# 두 원의 대소 관계를 비교하여 필요에 따라 교환을 반복하는 알고리즘 ==단순교환 정렬

## 비교|교환 하는 작업을 pass 라고한다.


### 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a:MutableSequence) -> None:
    """ 
    버블 정렬
    """
    n=len(a)
    for j in range(n-1):
        for i in range(j-1):
            if a[n-i]<a[n-i-1]:
                a[n-i],a[n-i-1]=a[n-i-1],a[n-i]
            
            
            
            
a=int(input("숫자를 입력해주세요: "))
list1=[None]*a

for i in range(a):
    list1[i]=int(input(f"list1[{i}]= "))


bubble_sort(list1)

print('정렬후 리스팅')
for i in range(a):
    print(f"list1[{i}]= {list1[i]}")