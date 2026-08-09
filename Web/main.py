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
