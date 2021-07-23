# 규칙

---

- 브랜치는 제품 백로그 단위로 생성한다
- 백로그는 pull request를 통해 생성한다.
- commit 할때 Commit Message Rule 을 지켜준다.

---

## Commit Message Rule

```
- feat : 새로운 기능 추가
- update : 버전 등 업데이트
- fix : 수정
- bug : 버그 수정
- docs : 문서
- style : 코드 스타일 혹은 포맷 등에 관한 커밋
- refactor : 코드 리펙토링
- test : 테스트 코드 수정
```

1. 첫글자는 대문자
2. 커밋메시지 예시
  ex) [Feat] 생리대 지도

---

## Pull Request Rule

- 브랜치의 이름은 feature/ 기능 으로 설정한다.

    ex) feature/login

- pull request의 경우에는 스프린트 백로그를 기준으로 생성하고 제목은 커밋 제목


## 브랜치 전략
```
- master : 라이브 서버에 제품으로 출시되는 브랜치.
- develop : 다음 출시 버전을 대비하여 개발하는 브랜치.
- feature : 기능 개발 브랜치. develop 브랜치에 들어간다.
- release : 다음 버전 출시를 준비하는 브랜치. develop 브랜치를 release 브랜치로 옮긴 후 QA, 테스트를 진행하고 master 브랜치로 합친다.
- hotfix : master 브랜치에서 발생한 버그를 수정하는 브랜치.
```











