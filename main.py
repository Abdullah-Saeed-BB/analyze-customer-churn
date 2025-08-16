from flask import Flask, render_template
from routes.dashboard import dashboard_bp
from routes.analyze_customer import analyze_customer_bp

app = Flask(__name__)

app.register_blueprint(dashboard_bp)
app.register_blueprint(analyze_customer_bp, url_prefix="/analyze_customer")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("not_found_page.html"), 404

if __name__ == "__main__":
    app.run(debug=True)