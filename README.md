# edu-2026h2-playwright-mcp

2026 하반기 4회차 **웹 크롤링과 Playwright MCP** (EDU-2026-H2-04, 2026-10-01) 실습 저장소입니다.

목표: `books.toscrape.com` Travel 카테고리 도서의 제목·가격·재고 수량을 JSON으로 모으기. 같은 목표를 세 가지 방식으로 수행하고 비교합니다.

```bash
pip install -r requirements.txt
playwright install chromium
```

| 파일 | 방식 |
| --- | --- |
| `a_bs4.py` | Requests + BeautifulSoup |
| `b_playwright.py` | Playwright 코드 |
| `c_mcp_prompt.md` | Playwright MCP에 줄 요청문 (결과는 `results/c_mcp.json`) |
| `mcp_config.example.json` | AI 도구에 Playwright MCP 연결 |
| `compare.py` | 세 결과를 정답(`results/answer.json`)과 비교 |
| `injection_demo.html` | Prompt Injection 데모 페이지 (로컬에서 열기) |

## 과제

자기 업무와 관련된 공개 페이지 하나를 골라 세 방식 중 두 가지로 같은 정보를 수집하고 비교표를 제출합니다. 기한 10/7(수) 23:59.
