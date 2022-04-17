from flask import Flask

from utils import read_json, print_candidat, print_candidat_id, candidat_skills

app = Flask(__name__)

candidates = read_json("candidates.json")


@app.route("/")
def main():
    return print_candidat(candidates)


@app.route("/candidates/<int:cand_id>")
def list_candidates_x(cand_id):
    candidate = print_candidat_id(candidates, cand_id)
    result = f'<img src="{candidate["picture"]}">'
    return result + print_candidat([candidate])


@app.route("/skills/<skill>")
def skills(skill):
    return print_candidat(candidat_skills(candidates, skill))


app.run()
