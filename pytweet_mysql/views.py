from flask import request, redirect, url_for, render_template, flash, abort, jsonify, session, g
from pytweet_mysql import app, db
# EXERCISE: Pytweetモデルをimportしましょう ==========
# EXERCISE: Let's import Pytweet as model =========
from pytweet_mysql.models import *
# =================================================


@app.route('/')
def home():
    return "<h1>Hello PyTweet</h1>"


@app.route('/pytweets')
def list_pytweets():
    pytweets = Pytweet.query.order_by(Pytweet.id.desc()).all()
    return render_template('pytweet/list.html', pytweets=pytweets)


@app.route('/pytweets/<int:pytweet_id>')
def show_pytweet(pytweet_id):
    pytweet = Pytweet.query.get(pytweet_id)
    return render_template('pytweet/show.html', pytweet=pytweet)


@app.route('/pytweets/new/', methods=['GET', 'POST'])
def create_pytweet():
    if request.method == 'POST':
        pytweet = Pytweet(author_name=request.form['author_name'],
                          body=request.form['body'])
        db.session.add(pytweet)
        db.session.commit()
        flash('New Pytweet was successfully posted')
        return redirect(url_for('list_pytweets'))
    return render_template('pytweet/edit.html')


@app.route('/pytweets/<int:pytweet_id>/edit/', methods=['GET', 'POST'])
def edit_pytweet(pytweet_id):
    pytweet = Pytweet.query.get(pytweet_id)
    if pytweet is None:
        response = jsonify({'status': 'Not Found'})
        response.status_code = 404
        return response
    if request.method == 'POST':
        pytweet.author_name = request.form['author_name']
        pytweet.body = request.form['body']
        db.session.commit()
        return redirect('show_pytweet')
    return render_template('pytweet/edit.html', pytweet=pytweet)


@app.route('/pytweet/<int:pytweet_id>/delete/', methods=['DELETE'])
def delete_pytweet(pytweet_id):
    pytweet = Pytweet.query.get(pytweet_id)
    if pytweet is None:
        response = jsonify({'status': 'Not Found'})
        response.status_code = 404
        return response
    db.session.delete(pytweet)
    db.session.commit()
    flash('The pytweet was successfully deleted')
    return redirect('list_pytweets')
