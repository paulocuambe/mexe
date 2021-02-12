from flask import Flask, render_template, flash, url_for, redirect
from forms import FileForm
from PIL import Image

app = Flask(__name__)
app.secret_key = "ajsnjasnasj"

if __name__ == "main":
    app.debug(True)


@app.route('/', methods=["GET", "POST"])
def home():
    form = FileForm()
    if form.validate_on_submit():
        form_top = int(form.top.data) if form.top.data else 0
        form_down = int(form.down.data) if form.down.data else 0
        form_right = int(form.right.data) if form.right.data else 0
        form_left = int(form.left.data) if form.left.data else 0

        image = Image.open(form.image.data)
        width, height = image.size
        # image = image.crop((100, 20, 300, 200))
        # image = image.resize((200, 400))
        # image = image.rotate(180)
        # image.save("somme-sasa.png")

        form_rotation = int(form.rotation.data) if form.rotation.data else 0
        form_height = int(form.height.data) if form.height.data else None
        form_width = int(form.width.data) if form.width.data else None

        crop = (form_left, form_top, form_right, form_down)
        scale = (form_width, form_height)
        image = treat_image(image,
                            rotation=form_rotation,
                            scale=scale,
                            crop=crop)
        image.show()
        flash("Manipulação da imagem feita com sucesso", "success")
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


#   rotate, left, right, top, down, height, width, submit
def treat_image(image, rotation, scale=(), crop=()):
    if len(crop) == 4 and crop[0] and crop[1] and crop[2] and crop[3]:
        print("CROPS")
        image = image.crop(crop)

    if rotation:
        print("ROTATES")
        print(rotation)
        image = image.rotate(rotation)

    if len(scale) == 2 and scale[0] and scale[1]:
        print("SCALES")
        image = image.resize(scale)

    return image
