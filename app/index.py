from flask import Blueprint, request, render_template, jsonify, current_app
from redis import Redis
from rq import get_current_job

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/", methods=("GET",))
def index():
    return render_template("index.html")

@bp.route("/launch", methods=("POST",))
def launch():
    inputs = request.get_json()
    job = current_app.task_queue.enqueue("app.worker.run", inputs)
    response = {
        "job_id": job.get_id()
    }
    return jsonify(response)

@bp.route("/status/<string:job_id>", methods=("GET",))
def status(job_id):
    job = current_app.task_queue.fetch_job(job_id)

    if not job:
        return jsonify({"finished": False})

    return jsonify({"finished": job.is_finished})
    
