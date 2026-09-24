# -*- coding: utf-8 -*-
V = '55'
IG = 'https://www.instagram.com/bpm.bodynox'
KAKAO = 'https://pf.kakao.com/_xexjbUT/chat'
LINE_BANGKOK = 'https://lin.ee/ONPqSSP'
IG_BANGKOK = 'https://www.instagram.com/thewaypilates_official'

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

HANNA = dict(
    name='홍한나', role='마스터', field='The Way Pilates CEO',
    photo='instructor-3.jpg',
    career=['BPM Master Instructor',
            '이화여자대학교 스포츠교육학 석사',
            '전) 더 모던 필라테스 대표',
            '필라테스 지도 경력 20년'],
    intro=None,
)

# 방콕센터 페이지용 — 홍한나.pdf 의 CAREER / QUALIFICATIONS 기준
HANNA_BKK = dict(
    name='홍한나', role='마스터', field='BPM Teacher Training Master',
    photo='instructor-3.jpg',
    career=['BPM Teacher Training Master',
            '이화여자대학교 스포츠교육학 석사',
            '전) 더 모던 필라테스 대표 (2012~2024)',
            '필라테스 지도 경력 20년',
            'STOTT PILATES\u00ae IMP',
            'Balanced Body\u00ae Comprehensive Apparatus',
            'GYROTONIC\u00ae \u00b7 GYROKINESIS\u00ae \uc9c0\ub3c4\uc790',
            'Jumping Stretching Board 지도자'],
    intro=('20년 넘게 필라테스를 지도해 온 홍한나 마스터는, 교육생이 동작을 외우는 데 그치지 않고 '
           '그 동작이 왜 그렇게 설계되었는지를 이해한 뒤 실제 수업에서 자신 있게 적용할 수 있도록 이끕니다. '
           '정확한 관찰, 목적이 분명한 동작 선택, 군더더기 없는 큐잉, 효과적인 수업 설계 — '
           '이 네 가지에 집중해 아는 것을 가르칠 수 있는 지도자로 성장시킵니다.'),
)


def blank(n=1):
    return [dict(name=None, role=None, field=None, photo=None, career=None, intro=None) for _ in range(n)]

CENTERS = [
    dict(slug='seoul', name='바디녹스 서울역센터', short='서울역센터',
         flag='kr', country='대한민국', note='주말반 · 주중반 진행',
         address='서울특별시 용산구 한강대로 366, 남산트윈시티 B동 1층 105호',
         phone='010-2364-4499', masters=[YONGHO, JIYOUNG], photos=10),
    dict(slug='gwanghwamun', name='바디녹스 광화문센터', short='광화문센터',
         flag='kr', country='대한민국', note='연습 공간의 확장',
         address='서울시 중구 세종대로 136, 서울파이낸스센터 지하 1층 (버핏그라운드 피트니스 센터 내부)',
         phone='010-9446-3238',
         practice=True, masters=[], photos=10),
    dict(slug='seocho', name='바디녹스 서초센터', short='서초센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='gangbuk', name='바디녹스 강북센터', short='강북센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='jakarta', name='자카르타센터', short='자카르타센터',
         flag='id', country='인도네시아', note='주말반 진행',
         address=None, phone=None, masters=blank(3), photos=10),
    dict(slug='bangkok', name='BPM Bangkok Center', short='BPM Bangkok Center',
         flag='th', country='태국', note='주말반 진행',
         address=('4th Floor, O-NES Tower, 6 Sukhumvit 6 Alley, Khlong Toei, '
                  'Bangkok 10110, Thailand'
                  '<span class="cinfo__sub">BTS 나나(Nana)역 2번 출구 스카이브릿지로 바로 연결됩니다.</span>'),
         phone='080-009-7024', tel='+66800097024',
         chat=('line', LINE_BANGKOK),
         ig=IG_BANGKOK,
         masters=[HANNA_BKK], photos=8),
]
