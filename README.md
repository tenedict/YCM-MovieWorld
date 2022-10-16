## 프로젝트 소개

- 🗓 프로젝트 기간
  - 2022.10.14
- 💻 사용 기술
  - Python, Django, HTML, CSS, Bootstrap5
- ⭐ 나의 역할
  - Django에서 Userchangeform 과 Usercreationform을 사용해서 회원가입시스템과 회원정보 수정 페이지의 url연결과 view함수 작성 그리고 모델을 만들었습니다.
- 💡 배운 점
  - 저번주의 페어프로젝트와 같은 측면의 전체적인 Django의 개발 흐름을 복습하게 되었습니다.
  - Userchangeform 과 Usercreationform을더 익숙하게 사용할 수 있게 되었습니다.
  - 포린키를 이용하여 테이블간의 연결하는 것을 팀원들을 통해 알게 되었습니다.



## 🚩목적

페어 프로그래밍을 통해 영화 리뷰 커뮤니티 서비스를 개발

- **ModelForm**을 활용한 CRUD 구현
- **Staticfiles** 활용
- **Userchangeform** 과 **Usercreationform** 활용
- 패스워드 변경 구현


# 🧾기능 소개

`signin(accounts)`: 회원가입하는 페이지를 Usercreationform을 활용하여 구현하였습니다.

`login(accounts)`: AuthenticationForm을 활용하여 로그인 페이지를 구현하였습니다.

`update(accounts)`: Userchangeform을 활용하여 회원정보를 수정하는 페이지를 구현하였습니다.

`password(accounts)`: PasswordChangeForm을 활용하여 패스워드 변경을 구현하였습니다.

`logout(accounts)`: 로그아웃을 하는 페이지를 만들었습니다.

`delete(accounts)`: signup에서 만들었던 게정이 삭제됩니다.

`create(reviews)`: 리뷰를 작성하는 ModelForm을 제공하고 ModelForm에서 request를 받아 처리하였습니다.

`index(reviews)`: DB에 저장된 모든 리뷰들을 읽어서 간단한 정보를 사용자에게 보여줍니다.

`detail(reviews)`: 선택한 리뷰의 제목, 내용 등 모든 정보를 보여줍니다.

`update(reviews)`: 이미 작성된 리뷰 인스턴스를 가져와서 ModelForm을 제공하고 request를 처리합니다.

`delete(reviews)`: 선택한 리뷰를 삭제 후 index로 redirect 합니다.

