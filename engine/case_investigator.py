import json
import os

class CaseInvestigator:

    def __init__(self, law_index, retriever, error_detector, strategy_engine):
        self.law_index = law_index
        self.retriever = retriever
        self.error_detector = error_detector
        self.strategy_engine = strategy_engine

    def load_case(self, case_path):
        docs = []
        events = []

        for root, dirs, files in os.walk(case_path):
            for f in files:
                if f.endswith(".json"):
                    path = os.path.join(root, f)
                    with open(path, "r") as f:
                        data = json.load(f)

                    if "event" in data:
                        events.append(data)
                    else:
                        docs.append(data)

        return docs, events

    def analyze_case(self, case_path):
        docs, events = self.load_case(case_path)

        report = []

        for event in events:
            errors = self.error_detector.detect(event, docs)

            if errors:
                strategy = self.strategy_engine.generate(
                    problem=",".join(errors),
                    law=event.get("legal_basis", []),
                    evidence=docs
                )

                report.append({
                    "event": event.get("event"),
                    "errors": errors,
                    "strategy": strategy
                })

        return report


def run_investigation(case_path, investigator):
    result = investigator.analyze_case(case_path)
    print(json.dumps(result, indent=2))
