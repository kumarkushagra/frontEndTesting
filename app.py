from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)
CN_FOLDER = os.path.join(os.getcwd(), 'DSP')  # Path to your folder

# Route to list files
@app.route('/')
def index():
    try:
        files = [f for f in os.listdir(CN_FOLDER) if f.endswith('.pkt')]
        return render_template('index.html', files=files)
    except Exception as e:
        return f"Error: {str(e)}"

# Route to download a file
@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(CN_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
