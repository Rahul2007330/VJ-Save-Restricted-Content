import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28365211"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "191dc355c31100998c7082e7c1fc7bd2")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rahulkukna77:mJMk2ZrOrIgHFuTk@cluster0.kpqi6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
