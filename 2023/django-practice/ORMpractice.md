## shell_plus를 활용하여 shell 환경에서 ORM 코드 작성
**ORM 실습**

"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
```bash
In [2]: from datetime import datetime
In [3]: now = datetime.now()
In [4]: Todo.objects.create(content='실습 제출', priority=5, completed=False, deadline=now.date())
Out[4]: <Todo: Todo object (1)>
```
"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
```bash
In [1]: from datetime import datetime
In [2]: now = datetime.now()
In [3]: Todo.objects.create(content='데일리 설문(오후) 제출', deadline=now.date())
Out[3]: <Todo: Todo object (2)>
```
"""
3. 임의의 할 일 5개 생성
"""
```bash
In [4]: random_todo_1 = Todo()
In [5]: random_todo_2 = Todo()
In [6]: random_todo_3 = Todo()
In [7]: random_todo_4 = Todo()
In [8]: random_todo_5 = Todo()
In [9]: random_todo_1.save()
In [10]: random_todo_2.save()
In [11]: random_todo_3.save()
In [12]: random_todo_4.save()
In [13]: random_todo_5.save()
```
"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
```bash
In [19]: today_todos = Todo.objects.all().order_by()
In [20]: print(today_todos)
<QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>
```
"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
```bash
In [50]: import random

In [51]: for todo in today_todos: todo.priority=random.randint(1, 5)

In [52]: today_todos.order_by('priority').reverse()
Out[52]: <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>
In [53]: for todo in today_todos: print(f'id {todo.id}: priority {todo.priority},')
id 2: priority 5,
id 3: priority 3,
id 4: priority 3,
id 5: priority 1,
id 6: priority 1,
id 7: priority 3,
id 1: priority 2,
```
"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
```bash
In [55]: todo_1 = Todo.objects.get(pk = 1)
In [56]: todo_1.pk
Out[56]: 1
In [57]: todo_1.content
Out[57]: '실습 제출'
In [58]: todo_1.priority
Out[58]: 5
In [59]: todo_1.deadline
Out[59]: datetime.date(2023, 4, 4)
In [61]: todo_1.created_at
Out[61]: datetime.date(2023, 4, 4)
```