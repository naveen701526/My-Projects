#pip install fpdf

from fpdf import FPDF
pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial",size = 25)

pdf.cell(200,10,txt = " MY PROJECT WORK ",
         ln = 1,align = 'C')

pdf.cell(200,10,
         txt = " To create PDF using python ",
         ln = 2,align = 'C')

pdf.output("data.pdf")

         
