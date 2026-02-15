from bs4 import BeautifulSoup
from difflib import SequenceMatcher

class SelfHealingEngine:

    def similarity(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def find_best_match(self, failed_selector, page_content):
        soup = BeautifulSoup(page_content, "html.parser")

        candidates = soup.find_all(True)

        best_score = 0
        best_element = None

        for element in candidates:
            attrs = " ".join([str(v) for v in element.attrs.values()])
            score = self.similarity(failed_selector, attrs)

            if score > best_score:
                best_score = score
                best_element = element

        if best_score > 0.75:
            return best_element, best_score

        return None, 0
