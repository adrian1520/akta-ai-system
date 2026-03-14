import json

class LegalReasoningGraphEngine:

    def __init__(self):
        self.nodes = []
        self.relations = []

    def add_node(self, node_id, node_type, metadata=None):
        node = {
            "id": node_id,
            "type": node_type,
            "metadata": metadata or {}
        }
        self.nodes.append(node)

    def add_relation(self, source, target, relation_type):
        rel = {
            "from": source,
            "to": target,
            "type": relation_type
        }
        self.relations.append(rel)

    def build_from_case(self, documents, events, law):
        """Build reasoning graph from case data"""

        for d in documents:
            doc_id = f"DOC_{ d.get('id', id(d))}"
            self.add_node(doc_id, "CASE_DOCUMENT", d)

        for e in events:
            event_id = f"EVENT_{ e.get('id', id(e))}"
            self.add_node(event_id, "EVENT", e)

            for basis in e.get("legal_basis", []):
                law_id = f"LAW_{basis}"
                self.add_node(law_id, "LAW_ARTICLE")
                self.add_relation(event_id, law_id, "BASED_ON")

    def detect_argument_chains(self):
        """Detect potential legal argument chains from graph"""

        chains = []

        for rel in self.relations:
            if rel["type"] == "BASED_ON":
                chains.append({
                    "event": rel["from"],
                    "law": rel["to"],
                    "argument": f"Event {rel['from']} supports application of {rel['to']}"
                })

        return chains

    def export_graph(self, path):
        graph = {
            "nodes": self.nodes,
            "relations": self.relations
        }

        with open(path, "w") as f:
            json.dump(graph, f, indent=2)

        return graph
