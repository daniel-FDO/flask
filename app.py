
from flask import Flask, render_template, abort

app = Flask(__name__)

events = [
    {"EventID": 1, "Title": "Scratch Games Night", "EventDate": "2026-10-10",
     "StartTime": "10:00", "EndTime": "12:00", "Location": "Room B12", "Capacity": 20},
    {"EventID": 2, "Title": "Build a Website", "EventDate": "2026-10-17",
     "StartTime": "10:00", "EndTime": "12:30", "Location": "Room B12", "Capacity": 16},
    {"EventID": 3, "Title": "Python Robots", "EventDate": "2026-10-24",
     "StartTime": "13:00", "EndTime": "15:00", "Location": "Lab 3", "Capacity": 12},
]

@app.route("/")
def home():
    club_name = "CoderDojo Canterbury"
    next_session = "Saturday 10am"
    return render_template("home.html", club_name=club_name, next_session=next_session )

@app.route("/about")
def about():
    mentors = ["Asha", "Ben", "Chloe"]
    club = {"Room": "B12", "Day":"Saturday", "Ages": "7 to 17"}
    return render_template("about.html", mentors=mentors, club=club)

@app.route("/events")
def event_list():
    return render_template("events.html", events=events)
@app.route("/events/<int:event_id>")
def event_detail (event_id):
    for event in events: 
        if event["EventID"] == event_id:
            return render_template("event_detail.html", event=event)
    abort(404)
    
    
    
    

if __name__ == "__main__":
    app.run(port=8080, debug=True)




