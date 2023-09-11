import datetime
import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/", status_code=200, tags=["index"])
def index(slack_name: str = "yuba", track: str = "backend"):
    # Get the current date
    current_date = datetime.datetime.now()

    # Get the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week = current_date.weekday()

    # Create a list of day names
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Get the name of the current day
    current_day = days[day_of_week]
    # Get the current UTC time
    current_utc_time = datetime.datetime.utcnow()
    formatted_utc_time = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": formatted_utc_time,
        "track": track,
        "github_file_url": "",
        "github_repo_url": "",
        "status_code": 200,
    }
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)