import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

client = Groq(api_key=GROQ_API_KEY)

def split_message(message, max_length=2000):
    return [message[i:i+max_length] for i in range(0, len(message), max_length)]


def generate_groq_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if bot.user.mention in message.content:
        prompt = message.content.replace(bot.user.mention, "").strip()
        
        response = generate_groq_response(prompt)
        
        response_parts = split_message(response)
        
        for part in response_parts:
            await message.channel.send(part)

bot.run(DISCORD_TOKEN)
