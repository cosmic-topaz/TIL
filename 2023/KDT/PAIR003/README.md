# pair_django_3

## 개발 명세서

**Environment**
- django 버전 : 3.2.18
- Database : SQLite

**ERD (#primary key, *foregin key)**

1. Review
  - #pk   int
  - *user  int    fk-User
  - title   varchar
  - content   varchar
  - movie   varchar
  
1. Comment
  - #pk  int
  - *review  int    fk-Review
  - *user    int    fk-User
  - content   varchar

1. User
  - #pk   int

**요구사항**
1. 사용자는 회원가입 / 로그인 / 로그아웃을 할 수 있다.
1. 회원가입을 할 때 아래 정보를 필수로 입력받는다.
  - 회원이름
  - 이메일
  - 비밀번호
1. 사용자는 영화에 대한 리뷰를 조회 / 생성 / 수정 / 삭제룰 할 수 있다.
>단, 비로그인 사용자는 조회만 가능하다.
1.리뷰를 작성할 때 아래 정보를 필수로 입력받는다.
  - 리뷰 제목
  - 리뷰 내용
  - 영화 이름
1. 사용자는 영화 리뷰에 댓글을 조회 / 생성 / 삭제를 할 수 있다.
>단, 비로그인 사용자는 조회만 가능하다.
1. 로그인한 사용자는 자신의 사용자 프로필 페이지를 조회할 수 있으며 아래 정보를 확인할 수 있다.
  - 회원이름
  - 이메일
  - 작성한 리뷰 목록