from flask import Flask,render_template
import os

app = Flask(__name__)

#True img_folder=os.path.exists("templates/img")
#img_folder=os.listdir("templates/img")
#['sample1.png', 'sample2.png', 'sample3.png', 'sample4.png']

#list_img=os.listdir("templates/img")
#print(list_img)

list_img=os.path.join("static/img/","sample1.png")
print(type(list_img))
img_folder=os.path.exists(list_img)
print(list_img)
print(img_folder)

@app.route('/')
def go_to_index():
    return render_template("fig_gallery.html",list_image=list_img)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)

