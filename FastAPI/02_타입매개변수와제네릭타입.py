## 타입 매개변수를 활용한 Generic(제네릭) 타입

## dict, list, set, tuple 
## 데이터구조의 내부타입에 대한 힌트 제공

from typing import List, Set, Tuple, Dict

def process_items(items: List[str]):
    for item in items:
        print(f"Processing item: {item}")

process_items(["apple", "banana", "cherry"])

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

print(process_items(["apple", "banana", "cherry"], {"apple", "banana"}))

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


process_items({"apple": 1.0, "banana": 2.0, "cherry": 3.0})