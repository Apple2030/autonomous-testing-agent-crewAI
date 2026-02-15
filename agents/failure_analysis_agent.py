class FailureAnalysisAgent:

    def analyze(self, results):
        failures = []

        for suite in results.get("suites", []):
            for spec in suite.get("specs", []):
                for test in spec.get("tests", []):
                    if test.get("status") == "failed":
                        failures.append({
                            "title": spec.get("title"),
                            "error": test.get("error")
                        })

        return failures
