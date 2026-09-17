import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ChatMemberHandler,
    ContextTypes,
    filters,
)

WELCOME = """🌹 Welcome to Our Group! 🌹

👋 হ্যালো {user}, আমাদের গ্রুপে স্বাগতম! 🎉

📌 Rules:
🤝 সবাইকে সম্মান করুন
🚫 Spam/Scam থেকে বিরত থাকুন
👮 Admin-এর নির্দেশনা মেনে চলুন

👑 Admins:
@Himel_NH • @Munna6844 • @darkXhunter

🌟 Enjoy the group! ❤️
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌹 Hello! আমি তোমাদের Group Management Bot.\n\n"
        "Commands:\n"
        "/rules - Group rules\n"
        "/id - Your Telegram ID"
    )


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Group Rules\n\n"
        "🤝 সবাইকে সম্মান করুন\n"
        "🚫 Spam/Scam করবেন না\n"
        "🔗 অনুমতি ছাড়া link শেয়ার করবেন না\n"
        "👮 Admin-এর নির্দেশনা মেনে চলুন"
    )


async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 Your Telegram ID: `{update.effective_user.id}`",
        parse_mode="Markdown"
    )


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = update.chat_member

    if chat_member.new_chat_member.status == "member":
        user = chat_member.new_chat_member.user

        mention = user.mention_html()

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=WELCOME.format(user=mention),
            parse_mode="HTML"
        )


async def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("id", user_id))

    app.add_handler(
        ChatMemberHandler(
            welcome,
            ChatMemberHandler.CHAT_MEMBER
        )
    )

    print("Bot is running...")
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
