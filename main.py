#imports
import random
from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#images for test
#images = ['image1.jpg', 'image2.png']

#class for create pdf
class img2pdf:
    def __init__(self, images: list):
        self.images = images

    def create_pdf(self):
        buffer = BytesIO()
        pdf_canvas = canvas.Canvas(buffer, pagesize=letter)

        for image in self.images:
            # open the image file
            img = Image.open(image)
            # resize the image to fit on a letter-sized page
            width, height = img.size
            aspect_ratio = height/width
            img_width = 550  # adjust this value as needed
            img_height = int(img_width * aspect_ratio)
            # draw the image on the canvas
            pdf_canvas.drawImage(image, x=25, y=25, width=img_width, height=img_height)
            # add a new page to the PDF
            pdf_canvas.showPage()

        # save the PDF file
        pdf_canvas.save()

        # return the PDF data as bytes
        pdf_data = buffer.getvalue()
        buffer.close()
        return pdf_data

    #save pdf
    def save_pdf(self, pdf_data):
        with open(f"output_{random.randint(99,9999)}.pdf", "wb") as f:
            return f.write(pdf_data)
        

#instance = img2pdf(images)
#pdf_data = instance.create_pdf()
#instance.save_pdf(pdf_data)