#Payton Schubel
#12/03
#Ch. 1 Task "Hello World" __init__

from flask import Flask

app = Flask(__name__)

#This is another file -- relies on the app variable, so
#import it at the bottom so no circular dependency problem
from app import routes


