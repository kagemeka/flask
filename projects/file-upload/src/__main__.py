import flask
from flask import (
  Flask,
  flash,
  request,
  redirect,
  url_for,
)
from werkzeug.utils import (
  secure_filename,
)

import os 


def set_globals():
  global cfd, root
  cfd = os.path.dirname(
    __file__,
  )
  cfd = os.path.abspath(cfd)
  root = f'{cfd}/../'


def main():
  set_globals()
  
  upload_dir = f'{root}/data/'
  
  app = Flask(__name__)
  app.config['upload_dir'] = (
    upload_dir
  )


  @app.route(
    '/',
    methods=['GET', 'POST'],
  )
  def upload():
    if (
      request.method != 'POST'
    ):
      return '''
      <!doctype html>
      <title>Upload new File</title>
      <h1>Upload new File</h1>
      <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
      </form>
      '''
    file = request.files['file']
    filename = secure_filename(
      file.filename,
    )
    file.save(
      f'{upload_dir}/'
      f'{filename}'
    )
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
  

  app.run(debug=True)


if __name__ == '__main__':
  main()