from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import pdfkit
from docx import Document
from datetime import datetime
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    allowed_extensions = {'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(f"{datetime.now().timestamp()}-{file.filename}")
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            metadata = {
                'name': file.filename,
                'size': os.path.getsize(filepath),
                'type': file.content_type,
                'path': filepath,
                'lastModified': datetime.now().isoformat()
            }
            
            return jsonify({'metadata': metadata})
        else:
            return jsonify({'error': 'File type not allowed'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/convert', methods=['POST'])
def convert_file():
    try:
        data = request.get_json()
        file_path = data.get('filePath')

        if not file_path:
            return jsonify({'error': 'Missing file path'}), 400

        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        # Convert DOCX to HTML first
        document = Document(file_path)
        html_content = "<html><body>"

        for para in document.paragraphs:
            html_content += f"<p>{para.text}</p>"

        html_content += "</body></html>"

        # Use pdfkit to convert HTML to PDF
        pdf = pdfkit.from_string(html_content, False)

        # Return the PDF as a file response
        return send_file(
            BytesIO(pdf),
            as_attachment=True,
            download_name='converted.pdf',
            mimetype='application/pdf'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        try:
            if 'file_path' in locals() and os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error cleaning up files: {e}")


if __name__ == '__main__':
    port = int(os.getenv('PORT', 4003))
    app.run(host='0.0.0.0', port=port)
