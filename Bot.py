from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import os

# دالة لمعالجة الأمر /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("مرحبًا! أرسل لي رابط فيديو من Instagram أو Facebook أو TikTok وسأحاول تحميله لك.")

# دالة لمعالجة الرسائل الواردة
def handle_message(update: Update, context: CallbackContext):
    url = update.message.text
    update.message.reply_text("جاري تحميل الفيديو...")

    try:
        # تحميل الفيديو باستخدام youtube-dl
        os.system(f"youtube-dl -o 'video.mp4' {url}")
        
        # إرسال الفيديو للمستخدم
        with open("video.mp4", "rb") as video:
            update.message.reply_video(video=video)
        
        # حذف الفيديو بعد الإرسال
        os.remove("video.mp4")
    except Exception as e:
        update.message.reply_text(f"حدث خطأ: {e}")

# الدالة الرئيسية لتشغيل البوت
def main():
    # استبدل YOUR_API_TOKEN بالرمز الذي حصلت عليه من BotFather
    updater = Updater("YOUR_API_TOKEN", use_context=True)
    
    # إضافة معالجات الأوامر والرسائل
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
