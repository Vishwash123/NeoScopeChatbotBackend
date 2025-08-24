import subprocess
import os

LLAMA_PATH = '/c/Users/Acer/Desktop/Integerating bots/llama.cpp/build/bin/llama-run.exe'
MODEL_PATH = '/c/Users/Acer/Desktop/Integerating bots/models/mistral/mistral.gguf'
WORKDIR = "C:/Users/Acer/Desktop/Integerating bots"
MSYS_BASH = "C:/msys64/usr/bin/bash.exe"

def generate_chat_response(prompt: str):
    safe_prompt = prompt.strip().replace('"', '\\"')
    prompt_text = f'<s>[INST] Prompt: {safe_prompt} [/INST]'
    bash_command = f'"{LLAMA_PATH}" "{MODEL_PATH}" "{prompt_text}"'
    try:
        result = subprocess.run(
            [MSYS_BASH, "-c", bash_command],
            cwd=WORKDIR,
            capture_output=True,
            text=True,
            env={"PATH": "/usr/bin:/mingw64/bin:/bin"}
        )
        if result.returncode != 0:
            return {"error": result.stderr.strip() or "Unknown error"}
        return {"response": result.stdout.strip() or "No response generated."}
    except Exception as e:
        return {"error": str(e)}
