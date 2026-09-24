# -*- coding: utf-8 -*-
V = '37'
IG = 'https://www.instagram.com/bpm.bodynox'
KAKAO = 'https://pf.kakao.com/_xexjbUT/chat'

YONGHO = dict(
    name='임용호', role='대표', field='BPM Founder',
    photo='instructor-1.jpg',
    career=['영국 GARUDA Method 마스터 강사',
            '스포츠의과학 전공 (건국대 박사 수료)',
            '운동지도 경력 26년',
            '전) 중앙대 · 수원여자대학 겸임교수'],
    intro=None,
)
JIYOUNG = dict(
    name='홍지영', role='원장', field='BPM Founder',
    photo='instructor-2.jpg',
    career=['영국 GARUDA Method 마스터 강사',
            '전) PSC Burn at the Barre 마스터 강사',
            '한성대 무용 전공',
            '필라테스 지도 경력 20년'],
    intro=None,
)

def blank(n=1):
    return [dict(name=None, role=None, field=None, photo=None, career=None, intro=None) for _ in range(n)]

CENTERS = [
    dict(slug='seoul', name='바디녹스 서울역센터', short='서울역센터',
         flag='kr', country='대한민국', note='주말반 · 주중반 진행',
         address='서울특별시 용산구 한강대로 366, 남산트윈시티 B동 1층 105호',
         phone='010-2364-4499', masters=[YONGHO, JIYOUNG], photos=10),
    dict(slug='gwanghwamun', name='바디녹스 광화문센터', short='광화문센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=[YONGHO, JIYOUNG], photos=10),
    dict(slug='seocho', name='바디녹스 서초센터', short='서초센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='gangbuk', name='바디녹스 강북센터', short='강북센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='jakarta', name='자카르타센터', short='자카르타센터',
         flag='id', country='인도네시아', note='주말반 진행',
         address=None, phone=None, masters=blank(3), photos=10),
    dict(slug='bangkok', name='방콕센터', short='방콕센터',
         flag='th', country='태국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
]
