# 본사 사이트(`www.bodynox.com`) 검색 노출 개선

이 저장소의 사이트가 아니라 **본사 Flutter 웹앱**을 고치는 작업이다.
소스가 이 맥에 없어 직접 고치지 못했다. 담당자에게 아래를 그대로 전달하면 된다.

확인 일자 2026-09-27.

---

## 지금 상태

`https://www.bodynox.com/` 이 내려주는 HTML 전체가 1,835 바이트이고,
`<body>` 안에 있는 것은 이 한 줄뿐이다.

```html
<body>
  <script src="main.dart.js" async></script>
</body>
```

그래서 이렇게 된다.

- 검색결과 제목이 **`bodynox_web`** — Flutter 프로젝트 이름이 그대로 나간다
- 설명이 **`bodynox`** 한 단어 (`<meta name="description" content="bodynox">`)
- `robots.txt` · `sitemap.xml` 둘 다 **404**
- 구글에 색인된 페이지 **1개**, 그 내용도 "bodynox" 뿐
  (같은 시점에 `bpm.bodynox.com` 은 8개 페이지가 내용과 함께 색인돼 있다)
- `bodynox.com` (apex) 은 **DNS 레코드가 없어** 주소창에 치면 접속이 안 된다

즉 본사 사이트는 검색엔진에게 빈 페이지다. 여기에 아카데미 링크를 걸어도
크롤러가 못 읽으므로, 링크를 걸기 **전에** 아래 1·2번을 먼저 해야 값이 생긴다.

---

## 1. `web/index.html` 머리말 교체 (효과 큼 · 위험 없음)

Flutter 프로젝트의 `web/index.html` 에서 `<title>` 과 description 을 바꾸고
정규 주소와 공유 카드 정보를 넣는다. 빌드하면 그대로 나간다.

```html
  <title>바디녹스 | Bodynox</title>
  <meta name="description" content="바디녹스 — 움직임을 과학으로 설계하는 필라테스. 서울역·광화문 센터와 BPM 지도자 양성 과정을 운영합니다." />
  <link rel="canonical" href="https://www.bodynox.com/" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="바디녹스" />
  <meta property="og:title" content="바디녹스 | Bodynox" />
  <meta property="og:description" content="움직임을 과학으로 설계하는 필라테스." />
  <meta property="og:url" content="https://www.bodynox.com/" />
  <meta property="og:image" content="https://www.bodynox.com/icons/Icon-512.png" />
  <meta name="twitter:card" content="summary_large_image" />
```

> 설명 문구는 초안이다. **마케팅 문구는 대표 확인을 받고 넣을 것.**

## 2. `robots.txt` 와 `sitemap.xml` 추가

`web/` 폴더에 두면 빌드 결과에 함께 복사된다.

`web/robots.txt`
```
User-agent: *
Allow: /

Sitemap: https://www.bodynox.com/sitemap.xml
```

`web/sitemap.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.bodynox.com/</loc>
    <priority>1.0</priority>
  </url>
</urlset>
```

## 3. 아카데미로 가는 링크 — 주의할 점

**Flutter 앱 안에 버튼만 다는 것으로는 SEO 효과가 없다.** 화면을 캔버스로
그리기 때문에 크롤러가 `<a href>` 를 보지 못한다. 사용자 이동 통로는 되지만
검색 순위에는 반영되지 않는다.

검색 효과까지 원하면 `web/index.html` 의 `<body>` 안, Flutter 스크립트보다
**앞에** 진짜 앵커를 둔다.

```html
<body>
  <a href="https://bpm.bodynox.com/">BPM 지도자 교육 — 바디녹스 아카데미</a>
  <script src="main.dart.js" async></script>
</body>
```

Flutter 가 올라오면 이 요소가 가려지거나 남을 수 있으니 **실제 화면을 확인**해야
한다. 화면에 잔상이 남으면 CSS 로 위치를 조정하되, `display:none` 으로 숨기지는
말 것 — 사용자에게 안 보이고 크롤러에만 보이는 링크는 구글이 제재한다.

가장 깔끔한 방법은 앱 안 푸터에 링크를 두고(사용자용), 위 앵커도 화면 맨 아래에
실제로 보이게 두는 것(크롤러용)이다.

## 4. apex 도메인

`bodynox.com` 에 A 레코드나 ALIAS 가 없다. `www` 로 보내는 리다이렉트를 걸면
주소창에 `bodynox.com` 만 쳐도 들어온다.

> **DNS 는 닷네임코리아 관리 화면에서 고치면 된다.** 네임서버는
> `miles.ns.cloudflare.com` · `jasmine.ns.cloudflare.com` 로 Cloudflare 를 가리키지만,
> 닷네임코리아 패널에서 넣은 레코드가 Cloudflare 응답에 그대로 나온다.
> Cloudflare 계정에 직접 접근할 필요가 없다. (2026-09-28 확인)

> **만료일 2026-11-11.** 갱신도 함께 확인할 것.

---

## 5. 메타 광고 도메인 인증 TXT — **완료 (2026-09-28)**

아카데미 사이트(`bpm.bodynox.com`)로 메타 광고를 돌리려면 메타가 도메인 소유를
확인해야 한다. **루트 도메인만 인증할 수 있어** 서브도메인으로는 우회가 안 된다.

Cloudflare 의 `bodynox.com` DNS 에 TXT 레코드 하나만 추가하면 된다.

```
Type     TXT
Name     @
Content  facebook-domain-verification=cabt1wmpojkopwg786i8gym8vceirl
TTL      Auto
```

- **기존 TXT(`google-site-verification=…`)는 지우지 말 것.** TXT 는 여러 개가 공존한다
- 사이트 동작에 영향을 주지 않는다. 메일·웹·인증서와 무관한 확인용 값이다
- **처리 완료.** 닷네임코리아에서 TXT 를 넣었고 메타에서 `Verified` 를 받았다.
  다만 같은 값이 안내 표 전체(`Type TXT ▎ Name @ ▎ …`)로 들어간 잘못된 레코드가
  하나 더 남아 있다. 지워도 무방하다

값은 메타 비즈니스 포트폴리오 `BPM 코리아` 에서 발급한 것이라 재발급하면 달라진다.

---

## 순서

1. 1번(머리말) · 2번(robots·sitemap) — 이것만 해도 검색결과 모양이 달라진다
2. 배포 후 서치콘솔에 `www.bodynox.com` 속성을 만들고 사이트맵 제출
3. 그다음 3번(링크)
4. 4번(apex)과 5번(메타 TXT)은 Cloudflare 작업이라 따로 진행
