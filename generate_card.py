from design import render_card
from translate import translate_text
import os

languages = {
    "en": {"font": "fonts/Roboto-Regular.ttf", "rtl": False},
    "hi": {"font": "fonts/NotoSansDevanagari-Regular.ttf", "rtl": False},
    "ar": {"font": "fonts/NotoSansArabic-Regular.ttf", "rtl": True},
}

template_path = "templates/traditional_template.png"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

base_text = {
    "names": "Aarav & Aisha",
    "date": "5th May 2025",
    "venue": "Taj Palace, New Delhi",
    "rsvp": "RSVP: +91-9876543210",
}

for lang, config in languages.items():
    text_elements = []
    for key, text in base_text.items():
        translated = translate_text(text, lang) if lang != "en" else text
        text_elements.append({
            "text": translated,
            "lang": lang,
            "size": 48 if key == "names" else 36,
            "color": "black",
            "pos": (100, 100 + 80 * list(base_text.keys()).index(key))
        })

    output_path = os.path.join(output_folder, f"invitation_{lang}.png")
    render_card(template_path, output_path, text_elements, 
                {lang: config['font'] for lang in languages}, 
                rtl=config['rtl'])
