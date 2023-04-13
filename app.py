'''from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def imagetopdf():
    return render_template('upload_image.html')


if __name__ == '__main__':
    app.run(debug=True)'''


from flask import Flask, render_template,Response, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from main import img2pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class UploadForm(FlaskForm):
    images = FileField('Select image(s)', render_kw={'multiple': True})
    submit = SubmitField('Convert to PDF')

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        images = request.files.getlist('images')
        # process images into a single PDF
        instance = img2pdf([image.filename for image in images])
        pdf_data = instance.save_pdf(instance.create_pdf())

        # send the PDF file to the user
        return redirect(url_for('send_pdf', pdf_data=pdf_data))

    return render_template('forms.html', form=form)

@app.route('/send-pdf')
def send_pdf():
    pdf_data = request.args.get('pdf_data')
    return Response(pdf_data, mimetype='application/pdf')
