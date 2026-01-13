# 💸 Expense Tracking System Automation (n8n)

## 📌 Project Overview

This project is an **automated expense tracking system** built using **n8n**, which extracts expense details from bank SMS messages and automatically logs them into **Google Sheets**.

The system uses an **AI model (Google Gemini)** to intelligently parse unstructured transaction messages and store structured expense data.

---

## 🚀 What This Project Does

* Accepts bank transaction messages via webhook
* Extracts **date and amount** from SMS text using AI
* Converts unstructured text into structured JSON
* Automatically appends expense data to Google Sheets
* Eliminates manual expense tracking

---

## 🔄 High-Level Workflow

1. Bank SMS is sent to webhook
2. Message text is extracted
3. AI model parses transaction details
4. Structured data is generated
5. Expense is logged into Google Sheets

---

## 🧩 Nodes Used (One-Line Each)

* **Webhook** – Receives bank transaction messages as HTTP requests
* **Set (Edit Fields)** – Extracts and prepares message content for processing
* **AI Agent** – Uses AI to analyze transaction message and extract expense details
* **Google Gemini Chat Model** – Provides the language model used by the AI agent
* **Structured Output Parser** – Ensures AI output follows a fixed JSON structure
* **Google Sheets** – Appends extracted expense data into a spreadsheet

---

## 🧪 Sample Input Message

```
Rs. 300.00 debited from HDFC Bank a/c Txn ID 123456 Bal:5000
```

## 📤 Sample Output Stored

| Date       | Money |
| ---------- | ----- |
| 2025-11-07 | 300   |

---

## 🛠️ Technologies Used

* n8n
* Google Gemini (PaLM API)
* Google Sheets API
* JavaScript
* Webhooks

---

## 💼 Resume One-Liner

> Built an AI-powered expense tracking automation using n8n that extracts financial data from SMS messages and logs expenses automatically into Google Sheets.

---

## 👤 Author

**Durga Prasad**
