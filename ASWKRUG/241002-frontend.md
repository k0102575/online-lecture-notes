# 주제
- Next.js 우아하게 사용하기

## 내용 
- Next.js AppRouter에서 활용할 수 있는 여러 기술(ex: Pararell Route, Route Group, middleware, Image 등)을 실무에서 활용할 수 있는 방법, 그리고 App router에서 데이터로 생각하고 개발하는 방법에 대해 소개합니다

## 일정
- 2024.10.02

## 메모

- Route Group
- Server Action => Server Function 명칭 이 바뀌고 장점이 뚜렷하다. (추가 문서 확인 필요 할듯)
  - ex) 클라이언트에서 실행 불가능한 라이브러리 실행 등
- Nextjs Image
- Middleware
  - 예시 1 다국적 지원 프로젝트에서 국적마다 특정 이벤트를 실행하는 케이스 (발표 이미지 참고 필요)
  - 예시 2 미들웨어에서 Auth Server 를 요청하면서 보안성 강화 케이스
- Build
  - 아무것도 설정하지 않은 빌드를 일반 빌드라 명칭하고 그렇게 했을떄 단점이있다. (서버를 구성하기 위한 파일 생성이 많음) (문서 확인 필요)
    - Standalone 서버에서 꼭 필수값인 값들만 따로 생성하면서 서버 크기가 감소, 도커 이미지 생성 감소 등 장점이 있다.
    - Standalone 에 들어가는 필수 조건, 서버 실행 & 미들웨어 & Server Action 등 (발표 이미지 일반 빌드와 Standalone 빌드 비교 참고필요)