import uvicorn
from pyngrok import ngrok
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
collection = client["LeadRex"]["Leads_From_Places"]

app = FastAPI(title="LeadRex Links")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    links = list(collection.find({}, {"Name": 1, "URL": 1}).sort("_id", -1))
    for link in links:
        link["_id"] = str(link["_id"])
    return templates.TemplateResponse(request, "index.html", {"links": links})


@app.get("/get_leads")
def main():
    links = list(collection.find({}, {"Name": 1, "URL": 1}).sort("_id", -1))
    for link in links:
        link["_id"] = str(link["_id"])

    return links


if __name__ == "__main__":
    import subprocess
    import time
    # Define the command and its arguments as a list

    website = ngrok.connect(6767).public_url

    print("Public Url:", website)

    server_process = subprocess.Popen(
        ["uvicorn", "web:app", "--host", "127.0.0.1", "--port", "6767", "--reload"]
    )

    # 2. Give the server a brief moment to initialize
    time.sleep(1.5)

    print("Server is up! Running subsequent code...")

    # Run the process
    command = ["brave", website]
    subprocess.run(command)
    server_process.wait()
