# BODYNOX ACADEMY

바디녹스 아카데미 필라테스 지도자 양성 과정(BPM 커리큘럼) 소개 정적 사이트.
빌드 도구 없이 `index.html`을 브라우저에서 바로 열면 동작합니다.

## 폴더 구조

```
bodynox-academy/
├─ index.html              # 메인 페이지 (모든 섹션)
├─ foundation.html         # Foundation 과정 상세 페이지
├─ assets/
│  ├─ css/style.css        # 디자인 토큰 + 전체 스타일
│  ├─ js/main.js           # 모바일 메뉴, 스크롤 등장, 내비 하이라이트
│  └─ img/                 # 로고 에셋 + 스튜디오 · 강사 사진
├─ .nojekyll               # GitHub Pages에서 Jekyll 처리 비활성화
└─ README.md
```

## 브랜드 컬러 · 로고

톤앤매너는 BPM 로고(`BPM logo 1.jpg`)에서 추출한 딥 라즈베리를 기준으로 맞췄습니다.
색상은 전부 `assets/css/style.css` 상단의 CSS 변수로 관리되므로, 변수만 바꾸면 사이트 전체가 따라갑니다.

| 변수 | 값 | 용도 |
|---|---|---|
| `--c-accent` | `#BE0A4C` | BPM 브랜드 컬러 — CTA 버튼, 아이브로우, 태그, 불릿 |
| `--c-accent-dk` | `#98093D` | 버튼 호버, 링크 강조 |
| `--c-accent-lt` | `#E37FA0` | 어두운 배경 위 포인트 |
| `--c-accent-bg` | `#FAE6EC` | 옅은 브랜드 틴트 (뱃지 배경) |
| `--c-dark` | `#2A171E` | 와인 블랙 — 진로 섹션 배경 |
| `--c-bg` / `--c-bg-tint` | `#FBF9F7` / `#F4EEE9` | 웜 아이보리 / 베이지 섹션 |

로고 에셋은 원본 JPG의 흰 배경을 제거해 투명 PNG로 만들어 두었습니다.

| 파일 | 내용 | 사용 위치 |
|---|---|---|
| `bpm-logo.png` | 원형 마크 + 워드마크 전체 락업 | 히어로 뱃지, 푸터 |
| `bpm-mark.png` | 원형 BPM 마크만 | 헤더 |
| `bpm-logo-white.png` | 전체 락업 흰색 버전 | 어두운 배경용 (예비) |
| `bpm-mark-white.png` | 마크 흰색 버전 | 진로 섹션 카드 |
| `favicon.png` / `apple-touch-icon.png` | 파비콘 · iOS 홈화면 아이콘 | `<head>` |

원본 AI 파일로 더 선명한 로고를 쓰려면, 배경 투명 PNG(폭 600px 이상)로 내보내 같은 이름으로 덮어쓰면 됩니다.

## 로컬에서 열기

**방법 1 — 바로 열기 (가장 간단)**

```bash
open index.html
```

Finder에서 `index.html`을 더블클릭해도 됩니다.

**방법 2 — 로컬 서버로 열기 (권장, 실제 배포 환경과 동일)**

```bash
python3 -m http.server 8000
```

그다음 브라우저에서 <http://localhost:8000> 접속. (종료: `Ctrl + C`)

## 교체해야 할 임시 항목

| 위치 | 내용 |
|---|---|
| `index.html` 문의 섹션 | 카카오톡 채널 링크 (`<!-- TODO: 카카오톡 채널 URL로 교체 -->`) |
| `index.html` 문의 섹션 | 구글폼 링크 (`<!-- TODO: 구글폼 URL로 교체 -->`) |
| `index.html` 문의 정보 | 주소 · 전화번호 · 이메일 · 인스타그램 |
| `index.html` 과정/일정/강사진 | 임시 텍스트를 실제 커리큘럼 · 기수 일정 · 약력으로 교체 |
| `.media-placeholder` 블록 | `assets/img/`에 사진을 넣고 `<img>`로 교체 |

사진 교체 예시:

```html
<!-- 기존 -->
<div class="media-placeholder media-placeholder--portrait">
  <span class="media-placeholder__label">강사 사진</span>
</div>

<!-- 교체 후 -->
<img class="media-placeholder--portrait" src="./assets/img/instructor-1.jpg"
     alt="김○○ 대표 강사" width="600" height="800" loading="lazy" />
```

## 사진

| 파일 | 사용 위치 |
|---|---|
| `hero-teaching.jpg` | 히어로 (데스크톱 5:4 / 모바일 4:3 크롭) |
| `scene-classroom.jpg` | 교육 현장 갤러리 — 왼쪽 큰 사진 |
| `scene-lecture.jpg` / `scene-handson.jpg` | 교육 현장 갤러리 — 오른쪽 2장 |

모두 가로형(3:2) 원본을 웹용으로 리사이즈·압축한 것이고, `object-fit: cover`로 크롭됩니다.
같은 파일명으로 덮어쓰면 레이아웃 수정 없이 교체됩니다.
강사진 사진 자리는 아직 플레이스홀더입니다.

## 캐시 주의

`index.html`에서 CSS·JS를 `style.css?v=2`, `main.js?v=2` 형태로 불러옵니다.
브라우저가 예전 파일을 계속 쓰는 것을 막기 위한 버전 표시이므로,
**CSS나 JS를 수정해 배포할 때는 이 숫자를 함께 올려주세요** (v=2 → v=3).
숫자를 올리지 않으면 재방문자에게 최대 10분간 이전 디자인이 보일 수 있습니다.

## GitHub Pages 배포

```bash
git init
git add .
git commit -m "Add Bodynox Academy site"
git branch -M main
git remote add origin https://github.com/<계정>/bodynox-academy.git
git push -u origin main
```

GitHub 저장소 → **Settings → Pages → Build and deployment**
→ Source: `Deploy from a branch`, Branch: `main` / `/ (root)` → Save.

1~2분 뒤 `https://<계정>.github.io/bodynox-academy/` 에서 확인할 수 있습니다.
모든 경로를 상대경로(`./assets/...`)로 작성했기 때문에 하위 경로 배포에서도 그대로 동작합니다.

커스텀 도메인을 쓰려면 저장소 루트에 도메인만 한 줄 적힌 `CNAME` 파일을 추가하고,
DNS에 GitHub Pages IP(A 레코드) 또는 `<계정>.github.io`(CNAME 레코드)를 연결하세요.
