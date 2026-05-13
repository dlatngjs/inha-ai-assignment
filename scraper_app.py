import argparse
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import Request, urlopen


class SimpleScraperParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.page_title = ""
        self.headings = []
        self.links = []

        self._inside_title = False
        self._inside_heading = None

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "title":
            self._inside_title = True

        if tag in {"h1", "h2", "h3"}:
            self._inside_heading = tag

        if tag == "a":
            href = attrs_dict.get("href")
            if href:
                absolute = urljoin(self.base_url, href)
                self.links.append(absolute)

    def handle_endtag(self, tag):
        if tag == "title":
            self._inside_title = False

        if tag in {"h1", "h2", "h3"}:
            self._inside_heading = None

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return

        if self._inside_title:
            self.page_title += text

        if self._inside_heading:
            self.headings.append((self._inside_heading, text))


def fetch_html(url: str, timeout: int = 10) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SimpleScraper/1.0)"})
    with urlopen(req, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def print_report(url: str, html: str, max_links: int):
    parser = SimpleScraperParser(url)
    parser.feed(html)

    print("=" * 60)
    print(f"URL: {url}")
    print(f"TITLE: {parser.page_title or '(없음)'}")
    print("=" * 60)

    print("\n[HEADINGS]")
    if parser.headings:
        for tag, text in parser.headings:
            print(f"- {tag.upper()}: {text}")
    else:
        print("- 수집된 헤더(h1/h2/h3)가 없습니다.")

    print("\n[LINKS]")
    unique_links = list(dict.fromkeys(parser.links))
    if unique_links:
        for link in unique_links[:max_links]:
            print(f"- {link}")
        if len(unique_links) > max_links:
            print(f"... (총 {len(unique_links)}개 중 {max_links}개만 표시)")
    else:
        print("- 수집된 링크가 없습니다.")


def main():
    parser = argparse.ArgumentParser(
        description="웹 페이지를 스크래핑하여 제목/헤더/링크를 출력하는 간단한 CLI 앱"
    )
    parser.add_argument("url", help="스크래핑할 URL (예: https://example.com)")
    parser.add_argument("--max-links", type=int, default=10, help="출력할 최대 링크 개수 (기본값: 10)")
    args = parser.parse_args()

    try:
        html = fetch_html(args.url)
        print_report(args.url, html, args.max_links)
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
