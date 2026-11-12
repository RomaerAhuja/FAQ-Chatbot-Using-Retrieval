import pandas as pd

from src.similarity import FAQSimilarity


class RetrievalEvaluator:

    def __init__(self):

        self.engine = FAQSimilarity()

    def evaluate(self, test_queries):

        results = []

        for item in test_queries:

            query = item["query"]

            expected_id = item["expected_id"]

            ranked = self.engine.rank_faqs(
                query,
                top_n=5
            )

            if not ranked:
                continue

            predicted_id = ranked[0]["id"]

            top_3_ids = [
                result["id"]
                for result in ranked[:3]
            ]

            results.append({

                "query": query,

                "expected_id": expected_id,

                "predicted_id": predicted_id,

                "top_1_correct": predicted_id == expected_id,

                "top_3_correct": expected_id in top_3_ids,

                "similarity": ranked[0]["similarity"]

            })

        return pd.DataFrame(results)

    @staticmethod
    def calculate_metrics(results):

        if results.empty:
            return {}

        return {

            "total_queries": len(results),

            "top_1_accuracy": round(
                results["top_1_correct"].mean() * 100,
                2
            ),

            "top_3_accuracy": round(
                results["top_3_correct"].mean() * 100,
                2
            )

        }


if __name__ == "__main__":

    evaluator = RetrievalEvaluator()

    # Replace these IDs with IDs from your actual dataset.
    test_queries = [
        {
            "query": "What is cybersecurity?",
            "expected_id": 1
        }
    ]

    results = evaluator.evaluate(test_queries)

    print(results)

    print("\nEvaluation Metrics:")

    print(evaluator.calculate_metrics(results))