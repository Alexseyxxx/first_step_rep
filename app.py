
from flask import(
    Flask,
    render_template,
    redirect,
    request
)

app = Flask(__name__)

@app.route("/log", methods =["GET","POST"])
def get_home():
  return render_template("log.html")

@app.route("/reg", methods =["GET","POST"])
def get_reg():
  return render_template("reg.html")

@app.route("/base", methods =["GET","POST"])
def get_log():
  return render_template("base.html")





if __name__=="__main__":
  app.run(
    debug = True,
    port= 8080
    )