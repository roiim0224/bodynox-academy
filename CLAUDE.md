# 바디녹스 아카데미 (BPM 지도자 교육) 홈페이지

Bodynox Pilates Method 필라테스 지도자 양성 과정의 모집 · 신청 사이트.
빌드 도구 없는 순수 HTML/CSS/JS 정적 사이트이며 GitHub Pages 로 배포된다.

- 운영 주소 https://bpm.bodynox.com
- 저장소 github.com/roiim0224/bodynox-academy (main 브랜치가 곧 배포본)
- 사업자 (주)바디녹스인터내셔널 · 대표 임용호 · 884-81-01065

---

## 작업 규칙

### 1. 캐시 버전을 반드시 올린다

CSS · JS · 로컬 이미지는 모두 `?v=NN` 로 캐시를 끊는다.
**무엇이든 고쳤으면 전 파일의 버전을 함께 올린다.** 안 올리면 사용자 브라우저에
옛 파일이 남아 "수정이 반영되지 않았다" 는 보고가 돌아온다. 실제로 여러 번 겪었다.

```bash
sed -i '' 's/v=87/v=88/g' *.html
sed -i '' "s/V = '87'/V = '88'/" tools/centers_data.py
python3 tools/build-centers.py
```

GitHub Pages 는 HTML 에 `max-age=600` 을 붙이며 이건 쿼리로 끊을 수 없다.
HTML 자체의 반영은 최대 10분 걸린다고 안내할 것.

### 2. 센터 페이지는 직접 고치지 않는다

`center-*.html` 6개는 생성물이다. 고칠 곳은 두 군데다.

- `tools/centers_data.py` — 센터 정보, 마스터 강사, 사진 장수
- `tools/build-centers.py` — 페이지 구조와 템플릿

고친 뒤 `python3 tools/build-centers.py` 를 실행한다.
**직접 편집하면 다음 생성 때 사라진다.**

### 3. 센터 사진 넣기

`~/Desktop/BPM 홈페이지/센터사진/<폴더>/` 에 `메인사진` 1장과 `1`~`10` 번호 파일을 두고

```bash
python3 tools/import-center-photos.py 태국\(방콕\) bangkok
```

아이폰 EXIF 회전 보정과 리사이즈가 자동 처리된다.
macOS 한글 파일명은 NFD 라서 비교 전에 `unicodedata.normalize('NFC', …)` 가 필요하다.

### 4. 배포

`git push origin main` 이 곧 배포다. 별도 빌드 단계가 없다.
푸시 후 `curl` 로 실제 반영을 확인한 뒤 완료를 보고한다.

### 5. 검증

HTML 을 고쳤으면 태그 짝과 JSON-LD 파싱을 확인한다. 과거에 섹션을 통째로
교체하다 `</div></section>` 를 날린 적이 있다. 숫자를 바꿨으면 합계도 다시 계산한다.

---

## 하지 말 것

- **CNAME 을 DNS 보다 먼저 커밋하지 말 것.** 사이트가 즉시 내려간다. 한 번 겪었다.
  `tools/go-live-domain.sh` 가 DNS 를 먼저 확인하도록 만들어 두었다.
- **사용자가 준 원문(소개글 · 마케팅 문구)을 임의로 고치지 말 것.**
  문법 오류나 사실 오류가 보이면 고치기 전에 무엇을 왜 바꾸는지 밝힌다.
- **경력 · 시간 · 가격 · 법령 근거를 추측으로 채우지 말 것.** 자료가 없으면 비워두고 묻는다.
- **미확인 사실을 자격 · 인증 문구에 쓰지 말 것.** 과거에 '한국교육개발원' 오기가 있었다.

---

## 현재 상태 (2026-09-25 기준)

### 공개

| 영역 | 상태 |
|---|---|
| 모집 기수 | 79기(서울역 주말) · 80기(방콕 주말) · 81기(서울역 화·목 주중) 전부 모집중 |
| 교육센터 | 서울역 · 광화문(연습공간) · BPM Bangkok Center |
| 과정 | Online · Foundation · Intermediate |
| 사이트맵 | 11개 URL |

### 비공개 (자료 대기)

`center-seocho` · `center-gangbuk` · `center-jakarta`
→ `centers_data.py` 에 `hidden=True`. 목록 카드 제거 + noindex + 사이트맵 제외.
자료가 오면 `hidden=True` 만 지우고 사이트맵에 URL 을 되돌리면 복구된다.

82 · 83기 모집 카드도 일정 미정이라 제거한 상태다.

### 연동

```
GA4                G-C2H8VEPDVC        (assets/js/analytics.js)
네이버 애널리틱스     1221efa822081f0     (같은 파일)
메타 픽셀            2370021590146728    (같은 파일 · BPM 코리아 소유 데이터 세트)
메타 비즈니스        BPM 코리아 556954782452067 · 광고계정 bpm.bpdynox 1650184236333483
구글 서치콘솔        소유확인 파일 google505bdee7b06aae57.html
네이버 서치어드바이저  index.html 의 naver-site-verification 메타
토스 결제 79기       buy.tosspayments.com/products/IGBnLL5poY
토스 결제 81기       buy.tosspayments.com/products/JbBoNVKo18
카카오톡 (국내)      pf.kakao.com/_xexjbUT/chat
LINE (방콕)         lin.ee/ONPqSSP
인스타그램           instagram.com/bpm.bodynox  (전 페이지 공통, 센터별 계정 쓰지 않음)
```

맞춤 이벤트 5개가 심겨 있다. 전부 `analytics.js` 의 `bpmTrack()` 을 거친다.

| 이벤트 | 시점 | 주요 매개변수 | 메타 표준 이벤트 |
|---|---|---|---|
| `apply_click` | 다른 페이지 → `apply.html` 링크 클릭 | `spot` 버튼 위치 · `label` | `ViewContent` |
| `form_open` | 신청서 열기 | `method` (현재 `임베드` 뿐) | `Lead` |
| `form_submit` | 신청서 제출(추정) | `sec` 체류초 · `loads` iframe 로드수 | `CompleteRegistration` |
| `payment_click` | 토스 결제 링크 클릭 | `intake` 기수 | `InitiateCheckout` (789,000 KRW) |
| `contact_click` | 상담 채널 클릭 | `channel` 카카오톡 / LINE / 전화 / 인스타그램 | `Contact` |

**`payment_click` 을 `Purchase` 로 보내지 않는다.** 토스에서 완료 신호가 돌아오지
않아 결제하지 않은 클릭까지 매출로 잡힌다. 메타 안에서 ROAS 는 측정할 수 없고
실제 매출은 토스 정산 내역으로 따로 계산해야 한다.

자동 고급 매칭은 꺼 두었다. 켜려면 `privacy.html` 제7조의 이전 항목을 먼저 고친다.
**건강 정보(체형 · 통증 · 질환)는 어떤 경우에도 메타로 보내지 않는다.** 약관 위반이다.

**`form_submit` 은 추정값이다.** 구글폼이 다른 도메인이라 제출을 읽을 수 없어,
iframe 의 두 번째 load 를 제출로 본다(`main.js` 의 `finish()`). `sec` 이 지나치게
짧거나 `loads` 가 3 이상이면 오탐일 수 있다. **구글폼 실제 응답 수와 대조해야
이 숫자를 신뢰할 수 있다.**

신청 경로는 임베드 하나뿐이다. `apply.html` 의 '새 창에서 신청서 열기' 링크는
`<noscript>` 안에 있어 JS 가 켜진 브라우저에는 DOM 에 존재하지 않는다.
새 창 링크를 본문으로 꺼내면 그 경로의 제출은 측정할 수 없게 되니 주의한다.

---

## 확정된 사실 (추측하지 말고 이 값을 쓸 것)

### 교육비

```
월 789,000원 x 6개월 = 총 4,734,000원

대면 강의   3,194,000원   79기 16일(1일 199,625원) / 81기 32일(1일 99,812원)
온라인 강좌   210,000원   (200,000 + 교재 10,000)
교재 9권     180,000원   권당 20,000원
그룹수업 20회 400,000원   회당 20,000원
마스터 1:1 5회 750,000원  회당 150,000원
```

대면은 두 반 모두 128시간. 79기는 1일 8시간 x 16일, 81기는 1일 4시간 x 32일.
총 학습 450시간 = 대면 128 + 온라인 20 + 관찰 100 + 자가연습 100 + 티칭 100 + 시험 2.

### 자격

- 등록민간자격 **2022-004967**, 자격명 **바디녹스 필라테스 지도자 3급, 2급**
- Foundation 수료 → **3급**, Intermediate 수료 → **2급**. 둘 다 자격증이다(수료증 아님)
- 국가공인 아님. 표시사항 블록(`#qualification`)이 5개 페이지에 들어가 있고
  '국가공인 여부' 행은 빼되 법정 고지 문장은 블록 하단에 유지한다
- **PMA ITTAP 는 승인 신청 단계이며 아직 미승인.** 승인된 것처럼 쓰지 말 것

### 환급

월별 등록이라 다음 달 교육비는 애초에 청구되지 않는다. 자동 결제가 아니라
매월 결제 링크를 보낸다. 중단 신청 마감은 **다음 교육월 결제일 10일 전**.

환급액 = 누적 결제액 − 누적 제공 항목 금액 (월별로 끊지 않고 누적).
대면은 결석해도 진행된 교육일로 공제한다(정원제 기수 수업).
누적 제공액이 결제액을 넘어도 초과분은 청구하지 않되 다음 달 계산에는 반영한다.

### 강사

- 임용호 대표 (BPM Founder) · 홍지영 원장 (BPM Founder) — 서울역센터
- 홍한나 마스터 (BPM Teacher Training Master) — BPM Bangkok Center

---

## 남은 일

**자료 대기**
- 서초 · 강북 센터: 주소 · 연락처 · 마스터 1명 · 사진
- 자카르타 센터: 주소 · 연락처 · 마스터 3명 · 사진 (상담 채널은 WhatsApp 확인 필요)
- 82 · 83기 교육기간, 83기 배너 이미지
- 80기 방콕 결제 경로 (현재 '센터 문의' 로만 안내)

**유입 분석 (2026-09-27)**

처리 완료
- 강북센터가 구글에 색인돼 있었다 → 서치콘솔 **삭제 요청 접수**(임시, 6개월).
  `noindex` 는 붙기 전에 수집된 탓이다. 서초·자카르타는 색인 안 됐다
- 81기 검색 스니펫이 '13~18시' 옛 값이었다 → **색인 생성 요청**
- **인스타그램 바이오 링크에 UTM 을 붙였다** (2026-09-27)

  ```
  https://bpm.bodynox.com/?utm_source=instagram&utm_medium=bio
  ```

  게시물·스토리에서 유도할 때는 `utm_medium` 을 `post` · `story` 로 바꿔 쓴다.
  링크 수정은 **인스타그램 앱에서만** 된다. 데스크톱 웹은 칸이 잠겨 있다.
  인스타그램이 클릭 시점에 `utm_content=link_in_bio` 와 `fbclid` 를 덧붙인다.
  유효한 `utm_medium` 이 없으면 제멋대로 `utm_medium=social` 을 넣으므로
  오타가 나면 조용히 값이 바뀐다. 실제로 한 번 겪었다(`utm_medium-bio`)
- **홈페이지·신청·Foundation·서울역센터 4개가 색인돼 있지 않았다**
  ('발견됨, 현재 색인이 생성되지 않음' — 크롤링 이력 자체가 없음) → 4개 모두
  색인 생성 요청. 며칠 뒤 `site:bpm.bodynox.com` 으로 반영을 확인할 것

남은 것
- 본사 사이트 개선 → `docs/www-bodynox-seo.md` 참고. 담당자 전달용으로 써 뒀다
- GA4 에 옛 주소(`/bodynox-academy/…`, github.io) 데이터가 섞여 있다

측정된 실태
- 9월 세션 29 · 사용자 26 · 이벤트 138 · 주요 이벤트 0 · 신청 0
- 도시별로 보면 Boardman·Prineville(오리건)·Forest City 가 10명 — 데이터센터 봇이다.
  **국내 실제 방문자는 서울 3 · 성남 2 로 5명.** 참여율 3.45% 도 이 때문이다
- 검색 유입 0. 외부 유입은 m.facebook.com 1건이 전부
- 원인은 색인이 아니라 **외부 링크가 하나도 없는 것**이다
  (서치콘솔 '참조 페이지: 감지된 페이지 없음')

**사용자 직접**
- 도메인 갱신 — **bodynox.com 만료 2026-11-11**
- GA4 주요 이벤트 별표 — `form_submit` · `payment_click` · `contact_click`
  (이벤트가 최근 활동 목록에 오른 뒤). `channel` · `spot` · `method` 는
  맞춤 측정기준으로 등록해야 보고서에서 쪼개 볼 수 있다
- 구글폼 응답 수와 GA4 `form_submit` 수 대조 (추정 정확도 확인)
- 환급 계산 방식 법률 검토 (결석일 공제 · 온라인 즉시 공제가 법정 기준보다 불리할 소지)

**메타 광고 (2026-09-27 픽셀 설치)**
- 픽셀 동작은 `Test events` 로 확인 완료 — PageView · Lead · CompleteRegistration ·
  InitiateCheckout 전부 `Processed`
- 남은 준비: **광고 계정에 데이터 세트 할당**(비즈니스 설정 > 데이터 소스 > 자산 추가),
  **`bodynox.com` 도메인 인증**(DNS TXT 권장 — 루트를 인증하면 서브도메인이 덮인다).
  둘 다 안 하면 전환 목록이 비거나 iOS 전환이 샌다
- 광고는 바로 켜지 않는다. 픽셀 데이터가 쌓여야 최적화·리타겟팅이 작동한다.
  1~2주 두고 인스타 바이오 UTM 부터 거는 편이 같은 예산으로 성과가 낫다
- 초기 최적화 기준은 `Purchase` 가 아니라 `Contact` 또는 `Lead` 로 잡는다.
  광고세트당 주 50건이 있어야 메타 학습이 끝나는데 473만원 상품에서 결제 50건은 안 나온다
- 광고 문구 금지 — **PMA ITTAP 승인됨**(미승인) · **국가공인**(등록민간자격) ·
  취업 · 수입 보장 표현(표시광고법)
- **2026-09-27 테스트 흔적** — 이날 GA4 · 네이버 · 구글폼에 테스트 제출 1건이 섞여 있다.
  실제 지원자가 아니다. 숫자를 셀 때 이 날짜를 뺀다

**보류**
- 영문판 — 한국어판 완성 후 진행하기로 함. `/en/` 디렉터리 + hreflang 방식 권장
- `www.bodynox.com` 에서 이 사이트로 링크 걸기 (검색 노출에 가장 효과적)

---

## 문서 · 도구

```
tools/build-centers.py        센터 페이지 생성
tools/centers_data.py         센터 · 마스터 데이터, 캐시 버전 V
tools/import-center-photos.py 센터 사진 변환
tools/go-live-domain.sh       도메인 전환 (DNS 확인 후에만 CNAME 커밋)
tools/decode-qr.py            QR 이미지에서 URL 추출
README.md                     폴더 구조, 브랜드 토큰, 사진 규격
```
