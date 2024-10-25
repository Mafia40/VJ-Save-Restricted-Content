import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7921974642:AAGBZhytYZcL8WU3Dd79ZDeiNn9xhD47pGg")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23116526"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7422a0f603a9549fb19940a10757dac4")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://saovishal:CjSnHc5oSyH3xgIM@cluster0.0d5dk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
