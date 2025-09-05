import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Speicherung: alle gesendeten Nachrichten + letzte Nachricht
saved_messages = {}   # message_id -> Message Objekt
last_message = None   # letzte gesendete Bot-Nachricht

# Prüffunktion: Nur Admins
def is_admin(interaction: discord.Interaction) -> bool:
    return interaction.user.guild_permissions.administrator


@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Slash Commands synchronisiert: {len(synced)}")
    except Exception as e:
        print(e)


# /send text:<Inhalt>
@bot.tree.command(name="send", description="Eine neue Bot-Nachricht senden")
@app_commands.describe(text="Der Inhalt der Nachricht")
async def send(interaction: discord.Interaction, text: str):
    global last_message

    if not is_admin(interaction):
        return await interaction.response.send_message("❌ Du bist kein Admin.", ephemeral=True)

    msg = await interaction.channel.send(text)
    saved_messages[msg.id] = msg
    last_message = msg
    await interaction.response.send_message(f"✅ Nachricht gesendet (ID: `{msg.id}`)", ephemeral=True)


# /edit [message_id] text:<neuer Inhalt>
@bot.tree.command(name="edit", description="Eine bestehende Bot-Nachricht bearbeiten")
@app_commands.describe(message_id="(Optional) Die ID der Nachricht", text="Neuer Inhalt")
async def edit(interaction: discord.Interaction, text: str, message_id: str = None):
    if not is_admin(interaction):
        return await interaction.response.send_message("❌ Du bist kein Admin.", ephemeral=True)

    try:
        msg = None
        if message_id:  # wenn eine ID übergeben wurde
            message_id = int(message_id)
            msg = saved_messages.get(message_id)
        else:  # sonst letzte Nachricht
            msg = last_message

        if not msg:
            return await interaction.response.send_message("❌ Nachricht nicht gefunden.", ephemeral=True)

        await msg.edit(content=text)
        await interaction.response.send_message(f"✅ Nachricht bearbeitet (ID: `{msg.id}`)", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"⚠️ Fehler: {e}", ephemeral=True)


# /delete [message_id]
@bot.tree.command(name="delete", description="Eine bestehende Bot-Nachricht löschen")
@app_commands.describe(message_id="(Optional) Die ID der Nachricht")
async def delete(interaction: discord.Interaction, message_id: str = None):
    global last_message

    if not is_admin(interaction):
        return await interaction.response.send_message("❌ Du bist kein Admin.", ephemeral=True)

    try:
        msg = None
        if message_id:  # wenn eine ID übergeben wurde
            message_id = int(message_id)
            msg = saved_messages.get(message_id)
        else:  # sonst letzte Nachricht
            msg = last_message

        if not msg:
            return await interaction.response.send_message("❌ Nachricht nicht gefunden.", ephemeral=True)

        await msg.delete()
        saved_messages.pop(msg.id, None)

        # Falls es die letzte Nachricht war → zurücksetzen
        if last_message and msg.id == last_message.id:
            last_message = None

        await interaction.response.send_message(f"🗑️ Nachricht gelöscht (ID: `{msg.id}`)", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"⚠️ Fehler: {e}", ephemeral=True)


import os
bot.run(os.getenv("DISCORD_TOKEN"))

