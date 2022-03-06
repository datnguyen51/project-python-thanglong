import os
from werkzeug.utils import secure_filename

from settings import ALLOWED_EXTENSIONS, BASE_DIR, UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(file):
    file_path = ''

    if file and allowed_file(file.filename):
        location = os.path.join(BASE_DIR, UPLOAD_FOLDER)
        if not os.path.exists(location):
            os.makedirs(location)

        filename = secure_filename(file.filename)
        file_path = os.path.join(location, filename)
        file.save(file_path)

        file_path = file_path.replace(BASE_DIR, "")

    else:
        file_path = ''

    return file_path
