from send_availability_email import send_availability_email
from flask import Flask, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def is_auth():
  return request.args.get("secret") == os.getenv('SECRET')
  

@app.route('/')
def home():
  if not is_auth():
    return "Not authorized", 401
  
  urls = request.args.get("urls")
  sizes_to_check = request.args.get("sizes_to_check")
  item_names = request.args.get("item_names")
  
  lulu_data = list(zip(urls.split(","), sizes_to_check.split(","), item_names.split(",")))
  
  return send_availability_email(lulu_data)