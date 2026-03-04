from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from matcher import match_resume

app = Flask(__name__)
UPLOAD_FOLDER = "resumes"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['resume']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        resume_text = extract_text(path)
        score = match_resume(resume_text)

        return render_template('results.html', score=score)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
