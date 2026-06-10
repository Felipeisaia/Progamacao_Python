import os
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Criar banco de dados local (SQLite) e garantir que a tabela exista
def init_db():
    # Use a separate connection for initialization; do not share connections between threads
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        telegram_id INTEGER PRIMARY KEY,
        username TEXT
    )
    """)
    conn.commit()
init_db()

async def start(update: Update, context: CallbackContext):
    telegram_id = update.message.from_user.id
    username = update.message.from_user.username

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    # Verifica se o usuário já está registrado
    cursor.execute("SELECT * FROM usuarios WHERE telegram_id = ?", (telegram_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO usuarios (telegram_id, username) VALUES (?, ?)", (telegram_id, username))
        conn.commit()
        print(f"✅ Novo usuário registrado: {username} ({telegram_id})")

    cursor.close()
    conn.close()

    keyboard = [
        [InlineKeyboardButton("💵 Meu Saldo", callback_data="saldo")],
        [InlineKeyboardButton("💰 Depositar Saldo", callback_data="depositar")],
        [InlineKeyboardButton("🛍️ Catálogo de Produtos", callback_data="catalogo")],
        [InlineKeyboardButton("📜 Histórico de Compras", callback_data="historico")],
        [InlineKeyboardButton("📄 Termos e Regras", callback_data="termos")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"👋 Olá, {username or 'cliente'}! Bem-vindo ao nosso bot de vendas.\n"
        "Escolha uma opção abaixo:",
        reply_markup=reply_markup
    )

def main():
    # Criar aplicação com o token
    app = Application.builder().token(TOKEN).build()

    # Registrar comando /start
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
