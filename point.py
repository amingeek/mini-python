import random

memory = []

discussed_topics = []

# احساسات و پاسخ‌ها
emotion_responses = {
    "مثبت": ["چقدر عالی! تعریف کن بیشتر.", "این خیلی خوبه! خوشحال شدم.", "آفرین! ادامه بده."],
    "منفی": ["متاسفم اینو می‌شنوم. می‌خوای حرف بزنی؟", "نگران نباش، درست میشه.", "اگه کمکی ازم برمیاد بگو."],
    "خنثی": ["جالب بود، بیشتر بگو.", "خب، دیگه چی؟", "ادامه بده، گوش میدم."]
}

# موضوعات و پاسخ‌ها
topic_responses = {
    "ورزش": ["ورزش خیلی خوبه! چه ورزشی رو دوست داری؟", "ورزشکار حرفه‌ای هستی یا تفریحی؟"],
    "فیلم": ["فیلم چی دیدی آخرین بار؟", "چه سبک فیلمی رو دوست داری؟"],
    "موزیک": ["چه آهنگی گوش میدی؟", "خواننده مورد علاقت کیه؟"],
    "برنامه‌نویسی": ["با چه زبانی کار می‌کنی؟", "پروژه خاصی داری؟"]
}

# پاسخ‌های تصادفی برای سوالات
question_responses = [
    "سوال جالبیه! نظر خودت چیه؟",
    "بذار فکر کنم... شاید جوابش پیچیده باشه.",
    "خودت تا حالا بهش فکر کردی؟"
]

# عمومی
general_responses = [
    "عجب! بیشتر توضیح بده.",
    "جالبه! ادامه بده.",
    "گوش میدم، بگو."
]

def detect_emotion(text):
    mosbat = ['خوشحال', 'عالی', 'آفرین', 'خوب', 'مثبت', 'خوشا', 'عالیه', 'شاد']
    manfi = ['ناراحت', 'مشکل', 'بد', 'غمگین', 'استرس', 'نگران', 'درد', 'اندوه']
    for word in mosbat:
        if word in text:
            return "مثبت"
    for word in manfi:
        if word in text:
            return "منفی"
    return "خنثی"

def detect_topic(text):
    words = text.split()
    for word in words:
        if word in topic_responses:
            return word
    return None

def is_question(text):
    if '؟' in text or any(q in text for q in ['چرا', 'چطور', 'چی', 'کی', 'کجا', 'آیا']):
        return True
    return False

def generate_response(user_input):
    emotion = detect_emotion(user_input)
    topic = detect_topic(user_input)
    is_q = is_question(user_input)
    
    response = None
    
    if is_q:
        response = random.choice(question_responses)
    
    if not response and topic:
        if topic in discussed_topics:
            response = f"قبلاً درباره {topic} صحبت کردیم، میخوای بیشتر بگی؟ " + random.choice(topic_responses[topic])
        else:
            discussed_topics.append(topic)
            response = random.choice(topic_responses[topic])
    
    if not response:
        response = random.choice(emotion_responses.get(emotion, general_responses))
    
    if not response:
        response = random.choice(general_responses)
    
    return response

if __name__ == "__main__":
    while True:
        user_input = input("شما: ")
        if user_input.lower() == 'خروج':
            print("بات: خداحافظ!")
            break
        
        if user_input.lower() == 'تاریخچه':    
            print("--- مموری کامل ---")
            for msg in memory:
                print(msg)
                
        memory.append(f"کاربر: {user_input}")
        
        bot_response = generate_response(user_input)
        print("بات:", bot_response)
        
        memory.append(f"بات: {bot_response}")
