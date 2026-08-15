from flask import Flask, render_template, request, redirect, url_for

from aws.s3 import upload_resume
from screening import screen_resume
from ranker import rank_candidates

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Store the latest screening results
ranked_candidates = []


@app.route("/", methods=["GET", "POST"])
def home():

    global ranked_candidates

    if request.method == "POST":

        resumes = request.files.getlist("resume")
        job_description = request.form.get("job_description")

        candidates = []

        for resume in resumes:

            if resume.filename == "":
                continue

            # Save a local copy
            local_path = os.path.join(
                UPLOAD_FOLDER,
                resume.filename
            )

            resume.save(local_path)

            # Upload resume to S3
            resume.seek(0)

            filename = upload_resume(resume)

            # Screen candidate
            result = screen_resume(
                local_path,
                job_description
            )

            candidates.append(result)

        # Rank all uploaded candidates
        ranked_candidates = rank_candidates(
            candidates
        )

        # Go to dashboard
        return redirect(url_for("dashboard"))

    return render_template("upload.html")


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        candidates=ranked_candidates
    )


if __name__ == "__main__":
    app.run(debug=True)