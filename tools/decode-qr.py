#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
이미지 안의 QR 코드를 읽어 문자열을 출력합니다. (macOS Core Image 사용, 설치 불필요)

사용법:
  python3 tools/decode-qr.py <이미지 경로>
"""
import subprocess, sys, os

JXA = r'''
ObjC.import("Foundation"); ObjC.import("CoreImage");
var path = "%s";
var img = $.CIImage.imageWithContentsOfURL($.NSURL.fileURLWithPath(path));
if (img.js === undefined && !img) { "ERR:이미지를 열 수 없습니다"; }
else {
  var det = $.CIDetector.detectorOfTypeContextOptions($.CIDetectorTypeQRCode, $(), $({}));
  var fs = det.featuresInImage(img);
  var out = [];
  for (var i = 0; i < fs.count; i++) {
    out.push(ObjC.unwrap(fs.objectAtIndex(i).messageString));
  }
  out.length ? out.join("\n") : "NONE";
}
'''


def decode(path):
    p = os.path.abspath(path)
    r = subprocess.run(['osascript', '-l', 'JavaScript', '-e', JXA % p],
                       capture_output=True, text=True)
    return (r.stdout or r.stderr).strip()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for f in sys.argv[1:]:
        print('%s\n  → %s' % (f, decode(f)))
