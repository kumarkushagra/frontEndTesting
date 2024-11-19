from flask import Flask, render_template, request
import os

app = Flask(__name__)
DSP_FOLDER = os.path.join(os.getcwd(), 'DSP')  # Path to your DSP folder

# Ensure the DSP folder exists
if not os.path.exists(DSP_FOLDER):
    os.makedirs(DSP_FOLDER)

# Route to list files
@app.route('/')
def index():
    try:
        # List all .txt files in the DSP folder and sort them in ascending order
        files = sorted([f for f in os.listdir(DSP_FOLDER) if f.endswith('.txt')])
        return render_template('index.html', files=files)
    except Exception as e:
        return f"Error: {str(e)}"

# Route to view the content of a file
@app.route('/view/<filename>')
def view_file(filename):
    try:
        file_path = os.path.join(DSP_FOLDER, filename)
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template('view.html', filename=filename, content=content)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
