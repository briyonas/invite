def translate_text(text, target_lang):
    # Dummy translations for demo purposes
    translations = {
        "hi": {
            "Aarav & Aisha": "आरव और आयशा",
            "5th May 2025": "5 मई 2025",
            "Taj Palace, New Delhi": "ताज पैलेस, नई दिल्ली",
            "RSVP: +91-9876543210": "आरएसवीपी: +91-9876543210"
        },
        "ar": {
            "Aarav & Aisha": "آراف وآيشا",
            "5th May 2025": "٥ مايو ٢٠٢٥",
            "Taj Palace, New Delhi": "قصر تاج، نيودلهي",
            "RSVP: +91-9876543210": "الرد: +91-9876543210"
        }
    }
    return translations.get(target_lang, {}).get(text, text)
