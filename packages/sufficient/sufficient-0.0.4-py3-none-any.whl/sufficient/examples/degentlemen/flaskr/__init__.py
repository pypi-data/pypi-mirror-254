from flask import Flask, send_file, request
import os
import io
import json
from sufficient.frames.frame_app_runner import FrameAppRunner, ImageFile, ImageView
from frame import app as frame_app


def create_app(test_config=None):
    app = Flask(__name__)
    # app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(
    #     app.instance_path, 'flaskr.sqlite'))
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    runner = FrameAppRunner(frame_app, "https://b24ef6151e56.ngrok.app")

    @app.route('/')
    def frame_index():
        frame_meta = runner.start()
        og_meta = runner.gen_og_meta()
        html = runner.gen_frame_html(frame_meta | og_meta)
        return html

    @app.route('/<string:page>/view/<string:state>')
    def frame_image(page, state):
        view = runner.gen_frame_view(page, state)
        if isinstance(view, ImageView):
            return send_file(io.BytesIO(view.content),  mimetype=view.content_type)
        elif isinstance(view, ImageFile):
            return app.send_static_file(view.path)

    @app.route('/<string:page>/click', methods=['POST', 'GET'])
    def frame_click(page):
        frame_meta = runner.click(page, request.json)
        html = runner.gen_frame_html(frame_meta)
        return html

    return app
