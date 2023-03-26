from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'data engineeer',
  'salary': '10,000,00',
  'location': ' Delhi, Tmailnadu'
}, {
  'id': 2,
  'title': 'data clint',
  'salary': '10,000,00',
  'location': ' Delhi, Tmailnadu'
}, {
  'id': 3,
  'title': 'data Browser',
  'salary': '10,000,00',
  'location': ' Delhi, Tmailnadu'
}, {
  'id': 4,
  'title': 'data Scientist',
  'location': ' Delhi, Tmailnadu'
}, {
  'id': 5,
  'title': 'data master',
  'salary': '10,000,00',
  'location': ' Delhi, Tmailnadu'
}]


@app.route("/")
def helloworld():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def lift_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
