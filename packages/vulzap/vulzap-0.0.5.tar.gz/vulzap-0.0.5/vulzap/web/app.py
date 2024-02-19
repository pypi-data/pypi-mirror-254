import os

from flask import Flask, jsonify, render_template, request

from vulzap.core.crawl import Crawl
from vulzap.db.models import SqliReport, XssReport
from vulzap.settings import Env

pwd = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=pwd + "/templates",
    static_folder=pwd + "/static",
)


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        url = request.form["url"]
        target = request.form.get("targetInput")
        header = request.form.get("headerInput", "{}")
        output = request.form.get("outputInput")

    return render_template("index.html", error=error)


@app.route("/output", methods=["GET"])
def output():
    return render_template("output.html")


@app.route("/get_table_data", methods=["GET"])
def get_table_data():
    table_name = request.args.get("table")

    if table_name == "xss":
        print(XssReport.value(), type(XssReport.value()))
        data = XssReport.value()
    elif table_name == "sqli":
        data = SqliReport.value()
    # elif table_name == "ssrf":
    #     data = get_ssrf_data()
    else:
        return jsonify(success=False, message="Invalid table name"), 400

    return jsonify(
        success=True,
        data=[dict(zip(["cve", "payload", "url", "is_vuln"], item)) for item in data],
    )


@app.route("/save_db_info", methods=["POST"])
def save_db_info():
    host = request.form.get("host")
    port = request.form.get("port")
    name = request.form.get("name")
    user = request.form.get("user")
    password = request.form.get("password")

    env = Env()
    env.DB_HOST = host
    env.DB_PORT = port
    env.DB_NAME = name
    env.DB_USER = user
    env.DB_PASSWD = password
    env.save()

    return jsonify(success=True)


@app.route("/run_crawl", methods=["POST"])
def run_crawl():
    url = request.form["url"]
    target = request.form.get("targetInput")
    header = request.form.get("headerInput")
    output = request.form.get("outputInput")

    # TODO: Add depth and headless options
    # crawl = Crawl(depth=0, headless=True)
    crawl = Crawl()
    crawl_result = crawl.run(
        base=url,
        header=header,
    )

    xss_checked = request.form.get("xss")
    sqli_checked = request.form.get("sqlInjection")
    ssrf_checked = request.form.get("ssrf")

    xss_data = get_xss_data() if xss_checked else None
    sqli_data = get_sqli_data() if sqli_checked else None
    ssrf_data = get_ssrf_data() if ssrf_checked else None

    return jsonify(success=True, xss=xss_data, sqli=sqli_data, ssrf=ssrf_data)
