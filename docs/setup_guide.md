# Akki Bot – Setup Guide

Welcome! This guide will help you set up and host **Akki Bot** on your server without needing to touch the frontend or server logic. You will only interact with the bot files and documentation. This project is licensed under the **MIT License**.

---

## 🔖 Overview

- **Repo:** [akki-bot GitHub](https://github.com/Akkiraj1234/akki-bot)
- **Target Users:** Developers wanting a self-hosted Discord bot
- **Note:** You don’t need to clone the entire repo. Just download the latest release `.tar.gz` and follow this guide.

---

## 📁 Included in the Release

When you extract the release archive, you'll see:

```
akki-bot/
├── akkibot/        ← You only work inside this folder
│   ├── bot.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   └── server.py
├── docs/           ← Helpful documentation
│   ├── basic.md
│   └── how_its_working.md
├── README.md
├── requirements.txt
```

You do **not** need to touch:

- `resource/`
- `server/`
- `webpage/`

These folders are proprietary and handled by the hosting/server setup.

---

## 🚀 How to Set Up the Bot

### 1. Extract the Release Archive

Download and extract the `.tar.gz` release from [GitHub Releases](https://github.com/Akkiraj1234/akki-bot/releases).

```bash
tar -xvzf akki-bot-x.y.z.tar.gz
cd akki-bot
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Bot

Inside the `akkibot/config.py` or using environment variables, set:

- `DISCORD_TOKEN`: Your bot token
- `BOT_PREFIX`: Bot command prefix (e.g. `!`)
- Any database or API keys (optional)

You can also create a `.env` file and load it with `dotenv` (if supported).

### 5. Run the Bot

```bash
python akkibot/main.py
```

Done! 🎉

The bot will be up and running. You can customize commands in `bot.py`, database logic in `database.py`, and adjust server features in `server.py`.

---

## 💡 Tips

- Don't touch `/resource`, `/server`, or `/webpage` — these are used by the hosted dashboard and are not needed for bot operation.
- Check the `docs/` folder for more advanced information.
- PRs are welcome only for `akkibot/` or `docs/` contributions.

---

## 🪪 License

Only the `akkibot/` and `docs/` folders are under the [MIT License](https://opensource.org/licenses/MIT). The rest of the project is proprietary.

---

Made with ❤️ by Akki