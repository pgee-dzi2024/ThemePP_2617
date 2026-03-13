@app.route("/urls")
def urls():
    return """
Camera Server URLs

Web interface:
http://192.168.1.50:5000/

Live stream:
http://192.168.1.50:5000/video_feed

Snapshot:
http://192.168.1.50:5000/snapshot

Motion status:
http://192.168.1.50:5000/motion_status

JSON API:
http://192.168.1.50:5000/api/status
"""