## 파이썬 타입 힌트.

## 편집기에게 변수의 타입을 알려줌.
## 자동완성과 에러 확인이 가능. 
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

## simple type

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e


print(get_items("a", 1, 1.0, True, b"b"))