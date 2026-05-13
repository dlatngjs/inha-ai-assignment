# Simple Web Scraper CLI

인터넷 웹페이지에서 기본 정보를 스크래핑해 출력하는 Python CLI 앱입니다.

## 기능

- 페이지 제목(`<title>`) 출력
- 헤더 태그(`h1`, `h2`, `h3`) 출력
- 링크(`<a href="...">`) 수집 및 출력

## 실행 방법

```bash
python scraper_app.py https://example.com
```

링크 출력 개수를 제한하려면:

```bash
python scraper_app.py https://example.com --max-links 5
```

## 요구 사항

- Python 3.x
- 외부 라이브러리 불필요 (표준 라이브러리만 사용)

## 파일 구성

- `scraper_app.py`: 스크래핑 CLI 메인 코드
- `README.md`: 사용법 문서
