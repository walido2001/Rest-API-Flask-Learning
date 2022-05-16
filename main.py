from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("Name", type=str, help="Video Name", required=True)
video_post_args.add_argument("Views", type=int, help="Video Views", required=True)
video_post_args.add_argument("Likes", type=int, help="Video Likes", required=True)

videos = {}

class Video(Resource):
    def get(self, videoID):
        return videos[videoID]
    def post(self, videoID):
        videoProps = video_post_args.parse_args()
        return {videoID: videoProps}

# api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Video, "/video/<string:videoID>")

if __name__ == "__main__":
    app.run(debug=True)
