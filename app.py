import os
from flask import Flask, jsonify, render_template, send_from_directory, request, session
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="")

Video_dir = "static/movies"   

def get_movies():
    files = []
    for entry in os.scandir(Video_dir):
        if entry.is_file():
            if not (entry.name.lower().endswith(".mp4") or entry.name.lower().endswith(".mkv")):
                files.append(entry.name)
        elif entry.is_dir():
            files.append(entry.name)

    return files

@app.route("/")
def home():
    return render_template("index.html") 

@app.route('/css/<path:filename>')
def custom_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def custom_js(filename):
    return send_from_directory('js', filename)

@app.route('/resources/<path:filename>')
def folder_images(filename):
    return send_from_directory('resources', filename)

@app.route('/Templates/<path:filename>')
def templates(filename):
    return send_from_directory('Templates',filename)

@app.route("/api/videos")
def api_vid():
    videos = get_movies()
    return jsonify({
        "count":len(videos),
        "files":videos
    })

@app.route('/watch')
def selected_movie():
    return render_template("watch.html")

@app.route("/watch-movie", methods=["POST"])
def watch_movie():
    data = request.get_json()
    session["folder"] = data.get("folder")
    return{"status":"ok"}

@app.route('/play-movie')
def play_movie():
    full_path = os.path.join(Video_dir,session.get("folder"))
    print(full_path)
    return jsonify({"folder":full_path})
    


@socketio.on('connect')
def handle_connect():
    print("client Connected")
    socketio.emit("server message", {"msg": "Welcome! Live updates enabled."})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)