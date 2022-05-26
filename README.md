# Movie-Recommender



## 프로젝트 명세서

### 📂 프로젝트 개요

- **프로젝트명 ** moBee

- **팀원  **임윤혁, 백한나



### 🤹🏻‍♀️ **기술스택**

<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"><img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">



### 🤔 **프로젝트 컨셉**

영화 추천, 영화 상세 조회

꿀벌이 추천해주는 어쩌구



### 주요 기능

**인트로 페이지 (Intro)**

- 애니메이션

**홈페이지 (Home)**

- 현재 상영 중인 영화
- 추천 알고리즘에 의한 추천 영화
- 영화 정렬(추천, 나이, 장르)
- 상영중인 영화 목록
- 검색 창

**검색 목록 페이지 (Search List)**

- 각 영화의 제목과 줄거리, 포스터 1장
- 영화의 평점

**로그인, 회원가입 페이지**

**마이페이지**

- 마일리지
- 찜한 영화 목록(분류 남기기)
- 본 영화 목록 - 남긴 댓글 (별점)
- 신상 (나이, 성별, 선호 장르 등)

**마일리지 샵**

- 마일리지로 구매할 수 있는 아이템

**영화 상세 페이지 (Movie Detail)**

- TMDB 영화 정보 받아오기
- 트레일러 - 유튜브
- 장르
- 줄거리
- 나이별 만족도
- 댓글 + 별점(생성 수정 시각 정보 포함) ⇒ 누르면 모달로
  - 로그인한 사용자만 작성(본인만 수정, 삭제)
  - 스포 여부
  - 베스트 댓글 순으로 정렬
  - 워스트 댓글 눌러서 볼 수 있게, 최신 댓글이나
  - 한 계정 당 하나의 평점만
- (티빙, 넷플릭스, 등등에 있는지 여부)
- 출연 배우, 감독
- 보고 싶은 영화 등록 버튼(찜)

**커뮤니티 (Community)**

- 영화 관련 게시글(좋아요 기능)
- 좋아요 많은 게시글 상단에 노출, 나머진 최신 순으로 정렬
- 댓글(좋아요)

**출연진/감독 페이지**

- 배우/감독의 영화 목록
- 나이/국가
- 좋아요(시간 남으면)

토마토처럼 디자인 ㄱㅊ(평점마다 디자인 변화)



> - **balsamic**
>
> - member
>
>   | int    | seq         |
>   | ------ | ----------- |
>   | String | id          |
>   | String | pw          |
>   | String | profileName |
>   | String | profileUri  |
>   | String | tier        |
>   | String | stack       |
>   | String | language    |
>   | String | info        |
>
> - **mainboard**
>
>   | int    | seq      |
>   | ------ | -------- |
>   | String | category |
>   | String | writer   |
>   | String | title    |
>   | String | content  |
>   | String | regDate  |
>   | int    | like     |
>
> - **board_comment**
>
>   | int    | seq       |
>   | ------ | --------- |
>   | int    | board_seq |
>   | String | writer    |
>   | String | comment   |
>   | String | regDate   |
>
> [Company goals](https://www.notion.so/ebadd56c660e478b9e821a2562aa81b1)