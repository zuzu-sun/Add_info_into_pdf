from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function fill data into specify position of original pdf, generate new pdf file with data filled.
# @ Position_x, Position_y: the position of original pdf need to be processed.
# @ data_to_fill:  The data to be filled.
# @ original_pdf, destination_pdf: the path of pdf files.

def fill_data_in_pdf(Position_X=10,Position_y=100,data_to_fill="Hello world", original_pdf="LSTM.pdf", destination_pdf="destination.pdf"):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(Position_X, Position_y, data_to_fill)
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(original_pdf, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(destination_pdf, "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ == '__main__':
    fill_data_in_pdf(Position_X=100,Position_y=90, data_to_fill="gaopeng")
