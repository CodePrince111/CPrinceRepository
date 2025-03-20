import json
import re

def extract_solution(
    llm_response: str, # Must be a raw string
    include_markers: bool = False,
    prefix: str = "" # Optional: A directory path to prepend to each extracted file path
) -> list[tuple[str, str]]:

    try:
        json_match = re.search(r"```json\s*\n(.*?)\n```", llm_response, re.DOTALL)
        if json_match:
            json_data = json.loads(json_match.group(1))
        else:
            json_data = json.loads(llm_response)
            
        if "file_path" not in json_data or "code" not in json_data:
            raise ValueError("Missing 'file_path' or 'code' in the JSON response.")

        file_path = json_data["file_path"].strip()
        code = json_data["code"].strip()

        # Construct full path if prefix is provided
        full_file_path = f"{prefix}/{file_path.lstrip('/')}" if prefix else file_path
        full_file_path = re.sub(r'[^a-zA-Z0-9/._-]', '', full_file_path)  # Sanitize path

        if include_markers:
            return [(full_file_path, f"```tsx\n{code}\n```")]
        else:
            return [(full_file_path, code)]
    
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in LLM response.")
