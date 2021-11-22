from flask import  render_template, request, Flask, flash, redirect, url_for
from werkzeug.utils  import secure_filename
import os
import logging
from data_manip import process_file
from db_operations import insert_into_db, create_database, get_latest_results

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
app.secret_key = b"asdf2332948501132466"

ALLOWED_EXTENSIONS = ["csv"]


@app.route("/")
def main_page():
    if not os.path.exists("database.db"):
        app.logger.debug("creating database")
        create_database()
    app.logger.info(f"getting results")
    rows = get_latest_results()
    #app.logger.info(f"rows contains {rows[0][1]}, {rows[0][2]}")
    return render_template("list.html", rows=rows)


@app.route('/submit', methods = ['POST', 'GET'])
def submit_new_file():
    if request.method == 'POST':
        app.logger.debug('getting postrequest')
        if 'file' not in request.files:
            flash('Geen csv geupload')
            app.logger.info('geen csv geupload')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('geen csv geupload')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            app.logger.debug(f"file {file.filename} uploaded")
            filename = secure_filename(file.filename)
            filelocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filelocation)

            opmerking = request.form['opmerking']
            team_naam = request.form['team_naam']
            kilos, streetworth = process_file(filelocation)
            app.logger.debug(f"{kilos}, {streetworth}, {team_naam}, {opmerking}")
            msg = insert_into_db(kilos, streetworth, team_naam, opmerking)

        return render_template("result.html")

    return render_template("submission.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    logging.basicConfig()
    app.run(host="0.0.0.0", debug = True)
    app.logger.info("starting application")
    # some gunicorn settings here.
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
