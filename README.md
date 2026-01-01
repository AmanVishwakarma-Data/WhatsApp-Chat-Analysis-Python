# 📊 WhatsApp Chat Analysis — Python & Streamlit

An interactive Python project that analyzes exported WhatsApp chats and displays useful insights using a Streamlit dashboard.

---

## 🚀 Project Overview

This tool allows users to upload their WhatsApp chat export and generates analytics such as:

* Total messages & word count
* Media and link sharing stats
* Most active users (Overall or user-wise)
* Most common words analysis
* Emoji usage distribution
* Monthly and daily message trends
* Activity maps by day and month
* Heatmap of online activity by hour

---

## 🧠 How It Works (Logic Explained Simply)

1. The chat text is processed using regex to extract **timestamps and messages**.
2. Messages are converted into a **structured Pandas DataFrame**.
3. The dashboard filters analysis based on the selected user or overall chat.
4. Visual insights are generated using **Matplotlib and Seaborn heatmap**.

---

## 🛠️ Tech Stack

```
Python  
Pandas  
Streamlit  
Matplotlib  
Seaborn  
Regex (re)  
URLExtract  
Emoji Library  
```

---

## 📁 Folder Structure

```
CHAT_ANALYSIS/
├── app.py
├── preprocessor.py
├── helper.py
├── stop_hinglish.txt
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Run

1. Clone this repository:

   ```powershell
   git clone <repo-link>
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```powershell
   streamlit run app.py
   ```

---

## 🔒 Privacy Notice

* This project **does NOT store or upload any personal chat data**.
* Users must upload their own WhatsApp chat export file manually for analysis.
* The repository contains only code and logic, no real personal chat exports.

---



