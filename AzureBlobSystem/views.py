from flask import request, redirect, url_for, render_template, flash
from AzureBlobSystem import app 

@app.route('/')
def show_upload():
    return "Hello Azure"