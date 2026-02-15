class RiskEngine:

    def calculate(self, metrics):
        return (
            0.3 * metrics["business_value"] +
            0.2 * metrics["code_churn"] +
            0.2 * metrics["defect_history"] +
            0.15 * metrics["dependency_impact"] +
            0.15 * metrics["traffic"]
        )

    def prioritize(self, stories):
        return sorted(stories, key=lambda s: s["risk_score"], reverse=True)
