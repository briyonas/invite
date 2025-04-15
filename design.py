from PIL import Image, ImageDraw, ImageFont

def render_card(template_path, output_path, text_elements, font_paths, rtl=False):
    img = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    for item in text_elements:
        font = ImageFont.truetype(font_paths[item['lang']], item['size'])
        text = item['text'][::-1] if rtl else item['text']
        draw.text(item['pos'], text, font=font, fill=item['color'])

    img.save(output_path)