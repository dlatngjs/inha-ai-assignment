# Simple Data CLI Apps

인터넷 웹페이지 스크래핑 및 CSV 추이 그래프 생성을 위한 Python CLI 예제 프로젝트입니다.

---

# 기능

## 1. 웹 스크래핑 기능

- 페이지 제목(title) 출력
- h1 / h2 / h3 헤더 수집
- 링크(a href) 수집 및 출력

## 2. CSV 추이 그래프 기능

- CSV(date,value) 데이터 읽기
- matplotlib 기반 라인 그래프 생성
- PNG 파일 저장

---

# 실행 방법

## 1) 웹 스크래핑 실행

```bash
python scraper_app.py https://example.com
```

링크 출력 개수 제한:

```bash
python scraper_app.py https://example.com --max-links 5
```

---

## 2) CSV 추이 그래프 실행

```bash
python plot_trend.py sample_trend_data.csv --output trend_plot.png --title "Sample Trend"
```

실행 후:
- trend_plot.png 파일 생성
- CSV 데이터 기반 추이 그래프 출력

---

# 생성 파일

- scraper_app.py : 웹 스크래핑 CLI 코드
- plot_trend.py : CSV 추이 그래프 생성 코드
- sample_trend_data.csv : 샘플 CSV 데이터
- trend_plot.png : 생성된 그래프 이미지
- README.md : 프로젝트 설명 문서

---

# 사용 기술

- Python
- urllib
- html.parser
- matplotlib

---

# GitHub 주소

https://github.com/dlatngjs/scraping-app
