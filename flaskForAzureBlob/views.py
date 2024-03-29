from flask import request, redirect, url_for, render_template, flash
from flaskForAzureBlob import app 
from azure.storage.blob import ContentSettings
from azure.storage.blob import BlockBlobService
from azure.storage.blob import PublicAccess
import os
from os.path import join,dirname
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

account_name = os.environ.get("account_name")
account_key = os.environ.get("account_key")
contaner_name = os.environ.get("container_name")
blob_name = 'test'
fule_path = ''



@app.route('/')
def show_upload():

    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file_path = request.files['pdf_file']
    
    local_path = os.path.expanduser("~\Documents")
    file_path = os.path.join(local_path,"test.pdf")
    print(file_path)
    block_blob_service = BlockBlobService(account_name=account_name,account_key=account_key)
    block_blob_service.create_blob_from_path(
        contaner_name,
        blob_name,
        file_path,
        content_settings=ContentSettings(content_type="application/pdf")
    )

    return render_template('success.html')