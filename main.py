import os
from google import genai
from google.genai import types
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from openAI import call_openAI

# Load .env only in development
if os.getenv("ENV") != "production":
    from dotenv import load_dotenv

    load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Google Gemini Client initialization
client = genai.Client(api_key=GEMINI_API_KEY)


async def translate_text(text: str) -> str:
    """Uses Google Gemini API to translate text."""
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",
        config=types.GenerateContentConfig(
            system_instruction="You’re great at translating between Traditional Chinese and indonesian in a way that feels natural and easy to read, keeping the meaning, tone, and vibe just right for everyday conversation. Respond translated text only"
        ),
        contents=text,
    )
    return response.text


async def handle_message(update: Update, context: CallbackContext) -> None:
    """Processes incoming messages and translates them."""
    user_text = update.message.text
    print(user_text)
    translated_text = call_openAI(user_text)
    await update.message.reply_text(translated_text)


def main():
    """Starts the bot."""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register the handler for text messages that are not commands
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # Start polling to receive updates
    application.run_polling()


if __name__ == "__main__":
    main()
