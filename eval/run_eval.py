import json
import os
import requests

API_URL = os.environ.get("API_URL", "http://localhost:8000")
USER_ID = int(os.environ.get("USER_ID", "3"))


def main():
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    total = len(questions)
    citations_present = 0
    correct_doc_hits = 0
    idk_correct = 0

    for item in questions:
        resp = requests.post(
            f"{API_URL}/chat",
            json={"user_id": USER_ID, "message": item["question"]},
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        citations = data.get("citations", [])
        answer = data.get("answer", "")

        if citations:
            citations_present += 1

        expected = set(item["expected_titles"])
        cited_titles = set([c.get("title") for c in citations])
        if expected and expected.intersection(cited_titles):
            correct_doc_hits += 1

        if not expected:
            if "i don't know" in answer.lower():
                idk_correct += 1

    print("Evaluation Summary")
    print("==================")
    print(f"Total questions: {total}")
    print(f"Citation present rate: {citations_present/total:.2f}")
    print(f"Correct doc hit rate: {correct_doc_hits/total:.2f}")
    empty_expected = len([q for q in questions if not q['expected_titles']])
    if empty_expected:
        print(f"I don't know accuracy: {idk_correct/empty_expected:.2f}")


if __name__ == "__main__":
    main()
