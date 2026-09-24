#!/bin/bash
# bpm.bodynox.com 도메인 전환 스크립트
#
# DNS 가 먼저 연결되어야 합니다. CNAME 을 먼저 커밋하면 사이트가 내려갑니다.
#   Cloudflare > bodynox.com > DNS
#   Type CNAME / Name bpm / Target roiim0224.github.io / Proxy status: DNS only (회색 구름)
#
# 사용법: bash tools/go-live-domain.sh

set -e
cd "$(dirname "$0")/.."

DOMAIN="bpm.bodynox.com"
TARGET="roiim0224.github.io"

echo "1) DNS 확인 — $DOMAIN"
RESOLVED=$(dig +short "$DOMAIN" CNAME 2>/dev/null | sed 's/\.$//')
[ -z "$RESOLVED" ] && RESOLVED=$(dig +short "$DOMAIN" 2>/dev/null | head -1)

if [ -z "$RESOLVED" ]; then
  echo "   ✗ 아직 응답이 없습니다. CNAME 을 커밋하면 사이트가 내려갑니다. 중단합니다."
  exit 1
fi
echo "   ✓ $DOMAIN → $RESOLVED"

if ! echo "$RESOLVED" | grep -q "$TARGET"; then
  echo "   ⚠ 목표($TARGET)와 다릅니다. 레코드를 다시 확인하세요. 중단합니다."
  exit 1
fi

echo "2) CNAME 파일 생성 후 커밋"
cp CNAME.ready CNAME
git add CNAME
git commit -q -m "커스텀 도메인 bpm.bodynox.com 연결

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
git push -q origin main
echo "   ✓ 푸시 완료"

echo "3) GitHub Pages 설정 — 아래는 수동입니다"
echo "   · Settings > Pages > Custom domain 에 $DOMAIN 입력 후 Save"
echo "   · 인증서 발급(수 분)이 끝나면 Enforce HTTPS 체크"
echo
echo "4) 발급 후 확인"
echo "   curl -sI https://$DOMAIN/ | head -1"
echo "   → HTTP/2 200 이면 완료입니다."
