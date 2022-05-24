# final-pjt-front

추후 내용을 삭제하거나 줄인다 하더라도 나중을 위해 대부분 기록함.



## 목을 차

- **0521** vue 초기 생성









---





## 1. 0521 vue 초기 생성



### 1. 브랜치 생성

 Django를 활용한 back-end 작업중이므로, 영향을 미치지 않기 위해서 그리고 잘못된 커밋을 방지하기 위해 branch를 하여 추후 pull request를 이용하여 기존 commit과 비교하고, merge 여부를 결정하기로 한다.

- git branch vue01

- git checkout vue01



### 2. Vue 초기설정

- vue create final-pjt-front
  - Default Vue 2 Babel, eslint
- cd final-pjt-front/
- vue add router
  - Yes (router 깔기 전에 커밋할 거 있으면 먼저 해라)
  - Yes (history mode)
- vue add vuex
  - Yes (vuex 깔기 전에 커밋할 거 있으면 먼저 해라)
- npm i (혹은 npm install)
- npm run serve (실행)



### 3. 컴포넌트 구조 정리

- axios 요청 모듈화
  - src/api/drf.js
- store 모듈화 (movies.js XXX)
- router view 정리
- name, components 기입



### 해야할 것

- 컴포넌트 구조 조율 및 수정
- store/modules/movies.js 기입
- css 기본 구조(navbar 위치, 크기, 색상, 테마 등) 그리기



---

