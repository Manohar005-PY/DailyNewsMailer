# 🗞️ Daily News Mailer

A Python automation script that fetches the **top 5 daily technology news headlines** using [NewsAPI.org](https://newsapi.org/) and sends them to your email inbox using Gmail SMTP.

---

## 📌 Features

- ✅ Fetches latest news headlines using NewsAPI
- ✅ Sends formatted email via Gmail SMTP
- ✅ Secures sensitive data using environment variables (`.env`)
- ✅ Uses Python's `schedule` module to send news daily at 6:00 AM

---

## 🛠️ Requirements

- Python 3.7 or later
- A NewsAPI key (free at [newsapi.org](https://newsapi.org/))
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833) if 2FA is enabled

Install required libraries:

```bash
pip install requests schedule python-dotenv

📁 Project Structure
DailyNewsMailer/
├── main.py          # Main script
├── .env             # Stores API key and credentials (DO NOT push to GitHub)
├── README.md        # Project documentation
├── LICENSE          # Open-source license
└── .gitignore       # Prevents uploading sensitive files

🔐 .env File Example
Create a .env file in your root folder and add:

ini
Copy
Edit
API_KEY=your_newsapi_key
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com

📧 Output Example
You'll receive a clean email like:

markdown
Copy
Edit
Subject: This Is The Todays Top 5 Headline

1. Apple Unveils New AI Features in iOS 18
2. Google Announces Quantum Breakthrough
3. Microsoft to Invest $10 Billion in AI Startups
4. OpenAI Releases GPT-5 Model
5. Tesla Launches New AI-Powered Car Assistant

📌 Improvements for Future
Add category selection (e.g., sports, health)

HTML-formatted email

Store sent headlines in a database or file

🧑‍💻 Author
Made with ❤️ by Manohar

