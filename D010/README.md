# D010 · Pokémon 타입별 기본 능력치 웹 스크래핑 & EDA

**출처:** [Pokémon Database · Pokémon stats](https://pokemondb.net/pokedex/all)  
**과정:** AIFFEL AI DATA INTELLIGENCE 2기 · 웹 스크래핑 실습  
**주제:** 포켓몬 1차 타입에 따라 HP·공격·방어·특수공격·특수방어·스피드 평균이 어떻게 다른가?

## 실행과 결과의 증거 상태 — 제출 전 확인

- **이 저장소의 사전 생성 CSV, HTML fixture, 보고서 PDF, 시각화는** 1~70번 기본형 포켓몬 능력치를 기반으로 한 **검증용 70행 표본 분석**입니다. 데이터는 공식 웹페이지를 참고해 재구성한 표본으로, **실시간 웹 스크래핑으로 수집한 결과가 아닙니다.**
- **실시간 수집은** `D010_pokemon_type_scraping_EDA.ipynb`를 인터넷에 연결된 Jupyter 환경에서 실행했을 때 성공 여부를 확인할 수 있습니다.
- 실행 뒤 노트북의 `자료 출처 상태:` 및 `output/process_log.txt`를 확인하세요. `LIVE`일 때만 실시간 웹 수집 성공으로 표시하고, `OFFLINE_FIXTURE`일 때는 교육용 HTML 대체 실행입니다.
- **현재 PDF 보고서의 수치/차트는 70행 표본 기준**이며, 실행 시 `LIVE` 데이터의 통계와 다를 수 있습니다. 라이브 실행 결과를 제출하려면 결과를 대조해 보고서도 실제 수치로 갱신해야 합니다.

## 산출물

| 파일 | 용도 | 근거 수준 |
|---|---|---|
| `D010_pokemon_type_scraping_EDA.ipynb` | requests → BeautifulSoup → pandas → 시각화 및 실행 로그 | 직접 실행 후 확인 필요 |
| `D010_pokemon_표본실행예시.ipynb` | 교육용 표본을 이용한 실행 예시 | 오프라인 예시 |
| `Pokemon_Type_Stats_EDA_Report.pdf` | 6쪽 컬러 EDA 보고서 | 70행 표본 분석 |
| `Pokemon_Type_Stats_EDA_Report.html` | HTML 보고서 | 70행 표본 분석 |
| `pokemon_verified_70.csv` | 70행 데이터 | 공개 표 참고·재구성 표본 |
| `pokemon_type_summary_70.csv` | 1차 타입별 요약 | 공개 표 참고·재구성 표본 |
| `educational_fixture_70.html` | 실시간 접속 실패시 사용하는 교육용 HTML | 실제 사이트 원본 HTML 아님 |
| `assets/*.png` | 컬러 시각화 | 70행 표본 |
| `process_log_OFFLINE_example.txt` | 결과 생성 과정 기록 예시 | 실제 라이브 스크래핑 로그 아님 |

## 실행 방법

1. Python 3.12 기반 Jupyter에 `requests`, `beautifulsoup4`, `pandas`, `numpy`, `matplotlib`, `ipykernel`가 설치되어 있어야 합니다.
2. VS Code에서 이 폴더의 `D010_pokemon_type_scraping_EDA.ipynb`를 열고 커널을 선택한 뒤 **Run All**로 실행합니다.
3. `자료 출처 상태: LIVE`와 각 데이터 검증 결과를 확인합니다. 실제 수집 실패가 나오면 원인을 확인하고 결과를 표본 실행으로 표시하세요.
4. `output/` 폴더의 `pokemon_raw.csv`, `pokemon_clean.csv`, `type_summary.csv`, PNG 차트, `process_log.txt`를 확인합니다.
5. 실제 데이터로 실행했다면 분석 보고서의 표본 수·결과를 갱신한 뒤 제출합니다.

## 분석 질문과 한계

- Q1. 1차 타입별 포켓몬 수는 어떻게 다른가?
- Q2. 1차 타입별 여섯 종족값의 평균은 어떻게 다른가?
- Q3. 공격력과 스피드는 어떤 관계를 보이는가?
- Q4. 종족값 총합이 높은 포켓몬은 누구인가?

**범위 한계:** 70행 표본에는 전국도감 초기 번호만 포함되어, 전체 세대 포켓몬을 대표하지 않습니다. 같은 전국도감 번호의 여러 폼을 단일 기본형으로 대표시키고 복합 타입은 1차 타입으로만 분류했습니다. 종족값은 특성(Ability)이나 대전 승률과 다릅니다.

## GitHub 공개 범위 주의

이 폴더는 직접 제작한 실습 코드와 그 결과물입니다. **LMS 원본 교안 노트북과 비공개 수업 자료는 GitHub 공개 저장소에 추가하지 않습니다.** 사이트 이용조건과 robots.txt를 확인하고 공개된 표 전체를 무분별하게 재배포하지 않습니다.
