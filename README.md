# Discord Message Bot ✉️🤖

Ein Discord-Bot, der als **gemeinsamer Account** dient, um Nachrichten zentral über den Bot zu senden, zu bearbeiten oder zu löschen.
So können **Admins gemeinsam** an großen Texten arbeiten oder serverweite Informationen konsistent verwalten.

---

## 🚀 Features

* `/send <text>` → sendet eine neue Nachricht über den Bot
* `/edit [message_id] <text>` → bearbeitet entweder die letzte gesendete Nachricht oder eine bestimmte Nachricht per ID
* `/delete [message_id]` → löscht entweder die letzte gesendete Nachricht oder eine bestimmte Nachricht per ID
* Nur **Admins** können diese Befehle nutzen
* Nachrichten werden zentral über den Bot verwaltet → alle Admins können Nachrichten von allen Admins editieren/löschen

---

## ⚙️ Installation

### Voraussetzungen

* Python **3.8+**
* [discord.py 2.x](https://pypi.org/project/discord.py/)

### Setup

```bash
# Repository klonen
git clone https://github.com/deinuser/discord-message-bot.git
cd discord-message-bot

# Virtuelle Umgebung erstellen (empfohlen)
python3 -m venv venv
source venv/bin/activate

# Abhängigkeiten installieren
pip install -U -r requirements.txt
```

### Starten

```bash
DISCORD_TOKEN="DEIN_BOT_TOKEN" python bot.py
```

---

## 🐳 Docker Deployment

Der Bot lässt sich auch in einem Docker-Container betreiben.

```bash
docker build -t discord-message-bot .
docker run -d --name message-bot \
  -e DISCORD_TOKEN="DEIN_BOT_TOKEN" \
  --restart always \
  discord-message-bot
```

---

## 🔑 Berechtigungen

Beim Einladen des Bots muss er mindestens folgende Berechtigungen haben:

* **Nachrichten senden**
* **Nachrichten verwalten** (zum Bearbeiten/Löschen)
* **Anwendungen in Befehlen verwenden** (für Slash Commands)

Invite-URL Beispiel (ersetze `CLIENT_ID`):

```
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&permissions=2048&scope=bot%20applications.commands
```

👉 Für volle Admin-Rechte kannst du auch `permissions=8` nutzen.

---

## 📜 Beispiel

1. `/send text:"Server-Wartung morgen 20 Uhr"`
2. Ein anderer Admin führt `/edit text:"Server-Wartung verschoben auf 21 Uhr"` aus
3. Später wird die Nachricht mit `/delete` wieder entfernt

---

## 🤝 Mitwirken

Pull Requests und Issues sind willkommen.

---

## 📄 Lizenz

MIT

---

Für den Bot brauchst du wirklich nur drei Dinge:

1. **Nachrichten senden**
2. **Nachrichten verwalten** (löschen, bearbeiten)
3. **Slash Commands nutzen**

Das entspricht im Discord-Permissions-System den Bits:

* `SEND_MESSAGES` → `2048`
* `MANAGE_MESSAGES` → `8192`
* `USE_APPLICATION_COMMANDS` → `2147483648`

Addiert ergibt das:

```
2048 + 8192 + 2147483648 = 2147493888
```

---

## 📌 Invite-Link mit minimalen Rechten

Einfach `CLIENT_ID` durch die ID deines Bots ersetzen:

```
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&permissions=2147493888&scope=bot%20applications.commands
```

Damit hat der Bot **genau die Rechte, die er für deine Funktionen braucht** – nicht mehr und nicht weniger.

