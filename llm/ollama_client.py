import subprocess

def run_ollama(prompt: str, model: str = "mistral") -> str:
    result = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
