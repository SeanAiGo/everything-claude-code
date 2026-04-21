import sys
from pathlib import Path
from unittest.mock import MagicMock

# Mock dependencies before any llm imports
sys.modules["anthropic"] = MagicMock()
sys.modules["openai"] = MagicMock()

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
