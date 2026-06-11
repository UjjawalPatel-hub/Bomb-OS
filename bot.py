from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import json
from datetime import date

TOKEN = "8630810659:AAH27QFfpoyeaarwnHEmd3MVZFg039_l6Fs"

motivations = [
    "Discipline beats motivation.",
    "Small steps every day create massive results.",
    "Focus on progress, not perfection.",
    "Your future is created by what you do today.",
    "Stay consistent. Success follows."
]
def load_data():
    try:
        with open("user_data.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open("user_data.json", "w") as file:
        json.dump(data, file, indent=4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to BomBrain AI!\n\n"
        "Available Commands:\n"
        "/help\n"
        "/motivation\n"
        "/goal\n"
        "/setgoal\n"
        "/mygoal\n"
        "/checkin\n"
        "/level\n"
        "/profile\n"
        "/roadmap\n"
        "/english\n"
        "/about" 
        
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
       "/help\n"
       "/motivation\n"
       "/goal\n"
       "/setgoal\n"
       "/mygoal\n"
       "/checkin\n"
       "/level\n"
       "/profile\n"
       "/roadmap\n"
       "/english\n"
       "/about" 
    )

async def motivation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(motivations))

async def goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 Today's BOMB Mission:\n\n"
        "✅ 1 hour coding\n"
        "✅ 10 new English words\n"
        "✅ 30 min AI learning\n"
        "✅ No mindless scrolling"
    )
async def setgoal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if not context.args:
        await update.message.reply_text(
            "❌ Usage:\n/setgoal Your Goal"
        )
        return

    goal = " ".join(context.args)

    data = load_data()
    data[user_id] = {
    "goal": goal,
    "xp": 0,
    "streak":0,
    "last_checkin": ""

}
    save_data(data)

    await update.message.reply_text(
        f"✅ Goal Saved!\n\n🎯 {goal}"
    )

async def mygoal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    data = load_data()

    if user_id in data:
        goal = data[user_id]["goal"]

        await update.message.reply_text(
            f"🎯 Your Goal:\n\n{goal}"
        )
    else:
        await update.message.reply_text(
            "❌ No goal found.\nUse /setgoal first."
        )

    data = load_data()
async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    data = load_data()

    if user_id not in data:
        await update.message.reply_text(
            "❌ First set a goal using /setgoal"
        )
        return

    data.setdefault(user_id, {})
    data[user_id].setdefault("xp", 0)
    data[user_id].setdefault("streak", 0)
    data[user_id].setdefault("last_checkin", "")

    from datetime import date
    today = str(date.today())

    if data[user_id]["last_checkin"] == today:
        await update.message.reply_text(
            "⚠️ You already checked in today.\nCome back tomorrow!"
        )
        return

    data[user_id]["last_checkin"] = today
    data[user_id]["xp"] += 10
    data[user_id]["streak"] += 1

    save_data(data)

    xp = data[user_id]["xp"]
    streak = data[user_id]["streak"]
    level = xp // 50 + 1

    await update.message.reply_text(
        f"🔥 Daily Check-in Complete!\n\n"
        f"⭐ XP: {xp}\n"
        f"🏆 Level: {level}\n"
        f"🔥 Streak: {streak} Days\n"
        f"+10 XP Earned"
    )

async def level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    data = load_data()

    if user_id not in data:
        await update.message.reply_text(
            "❌ First set a goal using /setgoal"
        )
        return

    xp = data[user_id]["xp"]
    level_num = xp // 50 + 1

    await update.message.reply_text(
        f"🏆 Your Level: {level_num}\n"
        f"⭐ XP: {xp}"
    )
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    data = load_data()

    if user_id not in data:
        await update.message.reply_text(
            "❌ First set a goal using /setgoal"
        )
        return

    goal = data[user_id]["goal"]
    xp = data[user_id]["xp"]
    streak = data[user_id]["streak"]

    level_num = xp // 50 + 1

    await update.message.reply_text(
        f"👤 BomBrain Profile\n\n"
        f"🎯 Goal: {goal}\n"
        f"⭐ XP: {xp}\n"
        f"🏆 Level: {level_num}\n"
        f"🔥 Streak: {streak} Days"
    )
   
english_words = [
    ("Consistency", "लगातार प्रयास"),
    ("Discipline", "अनुशासन"),
    ("Growth", "विकास"),
    ("Focus", "ध्यान"),
    ("Opportunity", "अवसर")
]

async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 AI & Analytics Roadmap\n\n"
        "1️⃣ Python\n"
        "2️⃣ SQL\n"
        "3️⃣ Pandas & NumPy\n"
        "4️⃣ Data Analysis Projects\n"
        "5️⃣ Machine Learning\n"
        "6️⃣ Git & GitHub\n"
        "7️⃣ Internships\n"
        "8️⃣ Advanced AI"
    )

async def english(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word, meaning = random.choice(english_words)
    await update.message.reply_text(
        f"📚 English Word of the Day\n\n"
        f"Word: {word}\n"
        f"Meaning: {meaning}"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BomBrain AI\n\n"
        "A student growth assistant built under Project BOMB.\n"
        "Mission: Help students learn AI, coding, English and career skills."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("motivation", motivation))
app.add_handler(CommandHandler("goal", goal))
app.add_handler(CommandHandler("roadmap", roadmap))
app.add_handler(CommandHandler("english", english))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("setgoal", setgoal))
app.add_handler(CommandHandler("mygoal", mygoal))
app.add_handler(CommandHandler("checkin", checkin))
app.add_handler(CommandHandler("level", level))
app.add_handler(CommandHandler("profile", profile))
print("🤖 BomBrain AI is running...")

app.run_polling()
