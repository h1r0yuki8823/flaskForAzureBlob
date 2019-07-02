from flask import request, redirect, url_for, render_template, flash
from flaskForAzureBlob import app 

@app.route('/')
def show_upload():
    return render_template('upload.html')