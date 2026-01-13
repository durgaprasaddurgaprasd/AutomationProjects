# 🔐 Telegram Password Vault Automation (n8n)

## 📌 Project Overview

This project is a **Telegram-based Password Vault Automation** built using **n8n**, which allows users to **store, retrieve, and list passwords** securely through simple Telegram chat commands.

The entire system works without a traditional UI and is controlled fully via a Telegram bot.

---

## 🚀 Features

* Insert passwords using Telegram commands
* Retrieve passwords by password type
* List all stored password types
* Input validation using conditional logic
* Persistent storage using n8n Data Tables
* Instant Telegram responses

---

## 🧠 How It Works (High Level)

1. User sends a command in Telegram
2. n8n workflow is triggered
3. Message is parsed using JavaScript
4. Command is routed using Switch & IF nodes
5. Data is stored or fetched from Data Table
6. Response is sent back to Telegram

---

## 💬 Supported Commands

### ➕ Insert Password

```
/insert
gmail
mypassword123
```

### 🔍 Get Password

```
/get
gmail
```

### 📋 Get All Password Types

```
/getall
```

---

## 🧩 Nodes Used (One-Line Each)

* **Telegram Trigger** – Triggers workflow when user sends a Telegram message
* **Code (JavaScript)** – Parses command, password type, and password from message
* **Switch** – Routes workflow based on command
* **IF** – Validates user input
* **Data Table** – Stores and retrieves password data
* **Telegram** – Sends responses back to the user

---

## 🛠️ Technologies Used

* n8n
* Telegram Bot API
* JavaScript
* n8n Data Tables

---



## 👤 Author

**Durga Prasad**

---

## 📎 Notes

⚠️ This project is for learning and demonstration purposes.
