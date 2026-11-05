import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

DIST_DIR = Path(r"d:\Users\jjjj\day04_incidentdb\distribution")
DIST_DIR.mkdir(parents=True, exist_ok=True)

def draw_cyber_grid(draw, width, height, cell_size=40, color=(18, 28, 48)):
    for x in range(0, width, cell_size):
        draw.line([(x, 0), (x, height)], fill=color, width=1)
    for y in range(0, height, cell_size):
        draw.line([(0, y), (width, y)], fill=color, width=1)

def draw_radial_glow(img, center_x, center_y, max_radius, start_color, end_color):
    draw = ImageDraw.Draw(img, "RGBA")
    # Draw concentric circles with decreasing alpha
    steps = 40
    for i in range(steps, 0, -1):
        r = int(max_radius * (i / steps))
        alpha = int(start_color[3] * (1 - (i / steps) ** 1.5))
        col = (start_color[0], start_color[1], start_color[2], alpha)
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=col)

def create_banner():
    width, height = 1280, 720
    img = Image.new("RGBA", (width, height), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)

    # 1. Subtle Cyber Grid
    draw_cyber_grid(draw, width, height, cell_size=32, color=(16, 26, 46, 255))

    # 2. Glowing Accents (Crimson Alert & Cyan Telemetry)
    draw_radial_glow(img, 200, 200, 350, (230, 57, 70, 70), (11, 15, 25, 0))
    draw_radial_glow(img, 1050, 450, 400, (0, 210, 211, 50), (11, 15, 25, 0))

    draw = ImageDraw.Draw(img)

    # 3. Decorative Frame & Border
    draw.rectangle([20, 20, width - 20, height - 20], outline=(40, 60, 90, 255), width=2)
    draw.rectangle([24, 24, width - 24, height - 24], outline=(20, 35, 60, 255), width=1)

    # Corner brackets
    corner_len = 25
    c_color = (255, 71, 87, 255)
    # Top-Left
    draw.line([(20, 20), (20 + corner_len, 20)], fill=c_color, width=4)
    draw.line([(20, 20), (20, 20 + corner_len)], fill=c_color, width=4)
    # Top-Right
    draw.line([(width - 20, 20), (width - 20 - corner_len, 20)], fill=c_color, width=4)
    draw.line([(width - 20, 20), (width - 20, 20 + corner_len)], fill=c_color, width=4)
    # Bottom-Left
    draw.line([(20, height - 20), (20 + corner_len, height - 20)], fill=c_color, width=4)
    draw.line([(20, height - 20), (20, height - 20 - corner_len)], fill=c_color, width=4)
    # Bottom-Right
    draw.line([(width - 20, height - 20), (width - 20 - corner_len, height - 20)], fill=c_color, width=4)
    draw.line([(width - 20, height - 20), (width - 20, height - 20 - corner_len)], fill=c_color, width=4)

    # Fonts
    try:
        font_huge = ImageFont.truetype("arialbd.ttf", 64)
        font_sub = ImageFont.truetype("arialbd.ttf", 26)
        font_body = ImageFont.truetype("arial.ttf", 20)
        font_mono = ImageFont.truetype("consola.ttf", 16)
        font_mono_bold = ImageFont.truetype("consolab.ttf", 17)
    except:
        font_huge = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_mono = ImageFont.load_default()
        font_mono_bold = ImageFont.load_default()

    # 4. Badge on Top
    draw.rounded_rectangle([70, 60, 310, 95], radius=6, fill=(230, 57, 70, 220))
    draw.text((85, 68), "CRITICAL ALERT GROUND-TRUTH", fill=(255, 255, 255), font=font_mono_bold)

    draw.rounded_rectangle([325, 60, 530, 95], radius=6, fill=(15, 30, 55, 240), outline=(0, 210, 211, 200), width=1)
    draw.text((340, 68), "2026 SRE & AI BENCHMARK", fill=(0, 210, 211), font=font_mono_bold)

    # 5. Main Title & Subtitle
    draw.text((70, 115), "INCIDENT DB", fill=(255, 255, 255), font=font_huge)
    draw.text((70, 195), "500+ Real Production Outages, Root-Cause Diffs & Runbooks", fill=(255, 107, 129), font=font_sub)
    draw.text((70, 235), "Curated postmortems from Cloudflare, AWS, GitLab, CrowdStrike, Netflix, Fastly & Meta.", fill=(164, 176, 190), font=font_body)

    # 6. Terminal Diff Card (Right Side)
    card_x, card_y, card_w, card_h = 670, 100, 550, 480
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=10, fill=(15, 20, 32, 245), outline=(50, 75, 110), width=2)
    
    # Terminal Title Bar
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + 40], radius=10, fill=(22, 30, 48, 255))
    draw.ellipse([card_x + 15, card_y + 14, card_x + 27, card_y + 26], fill=(255, 71, 87))
    draw.ellipse([card_x + 35, card_y + 14, card_x + 47, card_y + 26], fill=(255, 165, 2))
    draw.ellipse([card_x + 55, card_y + 14, card_x + 67, card_y + 26], fill=(46, 213, 115))
    draw.text((card_x + 85, card_y + 12), "incident_diff_viewer — INC-2024-CROWDSTRIKE-01", fill=(160, 180, 210), font=font_mono)

    # Terminal Code Lines
    terminal_lines = [
        ("[!] SYMPTOM LOGS [PAGE_FAULT_IN_NONPAGED_AREA]", (255, 71, 87)),
        ("KERNEL_SECURITY_CHECK_FAILURE (139) csagent.sys", (255, 165, 2)),
        ("FAILURE_BUCKET_ID: AV_R_INVALID_csagent!unknown", (170, 180, 200)),
        ("", (0, 0, 0)),
        ("[-] BREAKING CONFIG / UNCHECKED CHANNEL BUFFER:", (255, 71, 87)),
        ("    ChannelFile291 = LoadChannelPayload(offset=0x18);", (255, 120, 130)),
        ("    ExecuteValidation(ChannelFile291->Rules[21]); // NULL deref", (255, 120, 130)),
        ("", (0, 0, 0)),
        ("[+] REMEDIATION & BOUNDED VALIDATION PATCH:", (46, 213, 115)),
        ("    if (!ValidateChannelPayloadSanity(pChannel, size)) {", (100, 240, 160)),
        ("        LogKernelDiagnosticError(STATUS_INVALID_IMAGE_FORMAT);", (100, 240, 160)),
        ("        return STATUS_CANCELLED;", (100, 240, 160)),
        ("    }", (100, 240, 160)),
        ("", (0, 0, 0)),
        ("[*] RAG RUNBOOK: /rag_vault/windows_kernel/INC-2024.md", (0, 210, 211))
    ]

    ty = card_y + 55
    for line, col in terminal_lines:
        if line:
            draw.text((card_x + 20, ty), line, fill=col, font=font_mono)
        ty += 24

    # 7. Feature Badges (Bottom Left)
    features = [
        ("[x] 100% Census Audit Passed", (46, 213, 115)),
        ("[x] Zero Toy Stubs / Zero TODOs", (46, 213, 115)),
        ("[x] Structured JSONL + RAG Markdown", (0, 210, 211)),
        ("[x] Instant CLI Search Engine Included", (0, 210, 211)),
        ("[x] Compatible with LangChain / LlamaIndex", (255, 165, 2)),
    ]

    fy = 320
    for feat, col in features:
        draw.rectangle([70, fy, 74, fy + 24], fill=col)
        draw.text((85, fy + 2), feat, fill=(225, 235, 245), font=font_body)
        fy += 40

    # 8. Bottom Status Strip
    draw.rectangle([70, 580, 600, 640], fill=(16, 24, 40), outline=(35, 55, 85))
    draw.text((90, 595), "TIER-1 DEVOPS DATASET | COMMERCIAL PRO LICENSE AVAILABLE", fill=(120, 145, 180), font=font_mono_bold)

    final_img = img.convert("RGB")
    out_file = DIST_DIR / "incidentdb_banner_16x9.jpg"
    final_img.save(out_file, "JPEG", quality=95)
    print(f"[OK] Saved Banner: {out_file} ({width}x{height})")


def create_thumbnail():
    size = 800
    img = Image.new("RGBA", (size, size), (11, 15, 25, 255))
    draw = ImageDraw.Draw(img)

    # 1. Subtle Cyber Grid
    draw_cyber_grid(draw, size, size, cell_size=25, color=(16, 26, 46, 255))

    # 2. Glowing Accents
    draw_radial_glow(img, 400, 350, 380, (230, 57, 70, 75), (11, 15, 25, 0))
    draw_radial_glow(img, 400, 450, 300, (0, 210, 211, 40), (11, 15, 25, 0))

    draw = ImageDraw.Draw(img)

    # 3. Outer Border
    draw.rectangle([16, 16, size - 16, size - 16], outline=(50, 75, 110, 255), width=2)
    draw.rectangle([20, 20, size - 20, size - 20], outline=(255, 71, 87, 180), width=2)

    # Fonts
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 68)
        font_sub = ImageFont.truetype("arialbd.ttf", 26)
        font_badge = ImageFont.truetype("consolab.ttf", 18)
        font_item = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_item = ImageFont.load_default()

    # 4. Top Tag
    draw.rounded_rectangle([220, 60, 580, 100], radius=8, fill=(230, 57, 70, 230))
    draw.text((250, 70), "RAG DEVOPS VAULT 2026", fill=(255, 255, 255), font=font_badge)

    # 5. Core Branding
    draw.text((120, 140), "INCIDENT DB", fill=(255, 255, 255), font=font_title)
    draw.text((120, 225), "500+ Real Production Outages", fill=(255, 107, 129), font=font_sub)
    draw.text((120, 265), "Disaster Runbooks & Root-Cause Diffs", fill=(0, 210, 211), font=font_sub)

    # 6. Center Graphic / Metric Card
    card_x, card_y, card_w, card_h = 100, 330, 600, 300
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=12, fill=(16, 24, 40, 245), outline=(40, 65, 100), width=2)

    items = [
        ("• 500+ Verified Ground-Truth Postmortems", (255, 255, 255)),
        ("• Full Symptom Logs & Core Stack Diffs", (255, 165, 2)),
        ("• Automated Remediation & Hardening Patches", (46, 213, 115)),
        ("• Formatted RAG Vaults (LangChain / LlamaIndex)", (0, 210, 211)),
        ("• Zero Hallucinations / 100% Census Audited", (255, 71, 87))
    ]

    iy = card_y + 35
    for text, col in items:
        draw.text((card_x + 30, iy), text, fill=col, font=font_item)
        iy += 48

    # 7. Bottom Brand Seal
    draw.rounded_rectangle([150, 670, 650, 720], radius=8, fill=(25, 40, 65), outline=(0, 210, 211), width=1)
    draw.text((175, 685), "TIER-1 PRO DEVELOPER SUITE • $39", fill=(0, 210, 211), font=font_badge)

    final_img = img.convert("RGB")
    out_file = DIST_DIR / "incidentdb_thumb_1x1.jpg"
    final_img.save(out_file, "JPEG", quality=95)
    print(f"[OK] Saved Thumbnail: {out_file} ({size}x{size})")

if __name__ == "__main__":
    create_banner()
    create_thumbnail()
