import os
from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
from livereload import Server

app = Flask(__name__)
CORS(app)


Video_dir = "static/movies"   

def get_movies():
    files = []
    for entry in os.scandir(Video_dir):
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

@app.route("/api/videos")
def api_vid():
    videos = get_movies()
    return jsonify({
        "count":len(videos),
        "files":videos
    })

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.watch('templates/*.*')
    server.watch('css/*.*')
    server.watch('js/*.*')
    server.serve(host="0.0.0.0" , port=5000, debug=True)