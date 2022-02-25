from typing import Optional
from fastapi import FastAPI
from lucky_me import Course

app = FastAPI()


@app.get("/")
def root():
    return {"We slow down..."}


# @app.get("/courses/{course_name}")
# def read_course(course_name):
#     return {"course_name": course_name}


course_items = [{"course_name": "Python"}, {
    "course_name": "Ruby"}, {"course_name": "Java"}, ]


@app.get("/courses/")
def read_courses(start: int = 0, end: int = 10):
    return course_items[start: start + end]


course_items = {1: "We", 2: "shall", 3: "remain..."}


@app.get("/courses/{course_id}")
def read_courses(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q}
    return {"course_name": course_items[course_id]}


@app.post("/courses/")
def create_course(course: Course):
    return course
