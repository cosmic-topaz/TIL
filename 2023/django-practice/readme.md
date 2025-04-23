readme.md

# Django ORM

**실습 목표**
- Model 정보가 주어졌을 때 Django Model을 설계할 수 있다.
- shell_plus를 활용하여 shell 환경에서 CRUD 코드를 작성할 수 있다.

**실습 명세서**
Environment
- django 버전 : 3.2.18
- Database : SQLite
- 필수 패키지
    - ipython
    - django_extensions

## 할일 App & Model

**아래 정보를 기반으로 앱 생성 및 모델 작성**
- 앱 이름 : todos
- 모델 이름 : Todo
- 모델 필드 및 속성
필드 이름	역할	django 필드	속성
content	할 일 내용	Char	max_length=80
completed	완료 여부	Boolean	default=False
priority	우선순위	Integer	default=3
created_at	생성 날짜	Date	auto_now_add=True
deadline	마감 기한	Date	null=True

## 신문 Model & ORM

**아래 모델 정보를 기반으로 newspapers 앱 model 코드 작성**
- 앱 이름 : newspapers
- 모델 이름 : Newspaper
- 모델 필드 및 속성
필드 이름	역할	django 필드	속성
title	신문 제목	Char	max_length=80
content	신문 내용	Text	
journalist	작성자	Char	max_length=80
created_at	작성일	DateTime	auto_now_add=True

# Todo 서비스 개발 1

**실습 목표**
- Model 정보가 주어졌을 때 Django Model을 작성할 수 있다.
- CR 기능이 탑재된 웹 서비스를 개발할 수 있다.  

**할 일 전체 조회 Index** **할 일 단일 조회 Detail** **할 일 생성 New** **할 일 생성 Create**
Url GET todos/ GET todos/<int:todo_pk>/ GET todos/new/ GET todos/create/
View 데이터 전체 조회    pk가 todo_pk인 데이터 조회      할 일 생성 템플릿 렌더링(응답)      HTML Form을 통해 사용자에게 입력받은 데이터로 할 일 데이터 생성
조회한 데이터를 전달한 전체 조회 템플릿 렌더링  조회한 데이터를 전달한 단일 조회 템플릿 렌더링      할 일 생성 템플릿 렌더링(응답)
Template 조회한 데이터 출력      조회한 데이터 출력      할 일 작성 폼(HTML Form) 설계       (필수) 추가 디자인 작업
할 일 생성 New 페이지 이동 버튼                 입력 input 요소 [제목(text), 내용(textarea), 우선 순위(number), 마감기한(date)]
각 할 일을 클릭하면 해당 할 일 단일 조회 페이지 이동

**코드 리뷰 주제**
생성Create과 조회Read에 대하여
데이터 생성에서 HTML form과 input의 역할과 기능 구현 형태
Django를 활용한 웹 서비스 기능 구현 흐름
