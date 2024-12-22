# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25047243"))
    API_HASH = getenv("API_HASH", "f68cde581603434533bbdf92763d158b")
    BOT_TOKEN = getenv("BOT_TOKEN", "7760935742:AAFoisU71ElLwY-WJBLMx9_8x-RnQI2Xvcc")
    FSUB = getenv("FSUB", "LogAccept")
    CHID = int(getenv("CHID", "-1002425184589"))
    SUDO = list(map(int, getenv("SUDO", "8023016938").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ashinr2008:LGEMC9j6dsIvqqT0@cluster0.5pzpw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
