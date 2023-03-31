from flask import Flask
from flask import request, send_file, render_template
from flask_cors import CORS

from utilss import docx_to_pdf, pdf_to_docx

app = Flask(__name__, template_folder='./dist', static_folder="./dist/assets")
# 支持跨域
CORS(app)

@app.route('/')
def template():
    return render_template('index.html')

@app.route("/pdf_or_docx", methods=['POST'])
def pdf():

    f = request.files['file']
    file_type = f.content_type.split('/')[-1]
    file_name = f.filename

    path = f'./upload/{file_name}'

    out_path = ''

    if file_type == 'pdf':
        # 保存文件
        f.save(path)
        # 转换文件
        pdf_to_docx(file_name)

        out_file_name = file_name.split('.')[0]
        out_path = f'./out_docx/{out_file_name}.docx'
        
        return {
            'file_name': out_file_name + '.docx'
        }

    elif file_type == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
        # 处理docx 转换 pdf
        f.save(path)
        docx_to_pdf(file_name)

        out_file_name = file_name.split('.')[0]
        out_path = f'./out_pdf/{out_file_name}.pdf'
        return {
            'file_name': out_file_name + '.pdf'
        }
    
    return ''

@app.route('/download')
def download():
    file_name = request.args.get('file_name')
    
    file_type = file_name.split('.')[-1]

    
    if file_type == 'pdf':
        return send_file(f'./out_pdf/{file_name}', as_attachment=True)
    elif file_type == 'docx':
        return send_file(f'./out_docx/{file_name}', as_attachment=True)
    
    return ''
    
   


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9527)
