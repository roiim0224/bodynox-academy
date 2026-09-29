#!/usr/bin/env python3
"""
rss.xml 생성 — 네이버 서치어드바이저 제출용.

sitemap.xml 에 들어 있는 URL 을 읽어, 각 HTML 의 <title> 과 meta description 으로
RSS 2.0 피드를 만든다. 사이트맵이 곧 목록이므로 따로 관리할 것이 없다.

    python3 tools/build-rss.py

네이버는 사이트맵보다 RSS 를 자주 확인한다. 페이지를 추가하거나 제목 · 설명을
고쳤으면 사이트맵을 손본 뒤 이 스크립트를 다시 돌린다.
"""

import html
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://bpm.bodynox.com'
KST = timezone(timedelta(hours=9))

CHANNEL_TITLE = '바디녹스 아카데미 — BPM 필라테스 지도자 교육'
CHANNEL_DESC = (
    'Bodynox Pilates Method(BPM) 필라테스 지도자 양성 과정. '
    '월 구독형 6개월 450시간, 등록 민간자격 3급 · 2급. 서울역 · 광화문 · 방콕 교육센터.'
)

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def rfc822(dt):
    """RFC-822 형식. 요일 · 월 이름은 로케일과 무관하게 영문으로 고정한다."""
    return '%s, %02d %s %04d %02d:%02d:%02d %s' % (
        DAYS[dt.weekday()], dt.day, MONTHS[dt.month - 1], dt.year,
        dt.hour, dt.minute, dt.second, dt.strftime('%z'),
    )


def local_path(loc):
    """https://bpm.bodynox.com/foo.html → ROOT/foo.html"""
    rel = loc[len(SITE):].lstrip('/')
    return ROOT / (rel if rel else 'index.html')


def extract(path):
    src = path.read_text(encoding='utf-8')

    m = re.search(r'<title>(.*?)</title>', src, re.S)
    title = html.unescape(m.group(1)).strip() if m else path.stem

    m = re.search(r'<meta\s+name="description"\s+content="(.*?)"', src, re.S)
    desc = html.unescape(m.group(1)).strip() if m else ''

    return title, desc


def main():
    sitemap = ROOT / 'sitemap.xml'
    if not sitemap.exists():
        sys.exit('sitemap.xml 이 없습니다.')

    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    tree = ET.parse(sitemap)

    entries = []
    for url in tree.getroot().iter(ns + 'url'):
        loc = url.findtext(ns + 'loc', '').strip()
        if not loc.startswith(SITE):
            continue
        lastmod = (url.findtext(ns + 'lastmod') or '').strip()
        path = local_path(loc)
        if not path.exists():
            print(f'  건너뜀 (파일 없음): {loc}')
            continue
        title, desc = extract(path)
        try:
            dt = datetime.strptime(lastmod, '%Y-%m-%d').replace(tzinfo=KST)
        except ValueError:
            dt = datetime.fromtimestamp(path.stat().st_mtime, KST)
        entries.append((dt, loc, title, desc))

    if not entries:
        sys.exit('사이트맵에서 읽은 URL 이 없습니다.')

    # 최근에 고친 것을 위로
    entries.sort(key=lambda e: e[0], reverse=True)

    now = datetime.now(KST)
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
           '  <channel>',
           f'    <title>{html.escape(CHANNEL_TITLE)}</title>',
           f'    <link>{SITE}/</link>',
           f'    <description>{html.escape(CHANNEL_DESC)}</description>',
           '    <language>ko</language>',
           f'    <lastBuildDate>{rfc822(now)}</lastBuildDate>',
           f'    <atom:link href="{SITE}/rss.xml" rel="self" type="application/rss+xml" />']

    for dt, loc, title, desc in entries:
        out += ['    <item>',
                f'      <title>{html.escape(title)}</title>',
                f'      <link>{loc}</link>',
                f'      <description>{html.escape(desc)}</description>',
                f'      <pubDate>{rfc822(dt)}</pubDate>',
                f'      <guid isPermaLink="true">{loc}</guid>',
                '    </item>']

    out += ['  </channel>', '</rss>', '']

    (ROOT / 'rss.xml').write_text('\n'.join(out), encoding='utf-8')
    print(f'생성: rss.xml  ({len(entries)}개 항목)')


if __name__ == '__main__':
    main()
