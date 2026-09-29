from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang='en'>
<head><meta charset='utf-8'><title>Network Map</title></head>
<body>
<h1>Network Map Placeholder</h1>
<div id='map'>Map would appear here.</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
