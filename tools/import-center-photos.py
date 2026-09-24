#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
센터 사진 일괄 변환 스크립트

사용법:
  python3 tools/import-center-photos.py <폴더명> <slug>
  예) python3 tools/import-center-photos.py 광화문 gwanghwamun

~/Desktop/BPM 홈페이지/센터사진/<폴더명>/ 안의
  · 1~10 번호 파일  → assets/img/studio-<slug>-01.jpg ~ -10.jpg (가로 1600px)
  · '메인' 포함 파일 → assets/img/center-<slug>.jpg (1000x1000)

아이폰 사진의 EXIF 회전 태그를 픽셀에 반영하고 태그를 1로 되돌립니다.
(그대로 두면 브라우저에서 돌아간 채 표시되거나 이중 회전됩니다)
"""
import os, re, struct, subprocess, sys, tempfile, unicodedata

PROJ = '/Users/yongho/Projects/bodynox-academy'
BASE = '/Users/yongho/Desktop/BPM 홈페이지/센터사진'
IMG = os.path.join(PROJ, 'assets', 'img')


def exif_orientation(path):
    data = open(path, 'rb').read(300000)
    if data[:2] != b'\xff\xd8':
        return None
    i = 2
    while i < len(data) - 4:
        if data[i] != 0xFF:
            break
        m = data[i + 1]
        L = struct.unpack('>H', data[i + 2:i + 4])[0]
        if m == 0xE1 and data[i + 4:i + 8] == b'Exif':
            t = i + 10
            bo = '>' if data[t:t + 2] == b'MM' else '<'
            off = struct.unpack(bo + 'I', data[t + 4:t + 8])[0]
            p = t + off
            n = struct.unpack(bo + 'H', data[p:p + 2])[0]
            for k in range(n):
                e = p + 2 + k * 12
                if struct.unpack(bo + 'H', data[e:e + 2])[0] == 0x0112:
                    return struct.unpack(bo + 'H', data[e + 8:e + 10])[0]
            return None
        i += 2 + L
    return None


def reset_orientation(path):
    data = bytearray(open(path, 'rb').read())
    i = 2
    while i < len(data) - 4:
        if data[i] != 0xFF:
            break
        m = data[i + 1]
        L = struct.unpack('>H', bytes(data[i + 2:i + 4]))[0]
        if m == 0xE1 and bytes(data[i + 4:i + 8]) == b'Exif':
            t = i + 10
            bo = '>' if bytes(data[t:t + 2]) == b'MM' else '<'
            off = struct.unpack(bo + 'I', bytes(data[t + 4:t + 8]))[0]
            p = t + off
            n = struct.unpack(bo + 'H', bytes(data[p:p + 2]))[0]
            for k in range(n):
                e = p + 2 + k * 12
                if struct.unpack(bo + 'H', bytes(data[e:e + 2]))[0] == 0x0112:
                    struct.pack_into(bo + 'H', data, e + 8, 1)
                    open(path, 'wb').write(bytes(data))
                    return True
            return False
        i += 2 + L
    return False


def jpeg_size(path):
    with open(path, 'rb') as f:
        f.read(2)
        while True:
            b = f.read(1)
            while b and b != b'\xff':
                b = f.read(1)
            m = f.read(1)
            while m == b'\xff':
                m = f.read(1)
            if not m:
                return None
            if m[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                        0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                f.read(3)
                h, w = struct.unpack('>HH', f.read(4))
                return (w, h)
            L = struct.unpack('>H', f.read(2))[0]
            f.read(L - 2)


ROT = {3: 180, 6: 90, 8: 270}


def convert(src, dst, max_px, quality):
    o = exif_orientation(src) if src.lower().endswith(('.jpg', '.jpeg')) else None
    tmp = None
    work = src
    if o in ROT:
        tmp = tempfile.mktemp(suffix='.jpg')
        subprocess.run(['sips', '-r', str(ROT[o]), src, '--out', tmp],
                       capture_output=True)
        work = tmp
    subprocess.run(['sips', '-Z', str(max_px), '-s', 'format', 'jpeg',
                    '-s', 'formatOptions', str(quality), work, '--out', dst],
                   capture_output=True)
    if tmp:
        os.remove(tmp)
    if exif_orientation(dst) not in (None, 1):
        reset_orientation(dst)
    return o


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    folder, slug = sys.argv[1], sys.argv[2]
    src_dir = os.path.join(BASE, folder)
    if not os.path.isdir(src_dir):
        print('폴더를 찾을 수 없습니다:', src_dir)
        sys.exit(1)

    files = [f for f in os.listdir(src_dir) if not f.startswith('.')]
    # macOS 는 한글 파일명을 분해(NFD) 형태로 저장하므로 정규화 후 비교한다
    norm = {f: unicodedata.normalize('NFC', f) for f in files}

    # 메인 이미지
    main_img = next((f for f in files if '메인' in norm[f]), None)
    if main_img:
        dst = os.path.join(IMG, 'center-%s.jpg' % slug)
        convert(os.path.join(src_dir, main_img), dst, 1000, 72)
        w, h = jpeg_size(dst)
        print('메인   center-%s.jpg  %dx%d  %dKB' %
              (slug, w, h, os.path.getsize(dst) // 1024))
    else:
        print('메인   (메인 이미지 파일 없음 — 파일명에 "메인" 포함 필요)')

    # 번호 사진
    numbered = {}
    for f in files:
        m = re.match(r'^(\d+)\.', f)
        if m:
            numbered[int(m.group(1))] = f
    if not numbered:
        print('스튜디오 (번호 파일 없음)')
        return
    for i in sorted(numbered):
        if i > 10:
            print('스튜디오 %2d  건너뜀 (최대 10장)' % i)
            continue
        dst = os.path.join(IMG, 'studio-%s-%02d.jpg' % (slug, i))
        o = convert(os.path.join(src_dir, numbered[i]), dst, 1600, 62)
        w, h = jpeg_size(dst)
        note = '  (회전 %d° 반영)' % ROT[o] if o in ROT else ''
        print('스튜디오 %2d  %dx%d  %s  %dKB%s' %
              (i, w, h, '가로' if w >= h else '세로',
               os.path.getsize(dst) // 1024, note))


if __name__ == '__main__':
    main()
