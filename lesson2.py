# 링 버퍼      크기가 고정된 큐
# 장점 : 디큐할때 배열 안의 우너소를 옮기지않는 큐이다. 모든 처리의 복잡도는O(1)이다.
from typing import Any

class FixedQueue:
    class Empty(Exception):
        # 비어있는 클래스FixedQueue에서 디큐또는 피크할때 내보내는 예외처리
        pass
    class Full(Exception):
        # 채워져있는 클래스FixedQueue에서 인큐할때 내보내는 예외처리
        pass
    def __init__(self,capacity: int)->None:
        # 큐 초기화
        self.no=0 # 데이터의 갯수
        self.front=0 # 프론트 인덱스
        self.rear=0 # 리어 인덱스
        self.capacity=capacity
        self.que=[None]*capacity
    def __len__(self)->int:
        # self.no 데이터의 갯수
        return self.no
    
    def is_empty(self)->bool:
        #큐가 비어있는지 판단
        return self.no<=0
    
    def is_full(self)->bool:
        #큐가 가득차있는지 판단
        return self.no >=self.capacity
    
    def enque(self,value:Any) -> None:
        #데이터 value를 인큐
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear]=value
        self.rear+=1
        self.no+=1
        if self.rear == self.capacity:
            self.rear=0
            
            
    def deque(self)->Any:
        "데이터 디큐"
        #비어 있을시 오류 발생
        if self.is_empty():
            raise FixedQueue.Empty
        x= self.que[self.front]# 디큐 한 값 설정
        self.front+=1 #빠진 인덱스 위 value값 다시 프론트로 재설정
        self.no-=1 # 디큐 시 데이터 갯수 -1
        if self.front==self.capacity:
            self.front=0
        return x
        
        
    
    def peek(self)->Any:
        #큐에 있는 데이터를 피크 (맨 앞 데이터 읽기)
            if self.is_empty():
                #비어 있다면  예외처리를 발생
                raise FixedQueue.Empty
            #아니라면 맨앞에 있는 데이터 읽기
            return self.que[self.front]
    def find(self,value: Any)->Any:
        #큐에서 value를 찾아 인덱스를반환 없으면 -1반환
            for i in range(self.no):
                idx=(i+self.front)%self.capacity
                if self.que[idx]==value:#검색 성공
                    return idx
            return -1                   #검색 실패
        
    def count(self,value: Any)-> Any:
        #큐에 있는 value의 개수를 반환
        c=0
        for i in range(self.no):
            idx=(i+self.front)%self.capacity
            if self.que[idx]==value:#검색 성공
                c+=1                #검색 성공시 카운트
        return c
    
    def __contatins__(self,value:Any)->bool:
        #큐에 value가 있는지 판단
        return self.count(value)
    
    def clear(self)->None:
        """큐 초기화"""
        self.no=self.front=self.rear=0
    def dump(self)->None:
        #모든 데이터를 맨앞부터 맨끝순으로 출력
        if self.is_empty():
            print("큐가 비었습니다.")
        else:
            for i in range(self.no):
                print(self.que[(i+self.front)%self.capacity],end='')
            print()