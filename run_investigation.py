import json
import sys

from engine.case_investigator import CaseInvestigator
from engine.error_detector import ErrorDetector
from engine.strategy_engine import StrategyEngine


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_investigation.py <case_path>")
        return

    case_path = sys.argv[1]

    investigator = CaseInvestigator(
        law_index="law",
        retriever=None,
        error_detector=ErrorDetector({}),
        strategy_engine=StrategyEngine()
    )

    report = investigator.analyze_case(case_path)

    with open("investigation_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("Investigation complete. See investigation_report.json")


if __name__ == "__main__":
    main()
