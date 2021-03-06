from app import app
import app.ownFunctions as run
from flask import render_template, flash, redirect, url_for, request, jsonify
import base64


@app.route('/capture')
def capture():
    return render_template('capture.html')


@app.route('/search')
def search():
    dataURL = request.args.get('dataURL')
    data = dataURL.split(',')[1]
    with open("app/static/img/image.png", "wb") as fh:
        fh.write(base64.b64decode(data))
        fh.close()
    result = run.searchName('Family', 'app/static/img/image.png')
    return jsonify(result=result)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/add')
def add():
    dataURL = request.args.get('dataURL')
    name = request.args.get('name')
    data = dataURL.split(',')[1]
    with open("app/static/img/image.png", "wb") as fh:
        fh.write(base64.b64decode(data))
        fh.close()
    result = run.addFace('Family', 'app/static/img/image.png', name)
    return jsonify(result=result)


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/deleteFace')
def deleteFace():
    dataURL = request.args.get('dataURL')
    data = dataURL.split(',')[1]
    with open("app/static/img/image.png", "wb") as fh:
        fh.write(base64.b64decode(data))
        fh.close()
    result = run.deleteByImg('Family', 'app/static/img/image.png')
    return jsonify(result=result)
