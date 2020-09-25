from flask import Flask, render_template, request, redirect, url_for,session
from werkzeug.utils import secure_filename
import os
from Pluralistic.project_test import Project
import json
import PIL
from PIL import Image
app = Flask(__name__)

global file_name
# global res_img

# create the folders when setting up your app
os.makedirs(os.path.join(app.instance_path, 'UserFiles'), exist_ok=True)


def isValidFileName(filename):
    if filename.endswith('jpg') or filename.endswith('png'):
        return True
    else:
        print("Invalid file type")
        return False



@app.route('/')
def index():
   return render_template('index.html')


# @app.route('/fix_image')
# def fix_image():
#     print('In fix_image function')
#     print(file_name)

#     imageFill = Project()
#     res_file = imageFill.fill_mask(file_name)
#     print(res_file)

#     #result(res_file)
#     global res_img
#     res_img = res_file

#     return render_template('result.html', image_file = res_file)
#     # return "Nothing"



@app.route('/result', methods=['GET', 'POST'])
def result():
    print("result method")
    if request.method == 'POST':
        filename = request.form['text']
        filepath = "D://WebSite//app//static//uploads//"
        print("FIle name from user : "+filename)

        real_file = filepath+filename


        #resize image
        img = Image.open(real_file)
        img = img.resize((256, 256), PIL.Image.ANTIALIAS)
        img.save(real_file)

        

        imageFill = Project()
        res_file = imageFill.fill_mask(real_file)
        print("Result file : "+res_file)
        head, tail = os.path.split(res_file)

        return render_template('result.html', image_file = tail)

        # return "Hello boy!"



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    print("Upload file method")
    if request.method == 'POST':
        f = request.files['file']

        if isValidFileName(f.filename):
            print("Valid file name")
            print(secure_filename(f.filename))
            print(os.curdir)
            f.save(os.path.join('static/uploads', secure_filename(f.filename)))

            global file_name 
            file_name = os.path.abspath('static/uploads/'+f.filename)
            
            print("saved file")
            return render_template('uploaded.html', image_file = f.filename)

        

if __name__ == '__main__':
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug = True)