from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/graphs/<filename>')
def send_graph(filename):
    return send_from_directory('static/graphs', filename)

if __name__ == '__main__':
    app.run()

