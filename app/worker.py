import time
from rq import get_current_job

def run(inputs):
    job = get_current_job()
    seconds = int(inputs["seconds"])

    for i in range(seconds):
        job.meta["progress"] = 100.0 * i / seconds
        job.save_meta()

        # DO WORK
        time.sleep(1)

    job.meta["progress"] = 100
    job.save_meta()
