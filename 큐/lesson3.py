from enum import Enum
from lesson2 import FixedQueue

Menu=Enum('Menu',['인큐','디큐','피크','검색','덤프','exit'])

def select_menu()->Menu:
    
    s=[f'({m.value}){m.name}' for m in Menu]
    
    while True:
        print(*s,sep='  ',end='')
        n=int(input(': '))
        if 1 <=n<= len(Menu):
            return Menu(n)
        
        
q=FixedQueue(64)

while True:
    print(f'현재 데이터의 갯수 : {q.no}/{q.capacity}')
    menu= select_menu()
    
    if menu == Menu.인큐:
        pass
    elif menu == Menu.디큐:
        pass
    elif menu == Menu.피크:
        pass
    elif menu == Menu.검색:
        pass
    elif menu == Menu.덤프:
        pass
    else:
        break