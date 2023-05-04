from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ اهلا عمࢪي  {}
ٴ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯
 📮 ¦ في بوت 📬 {} 
ٴ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯
🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @DEV_SAMIR
ٴ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [InlineKeyboardButton(text="⚜️¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton(" ⚜️¦ بدأ استخراج الكود ", callback_data="generate")],
        [
            InlineKeyboardButton("⚜️¦ كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("⚜️¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج جلسة
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**⚜️¦حـول البـوت** 

- بـوت استخـراج كـود تيرمكـس خـاص بســورس سيمو 

- قنـاة السـورس : @FTTUTY

جروب السورس : [جروب سورس سيمو](https://t.me/FTTUTT0)

استخدم البوت : 

»[Pyrogram](docs.pyrogram.org)
🕹
»[Python](www.python.org)

لغة البوت : [بايثون](www.python.org)

🇪🇬 ¦ المطور  : [᥉ ᥲ️ ꪔ Ꭵٍ ᖇ](https://t.me/DEV_SAMIR)
    """
