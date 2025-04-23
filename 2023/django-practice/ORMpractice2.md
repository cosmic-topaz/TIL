ORM 실습
"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
```bash
In [2]: Newspaper.objects.get(pk = 1).journalist
Out[2]: 'Laney Mccullough'
```
"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""
```bash
In [10]: Newspaper.objects.filter(journalist = 'Laney Mccullough').count()
Out[10]: 858
```
"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""
```bash
In [14]: Newspaper.objects.order_by('pk').reverse()
Out[14]: <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, <Newspaper: Newspaper object (9998)>, <Newspaper: Newspaper object (9997)>, <Newspaper: Newspaper object (9996)>, <Newspaper: Newspaper object (9995)>, <Newspaper: Newspaper object (9994)>, <Newspaper: Newspaper object (9993)>, <Newspaper: Newspaper object (9992)>, <Newspaper: Newspaper object (9991)>, <Newspaper: Newspaper object (9990)>, <Newspaper: Newspaper object (9989)>, <Newspaper: Newspaper object (9988)>, <Newspaper: Newspaper object (9987)>, <Newspaper: Newspaper object (9986)>, <Newspaper: Newspaper object (9985)>, <Newspaper: Newspaper object (9984)>, <Newspaper: Newspaper object (9983)>, <Newspaper: Newspaper object (9982)>, <Newspaper: Newspaper object (9981)>, '...(remaining elements truncated)...']>
```

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""
```bash
In [15]: Newspaper.objects.order_by('created_at').reverse()
Out[15]: <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, <Newspaper: Newspaper object (5500)>, <Newspaper: Newspaper object (4918)>, <Newspaper: Newspaper object (5753)>, <Newspaper: Newspaper object (3706)>, <Newspaper: Newspaper object (4012)>, <Newspaper: Newspaper object (452)>, <Newspaper: Newspaper object (6865)>, <Newspaper: Newspaper object (3265)>, <Newspaper: Newspaper object (2643)>, <Newspaper: Newspaper object (7022)>, <Newspaper: Newspaper object (3700)>, <Newspaper: Newspaper object (3236)>, <Newspaper: Newspaper object (9607)>, <Newspaper: Newspaper object (4461)>, <Newspaper: Newspaper object (419)>, <
```
"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""
```bash
In [17]: Newspaper.objects.filter(journalist__contains='Britney').count()
Out[17]: 799
```
"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""
```bash
In [18]: Newspaper.objects.filter(journalist__in = ['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()
Out[18]: 2469
```
"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""
```bash
In [20]: from datetime import datetime
In [24]: Newspaper.objects.filter(created_at__gt=datetime(2000, 1, 1)).count()
Out[24]: 4355
```
"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""
```bash
In [42]: last_item = Newspaper.objects.order_by('pk').reverse()[0]
In [43]: attr_list = ['title', 'content', 'journalist']
In [45]: for attr in attr_list:
    ...:     value = eval('.'.join(['last_item', attr]))
    ...:     print(f'{attr} : {value}')
    ...: 
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
```