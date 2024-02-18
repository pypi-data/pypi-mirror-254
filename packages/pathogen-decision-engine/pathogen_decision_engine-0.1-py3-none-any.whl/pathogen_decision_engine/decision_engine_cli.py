import argparse
import json
from pathogen_decision_engine.pathogen_decision_engine import PathogenDecisionEngine


def main():
    parser = argparse.ArgumentParser(description='Decision Engine CLI')
    parser.add_argument('--rule_table_path', type=str, help='Input rule table for inference', required=True)
    parser.add_argument('--input_dict', type=str, help='Dictionary as a JSON string', required=True)
    args = parser.parse_args()

    # Parse inputs
    input_dict = args.input_dict
    rule_table_path = args.rule_table_path

    try:
        input_dict = json.loads(args.input_dict)
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Error: Invalid JSON string for dictionary.")

    # Perform inference
    decision_engine = PathogenDecisionEngine(rule_table_path)
    result = decision_engine.infer(input_dict)
    print(result)


if __name__ == '__main__':
    main()