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
  
  return 'Error'




@app.route('/')
def home():
  return render_template('home_page.html')


@socketio.on('tetris')
def tetris(data):
  #print()
  #print(data)
  room = data['room']
  emit('to_tetris',{'msg':'helloooo','room':room})



def run():
  socketio.run(app,host="0.0.0.0",port=8080)
def thread_run():
  t = Thread(target=run)
  t.start()
