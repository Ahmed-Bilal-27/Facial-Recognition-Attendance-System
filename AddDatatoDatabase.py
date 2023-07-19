import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recog-attendance-sy-8bd14-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "20080":
        {
            "name": "Emily Blunt",
            "major": "Robotics",
            "starting_year": 2018,
            "total_attendance": 42,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:57:46"
        },
    "20081":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2019,
            "total_attendance": 27,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:58:22"
        }
}
print("Transfer Started...")
for key, value in data.items():
    ref.child(key).set(value)
print("Transfer Complete")
print("Data Saved")