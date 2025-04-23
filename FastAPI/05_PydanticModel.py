## Pydantic:  데이터 검증(Validation)을 위한 파이썬 라이브러리


# "모양(shape)": 속성들을 포함한 클래스 형태 선언
# 각 속성은 타입을 가지고 있습니다.
# 이 클래스를 활용하여서 값을 가지고 있는 인스턴스를 만들게 되면, 
# 필요한 경우에는 적당한 타입으로 변환까지 시키기도 하여 데이터가 포함된 객체를 반환합니다.
# 그리고 결과 객체에 대해서는 에디터의 도움을 받을 수 있게 됩니다.

from datetime import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123