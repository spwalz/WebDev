#Sarah Walz
#12/3
#Ch.1 "Hello World"

from flask import Flask
from config import Config

app= Flask(__name__)
app.config.from_object(Config)

from app import routes #routes is a module, written next
#import at bottom, don't want secular independcies

