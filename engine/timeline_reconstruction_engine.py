import json
import os
from datetime import datetime

class TimelineReconstructionEngine:

    def parse_date(self, d):
        try:
            return datetime.fromisoformat(d)
        except:
            return None

    def extract_events_from_documents(self, documents):
        events = []
        for d in documents:
            if "date" in d and d['date']:
                events.append({
                    "timestamp": d["raw_date"] if "raw_date" in d else d["date"],
                    "topic": d.get("topic","document_event"),
                    "source": "document",
                    "actor": d.get("actor","unknown")
                })
        return events

    def reconstruct(self, events, documents):
        timeline = []

        timeline.extend(events)
        timeline.extend(self.extract_events_from_documents(documents))

        for e in timeline:
            e["parsed_date"] = self.parse_date(e.get("timestamp",""))

        timeline = [e for e in timeline if e["parsed_date"] is not None]

        timeline.sort(key=lambda x: x["parsed_date"])

        return timeline


def build_timeline(case_path):
    engine = TimelineReconstructionEngine()

    documents = []
    events = []

    for root, dirs, files in os.walk(case_path):
        for f in files:
            if f.endswith(".json"):
                p = os.path.join(root,f)
                with open(p,"re") as file:
                    data = json.load(file)

                if "id" in data and "event" in data:
                    events.append(data)
                else:
                    documents.append(data)

    timeline = engine.reconstruct(events, documents)

    return timeline
