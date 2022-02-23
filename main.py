from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"We slow down..."}


@app.get("/courses/{course_name}")
def read_course(course_name):
    return {"course_name": course_name}
