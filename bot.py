print("Бот запущен")
 
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ====== КНОПКИ МЕНЮ ======
keyboard = [
    ["💳 Кредиты", "🏦 Депозиты"],
    ["💰 Карты", "📈 Инвестиции"],
    ["ℹ️ Помощь"]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ====== УМНЫЙ ОТВЕТ ======
def smart_answer(text: str):
    text = text.lower()

    # приветствия
    if any(x in text for x in ["привет", "салам", "hello"]):
        return "Привет 👋 Я финансовый бот. Выбери тему в меню."

    # ===== СНАЧАЛА ТОЧНЫЕ ВОПРОСЫ =====
    if "виды" in text and "кредит" in text:
        return "Есть: потребительский, ипотечный, автокредит и микрозайм."

    if ("закрыть" in text or "погасить" in text) and "кредит" in text:
        return "Лучше закрывать кредит досрочно — меньше переплата."

    # ===== ПОТОМ ОБЩИЕ =====
    if any(x in text for x in ["кредит", "займ", "деньги", "loan"]):
        return (
            "💳 Кредит — это деньги банка, которые нужно вернуть с процентами.\n"
            "Оформить можно онлайн через приложение банка."
        )

    if any(x in text for x in ["счет", "счёт", "account"]):
        return "🏦 Счёт можно открыть в банке или через мобильное приложение."

    if any(x in text for x in ["карта", "card"]):
        return "💰 Если карту украли — срочно заблокируйте её через приложение банка."

    if any(x in text for x in ["депозит", "вклад"]):
        return "🏦 Депозит — это вклад в банк под проценты."

    if any(x in text for x in ["инвест", "акции", "биржа"]):
        return "📈 Инвестиции — это вложение денег в акции, облигации или фонды."

    return "🤖 Я не понял вопрос. Выбери тему в меню или напиши проще."

# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет 👋 Я финансовый бот.\nВыбери тему ниже:",
        reply_markup=markup
    )

# ====== ОБРАБОТКА ======
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💳 Кредиты":
        await update.message.reply_text(
            "💳 Кредиты:\n"
            "- Что такое кредит\n"
            "- Виды кредитов\n"
            "- Как оформить\n"
            "- Как закрыть"
        )
        return

    if text == "🏦 Депозиты":
        await update.message.reply_text(
            "🏦 Депозиты:\n"
            "- Что такое депозит\n"
            "- Как открыть\n"
            "- Проценты по вкладу"
        )
        return

    if text == "💰 Карты":
        await update.message.reply_text(
            "💰 Карты:\n"
            "- Что делать если украли карту\n"
            "- Как оформить карту\n"
            "- Блокировка карты"
        )
        return

    if text == "📈 Инвестиции":
        await update.message.reply_text(
            "📈 Инвестиции:\n"
            "- Что это такое\n"
            "- Куда инвестировать новичку"
        )
        return

    if text == "ℹ️ Помощь":
        await update.message.reply_text(
            "Напиши вопрос или выбери кнопку.\n"
            "Я отвечаю про кредиты, депозиты, карты и инвестиции."
        )
        return

    answer = smart_answer(text)
    await update.message.reply_text(answer)

# ====== MAIN ======
def main():
    TOKEN = "8457425975:AAHKWwGiX7bs8-R5Wjn1MxDB_qeLfamaPMM"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
