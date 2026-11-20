# -*- coding: utf-8 -*-
"""
====================================================================
بوت متجر Falcon Store الذكي - بلغة بايثون بالكامل (Pure Python)
الأقسام: رجالي • حريمي • كوتشات • إكسسوارات
====================================================================
"""
import os
import re
import json
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from google import genai
from google.genai import types

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
CORS(app)

BACKEND_BASE_URL = "https://karimelmasrey.pythonanywhere.com"


class FalconStoreBot:
    """المحرك الذكي لبوت Falcon Store مكتوب بالكامل بلغة بايثون"""

    def __init__(self):
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

        if is_asking_offers:
            if self.has_any(n, ["كل عروض المتجر", "عروض عامه"]):
                return self.format_general_offers(session)
            if mentioned_cat:
                session["last_category"] = mentioned_cat
                return self.format_category_offers(mentioned_cat, session)
            if session["last_category"] and session["last_intent"] != f"offers_{session['last_category']}":
                return self.format_category_offers(session["last_category"], session)
            return self.format_general_offers(session)

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

        if mentioned_cat:
            return self.format_category_reply(mentioned_cat, session)

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

        return ask_gemini_fallback(clean_input, session_id, self)


bot = FalconStoreBot()


def ask_gemini_fallback(user_message: str, session_id: str, bot_instance: FalconStoreBot) -> dict:
    """دالة الاتصال بـ Gemini باستخدام مكتبة google-genai الرسمية"""
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    api_key = os.getenv("GEMINI_API_KEY")
    choices = ["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"]
    last_category = bot_instance.get_session(session_id).get("last_category")

    if not api_key:
        return {
            "reply": "أهلاً بك في Falcon Store! أقدر أساعدك في معرفة تفاصيل المنتجات، الأسعار، العروض، والشحن.",
            "choices": choices,
            "last_category": last_category,
        }

    try:
        client = genai.Client(api_key=api_key.strip())
        system_text = (
            "أنت مساعد مبيعات ذكي ودود لمتجر ملابس واكسسوارات مصري اسمه Falcon Store. "
            "أجب بالعربية المصرية وبأسلوب شيك ومختصر. "
            "استخدم بيانات المتجر التالية كمرجع:\n"
            + json.dumps(bot_instance.catalog, ensure_ascii=False)
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_text,
                temperature=0.4,
                max_output_tokens=400,
            ),
        )

        reply_text = (response.text or "").strip()
        if not reply_text:
            raise ValueError("Gemini returned an empty response")

        return {
            "reply": reply_text,
            "choices": choices,
            "last_category": last_category,
        }

    except Exception as e:
        print("Gemini SDK Error:", e)
        return {
            "reply": "حصلت مشكلة أثناء الاتصال بالخدمة حالياً. تقدر تختار من الأقسام التالية للمساعدة:",
            "choices": ["رجالي", "حريمي", "كوتشات", "العروض"],
            "last_category": last_category,
        }


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "service": "Falcon Store Chatbot API"})


@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    session_id = data.get("session_id") or str(uuid.uuid4())
    result = bot.get_response(message, session_id)
    return jsonify(result)


@app.route("/widget.js", methods=["GET"])
def widget_js():
    api_url = f"{BACKEND_BASE_URL}/api/chat"

    js_code = f"""
(function() {{
  const API_URL = "{api_url}";
  const sessionId = "sess_" + Math.random().toString(36).substring(2, 10);

  if (document.getElementById("falcon-chat-root")) return;

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
        font-family: Inter, Cairo, Arial, sans-serif;
        color: var(--falcon-text);
        position: fixed;
        right: 24px;
        bottom: 24px;
        z-index: 99999;
        direction: rtl;
      }}
      #falcon-chat-root * {{ box-sizing: border-box; }}
      #falcon-chat-root button,
      #falcon-chat-root input {{ font: inherit; }}
      #falcon-chat-root .falcon-launcher {{
        width: 64px; height: 64px; border: 0; border-radius: 22px;
        color: #fff; cursor: pointer; font-size: 25px;
        background: linear-gradient(120deg, var(--falcon-cyan), #6577dc 52%, var(--falcon-pink));
        box-shadow: 0 10px 34px rgba(6, 201, 232, .22), 0 8px 30px rgba(236, 72, 153, .18);
        transition: transform .2s ease, box-shadow .2s ease;
        display: flex; align-items: center; justify-content: center;
      }}
      #falcon-chat-root .falcon-launcher:hover {{
        transform: translateY(-3px) scale(1.03);
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
      #falcon-chat-root .falcon-window.is-open {{
        display: flex;
        animation: falcon-pop .2s ease-out;
      }}
      @keyframes falcon-pop {{
        from {{ opacity: 0; transform: translateY(10px) scale(.98); }}
        to {{ opacity: 1; transform: translateY(0) scale(1); }}
      }}
      #falcon-chat-root .falcon-header {{
        padding: 14px 16px;
        background: var(--falcon-panel);
        border-bottom: 1px solid rgba(148, 163, 184, .16);
        display: flex; align-items: center; justify-content: space-between;
      }}
      #falcon-chat-root .falcon-title {{
        font-weight: 700; font-size: 15px;
      }}
      #falcon-chat-root .falcon-sub {{
        font-size: 12px; color: var(--falcon-muted);
      }}
      #falcon-chat-root .falcon-close {{
        background: transparent; border: 0; color: var(--falcon-muted);
        font-size: 20px; cursor: pointer; padding: 4px 8px;
      }}
      #falcon-chat-root .falcon-messages {{
        flex: 1; overflow-y: auto; padding: 14px;
        display: flex; flex-direction: column; gap: 10px;
      }}
      #falcon-chat-root .falcon-msg {{
        max-width: 85%; padding: 10px 13px; border-radius: 15px;
        font-size: 13.5px; line-height: 1.55; white-space: pre-line;
      }}
      #falcon-chat-root .falcon-msg.bot {{
        align-self: flex-start;
        background: var(--falcon-panel-2);
        border: 1px solid rgba(148, 163, 184, .14);
      }}
      #falcon-chat-root .falcon-msg.user {{
        align-self: flex-end;
        background: linear-gradient(120deg, #0891b2, #6366f1);
        color: #fff;
      }}
      #falcon-chat-root .falcon-choices {{
        display: flex; flex-wrap: wrap; gap: 6px; padding: 0 14px 10px;
      }}
      #falcon-chat-root .falcon-choice-btn {{
        background: var(--falcon-panel-2); color: var(--falcon-cyan);
        border: 1px solid rgba(6, 201, 232, .35); border-radius: 999px;
        padding: 5px 11px; font-size: 12px; cursor: pointer;
      }}
      #falcon-chat-root .falcon-choice-btn:hover {{
        background: rgba(6, 201, 232, .14);
      }}
      #falcon-chat-root .falcon-input-row {{
        display: flex; gap: 8px; padding: 12px;
        background: var(--falcon-panel);
        border-top: 1px solid rgba(148, 163, 184, .16);
      }}
      #falcon-chat-root .falcon-input {{
        flex: 1; background: var(--falcon-bg); color: var(--falcon-text);
        border: 1px solid rgba(148, 163, 184, .25);
        border-radius: 12px; padding: 9px 12px; font-size: 13.5px; outline: none;
      }}
      #falcon-chat-root .falcon-send {{
        background: var(--falcon-cyan); color: #050816; font-weight: 700;
        border: 0; border-radius: 12px; padding: 0 14px; cursor: pointer;
      }}
    </style>

    <div class="falcon-window" id="falcon-window">
      <div class="falcon-header">
        <div>
          <div class="falcon-title">مساعد Falcon Store</div>
          <div class="falcon-sub">متاح للمساعدة • رجالي، حريمي، كوتشات، إكسسوارات</div>
        </div>
        <button type="button" class="falcon-close" id="falcon-close" aria-label="إغلاق">✕</button>
      </div>
      <div class="falcon-messages" id="falcon-messages"></div>
      <div class="falcon-choices" id="falcon-choices"></div>
      <form class="falcon-input-row" id="falcon-form">
        <input type="text" class="falcon-input" id="falcon-input" placeholder="اكتب سؤالك هنا..." autocomplete="off" />
        <button type="submit" class="falcon-send">إرسال</button>
      </form>
    </div>

    <button type="button" class="falcon-launcher" id="falcon-launcher" aria-label="فتح المحادثة">💬</button>
  `;

  document.body.appendChild(root);

  const winEl = document.getElementById("falcon-window");
  const launcherEl = document.getElementById("falcon-launcher");
  const closeEl = document.getElementById("falcon-close");
  const msgsEl = document.getElementById("falcon-messages");
  const choicesEl = document.getElementById("falcon-choices");
  const formEl = document.getElementById("falcon-form");
  const inputEl = document.getElementById("falcon-input");

  function addMsg(text, sender) {{
    const div = document.createElement("div");
    div.className = "falcon-msg " + sender;
    div.textContent = text;
    msgsEl.appendChild(div);
    msgsEl.scrollTop = msgsEl.scrollHeight;
  }}

  function renderChoices(list) {{
    choicesEl.innerHTML = "";
    if (!Array.isArray(list)) return;
    list.forEach((label) => {{
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "falcon-choice-btn";
      btn.textContent = label;
      btn.addEventListener("click", () => sendMessage(label));
      choicesEl.appendChild(btn);
    }});
  }}

  async function sendMessage(text) {{
    const clean = (text || "").trim();
    if (!clean) return;
    addMsg(clean, "user");
    inputEl.value = "";
    renderChoices([]);

    const typingDiv = document.createElement("div");
    typingDiv.className = "falcon-msg bot";
    typingDiv.textContent = "جاري الكتابة...";
    msgsEl.appendChild(typingDiv);
    msgsEl.scrollTop = msgsEl.scrollHeight;

    try {{
      const res = await fetch(API_URL, {{
        method: "POST",
        headers: {{ "Content-Type": "application/json" }},
        body: JSON.stringify({{ message: clean, session_id: sessionId }})
      }});
      const data = await res.json();
      typingDiv.remove();
      addMsg(data.reply || "تم استلام رسالتك.", "bot");
      renderChoices(data.choices);
    }} catch (err) {{
      typingDiv.remove();
      addMsg("تعذر الاتصال بالسيرفر الآن، حاول مرة أخرى.", "bot");
    }}
  }}

  launcherEl.addEventListener("click", () => {{
    winEl.classList.toggle("is-open");
    if (winEl.classList.contains("is-open") && msgsEl.children.length === 0) {{
      addMsg("أهلاً بك في Falcon Store! كيف أقدر أساعدك اليوم؟", "bot");
      renderChoices(["العروض", "رجالي", "حريمي", "كوتشات", "إكسسوارات"]);
    }}
  }});

  closeEl.addEventListener("click", () => {{
    winEl.classList.remove("is-open");
  }});

  formEl.addEventListener("submit", (e) => {{
    e.preventDefault();
    sendMessage(inputEl.value);
  }});
}})();
"""
    return Response(js_code, mimetype="application/javascript")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)