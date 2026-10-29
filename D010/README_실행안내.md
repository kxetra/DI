# AIFFEL D010 — 포켓몬 웹 스크래핑 · 타입별 기본 능력치 EDA

## 시작
1. ZIP 전체 압축 해제 후 VS Code에서 `D010_pokemon_type_scraping_EDA.ipynb` 열기.
2. 커널(`myenv`)에서 위에서 아래로 `Run All`. 필요 패키지: `requests beautifulsoup4 pandas numpy matplotlib ipykernel`.
3. **인터넷 연결 성공 시 LIVE**, 아니면 교육용 재구성 HTML 표본(70종) 사용. 셀의 `자료 출처 상태` 및 `output/process_log.txt` 반드시 확인.
4. 실행 완료되면 `output/` 아래 **웹 수집 원본 CSV, 기본형 정제 CSV, 타입별 요약 CSV, PNG 5장, 로그** 생성.
5. 노트북 + 생성된 `output/` + 보고서 제출. LMS가 요구한 브랜치/PR/마감은 별도 준수.

## 자료원
- 표 원본: https://pokemondb.net/pokedex/all
- robots: https://pokemondb.net/robots.txt
- 교육용 70행 표본은 공개 웹페이지의 No.1~70 기본형 능력치를 검증하여 전사하고 다시 구성한 HTML/CSV이며, 실제 사이트에서 자동 다운로드한 원본 HTML이 **아닙니다**.
- `Pokemon_Type_Stats_EDA_Report.pdf`와 HTML 보고서의 모든 통계와 그래프는 위 70행 표본 기준입니다. **전국도감 전체 데이터의 분석 결과가 아닙니다.**

## 분석 범위/한계
- 분석 단위: 전국도감 번호별 기본형 (모든 폼 비교 아님)
- 복합 타입: `type1`만 그룹 기준; 2차 타입을 포함하는 이중 카운트 분석 아님
- 6가지 종족값(HP/ATK/DEF/SP.ATK/SP.DEF/SPEED)은 특성(Ability)과 다른 개념
- 종족값만으로 게임 대전 성능, 승률, 인과효과를 판단할 수 없음.
