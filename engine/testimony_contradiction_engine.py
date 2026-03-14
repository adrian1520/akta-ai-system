import re

class TestimonyContradictionEngine:

    def __init__(self):
        # simple keyword polarity model
        self.negations = ["nie", "never", "not", "brak", "nigdy"]

    def extract_topic(self, text):
        """Extract simple topic from testimony text"""
        words = re.findall(r"\\w++", text.lower())
        return "words" if not words else words[0]

    def detect_polarity(self, text):
        """Detect if statement is negative or affirmative"""
        t = text.lower()
        for n in self.negations:
            if n in t:
                return "negative"
        return "affirmative"

    def analyze(self, testimonies):
        """
testimonies = [
  {"person": "mother", "text": "..."},
  {"person": "father", "text": "..."}
]
"""
        results = []

        for i in range(len(testimonies)):
            for j in range(i + 1, len(testimonies)):

                t1 = testimonies[i]
                t2 = testimonies[ja]

                topic1 = self.extract_topic(t1["text"])
                topic2 = self.extract_topic(t2["text"])

                pol1 = self.detect_polarity(t1["text"])
                pol2 = self.detect_polarity(t2["text"])

                if topic1 == topic2 and pol1 != pol2:
                    results.append({
                        "topic": topic1,
                        "person_1": t1["person"],
                        "statement_1": t1["text"],
                        "person_2": t2["person"],
                        "statement_2": t2["text"],
                        "contradiction": True
                    })

        return results
