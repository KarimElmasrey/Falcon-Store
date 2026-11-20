# -*- coding: utf-8 -*-
"""
====================================================================
بوت متجر Falcon Store الذكي - بلغة بايثون بالكامل (Pure Python)
الأقسام: رجالي • حريمي • كوتشات • إكسسوارات
====================================================================
طريقة التشغيل:
1. تثبيت المكتبات المطلوبة:
   pip install flask flask-cors

2. ضبط مفتاح Gemini API في متغيرات البيئة أو وضعه مباشرة:
   set GEMINI_API_KEY=your_api_key_here

3. تشغيل سيرفر البوت:
   python falcon_chatbot.py

4. ربطه بالموقع عبر سطر واحد في HTML:
   <script src="http://127.0.0.1:5001/widget.js" defer></script>
====================================================================
"""
import os
import re
import sys
import json
import uuid
import urllib.request
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)


class FalconStoreBot:
    """المحرك الذكي لبوت Falcon Store مكتوب بالكامل بلغة بايثون"""

    def __init__(self):
        # قاعدة بيانات الأقسام الأربعة والعروض الخاصة بكل قسم
        self.catalog = {
            "men": {
                "title": "قسم الرجالي",
                "short_name": "الرجالي",
                "size_guide": (
                    "مقاسات الرجالي متوفرة من M إلى XXL (تلبيس مظبوط وأوفرسايز)، "
                    "والبنطلون الكارجو من 30 إلى 38. ابعتلي وزنك وطولك أقولك مقاسك بالظبط."
                ),
                "fabric_info": (
                    "خامات الرجالي قطن مصري بيما 100% معالج ضد الوبرة والانكماش، "
                    "والبنطلون الكارجو خامة وتربروف عملية جداً."
                ),
                "best_seller": "أكثر قطعة مطلوبة في الرجالي هي (بنطلون كارجو وتربروف + تيشيرت أوفرسايز أسود).",
                "offers": [
                    {"title": "عرض الـ 2 تيشيرت أوفرسايز", "desc": "بـ 780 ج بدلاً من 900 ج"},
                    {"title": "باكدج الكاجوال (تيشيرت + بنطلون كارجو)", "desc": "بـ 950 ج بدلاً من 1100 ج"},
                    {"title": "باكدج الشتاء (هودي ميلتون + بنطلون كارجو)", "desc": "بـ 1250 ج بدلاً من 1400 ج + شحن مجاني"},
                ],
                "items": [
                    {
                        "id": "m1",
                        "keywords": ["تيشيرت", "تيرشيرت", "اوفرسايز", "اوفر سايز", "تي شيرت"],
                        "name": "تيشيرت أوفرسايز قطن بيما",
                        "price": 450,
                        "sizes": "M - L - XL - XXL",
                        "colors": "أسود، أبيض، بيج، زيتي",
                    },
                    {
                        "id": "m2",
                        "keywords": ["قميص", "قمصان", "اكسفورد"],
                        "name": "قميص كاجوال أكسفورد",
                        "price": 580,
                        "sizes": "M - L - XL - XXL",
                        "colors": "كحلي، لبني، أبيض",
                    },
                    {
                        "id": "m3",
                        "keywords": ["كارجو", "بنطلون رجالي", "وتربروف"],
                        "name": "بنطلون كارجو وتربروف 6 جيب",
                        "price": 650,
                        "sizes": "30 إلى 38",
                        "colors": "أسود، رمادي، بيج",
                    },
                    {
                        "id": "m4",
                        "keywords": ["هودي", "هوديز", "سويت شيرت", "سويتشيرت", "شتوي رجالي"],
                        "name": "هودي شتوي مبطن ميلتون",
                        "price": 750,
                        "sizes": "M - L - XL - XXL",
                        "colors": "أسود، هافان، رمادي",
                    },
                ],
            },
            "women": {
                "title": "قسم الحريمي",
                "short_name": "الحريمي",
                "size_guide": (
                    "مقاسات الحريمي من S إلى XXL، والشميز الكتان Free Size يلبس من 55 إلى 85 كجم مرتاح، "
                    "والجينز الوايد ليج من 28 إلى 36."
                ),
                "fabric_info": "خامات الحريمي كريب ناعم وكتان طبيعي طري على الجسم ومش بيشف ولا يكش مع الغسيل.",
                "best_seller": "أكثر قطعة مطلوبة في الحريمي هي (طقم الكارديجان الطويل + البيزك) و(الدريس الكاجوال الكريب).",
                "offers": [
                    {"title": "عرض الكاجوال (شميز كتان + جينز وايد ليج)", "desc": "بـ 1050 ج بدلاً من 1200 ج"},
                    {"title": "باكدج الشياكة (دريس كريب + شنطة كروس جلد)", "desc": "بـ 1150 ج بدلاً من 1310 ج"},
                    {"title": "عرض التوينز + شميز كتان", "desc": "بـ 1220 ج بدلاً من 1370 ج + شحن مجاني"},
                ],
                "items": [
                    {
                        "id": "w1",
                        "keywords": ["دريس", "دريسات", "فستان", "فساتين"],
                        "name": "دريس كاجوال كريب ناعم",
                        "price": 720,
                        "sizes": "S - M - L - XL",
                        "colors": "كشمير، أسود، بيج، موف",
                    },
                    {
                        "id": "w2",
                        "keywords": ["شميز", "شميزات", "بلوزه", "بلوزات", "كتان"],
                        "name": "شميز كتان أوفرسايز",
                        "price": 520,
                        "sizes": "Free Size (يلبس حتى 85 كجم)",
                        "colors": "أبيض، بيستاج، فوشيا",
                    },
                    {
                        "id": "w3",
                        "keywords": ["وايد ليج", "جينز حريمي", "هاي ويست"],
                        "name": "بنطلون جينز وايد ليج",
                        "price": 680,
                        "sizes": "28 إلى 36",
                        "colors": "أزرق ثلجي، أسود، كحلي",
                    },
                    {
                        "id": "w4",
                        "keywords": ["كارديجان", "توينز", "طقم حريمي"],
                        "name": "طقم كارديجان طويل + بيزك",
                        "price": 850,
                        "sizes": "M - L - XL - XXL",
                        "colors": "بيج×أبيض، أسود×هافان",
                    },
                ],
            },
            "sneakers": {
                "title": "قسم الكوتشات",
                "short_name": "الكوتشات",
                "size_guide": (
                    "مقاسات الكوتشات متوفرة من 37 لحد 45 (قالب مظبوط). "
                    "لو حابب تتأكد، قيس طول رجلك بالسنتيمتر واكتبهولي وهقولك المقاس الأوروبي بالظبط."
                ),
                "fabric_info": (
                    "الكوتشات بنعل طبي فوم مريح جداً للمشي الطويل والوقوف، "
                    "وشبك تهوية يمنع العرق، والكلاسيك جلد طري سهل التنضيف."
                ),
                "best_seller": "الأكثر مبيعاً في الكوتشات هو (كوتشي أبيض كلاسيك جلد - رجالي وحريمي) و(كوتشي ألترا رانينج).",
                "offers": [
                    {"title": "عرض الـ 2 كوتشي (اختار أي موديلين)", "desc": "بـ 1550 ج بدلاً من 1810 ج + شحن مجاني"},
                    {"title": "باكدج الجيم (كوتشي سبورت + تيشيرت أوفرسايز)", "desc": "بـ 1090 ج بدلاً من 1240 ج"},
                    {"title": "عرض الكلاسيك (كوتشي أبيض + طقم محفظة وحزام جلد)", "desc": "بـ 1220 ج بدلاً من 1370 ج"},
                ],
                "items": [
                    {
                        "id": "s1",
                        "keywords": ["رانينج", "بوست", "جري", "مشى", "مشي"],
                        "name": "كوتشي ألترا رانينج خفيف",
                        "price": 920,
                        "sizes": "40 إلى 45",
                        "colors": "أسود×أبيض، رمادي، كحلي",
                    },
                    {
                        "id": "s2",
                        "keywords": ["كوتشي ابيض", "كلاسيك جلد", "ابيض سادة"],
                        "name": "كوتشي أبيض كلاسيك جلد",
                        "price": 850,
                        "sizes": "37 إلى 44 (رجالي وحريمي)",
                        "colors": "أبيض سادة، أبيض×أخضر",
                    },
                    {
                        "id": "s3",
                        "keywords": ["تشانكي", "نعل عالي", "كوتشي حريمي", "كوتشي بناتي"],
                        "name": "كوتشي تشانكي نعل عالي",
                        "price": 890,
                        "sizes": "37 إلى 41",
                        "colors": "بيج×أبيض، روز",
                    },
                    {
                        "id": "s4",
                        "keywords": ["سبورت", "جيم", "رياضي"],
                        "name": "كوتشي سبورت جيم تهوية",
                        "price": 790,
                        "sizes": "41 إلى 45",
                        "colors": "أسود كامل، أسود×أحمر",
                    },
                ],
            },
            "accessories": {
                "title": "قسم الإكسسوارات",
                "short_name": "الإكسسوارات",
                "size_guide": "كل الساعات والنظارات مقاس موحد قابل للتعديل، والأحزمة الجلد بطول 125 سم بتتظبط على أي مقاس بسهولة.",
                "fabric_info": (
                    "المحافظ والأحزمة جلد طبيعي بقري 100% مبيقشرش، "
                    "الساعات ستانلس ستيل ضد الصدأ والمياه بضمان سنة، والنظارات عدسات Polarized UV400."
                ),
                "best_seller": "الأكثر طلباً في الإكسسوارات هو (بوكس المحفظة والحزام الجلد الطبيعي) و(الساعة الكلاسيك الستانلس).",
                "offers": [
                    {"title": "بوكس الهدايا VIP (ساعة + محفظة وحزام جلد + نظارة)", "desc": "بـ 1290 ج بدلاً من 1520 ج"},
                    {"title": "عرض الساعة الستانلس + النظارة الشمسية", "desc": "بـ 850 ج بدلاً من 1000 ج"},
                    {"title": "عرض البنات (شنطة كروس جلد + نظارة شمسية)", "desc": "بـ 820 ج بدلاً من 970 ج"},
                ],
                "items": [
                    {
                        "id": "a1",
                        "keywords": ["ساعه", "ساعات", "ستانلس"],
                        "name": "ساعة كلاسيك ستانلس ضد المياه",
                        "price": 620,
                        "sizes": "مقاس موحد (بعلبة فخمة)",
                        "colors": "فضي×أسود، ذهبي، أسود",
                    },
                    {
                        "id": "a2",
                        "keywords": ["نظاره", "نضاره", "نظارات", "نضارات", "شمسيه", "شمس"],
                        "name": "نظارة شمسية Polarized UV400",
                        "price": 380,
                        "sizes": "مقاس موحد",
                        "colors": "أسود، بني هافان",
                    },
                    {
                        "id": "a3",
                        "keywords": ["محفظه", "محافظ", "حزام", "احزمه", "جلد"],
                        "name": "طقم محفظة وحزام جلد طبيعي 100%",
                        "price": 520,
                        "sizes": "بوكس هدايا",
                        "colors": "أسود، بني جملي",
                    },
                    {
                        "id": "a4",
                        "keywords": ["شنطه", "شنط", "كروس", "حقيبه"],
                        "name": "شنطة كروس جلد مستورد",
                        "price": 590,
                        "sizes": "مقاس وسط عملي",
                        "colors": "أسود، بيج، هافان",
                    },
                ],
            },
        }

        # حفظ الجلسات وسياق المحادثة لكل عميل
        self.sessions = {}

    @staticmethod
    def normalize_digits(text: str) -> str:
        arabic_digits = "٠١٢٣٤٥٦٧٨٩"
        persian_digits = "۰۱۲۳۴۵۶۷۸۹"
        for i, d in enumerate(arabic_digits):
            text = text.replace(d, str(i))
        for i, d in enumerate(persian_digits):
            text = text.replace(d, str(i))
        return text

    def normalize_arabic(self, text: str) -> str:
        text = self.normalize_digits(str(text)).lower().strip()
        text = re.sub(r"[\u064B-\u065F\u0640]", "", text)
        text = re.sub(r"[أإآ]", "ا", text)
        text = re.sub(r"ة", "ه", text)
        text = re.sub(r"ى", "ي", text)
        text = re.sub(r"ؤ", "و", text)
        text = re.sub(r"ئ", "ي", text)
        text = re.sub(r"(.)\1{2,}", r"\1", text)
        return text

    def has_any(self, norm_text: str, words: list) -> bool:
        return any(self.normalize_arabic(w) in norm_text for w in words)

    def get_session(self, session_id: str) -> dict:
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "last_category": None,
                "last_intent": None,
                "offer_variant": 0,
            }
        return self.sessions[session_id]

    def detect_category(self, norm_text: str):
        if self.has_any(norm_text, ["رجال", "ولادي", "شبابي"]):
            return "men"
        if self.has_any(norm_text, ["حريم", "بنات", "نسائي", "سيدات"]):
            return "women"
        if self.has_any(norm_text, ["كوتش", "شوز", "جزمه", "جزم", "حذاء", "احذيه", "سنيكر"]):
            return "sneakers"
        if self.has_any(norm_text, ["اكسسوار", "اكسورات", "ساع", "نظار", "نضار", "محفظ", "حزام", "شنط", "سلاسل"]):
            return "accessories"
        return None

    def find_specific_product(self, norm_text: str):
        for cat_key, cat_data in self.catalog.items():
            for item in cat_data["items"]:
                if self.has_any(norm_text, item["keywords"]):
                    return item, cat_data["title"], cat_key
        return None, None, None

    def format_category_reply(self, cat_key: str, session: dict) -> dict:
        cat = self.catalog[cat_key]
        session["last_category"] = cat_key
        session["last_intent"] = f"cat_{cat_key}"

        lines = [f"✨ {cat['title']} في Falcon Store:"]
        for item in cat["items"]:
            lines.append(
                f"• {item['name']} — {item['price']} ج\n"
                f"  (المقاسات: {item['sizes']} | الألوان: {item['colors']})"
            )
        return {
            "reply": "\n".join(lines),
            "choices": [f"عروض {cat['short_name']}", f"مقاسات {cat['short_name']}", "الشحن"],
            "last_category": cat_key,
        }

    def format_category_offers(self, cat_key: str, session: dict) -> dict:
        cat = self.catalog[cat_key]
        session["last_intent"] = f"offers_{cat_key}"

        lines = [f"🎁 العروض الخاصة بـ {cat['title']}:"]
        for off in cat["offers"]:
            lines.append(f"🔥 {off['title']}: {off['desc']}")
        lines.append("💡 متاح أيضاً خصم 15% على أي قطعة فردية بكود FALCON15")

        return {
            "reply": "\n".join(lines),
            "choices": ["كل عروض المتجر", f"مقاسات {cat['short_name']}", "الشحن"],
            "last_category": cat_key,
        }

    def format_general_offers(self, session: dict) -> dict:
        session["last_intent"] = "offers_general"
        session["offer_variant"] = (session["offer_variant"] + 1) % 2

        if session["offer_variant"] == 1:
            reply_text = (
                "🔥 أقوى عروض Falcon Store في كل الأقسام:\n"
                "• عروض الكوتشات: أي 2 كوتشي بـ 1550 ج بدلاً من 1810 ج + شحن مجاني.\n"
                "• عروض الرجالي: تيشيرت أوفرسايز + بنطلون كارجو بـ 950 ج بدلاً من 1100 ج.\n"
                "• عروض الحريمي: دريس كريب + شنطة كروس جلد بـ 1150 ج بدلاً من 1310 ج.\n"
                "• عروض الإكسسوارات: بوكس (ساعة + محفظة وحزام جلد + نظارة) بـ 1290 ج."
            )
        else:
            reply_text = (
                "🎁 باكدجات التوفير وكوبونات الخصم:\n"
                "1. كود خصم 15% فوري: استخدم كود FALCON15 على أي طلب.\n"
                "2. عرض الأصحاب: عند طلب 3 قطع مختلفة بتحصل على خصم 250 ج + شحن مجاني.\n"
                "3. اختر القسم بالأسفل لعرض باكدجات التوفير الخاصة به:"
            )

        return {
            "reply": reply_text,
            "choices": ["عروض الكوتشات", "عروض الرجالي", "عروض الحريمي", "عروض الإكسسوارات"],
            "last_category": session["last_category"],
        }

    def get_response(self, message: str, session_id: str = "default") -> dict:
        session = self.get_session(session_id)
        clean_input = str(message).strip()
        n = self.normalize_arabic(clean_input)
        words = set(re.findall(r"\w+", n))

        mentioned_cat = self.detect_category(n)

        is_asking_offers = (
            self.has_any(
                n,
                ["عرض", "عروض", "الاعروض", "عروص", "خصم", "خصومات", "تخفيض", "تخفيضات", "كوبون", "برومو", "باكدج"],
            )
            or "اوفر" in words
        )
        is_asking_sizes = self.has_any(n, ["مقاس", "سايز", "يلبس", "طولي", "طولك", "وزني", "وزنك"])
        is_asking_fabrics = self.has_any(
            n,
            ["خامه", "خامات", "قماش", "قطن", "بيوبر", "تغسل", "انكماش", "بيكش", "جوده", "اصلي", "ضمان", "الوان", "لون"],
        )
        is_asking_recommend = self.has_any(
            n,
            ["رشح", "ترشيح", "تنصح", "الاكثر مبيعا", "اكتر مبيعا", "افضل", "احسن", "مبيع"],
        )

        # 1. العروض
        if is_asking_offers:
            if self.has_any(n, ["كل عروض المتجر", "عروض عامه"]):
                return self.format_general_offers(session)
            if mentioned_cat:
                session["last_category"] = mentioned_cat
                return self.format_category_offers(mentioned_cat, session)
            if session["last_category"] and session["last_intent"] != f"offers_{session['last_category']}":
                return self.format_category_offers(session["last_category"], session)
            return self.format_general_offers(session)

        # 2. السؤال عن قطعة محددة بالاسم
        prod, cat_title, prod_cat_key = self.find_specific_product(n)
        if prod and not is_asking_sizes and not is_asking_fabrics and not self.has_any(
            n, ["قسم الرجالي", "قسم الحريمي", "قسم الكوتشات", "قسم الاكسسوارات"]
        ):
            session["last_category"] = prod_cat_key
            short_cat = self.catalog[prod_cat_key]["short_name"]
            return {
                "reply": (
                    f"متوفر في {cat_title}:\n"
                    f"• المنتج: {prod['name']}\n"
                    f"• السعر: {prod['price']} ج\n"
                    f"• المقاسات: {prod['sizes']}\n"
                    f"• الألوان: {prod['colors']}"
                ),
                "choices": [f"عروض {short_cat}", f"مقاسات {short_cat}", "الشحن"],
                "last_category": prod_cat_key,
            }

        # 3. الأرقام: مقاسات الكوتشي أو مقاسات الملابس حسب الوزن
        nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", self.normalize_digits(clean_input))]
        if nums:
            shoe_cm = next((v for v in nums if 22 <= v <= 31), None)
            has_cm_word = bool(re.search(r"سم|سنت|رجل|قدم", n))
            if shoe_cm and (has_cm_word or session["last_category"] == "sneakers"):
                sizes_eu = [
                    (23.5, "37"), (24.2, "38"), (25.0, "39"), (25.8, "40"),
                    (26.5, "41"), (27.3, "42"), (28.0, "43"), (28.8, "44"),
                ]
                eu = next((size for limit, size in sizes_eu if shoe_cm <= limit), "45")
                return {
                    "reply": f"👟 لطول قدم {shoe_cm:g} سم، المقاس الأنسب في الكوتشات هو {eu} EU.",
                    "choices": ["كوتشات", "عروض الكوتشات"],
                    "last_category": "sneakers",
                }

            has_weight_word = bool(re.search(r"كيلو|كجم|وزن", n))
            weight = next((v for v in nums if 40 <= v <= 145), None)
            if weight and has_weight_word:
                if weight < 60:
                    size, pant = "S", "28-30"
                elif weight <= 73:
                    size, pant = "M", "30-32"
                elif weight <= 86:
                    size, pant = "L", "32-34"
                elif weight <= 98:
                    size, pant = "XL", "34-36"
                else:
                    size, pant = "XXL", "36-38"
                return {
                    "reply": (
                        f"📏 لوزن {int(weight)} كجم:\n"
                        f"• مقاس التيشيرتات والقمصان والدريسات الأنسب هو: {size}\n"
                        f"• مقاس البنطلون الأنسب هو: {pant}"
                    ),
                    "choices": ["رجالي", "حريمي"],
                    "last_category": session["last_category"],
                }

        # 4. سؤال عن المقاسات
        if is_asking_sizes:
            target_cat = mentioned_cat or session["last_category"]
            if target_cat and target_cat in self.catalog:
                cat = self.catalog[target_cat]
                return {
                    "reply": f"📏 مقاسات {cat['title']}:\n{cat['size_guide']}",
                    "choices": [cat["short_name"], f"عروض {cat['short_name']}"],
                    "last_category": target_cat,
                }
            return {
                "reply": (
                    "📏 دليل مقاسات Falcon Store:\n"
                    "• الملابس (رجالي وحريمي): متاحة من S حتى XXL (وبناطيل من 28 لـ 38). "
                    "اكتبلي وزنك بالكيلو وطولك بالسنتيمتر وهقولك مقاسك فوراً.\n"
                    "• الكوتشات: متاحة من مقاس 37 لـ 45 قالب مظبوط."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات"],
                "last_category": session["last_category"],
            }

        # 5. سؤال عن الخامات والألوان
        if is_asking_fabrics:
            target_cat = mentioned_cat or session["last_category"]
            if target_cat and target_cat in self.catalog:
                cat = self.catalog[target_cat]
                return {
                    "reply": f"✨ خامات وجودة {cat['title']}:\n{cat['fabric_info']}",
                    "choices": [cat["short_name"], f"عروض {cat['short_name']}"],
                    "last_category": target_cat,
                }
            return {
                "reply": (
                    "✨ خامات وضمان Falcon Store:\n"
                    "• الملابس: قطن مصري بيما 100% معالج ضد الوبرة والانكماش.\n"
                    "• الكوتشات: نعل طبي طري وخفيف جداً للمشي الطويل والجيم.\n"
                    "• الإكسسوارات: محافظ وأحزمة جلد طبيعي 100% وساعات ستانلس ضد المياه بضمان سنة."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        # 6. سؤال عن الترشيحات والأكثر مبيعاً
        if is_asking_recommend:
            target_cat = mentioned_cat or session["last_category"]
            if target_cat and target_cat in self.catalog:
                cat = self.catalog[target_cat]
                return {
                    "reply": f"⭐ ترشيحنا ليك في {cat['title']}:\n{cat['best_seller']}",
                    "choices": [f"عروض {cat['short_name']}", cat["short_name"]],
                    "last_category": target_cat,
                }
            return {
                "reply": (
                    "🎁 أفضل ترشيحات Falcon Store والأكثر مبيعاً:\n"
                    "• للشباب: تيشيرت أوفرسايز + بنطلون كارجو + كوتشي أبيض كلاسيك.\n"
                    "• للبنات: دريس كاجوال كريب أو طقم كارديجان + شنطة كروس.\n"
                    "• كهدية شيك: طقم محفظة وحزام جلد طبيعي ببوكس هدايا (520 ج) أو ساعة ستانلس (620 ج)."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        # 7. عرض قسم من الأقسام الأربعة
        if mentioned_cat:
            return self.format_category_reply(mentioned_cat, session)

        # 8. الأسعار والمنيو
        if self.has_any(
            n,
            ["سعر", "اسعار", "بكام", "تكلفه", "تمن", "ثمن", "رخيص", "غالي", "منيو", "كتالوج", "منتجات", "عندكم ايه", "بتبيعوا ايه"],
        ):
            if session["last_category"]:
                return self.format_category_reply(session["last_category"], session)
            return {
                "reply": (
                    "📋 ملخص أسعار Falcon Store:\n"
                    "• الرجالي: تيشيرتات (450 ج)، قمصان (580 ج)، بناطيل كارجو (650 ج)، هوديز (750 ج).\n"
                    "• الحريمي: شميزات كتان (520 ج), جينز وايد ليج (680 ج)، دريسات (720 ج)، أطقم كارديجان (850 ج).\n"
                    "• الكوتشات: تبدأ من 790 ج حتى 920 ج (مقاسات 37 لـ 45).\n"
                    "• الإكسسوارات: نظارات (380 ج)، طقم محفظة وحزام جلد (520 ج)، شنط (590 ج)، ساعات (620 ج)."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات", "إكسسوارات", "العروض"],
                "last_category": session["last_category"],
            }

        # 9. الشحن والتوصيل والدفع
        if self.has_any(
            n, ["شحن", "توصيل", "بيوصل", "دفع", "فيزا", "انستا", "فودافون كاش", "عند الاستلام", "معاينه", "محافظات", "كام يوم"]
        ):
            return {
                "reply": (
                    "🚚 الشحن والدفع في Falcon Store:\n"
                    "• مصاريف الشحن: 60 ج لجميع المحافظات (ومجاني للطلبات فوق 1500 ج).\n"
                    "• مدة التوصيل: من 2 إلى 4 أيام عمل لحد باب البيت.\n"
                    "• طرق الدفع: الدفع عند الاستلام (مع إمكانية فتح ومعاينة الأوردر قبل الدفع) أو فودافون كاش وإنستا باي."
                ),
                "choices": ["العروض", "رجالي", "حريمي", "كوتشات"],
                "last_category": session["last_category"],
            }

        # 10. الاستبدال والاسترجاع
        if self.has_any(n, ["استبدال", "استرجاع", "ترجيع", "تبديل", "مرتجع", "ضيق", "واسع"]):
            return {
                "reply": (
                    "🔄 سياسة الاستبدال والاسترجاع:\n"
                    "• تقدر تعاين الطلب مع المندوب قبل الدفع.\n"
                    "• متاح استبدال أو استرجاع خلال 14 يوم من الاستلام بشرط وجود التيكت وحالة المنتج الأصلية."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        # 11. العنوان والفروع
        if self.has_any(n, ["عنوان", "فرع", "فروع", "مكان", "فين", "مواعيد", "بتفتحوا", "فاتحين", "تليفون", "رقم", "واتس", "تواصل"]):
            return {
                "reply": (
                    "📍 فروع وتواصل Falcon Store:\n"
                    "• العنوان: القاهرة - مدينة نصر - شارع عباس العقاد (ومتاح شحن لجميع المحافظات).\n"
                    "• مواعيد العمل: يومياً من 11 صباحاً حتى 11 مساءً."
                ),
                "choices": ["رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        # 12. التحيات والشكر
        if self.has_any(n, ["سلام", "اهلا", "مرحبا", "ازيك", "صباح", "مساء", "الو", "هاي", "هلا", "عامل ايه"]):
            return {
                "reply": "أهلاً وسهلاً بيك في Falcon Store 👋 منورنا! تحب أفرجك على أقسام الملابس والكوتشات والإكسسوارات ولا تشوف عروض النهاردة؟",
                "choices": ["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        if self.has_any(n, ["شكرا", "تسلم", "ميرسي", "اشطا", "تمام", "حلو", "جميل", "ممتاز", "عاش"]):
            return {
                "reply": "العفو، تحت أمرك في أي وقت في Falcon Store ✨ لو حابب تسأل عن أي قطعة أو مقاس أنا معاك.",
                "choices": ["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"],
                "last_category": session["last_category"],
            }

        # 13. أي سؤال خارج البيانات المحلية يروح لـ Gemini
        return ask_gemini_fallback(clean_input, session_id, self)


# إنشاء نسخة رئيسية من البوت
bot = FalconStoreBot()


from google import genai
from google.genai import types

def ask_gemini_fallback(user_message: str, session_id: str, bot_instance: FalconStoreBot) -> dict:
    """دالة الاتصال بـ Gemini باستخدام مكتبة google-genai الرسمية"""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    load_dotenv(env_path)
    
    api_key = os.getenv("GEMINI_API_KEY")
    choices = ["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"]
    last_category = bot_instance.get_session(session_id).get("last_category")

    if not api_key:
        print("❌ تنبيه: مفتاح GEMINI_API_KEY غير موجود في ملف .env")
        return {
            "reply": "أهلاً بك في Falcon Store! أقدر أساعدك في معرفة تفاصيل المنتجات، الأسعار، العروض، والشحن.",
            "choices": choices,
            "last_category": last_category,
        }

    try:
        # تهيئة عميل جوجل بالطريقة الرسمية الصحيحة
        client = genai.Client(api_key=api_key.strip())
        
        system_text = (
            "أنت مساعد مبيعات ذكي ودود لمتجر ملابس واكسسوارات مصري اسمه Falcon Store. "
            "أجب بالعربية المصرية وبأسلوب شيك ومختصر. "
            "استخدم بيانات المتجر التالية كمرجع:\n"
            + json.dumps(bot_instance.catalog, ensure_ascii=False)
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash", # أو gemini-1.5-flash لو ظهرت مشكلة
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_text,
                temperature=0.4,
                max_output_tokens=400,
            )
        )

        reply_text = response.text.strip()
        if not reply_text:
            raise ValueError("Gemini returned an empty response")

        return {
            "reply": reply_text,
            "choices": choices,
            "last_category": last_category,
        }

    except Exception as e:
        print("❌ Gemini SDK Error:", e)
        return {
            "reply": "حصلت مشكلة أثناء الاتصال بالخدمة. تقدر تختار من الأقسام التالية للمساعدة:",
            "choices": ["رجالي", "حريمي", "كوتشات", "العروض"],
            "last_category": last_category,
        }

@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json() or {}
    message = data.get("message", "")
    session_id = data.get("session_id", str(uuid.uuid4()))
    
    result = bot.get_response(message, session_id)
    return jsonify(result)


@app.route("/widget.js", methods=["GET"])
def widget_js():
    api_url = "https://karimelmasrey.pythonanywhere.com/api/chat"
    
    js_code = f"""
(function() {{
  const API_URL = "{api_url}";
  const sessionId = "sess_" + Math.random().toString(36).substring(2, 9);

  const root = document.createElement("div");
  root.id = "falcon-chat-root";
  root.innerHTML = `
    <style>
      #falcon-chat-root {{
        --falcon-bg: #050816;
        --falcon-panel: #0b1224;
        --falcon-panel-2: #101a30;
        --falcon-cyan: #06c9e8;
        --falcon-pink: #ec4899;
        --falcon-text: #f8fafc;
        --falcon-muted: #94a3b8;
        --falcon-border: rgba(148, 163, 184, .18);
        font-family: Inter, Cairo, Arial, sans-serif;
        color: var(--falcon-text);
        position: fixed;
        right: 24px;
        bottom: 24px;
        z-index: 99999;
        direction: ltr;
      }}
      #falcon-chat-root * {{ box-sizing: border-box; }}
      #falcon-chat-root button,
      #falcon-chat-root input {{ font: inherit; }}
      #falcon-chat-root .falcon-launcher {{
        width: 64px; height: 64px; border: 0; border-radius: 22px;
        color: white; cursor: pointer; font-size: 25px;
        background: linear-gradient(120deg, var(--falcon-cyan), #6577dc 52%, var(--falcon-pink));
        box-shadow: 0 10px 34px rgba(6, 201, 232, .22), 0 8px 30px rgba(236, 72, 153, .18);
        transition: transform .2s ease, box-shadow .2s ease;
      }}
      #falcon-chat-root .falcon-launcher:hover {{
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 14px 38px rgba(6, 201, 232, .3), 0 10px 34px rgba(236, 72, 153, .25);
      }}
      #falcon-chat-root .falcon-window {{
        display: none; flex-direction: column;
        width: min(380px, calc(100vw - 28px));
        height: min(570px, calc(100vh - 112px));
        margin-bottom: 14px; overflow: hidden;
        border: 1px solid rgba(6, 201, 232, .28);
        border-radius: 22px;
        background: var(--falcon-bg);
        box-shadow: 0 22px 70px rgba(0, 0, 0, .48), 0 0 32px rgba(6, 201, 232, .08);
      }}
      #falcon-chat-root .falcon-window.is-open {{ display: flex; animation: falcon-pop .2s ease-out; }}
      @keyframes falcon-pop {{
        from {{ opacity: 0; transform: translateY(10px) scale(.98); }}
        to {{ opacity: 1; transform: translateY(0) scale(1); }}
      }}
      #falcon-chat-root .falcon-header {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 16px; background: linear-gradient(110deg, #071526, #151027);
        border-bottom: 1px solid var(--falcon-border);
      }}
      #falcon-chat-root .falcon-brand {{ display: flex; align-items: center; gap: 11px; }}
      #falcon-chat-root .falcon-logo {{
        width: 40px; height: 40px; display: grid; place-items: center;
        border-radius: 13px; font-size: 19px;
        background: linear-gradient(135deg, var(--falcon-cyan), #6875d9 55%, var(--falcon-pink));
      }}
      #falcon-chat-root .falcon-title {{
        margin: 0; font-size: 15px; font-weight: 800; letter-spacing: .2px;
      }}
      #falcon-chat-root .falcon-subtitle {{
        margin-top: 4px; color: var(--falcon-muted); font-size: 11px;
      }}
      #falcon-chat-root .falcon-online {{
        display: inline-block; width: 7px; height: 7px; border-radius: 50%;
        margin-right: 5px; background: #22c55e; box-shadow: 0 0 9px #22c55e;
      }}
      #falcon-chat-root .falcon-close {{
        border: 0; background: transparent; color: #cbd5e1;
        font-size: 22px; cursor: pointer; padding: 4px 7px;
      }}
      #falcon-chat-root .falcon-messages {{
        flex: 1; overflow-y: auto; padding: 16px 13px;
        background:
          radial-gradient(ellipse at top right, rgba(6, 201, 232, .055), transparent 48%),
          radial-gradient(ellipse at bottom left, rgba(236, 72, 153, .05), transparent 45%),
          var(--falcon-bg);
      }}
      #falcon-chat-root .falcon-message-row {{ display: flex; margin: 0 0 12px; }}
      #falcon-chat-root .falcon-message-row.user {{ justify-content: flex-end; }}
      #falcon-chat-root .falcon-bubble {{
        max-width: 86%; padding: 11px 13px; border-radius: 15px;
        font-size: 13px; line-height: 1.75; white-space: pre-wrap;
        overflow-wrap: anywhere;
      }}
      #falcon-chat-root .falcon-message-row.bot .falcon-bubble {{
        color: #e2e8f0; background: var(--falcon-panel-2);
        border: 1px solid var(--falcon-border); border-top-left-radius: 5px;
      }}
      #falcon-chat-root .falcon-message-row.user .falcon-bubble {{
        color: #fff; background: linear-gradient(115deg, #087f9b, #5966c8 58%, #b83d87);
        border-top-right-radius: 5px;
      }}
      #falcon-chat-root .falcon-typing {{ color: var(--falcon-muted); font-size: 12px; padding: 2px 5px 10px; }}
      #falcon-chat-root .falcon-chips {{
        display: flex; gap: 7px; overflow-x: auto; padding: 10px 12px;
        border-top: 1px solid var(--falcon-border); background: #080e1e;
      }}
      #falcon-chat-root .falcon-chip {{
        flex: 0 0 auto; border: 1px solid rgba(6, 201, 232, .3);
        color: #bceefa; background: rgba(6, 201, 232, .08);
        border-radius: 999px; padding: 7px 11px; font-size: 11px; cursor: pointer;
      }}
      #falcon-chat-root .falcon-chip:hover {{ background: rgba(236, 72, 153, .13); border-color: rgba(236, 72, 153, .5); }}
      #falcon-chat-root .falcon-form {{
        display: flex; gap: 8px; padding: 12px;
        background: #080e1e; border-top: 1px solid var(--falcon-border);
      }}
      #falcon-chat-root .falcon-input {{
        min-width: 0; flex: 1; color: white; outline: none;
        border: 1px solid #26344d; border-radius: 12px;
        background: #0d172a; padding: 11px 12px; font-size: 12px;
      }}
      #falcon-chat-root .falcon-input:focus {{ border-color: var(--falcon-cyan); box-shadow: 0 0 0 3px rgba(6, 201, 232, .1); }}
      #falcon-chat-root .falcon-send {{
        border: 0; border-radius: 12px; padding: 0 15px;
        color: white; font-weight: 700; cursor: pointer;
        background: linear-gradient(115deg, var(--falcon-cyan), #6675d9 55%, var(--falcon-pink));
      }}
      #falcon-chat-root .falcon-send:disabled {{ opacity: .55; cursor: wait; }}
      @media (max-width: 480px) {{
        #falcon-chat-root {{ right: 14px; bottom: 14px; }}
        #falcon-chat-root .falcon-window {{
          width: calc(100vw - 28px); height: min(68vh, 560px);
        }}
        #falcon-chat-root .falcon-launcher {{ width: 58px; height: 58px; border-radius: 19px; }}
      }}
    </style>

    <section class="falcon-window" id="falcon-window" aria-label="Falcon Shop chat">
      <header class="falcon-header">
        <div class="falcon-brand">
          <div class="falcon-logo">✦</div>
          <div>
            <p class="falcon-title"><span style="color:#06c9e8">Falcon</span> <span style="color:#ec4899">Shop</span></p>
            <div class="falcon-subtitle"><span class="falcon-online"></span>Shopping assistant</div>
          </div>
        </div>
        <button class="falcon-close" id="falcon-close" type="button" aria-label="Close chat">×</button>
      </header>
      <div class="falcon-messages" id="falcon-messages" aria-live="polite"></div>
      <div class="falcon-chips" id="falcon-chips"></div>
      <form class="falcon-form" id="falcon-form">
        <input class="falcon-input" id="falcon-input" type="text"
          placeholder="Ask about products, offers or sizes..." autocomplete="off" maxlength="1000" />
        <button class="falcon-send" id="falcon-send" type="submit">Send</button>
      </form>
    </section>
    <button class="falcon-launcher" id="falcon-launcher" type="button"
      aria-label="Open Falcon Shop chat" aria-expanded="false">✦</button>
  `;

  document.body.appendChild(root);

  const win = root.querySelector("#falcon-window");
  const launcher = root.querySelector("#falcon-launcher");
  const close = root.querySelector("#falcon-close");
  const messages = root.querySelector("#falcon-messages");
  const chips = root.querySelector("#falcon-chips");
  const form = root.querySelector("#falcon-form");
  const input = root.querySelector("#falcon-input");
  const sendButton = root.querySelector("#falcon-send");

  function addMessage(text, sender) {{
    const row = document.createElement("div");
    row.className = "falcon-message-row " + sender;
    const bubble = document.createElement("div");
    bubble.className = "falcon-bubble";
    bubble.textContent = String(text ?? "");
    row.appendChild(bubble);
    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
    return row;
  }}

  function renderChips(list) {{
    chips.replaceChildren();
    (Array.isArray(list) && list.length ? list : ["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"])
      .forEach((label) => {{
        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = "falcon-chip";
        chip.textContent = String(label);
        chip.addEventListener("click", () => sendMessage(String(label)));
        chips.appendChild(chip);
      }});
  }}

  async function sendMessage(rawText) {{
    const text = String(rawText || "").trim();
    if (!text || sendButton.disabled) return;

    addMessage(text, "user");
    input.value = "";
    sendButton.disabled = true;

    const typing = addMessage("Falcon is typing...", "bot");

    try {{
      const response = await fetch(API_URL, {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ message: text, session_id: sessionId }})
      }});

      if (!response.ok) throw new Error("HTTP " + response.status);
      const data = await response.json();
      typing.remove();
      addMessage(data.reply || "Sorry, I couldn't prepare a reply.", "bot");
      renderChips(data.choices);
    }} catch (error) {{
      typing.remove();
      addMessage("Couldn't connect to Falcon Shop right now. Please make sure the Python server is running.", "bot");
    }} finally {{
      sendButton.disabled = false;
      input.focus();
    }}
  }}

  launcher.addEventListener("click", () => {{
    const open = !win.classList.contains("is-open");
    win.classList.toggle("is-open", open);
    launcher.setAttribute("aria-expanded", String(open));
    if (open) input.focus();
  }});

  close.addEventListener("click", () => {{
    win.classList.remove("is-open");
    launcher.setAttribute("aria-expanded", "false");
  }});

  form.addEventListener("submit", (event) => {{
    event.preventDefault();
    sendMessage(input.value);
  }});

  addMessage("Welcome to Falcon Shop! 👋 Ask me about our collections, prices, sizes or offers.", "bot");
  renderChips(["Shop men", "Shop women", "Sneakers", "Accessories", "Offers"]);
}})();
"""
    return Response(js_code, mimetype="application/javascript")


if __name__ == "__main__":
    print("====================================================")
    print("Falcon Store Python Chatbot Server is running!")
    print("API Endpoint : http://127.0.0.1:5001/api/chat")
    print("Widget Script: http://127.0.0.1:5001/widget.js")
    print("====================================================")
    app.run(host="127.0.0.1", port=5001, debug=False)