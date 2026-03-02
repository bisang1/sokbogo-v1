import json
import streamlit as st

st.set_page_config(page_title="채널별 건강 콘텐츠 생성기", page_icon="🫁", layout="wide")

st.title("🧪 채널별 유튜브 쇼츠 콘텐츠 생성기")
st.markdown("뉴트로 · 속보고 · 김앤리(연구소) 채널 규격으로 콘텐츠를 생성합니다.")
st.divider()

channel = st.selectbox("채널을 선택하세요", ["뉴트로", "속보고", "김앤리(연구소)"])
topic = st.text_input("주제(장기/건강 키워드)", placeholder="예: 심장, 폐, 장 건강")


def build_newtro_pack(subject: str) -> dict:
    image_prompt = f"""[NEWTRO Image Prompt]
Vertical 9:16, retro-futuristic medical toy set about {subject}, cinematic yet cute.
Two white cat hosts (pastel blue sweater+hat / pastel pink sweater+hat) guide the scene.
3D miniature clay diorama, toy world, strong tilt-shift macro look, educational mood.
Include one key organ mechanism and one practical lifestyle tip."""

    video_prompt = f"""[NEWTRO Kling 2.6 Prompt]
9:16 macro tracking shot through a retro-style clay lab focused on {subject}.
Strong tactile ASMR texture (tiny tools, clay taps, paper labels), shallow depth of field.
Two white cat hosts in pastel blue/pink outfits explain one mechanism and one easy habit."""

    narration = f"""오늘은 {subject}를 뉴트로 감성으로 빠르게 정리해볼게요.
핵심은 구조를 이해하고 생활 습관 한 가지를 바로 실천하는 것입니다.
{subject}의 기능은 몸의 균형 유지와 직결되며, 작은 이상도 누적되면 피로로 나타날 수 있어요.
오늘부터 물 섭취와 수면 시간을 일정하게 맞춰보세요.
작은 습관이 건강의 방향을 바꿉니다."""

    hashtags = f"#뉴트로 #건강정보 #{subject} #의학상식 #shorts"
    description = f"뉴트로 톤으로 {subject} 핵심을 1분 내로 요약합니다. 구조와 생활 습관 포인트를 함께 확인하세요."

    return {
        "channel": "뉴트로",
        "topic": subject,
        "image_prompt": image_prompt,
        "video_prompt": video_prompt,
        "narration": narration,
        "metadata": {
            "title": f"[뉴트로] {subject} 핵심 1분 요약",
            "hashtags": hashtags,
            "description": description,
            "pinned_comment": f"여러분의 {subject} 관리 루틴을 댓글로 공유해주세요!",
        },
    }


def build_sokbogo_pack(subject: str) -> dict:
    image_prompt = f"""[SOKBOGO Image Prompt]
Vertical 9:16 health briefing board centered on {subject}.
Two white cat hosts (pastel blue sweater+hat / pastel pink sweater+hat),
3D miniature clay diorama, toy world, strong tilt-shift effect, clean medical labeling.
Show symptom signal, cause clue, and one actionable prevention tip."""

    video_prompt = f"""[SOKBOGO Kling 2.6 Prompt]
Fast but clear 9:16 clay-diorama medical briefing on {subject}.
ASMR details: soft pointer taps, sticker placement sounds, gentle brush on clay textures.
Keep educational and practical with one immediate behavior change."""

    narration = f"""속보고 브리핑입니다.
{subject}는 우리 몸 신호와 밀접하게 연결됩니다.
핵심은 증상을 무시하지 않고 원인을 빠르게 확인하는 거예요.
오늘 실천할 한 가지는 가공식품 섭취를 줄이고 수분 섭취를 늘리는 것입니다.
지금의 작은 선택이 내일의 컨디션을 만듭니다."""

    hashtags = f"#속보고 #건강브리핑 #{subject} #건강정보 #shorts"
    description = f"속보고 포맷으로 {subject} 핵심 신호, 원인 단서, 실천 팁을 짧고 명확하게 전달합니다."

    return {
        "channel": "속보고",
        "topic": subject,
        "image_prompt": image_prompt,
        "video_prompt": video_prompt,
        "narration": narration,
        "metadata": {
            "title": f"[속보고] {subject} 건강 신호 브리핑",
            "hashtags": hashtags,
            "description": description,
            "pinned_comment": f"여러분이 느낀 {subject} 관련 변화가 있다면 댓글로 남겨주세요.",
        },
    }


def build_kimlee_pack(subject: str) -> dict:
    # 사용자 제공 Kim & Lee 이미지 템플릿 유지
    kimlee_image_prompt = f"""[DALL-E 3 Image Prompt]
Create a highly detailed 3D miniature clay diorama inside a toy-world laboratory showing a cross-section of the human {subject}, designed with strong tilt-shift photography.

Main Characters (fixed):
- A white cat wearing a pastel blue sweater and matching pastel blue hat.
- A white cat wearing a pastel pink sweater and matching pastel pink hat.
The cat couple are expert researchers and appear throughout the scene as protagonists.

Scientific Accuracy:
- Reflect accurate anatomical and physiological knowledge of the {subject}.
- Show educational labels for key structures and safe, practical health guidance cues.
- Keep visuals scientifically respectful and non-graphic.

Visual Composition:
- Vertical 9:16 layout for YouTube Shorts.
- Layered cutaway of the {subject}: outer protective tissue, functional inner tissue, and vascular/neural network.
- Tiny clay tools, microscopes, specimen trays, and diagnostic monitors around the cat couple.
- Rich handcrafted clay texture, finger-molded details, miniature props, soft ambient lab glow.
- Toy-world color palette with pastel accents and clean hospital lighting.

Style Keywords:
3D miniature clay diorama, toy world, tilt-shift macro, ultra-detailed, educational medical visualization, cinematic depth of field, high fidelity, 8k feel."""

    video_prompt = f"""[Kling 2.6 Video Prompt]
Vertical 9:16 cinematic macro video in a 3D miniature clay diorama toy world. A cross-section of a human {subject} fills the frame. Strong tilt-shift effect.

Fixed lead characters:
- White cat in pastel blue sweater and hat.
- White cat in pastel pink sweater and hat.
They act as an expert researcher couple, inspecting the {subject} with tiny diagnostic devices.

Direction:
- Start with a soft top-down reveal, then slow crane-down movement into the layered anatomy.
- Show tactile clay textures: matte clay skin, slightly glossy vascular lines, powdery pastel surfaces, tiny hand-crafted seams.
- Emphasize ASMR-like sensory moments: gentle brush strokes on clay tissue, subtle tapping of miniature tools, soft rustle of paper labels, tiny click sounds from lab devices.
- Include micro actions: sample tagging, marker tracing, gentle calibration of miniature scanners.

Medical integrity:
- Keep the anatomy of the {subject} educational and scientifically plausible.
- Present non-diagnostic wellness guidance text overlays in Korean.

Look and feel:
clean lab lighting, pastel toy-world palette, precise mini props, shallow depth of field, soothing but informative tone, ultra-detailed texture-driven cinematography."""

    narration = f"""{subject}를 60초 안에 정말 쉽게 설명해볼게요.
연구 단계에서는 {subject}의 핵심 구조가 어떤 역할을 맡는지 먼저 확인합니다.
메커니즘 단계에서는 이 구조들이 서로 신호를 주고받으며 균형을 유지하는 과정을 이해합니다.
균형이 흔들리면 피로감이나 불편감 같은 작은 신호가 먼저 나타날 수 있어요.
행동 한 가지, 오늘은 물 섭취량을 조금 더 늘려 {subject}의 부담을 줄여보세요.
작은 실천이 몸의 회복 리듬을 지키는 데 큰 도움이 됩니다.
김앤리 연구소였습니다."""

    hashtags = f"#김앤리 #연구소 #{subject} #건강정보 #임상병리 #shorts"
    description = (
        f"임상병리 지식 기반으로 {subject}를 60초 내 쉬운 언어로 설명합니다.\n"
        "연구 → 메커니즘 → 행동 1가지 구조로 핵심만 전달합니다."
    )

    return {
        "channel": "김앤리(연구소)",
        "topic": subject,
        "image_prompt": kimlee_image_prompt,
        "kimlee_image_prompt": kimlee_image_prompt,
        "video_prompt": video_prompt,
        "narration": narration,
        "metadata": {
            "title": f"[김앤리 연구소] {subject} 60초 핵심 설명",
            "hashtags": hashtags,
            "description": description,
            "pinned_comment": f"{subject} 관련해서 다음에 듣고 싶은 연구소 주제를 댓글로 남겨주세요!",
        },
    }


if topic:
    if channel == "뉴트로":
        content_pack = build_newtro_pack(topic)
    elif channel == "속보고":
        content_pack = build_sokbogo_pack(topic)
    else:
        content_pack = build_kimlee_pack(topic)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🖼️ 이미지 프롬프트")
        st.code(content_pack["image_prompt"], language="text")
        st.subheader("🎬 Kling 2.6 영상 프롬프트")
        st.code(content_pack["video_prompt"], language="text")

    with col2:
        st.subheader("📝 나레이션")
        st.text_area("narration", content_pack["narration"], height=280)
        st.subheader("📦 유튜브 메타데이터")
        st.text_area(
            "metadata",
            (
                f"[제목]\n{content_pack['metadata']['title']}\n\n"
                f"[해시태그]\n{content_pack['metadata']['hashtags']}\n\n"
                f"[영상 설명]\n{content_pack['metadata']['description']}\n\n"
                f"[고정 댓글]\n{content_pack['metadata']['pinned_comment']}"
            ),
            height=300,
        )

    st.subheader("🧾 JSON 출력")
    st.code(json.dumps(content_pack, ensure_ascii=False, indent=2), language="json")
    st.json(content_pack)
else:
    st.info("채널을 선택하고 주제를 입력하면 콘텐츠 패키지를 생성합니다.")
