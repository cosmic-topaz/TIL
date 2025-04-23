from typing import Optional

## Optional[str]을 str 대신 쓰게 되면, 
## 특정 값이 실제로는 None이 될 수도 있는데 
## 항상 str이라고 가정하는 상황에서 에디터가 에러를 찾게 도와줄 수 있습니다.

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


say_hi()
say_hi("john")
