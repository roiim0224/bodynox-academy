# -*- coding: utf-8 -*-
V = '82'
IG = 'https://www.instagram.com/bpm.bodynox'
KAKAO = 'https://pf.kakao.com/_xexjbUT/chat'
LINE_BANGKOK = 'https://lin.ee/ONPqSSP'

YONGHO = dict(
    name='임용호', role='대표', field='BPM Founder',
    photo='instructor-1.jpg',
    career=['영국 GARUDA Method 마스터 강사',
            '스포츠의과학 전공 (건국대 박사 수료)',
            '운동지도 경력 26년',
            '전) 중앙대 · 수원여자대학 겸임교수'],
    intro=(
        '저는 20년 넘게 인체 움직임을 탐구하며 강사를 길러 왔습니다. '
        '그 시간 동안 확인한 것은 하나입니다. '
        '동작을 많이 아는 강사와 회원의 몸을 읽는 강사는 다르다는 것입니다.\n'
        'BPM 지도자 교육은 호흡과 심부 안정화 시스템, 13가지 기본 움직임에서 시작합니다. '
        '이 과정은 운동사슬, 운동역학, 인체발달학을 기준으로 교육과정이 설계되었습니다.\n'
        '그래서 저는 이렇게 약속합니다. 첫 달 안에 이 교육이 다르다는 것을 보여드리겠습니다. '
        '월 구독으로 시작하고, 정말 좋은 강사가 될 수 있는지 자신이 직접 판단해 보세요.\n'
        '비전공자든 물리치료사든, 출발점은 달라도 도착점은 같습니다. '
        '회원 앞에서 자신 있는 강사, 그 자리로 함께 가겠습니다.'
    ),
)
JIYOUNG = dict(
    name='홍지영', role='원장', field='BPM Founder',
    photo='instructor-2.jpg',
    career=['영국 GARUDA Method 마스터 강사',
            '전) PSC Burn at the Barre 마스터 강사',
            '한성대 무용 전공',
            '필라테스 지도 경력 20년'],
    intro=(
        "무용수의 몸으로 20년을 가르쳐 온 저는 움직임을 '동작'이 아니라 '선'으로 봅니다. "
        '발레에서 익힌 축과 정렬, 움직임의 감각은 필라테스 기구 위에서 그대로 살아나고, '
        '회원의 몸에서 무너지는 지점을 가장 먼저 알아채는 눈이 되었습니다.\n'
        'GARUDA Method는 필라테스, 요가, 발레, 짐나스틱을 하나의 흐름으로 통합한 '
        '영국의 무브먼트 시스템입니다. 저는 지난 10년간 GARUDA Method 마스터 강사로 활동해 왔습니다. '
        '척추의 나선형 움직임과 근막 사슬을 따라 몸 전체를 하나로 잇는 GARUDA의 관점은, '
        '13가지 기본 움직임에서 출발해 회원을 평가하고 프로그램을 설계하는 '
        'BPM의 철학과 정확히 맞닿아 있습니다.\n'
        '지난 20년 동안 초보자부터 전문 무용수까지 가르치며 얻은 결론은 단순합니다. '
        '좋은 강사는 어려운 동작을 시키는 사람이 아니라, '
        '그 사람이 지금 할 수 있는 가장 좋은 움직임을 찾아주는 사람이라는 것입니다.'
    ),
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
    dict(slug='seoul', seo='바디녹스 서울역센터 — 서울 용산구 남산트윈시티. BPM 지도자 교육 주말반과 화·목 주중반이 진행되는 본원으로, 임용호·홍지영 마스터가 직접 지도합니다.', name='바디녹스 서울역센터', short='서울역센터',
         flag='kr', country='대한민국', note='주말반 · 주중반 진행',
         address='서울특별시 용산구 한강대로 366, 남산트윈시티 B동 1층 105호',
         phone='010-2364-4499', masters=[YONGHO, JIYOUNG], photos=10),
    dict(slug='gwanghwamun', seo='바디녹스 광화문센터 — 서울파이낸스센터 지하 1층. BPM 교육생이 추가 비용 없이 자유롭게 연습할 수 있는 전용 연습 공간입니다.', name='바디녹스 광화문센터', short='광화문센터',
         flag='kr', country='대한민국', note='연습 공간의 확장',
         address='서울시 중구 세종대로 136, 서울파이낸스센터 지하 1층 (버핏그라운드 피트니스 센터 내부)',
         phone='010-9446-3238',
         practice=True, masters=[], photos=10),
    dict(slug='seocho', hidden=True, seo='바디녹스 서초센터 — BPM 지도자 교육 주말반이 진행되는 교육센터입니다. 주소와 연락처는 확정 후 공지됩니다.', name='바디녹스 서초센터', short='서초센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='gangbuk', hidden=True, seo='바디녹스 강북센터 — BPM 지도자 교육 주말반이 진행되는 교육센터입니다. 주소와 연락처는 확정 후 공지됩니다.', name='바디녹스 강북센터', short='강북센터',
         flag='kr', country='대한민국', note='주말반 진행',
         address=None, phone=None, masters=blank(1), photos=10),
    dict(slug='jakarta', hidden=True, seo='자카르타센터 — 인도네시아 자카르타에서 국내와 동일한 BPM 커리큘럼으로 진행되는 해외 교육센터입니다.', name='자카르타센터', short='자카르타센터',
         flag='id', country='인도네시아', note='주말반 진행',
         address=None, phone=None, masters=blank(3), photos=10),
    dict(slug='bangkok', seo='BPM Bangkok Center — 태국 방콕 O-NES Tower, BTS 나나역 직결. 홍한나 마스터가 담당하는 BPM 지도자 교육 해외 교육센터입니다.', name='BPM Bangkok Center', short='BPM Bangkok Center',
         flag='th', country='태국', note='주말반 진행',
         address=('4th Floor, O-NES Tower, 6 Sukhumvit 6 Alley, Khlong Toei, '
                  'Bangkok 10110, Thailand'
                  '<span class="cinfo__sub">BTS 나나(Nana)역 2번 출구 스카이브릿지로 바로 연결됩니다.</span>'),
         phone='080-009-7024', tel='+66800097024',
         chat=('line', LINE_BANGKOK),
         masters=[HANNA_BKK], photos=8),
]
