import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-2956b-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
data = {
    "1":
        {
            "name": "Elon Mask",
            "major" : "Robotics",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year" : 4,
            "last_attendance_time": "2024-03-29 00:54:32"
        },
    "2":
        {
            "name": "Ratan Tata",
            "major": "Business",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year" : 4,
            "last_attendance_time": "2022-03-29 00:54:32"
        },
    "3":
        {
            "name": "Ramya sri Yalamarti",
            "major": "Machine Learning",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year" : 4,
            "last_attendance_time": "2022-03-29 00:54:32"
        },
    "4":
        {
            "name": "Bramhi",
            "major": "CSE",
            "starting_year": 2000,
            "total_attendance": 1,
            "standing": "G",
            "year" : 4,
            "last_attendance_time": "2022-03-29 00:54:32"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
