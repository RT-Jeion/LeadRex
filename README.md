# LeadRex

Local web viewer for MongoDB links.

Run:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Defaults:
- Mongo URI: `mongodb://localhost:27017/`
- DB: `LeadRex`
- Collection: `Leads_From_Places`