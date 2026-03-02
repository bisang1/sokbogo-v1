import streamlit as st

# 1. 앱 페이지 설정
st.set_page_config(page_title="속보고 콘텐츠 생성기", page_icon="🫁", layout="wide")

# 2. 제목 및 스타일 설정
st.title("🔬 속보고 유튜브 쇼츠 제작 자동화 도구")
st.markdown("임상병리사 관점의 **흰색 고양이 디오라마 건강 콘텐츠**를 자동 생성합니다.")
st.divider()

# 3. 사용자 입력
organ = st.text_input(
    "콘텐츠를 제작할 장기/신체 부위를 입력하세요:",
    placeholder="예: 심장, 폐, 간, 치아",
)

if organ:
    # --- [이미지 프롬프트 생성 로직] ---
    image_prompt = f"""[DALL-E 3 Image Prompt]
Create a highly detailed 3D miniature clay diorama in a toy-world clinical laboratory showing a cross-section of the human {organ}, with a strong tilt-shift macro look.

Main Characters (fixed):
- A white cat wearing a pastel blue sweater and matching pastel blue hat.
- A white cat wearing a pastel pink sweater and matching pastel pink hat.
The white-cat couple are always the protagonists and appear as a coordinated research team.

Clinical Laboratory Expertise:
- Build the educational flow from a clinical pathologist's perspective.
- Reflect scientifically plausible anatomy and physiology of the {organ}.
- Include clear, safe, non-diagnostic health guidance labels based on routine lab-health literacy.
- Keep visuals medically respectful and non-graphic.

Visual Composition:
- Vertical 9:16 framing for YouTube Shorts.
- Layered cutaway of the {organ}: protective outer structures, functional core tissue, and vascular/neural pathways.
- Mini clay microscopes, specimen slides, reagent racks, pipettes, and result panels surrounding the cat couple.
- Rich hand-molded clay textures, tiny fingerprints, soft lab glow, pastel toy-world color harmony.

Style Keywords:
3D miniature clay diorama, toy world, strong tilt-shift effect, ultra-detailed, educational medical visualization, cinematic depth of field, high fidelity, 8k feel."""

    # --- [영상 프롬프트 생성 로직] ---
    video_prompt = f"""[Kling 2.6 Video Prompt]
Vertical 9:16 cinematic macro video in a 3D miniature clay diorama toy world with a strong tilt-shift effect. A cross-section of the human {organ} fills the frame.

Fixed lead characters:
- White cat in pastel blue sweater and hat.
- White cat in pastel pink sweater and hat.
They are an expert white-cat couple leading a clinical-lab style walkthrough.

Direction:
- Open with a gentle top-down reveal, then slow crane-down into the layered {organ} anatomy.
- Focus on tactile clay details: matte tissue clay, lightly glossy vessel lines, powdery pastel surfaces, hand-crafted seams.
- Emphasize ASMR sensory cues: soft brush strokes across clay tissue, tiny tap sounds from mini lab tools, subtle label paper rustle, delicate clicks from compact analyzers.
- Show micro actions: slide labeling, marker tracing, careful pipette handling, mini scanner calibration.

Medical integrity:
- Keep anatomy educational, scientifically plausible, and clinically respectful.
- Add short Korean overlays with non-diagnostic wellness guidance informed by clinical pathologist knowledge.

Look and feel:
clean lab lighting, pastel toy-world palette, precise miniature props, shallow depth of field, soothing yet informative tone, texture-driven cinematography."""

    # --- [쇼츠 나레이션 대본] ---
    narration = f"""오늘은 임상병리사 관점으로 {organ} 건강의 핵심을 짧고 정확하게 정리해 드릴게요.
{organ}는 보호층, 기능 조직, 혈관·신경 네트워크가 균형 있게 맞물릴 때 가장 안정적으로 작동합니다.
이 균형이 흔들리면 피로감, 회복 지연, 컨디션 저하 같은 신호가 먼저 나타날 수 있어요.
생활 습관으로는 수분 충분히 섭취하기, 과도한 염분과 초가공식품 줄이기, 수면 시간을 일정하게 맞추기가 기본입니다.
증상이 반복되거나 오래가면 자가판단보다 의료진 상담과 필요한 검사를 통해 원인을 확인하는 것이 안전합니다.
내 몸의 작은 변화를 놓치지 않는 것, 그것이 건강을 지키는 가장 확실한 시작입니다.
속보고였습니다."""

    # --- [유튜브 메타데이터] ---
    title = f"속보고 | {organ} 건강 핵심 30초 정리 🔬🐱"
    hashtags = f"#속보고 #{organ} #건강정보 #임상병리 #의학상식 #shorts"
    description = f"""파스텔 블루/핑크 스웨터와 모자를 쓴 흰 고양이 커플이,
3D 미니어처 클레이 디오라마 토이 월드에서 {organ}의 구조와 관리 포인트를 설명합니다.

✅ 오늘의 핵심: {organ}의 구조, 기능, 생활 습관 관리 팁
✅ 전문 관점: 임상병리 지식 기반의 건강 정보 구성
✅ 연출 스타일: 강한 틸트 시프트 + ASMR 질감 강조

{hashtags}"""
    pinned_comment = f"오늘 영상에서 다룬 {organ} 건강 습관 중, 여러분이 바로 실천할 한 가지는 무엇인가요? 댓글로 남겨주시면 다음 속보고 주제에 반영할게요! 🐾"

    # --- [UI 출력부] ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼️ 이미지 프롬프트 (DALL-E 3)")
        st.code(image_prompt, language="text")

        st.subheader("🎬 Kling 2.6 영상 프롬프트 (ASMR 질감 강조)")
        st.code(video_prompt, language="text")

    with col2:
        st.subheader("📝 30초 나레이션 대본")
        st.text_area("나레이션", narration, height=300)

        st.subheader("📈 유튜브 메타데이터")
        st.text_area(
            "제목 / 해시태그 / 설명 / 고정 댓글",
            f"""[제목]\n{title}\n\n[해시태그]\n{hashtags}\n\n[영상 설명]\n{description}\n\n[고정 댓글]\n{pinned_comment}""",
            height=320,
        )

    st.subheader("🏷️ 썸네일 추천 문구")
    st.warning(f"'30초 {organ} 건강 브리핑' | '{organ} 미니어처 임상 랩' | '흰 고양이 커플의 건강 핵심 리포트'")
else:
    st.info("장기 이름을 입력하면 '속보고' 전용 콘텐츠 팩이 생성됩니다.")
