#!/usr/bin/env python3
"""part-tag와 실제 내용 매칭되게 일괄 수정"""

HTML_FILE = "/Users/jieun-/Desktop/바이브코딩/5월21일 무료라이브/presentation.html"

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# 단순 텍스트 치환 (part-tag 정리)
replacements = [
    # 인스타 9칸 진단 섹션
    ('PART 3 · 1부 진단', 'PART 3 · 인스타 1부 진단'),
    ('패턴 1 / 7', '인스타 패턴 1/7'),
    ('패턴 2 / 7', '인스타 패턴 2/7'),
    ('패턴 3 / 7', '인스타 패턴 3/7'),
    ('패턴 4 / 7', '인스타 패턴 4/7'),
    ('패턴 5 / 7', '인스타 패턴 5/7'),
    ('패턴 6 / 7', '인스타 패턴 6/7'),
    ('패턴 7 / 7', '인스타 패턴 7/7'),
    ('PART 3 · 셀프 진단', 'PART 3 · 인스타 9칸 셀프 진단'),
    # 9칸 공식 섹션
    ('PART 3 · 2부 공식', 'PART 3 · 인스타 9칸 공식 (도입)'),
    ('PART 3 · 실제 카드뉴스 샘플', 'PART 3 · 9칸 카드뉴스 샘플'),
    ('PART 3 · 상단 3칸', 'PART 3 · 9칸 상단 (신뢰)'),
    ('PART 3 · 중간 3칸', 'PART 3 · 9칸 중간 (차별화)'),
    ('PART 3 · 하단 3칸', 'PART 3 · 9칸 하단 (후기/일상)'),
    ('PART 3 · 업종별 변형', 'PART 3 · 9칸 업종별 변형'),
    ('PART 3 · 운영 주기', 'PART 3 · 인스타 운영 주기 (도입)'),
    ('PART 3 · 칸별 주기', 'PART 3 · 9칸 칸별 주기'),
    ('PART 3 · 채널별 주기', 'PART 3 · 인스타 3채널 주기'),
    # 잠깐 질문 슬라이드는 사실 네이버 도입 흐름
    ('PART 3 · 잠깐 질문', 'PART 3 · 네이버 (검색 질문)'),
]

for old, new in replacements:
    content = content.replace(f'>{old}<', f'>{new}<')

# PART 6 클로징 두 슬라이드 따로 처리 (둘 다 같은 태그)
# 62번 "근데 솔직히… 혼자 다 하실 수 있어요?"
content = content.replace(
    '<div class="part-tag">PART 6 · 클로징</div>\n            <h2 class="section-title">근데 솔직히…',
    '<div class="part-tag">PART 6 · 클로징 빌드업</div>\n            <h2 class="section-title">근데 솔직히…'
)
# 63번 "두 갈래 길"
content = content.replace(
    '<div class="part-tag">PART 6 · 클로징</div>\n            <h2 class="section-title">지금 원장님 앞에',
    '<div class="part-tag">PART 6 · 두 갈래 길</div>\n            <h2 class="section-title">지금 원장님 앞에'
)

with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ part-tag 일괄 정리 완료")
