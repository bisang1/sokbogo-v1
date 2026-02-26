import streamlit as st

st.set_page_config(page_title="속보고(Sokbogo) 콘텐츠 생성기", page_icon="🫁", layout="wide")

st.title("🔬 속보고(Sokbogo) 유튜브 쇼츠 제작 자동화 도구")
st.markdown("임상병리사의 전문성이 담긴 **3D 미니어처 클레이 디오라마 건강 콘텐츠**를 자동으로 생성합니다.")
st.divider()

organ = st.text_input(
    "콘텐츠를 제작할 장기/신체 부위를 입력하세요:",
    placeholder="예: 심장, 폐, 간, 치아",
)

if organ:
    image_prompt = f"""[DALL-E 3 Image Prompt]
Create a highly detailed 3D miniature clay diorama inside a toy-world laboratory showing a cross-section of the human {organ}, designed with strong tilt-shift photography.

Main Characters (fixed):
- A white cat wearing a pastel blue sweater and matching pastel blue hat.
- A white cat wearing a pastel pink sweater and matching pastel pink hat.
The cat couple are clinical laboratory specialists and appear throughout the scene as protagonists.

Medical Accuracy:
- Reflect clinical pathology knowledge with plausible anatomy and physiology of the {organ}.
- Show educational labels for key structures and safe, practical health guidance cues.
- Keep visuals scientifically respectful and non-graphic.

Visual Composition:
- Vertical 9:16 layout for YouTube Shorts.
- Layered cutaway of the {organ}: outer protective tissue, functional inner tissue, and vascular/neural network.
- Tiny clay tools, microscopes, specimen trays, and diagnostic monitors around the cat couple.
- Rich handcrafted clay texture, finger-molded details, miniature props, soft ambient lab glow.
- Toy-world color palette with pastel accents and clean hospital lighting.

Style Keywords:
3D miniature clay diorama, toy world, tilt-shift macro, ultra-detailed, educational medical visualization, cinematic depth of field, high fidelity, 8k feel."""

    video_prompt = f"""[Kling 2.6 Video Prompt]
Vertical 9:16 cinematic macro video in a 3D miniature clay diorama toy world. A cross-section of a human {organ} fills the frame. Strong tilt-shift effect.

Fixed lead characters:
- White cat in pastel blue sweater and hat.
- White cat in pastel pink sweater and hat.
They act as a clinical laboratory expert couple, inspecting the {organ} with tiny diagnostic devices.

Direction:
- Start with a soft top-down reveal, then slow crane-down movement into the layered anatomy.
- Show tactile clay textures: matte clay skin, slightly glossy vascular lines, powdery pastel surfaces, tiny hand-crafted seams.
- Emphasize ASMR-like sensory moments: gentle brush strokes on clay tissue, subtle tapping of miniature tools, soft rustle of paper labels, tiny click sounds from lab devices.
- Include micro actions: sample tagging, marker tracing, gentle calibration of miniature scanners.

Medical integrity:
- Keep the anatomy of the {organ} educational and clinically plausible.
- Present non-diagnostic wellness guidance text overlays in Korean.

Look and feel:
clean lab lighting, pastel toy-world palette, precise mini props, shallow depth of field, soothing but informative tone, ultra-detailed texture-driven cinematography."""

    narration = f"""당신의 {organ}, 생각보다 훨씬 바쁘게 일하고 있다는 사실 알고 계셨나요?
오늘은 임상병리사의 시선으로 {organ}의 핵심 구조를 쉽고 정확하게 살펴볼게요.
겉을 보호하는 조직, 실제 기능을 수행하는 중심 조직, 그리고 영양과 신호를 전달하는 혈관·신경 네트워크가 유기적으로 맞물려 움직입니다.
이 균형이 깨지면 피로감이나 이상 신호가 먼저 나타날 수 있어요.
물을 충분히 마시고, 짠 음식과 가공식품을 줄이고, 수면 리듬을 일정하게 유지하는 것만으로도 {organ} 건강에 큰 도움이 됩니다.
오늘도 내 몸의 신호를 가볍게 넘기지 말고, 작은 습관부터 실천해 보세요.
속보고와 함께라면 건강 정보, 더 정확하고 더 쉽게 이해할 수 있습니다."""

    title = f"내 몸속 미니어처 연구소! {organ} 건강의 핵심을 30초에 🔬🐱"
    hashtags = f"#속보고 #{organ} #건강정보 #임상병리 #인체해부 #의학상식 #shorts"
    description = f"""파스텔 블루/핑크 스웨터를 입은 흰 고양이 커플과 함께,
3D 미니어처 클레이 디오라마로 {organ}의 구조와 건강 포인트를 임상병리사 관점에서 쉽게 풀어드립니다.

✅ 오늘의 핵심: {organ}의 구조, 기능, 생활 속 관리 팁
✅ 형식: 토이 월드 + 강한 틸트 시프트 + ASMR 질감 연출

{hashtags}"""
    pinned_comment = f"여러분은 {organ} 건강을 위해 오늘 어떤 습관을 실천하셨나요? 궁금한 점은 댓글로 남겨주시면 속보고가 다음 영상에서 다뤄볼게요! 🐾"

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
    st.warning(f"'30초 {organ} 건강 브리핑' | '{organ} 속 미니어처 연구소' | '고양이 커플이 알려주는 핵심 의학상식'")
else:
    st.info("장기 이름을 입력하면 '속보고' 전용 콘텐츠 팩이 생성됩니다.")
