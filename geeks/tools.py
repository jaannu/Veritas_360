import os
import requests
MOCK = os.environ.get("MOCK_OLLAMA", "false").lower() == "true"

class OllamaLLM:
    def run(self, prompt):
        if MOCK:
            return f"💡 Simulated response for:\n\n{prompt[:150]}...\n\n(This is a mock output for deployment purposes.)"
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3", "prompt": prompt, "stream": False},
                timeout=30
            )
            if response.status_code == 200:
                return response.json()['response']
            else:
                return f"❌ Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"❌ Exception: {str(e)}"


class WebScraperTool:
    def run(self, query): return f"🔎 Mocked web data for: {query}" if MOCK else f"Web data for: {query}"


class APIClientTool:
    def run(self, query): return f"🔌 Mocked API result for: {query}" if MOCK else f"API results for: {query}"


class CustomMLModel:
    def run(self, query): return f"🧠 Mocked ML insights for: {query}" if MOCK else f"ML Insights for: {query}"
