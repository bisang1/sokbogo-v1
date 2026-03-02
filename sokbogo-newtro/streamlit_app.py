import streamlit as st

st.set_page_config(page_title="Sokbogo 콘텐츠 생성기", page_icon="🫁", layout="wide")

st.title("🎬 Sokbogo 유튜브 쇼츠 제작 자동화 도구")
st.markdown("채널 톤에 맞춘 **건강 콘텐츠 생성 프롬프트/대본/메타데이터**를 자동으로 생성합니다.")
st.divider()

channel = st.selectbox("채널을 선택하세요:", ["뉴트로", "속보고", "김앤리(연구소)"])
organ = st.text_input(
    "콘텐츠를 제작할 장기/신체 부위를 입력하세요:",
    placeholder="예: 심장, 폐, 간, 치아",
)


def build_newtro_content(target: str) -> dict:
    return {
        "image_prompt": f"""[DALL-E 3 Image Prompt | 뉴트로]
Create a highly detailed 3D miniature clay diorama in a toy world with a strong tilt-shift effect.
A white cat couple appears as fixed protagonists:
- White cat with pastel blue sweater and hat
- White cat with pastel pink sweater and hat
Set inside a cross-section of the human {target} with educational labels.
Style: retro-futuristic + playful clinical lab, cinematic lighting, handcrafted clay texture, 9:16 vertical composition.""",
        "video_prompt": f"""[Kling 2.6 Video Prompt | 뉴트로]
9:16 vertical macro cinematic scene in a 3D miniature clay diorama toy world.
White cat couple (pastel blue/pink sweaters and hats) explores the {target} zone.
Strong tilt-shift, tactile ASMR texture, soft tool clicks and brush sounds.
Tone: nostalgic + modern educational style, clinically respectful.""",
        "narration": f"""오늘은 {target}를 쉽고 빠르게 살펴볼게요.
겉 구조를 먼저 보고, 핵심 기능이 일어나는 구역을 확인한 뒤, 일상에서 지키기 쉬운 관리 포인트를 정리합니다.
{target}는 몸의 균형을 유지하는 중요한 역할을 하므로, 수면과 수분, 식습관만 안정적으로 관리해도 큰 도움이 됩니다.
오늘은 가공식품을 줄이고 물을 충분히 마시는 한 가지 습관부터 시작해 보세요.""",
        "title": f"[뉴트로] {target} 핵심 구조를 30초로 정리! 🧪🐱",
        "hashtags": f"#뉴트로 #{target} #건강정보 #의학상식 #shorts",
        "description": f"""뉴트로 감성의 미니어처 클레이 디오라마로 {target}의 구조와 건강 포인트를 쉽게 설명합니다.
임상병리 지식 기반으로 정확하고 쉬운 건강 정보를 전달합니다.""",
        "pinned_comment": f"{target} 건강을 위해 오늘 실천할 1가지 습관을 댓글로 남겨주세요!",
    }


def build_sokbogo_content(target: str) -> dict:
    return {
        "image_prompt": f"""[DALL-E 3 Image Prompt | 속보고]
Create a highly detailed 3D miniature clay diorama, toy world style, strong tilt-shift.
Fixed character couple:
- White cat with pastel blue sweater and hat
- White cat with pastel pink sweater and hat
Clinical-lab storytelling around the human {target}, with clear educational labels.
Texture-first handcrafted clay details, cozy pastel palette, vertical 9:16 composition.""",
        "video_prompt": f"""[Kling 2.6 Video Prompt | 속보고]
Vertical 9:16 ASMR-focused macro video in a 3D miniature clay diorama toy world.
White cat couple researches {target} with miniature medical tools.
Highlight clay texture sounds, gentle tapping, paper rustle, and scanner clicks.
Strong tilt-shift and cinematic depth of field.""",
        "narration": f"""속보고입니다.
오늘은 {target}의 핵심을 빠르게 짚어볼게요.
기본 구조를 이해하면, 왜 피로나 불편 신호가 나타나는지 훨씬 쉽게 파악할 수 있습니다.
{target} 건강은 갑자기 좋아지지 않기 때문에, 매일 반복 가능한 작은 습관이 가장 중요합니다.
오늘은 짠 음식 줄이기와 일정한 수면 시간 유지부터 시작해 보세요.""",
        "title": f"[속보고] {target} 건강 포인트 30초 브리핑 🔬",
        "hashtags": f"#속보고 #{target} #건강정보 #인체해부 #shorts",
        "description": f"""흰 고양이 커플이 안내하는 속보고 포맷으로 {target}의 구조와 관리 포인트를 압축 정리합니다.
임상병리 관점의 정확한 건강 정보를 짧고 쉽게 전달합니다.""",
        "pinned_comment": f"다음 속보고에서 다뤘으면 하는 신체 부위를 댓글로 남겨주세요! ({target} 관련 질문 환영)",
    }


def build_kimlee_content(target: str) -> dict:
    return {
        "image_prompt": f"""[DALL-E 3 Image Prompt | Kim & Lee Institute]
Design a "Kim & Lee Research Institute" themed educational visual, not a diorama.
Feature the fixed white cat couple researchers:
- White cat in pastel blue sweater and hat
- White cat in pastel pink sweater and hat
Scene: modern medical research briefing room focused on the human {target}.
Composition: clear research board with 3 blocks labeled "연구", "메커니즘", "행동 1가지".
Visual style: polished editorial medical illustration + soft 3D character rendering, clean Korean typography, vertical 9:16, friendly and trustworthy tone.""",
        "video_prompt": f"""[Kling 2.6 Video Prompt | Kim & Lee Institute]
9:16 vertical short-form educational video set in Kim & Lee Research Institute.
The white cat researcher couple (pastel blue/pink sweaters and hats) presents {target} in 3-step order:
1) 연구: what recent evidence says,
2) 메커니즘: how the body process works,
3) 행동 1가지: one practical daily action.
Keep language and visual pacing easy for the general public, within 60 seconds, with gentle texture-rich closeups and subtle ASMR ambience.""",
        "narration": f"""김앤리 연구소입니다. 오늘 주제는 {target}입니다.
연구: 최근 건강 데이터는 {target} 관리를 꾸준히 할수록 몸의 컨디션 변동이 줄어든다고 말합니다.
메커니즘: {target}는 영양, 순환, 신호 전달 같은 기본 기능과 연결되어 있어 작은 생활 습관 변화에도 민감하게 반응합니다.
행동 1가지: 오늘부터 물 섭취 시간을 정해서 하루 3번 규칙적으로 마셔보세요.
작고 쉬운 실천이 {target} 건강을 지키는 가장 현실적인 시작입니다.""",
        "title": f"[김앤리 연구소] {target} 60초 쉬운 설명: 연구→메커니즘→행동 1가지",
        "hashtags": f"#김앤리보고서 #{target} #건강정보 #연구소 #shorts",
        "description": f"""김앤리(연구소) 채널 포맷으로 {target}을 60초 이내로 쉽게 설명합니다.
구성: 연구 → 메커니즘 → 행동 1가지.
임상병리 지식 기반으로 정확성과 이해도를 함께 잡았습니다.""",
        "pinned_comment": f"오늘 영상의 행동 1가지, 바로 실천해보실 분? {target} 관련 다음 주제도 댓글로 알려주세요!",
    }


if organ:
    builders = {
        "뉴트로": build_newtro_content,
        "속보고": build_sokbogo_content,
        "김앤리(연구소)": build_kimlee_content,
    }
    content = builders[channel](organ)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼️ 이미지 프롬프트 (DALL-E 3)")
        st.code(content["image_prompt"], language="text")

        st.subheader("🎬 Kling 2.6 영상 프롬프트")
        st.code(content["video_prompt"], language="text")

    with col2:
        st.subheader("📝 나레이션 대본")
        st.text_area("나레이션", content["narration"], height=260)

        st.subheader("📈 유튜브 메타데이터")
        st.text_area(
            "제목 / 해시태그 / 설명 / 고정 댓글",
            f"""[제목]\n{content['title']}\n\n[해시태그]\n{content['hashtags']}\n\n[영상 설명]\n{content['description']}\n\n[고정 댓글]\n{content['pinned_comment']}""",
            height=320,
        )

    st.subheader("🧩 JSON 출력 (기존 구조 유지)")
    st.json(content)
else:
    st.info("채널을 선택하고 장기 이름을 입력하면 콘텐츠 팩이 생성됩니다.")
