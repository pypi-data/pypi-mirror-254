from typing import Any, Dict

import toml


def load_settings_from_file(setting_file_path: str) -> Dict[str, Any]:
    with open(setting_file_path, "r", encoding="utf-8") as toml_content:
        cleaned_content = toml_content.read().replace("#:schema", "# ")
        return toml.loads(cleaned_content)
