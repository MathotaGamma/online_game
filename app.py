from threading import Thread
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, send

app = Flask('')
socketio = SocketIO(app,cors_allowed_origins="*")
UPLOAD_FOLDER = 'upload_files'
app.config['SECRET_KEY'] = 'test'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'math'

@app.errorhandler(OSError)
@app.errorhandler(404)
def error_handler(error):
  print(error)
  return redirect(url_for('home'))




@app.route('/')
def home():
  return render_template('home_page.html')




@app.route('/login')
def login():
  print('hey')
  return render_template('login.html')


@app.route('/OnlineGame/list')
def online_list():
  return render_template('OnlineGame/list.html')


@app.route('/OnlineGame/play/<repository>')
def play(repository):
  return render_template('OnlineGame/play/'+repository)


@socketio.on('tetris')
def tetris(data):
  #print()
  #print(data)
  room = data['room']
  emit('to_tetris',{'msg':'helloooo','room':room})



def run():
  socketio.run(app,host="0.0.0.0",port=8080,allow_unsafe_werkzeug=True)
def thread_run():
  t = Thread(target=run)
  t.start()
