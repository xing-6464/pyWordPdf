from pdf2docx import Converter
from docx2pdf import convert

def pdf_to_docx(pdf_name: str):
    f = f'./upload/{pdf_name}'

    cv = Converter(f)
    
    
    docx_file = './out_docx/' + pdf_name.split('.')[0] + '.docx'
    
    cv.convert(docx_file)
    cv.close()


def docx_to_pdf(docx_file_path: str):
    pdf_save_path = './out_pdf/' + docx_file_path.split('/')[-1].split('.')[0] + '.pdf'
    
    convert(f'./upload/{docx_file_path}', pdf_save_path)

