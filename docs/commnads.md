# 📜 AkkiBot Command Documentation

Welcome to the official command reference for **Akkibot** – your Discord server's developer assistant, moderator helper, and community manager.

---

## 🧑‍💻 User Roles & Permissions

| Role Type | Description |
|-----------|-------------|
| 🟢 **User** | Any regular member of the server |
| 🔵 **Moderator** | Can warn, mute, purge, manage roles |
| 🔴 **Leader/Admin** | Full access – can ban, kick, reload, and shutdown the bot |

---

## 👤 Profile Commands

_Manage and share user developer profiles (Available to: 🟢 User)_

| Command | Description |
|---------|-------------|
| `!setgithub <url>` | Set your GitHub account |
| `!setleetcode <url>` | Set your LeetCode profile |
| `!setroadmap <url>` | Set your roadmap.sh link |
| `!setproject <url>` | Set your current working project |
| `!profile [@user]` | View someone’s full profile |
| `!github [@user]` | Show GitHub profile |
| `!leetcode [@user]` | Show LeetCode profile |
| `!roadmap [@user]` | Show roadmap profile |
| `!project [@user]` | Show current working project |
| `!akkibot` | Akkibot introduces itself (version, dev info) |

---

## 🛡️ Moderation & Admin Commands

_Moderation and admin tools for managing the server_

### 🔵 Available to: **Moderators & Leaders**

| Command | Description |
|---------|-------------|
| `!warn @user [reason]` | Warn a user and log it |
| `!warnings @user` | View warning history |
| `!mute @user [duration]` | Temporarily timeout a user |
| `!unmute @user` | Remove a user's timeout |
| `!purge <count>` | Bulk delete recent messages |
| `!punish @user level1 or 2 or 3` | Apply a predefined punishment level |
| `!modlogs @user` | Show logs of that user's infractions |

### 🔴 Available to: **Leaders/Admins Only**

| Command | Description |
|---------|-------------|
| `!ban @user [reason]` | Permanently ban a user |
| `!kick @user [reason]` | Remove a user from server |
| `!shutdown` | Shut down the bot |
| `!reload <cog>` | Reload a bot module (live update) |

---

## 🎭 Role Management

_Assign and manage user roles_

### 🔵 Available to: **Moderators & Leaders**

| Command | Description |
|---------|-------------|
| `!role add @user <role>` | Assign a role to user |
| `!role remove @user <role>` | Remove a role from user |
| `!role show @user` | Show roles user currently has |
| `!role modset <role>` | Mark a role as “Moderator” (used in punish logic) |

---

## 👋 Welcome & Verification System

_Used to welcome and verify new members automatically_

### 🟢 Available to: **Everyone (auto-triggered)**  
### 🔴 Setup available to: **Leaders/Admins**

| Feature | Description |
|--------|-------------|
| `@unverified` role auto-assigned | When a user joins |
| ✅ reaction on message → verified | Bot gives `@verified` role |
| `!setwelcome #channel` | Set the channel where welcome message is sent |
| Auto welcome/leave message | Sent to `#welcome` and `#farewell` channels (configured) |

---

## 📈 XP & Level System

_Track user activity and participation over time_

### 🟢 Available to: **All Users**

| Command | Description |
|---------|-------------|
| `!rank [@user]` | View XP, level, and rank |
| `!leaderboard` | Show top 10 XP holders |
| XP is auto-tracked | Cached in RAM, written to DB every 10 mins |
| Optional level-up alerts | Can be enabled per server |

---

## 🛠 Utility Commands

_Quick checks for users and developers_

### 🟢 Available to: **Everyone**

| Command | Description |
|---------|-------------|
| `!ping` | Show bot latency |
| `!uptime` | Show how long bot has been running |
| `!botstats` | Show version, server count, and RAM usage |

---

## 🗂️ Command Scope Summary

| Command Category | Role Access |
|------------------|-------------|
| Profile Commands | 🟢 User |
| Moderation Tools | 🔵 Moderator / 🔴 Leader |
| Admin Tools | 🔴 Leader Only |
| Role Management | 🔵 Moderator / 🔴 Leader |
| XP System | 🟢 User |
| Utility | 🟢 User |
| Welcome/Verify | 🟢 Auto (User) / 🔴 Setup by Leader |

---

## 🔐 Notes for Devs

- Commands with `[owner only]` or [leader] should be locked with `@commands.is_owner()` or custom role checks.
- Logging should only send to modlog channels, not database.
- Commands like `!warn`, `!modlogs`, and `!punish` should log actions cleanly.

---

🛠 Built with care by Akki  
📌 Contact: `@Akkibot Dev` in Discord  
📦 Powered by Python, PostgreSQL, and async love 💙
