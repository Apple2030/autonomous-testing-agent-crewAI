import subprocess
import json

class ExecutionAgent:

    def run_tests(self):
        subprocess.run(["npx", "playwright", "test", "--reporter=json"], check=False)

        with open("playwright-report/results.json") as f:
            results = json.load(f)

        return results
