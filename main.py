from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
db.create_all()

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("Name", type=str, help="Video Name", required=True)
video_post_args.add_argument("Views", type=int, help="Video Views", required=True)
video_post_args.add_argument("Likes", type=int, help="Video Likes", required=True)

videos = {}

def idCheck(videoID):
    if videoID not in videos:
        abort(404, message="VideoID doesn't exist")

class Video(Resource):
    def get(self, videoID):
        idCheck(videoID)
        return videos[videoID]

    def post(self, videoID):
        videoProps = video_post_args.parse_args()
        videos[videoID] = videoProps
        return videos[videoID], 201

    def delete(self, videoID):
        idCheck(videoID)
        del videos[videoID]
        return '', 204


# api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Video, "/video/<string:videoID>")

if __name__ == "__main__":
    app.run(debug=True)
