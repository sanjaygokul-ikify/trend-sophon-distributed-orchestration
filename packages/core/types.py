from enum import Enum
from typing import Dict

class LLMType(Enum):
    Codex = 1
    Claude = 2
    Gemini = 3

class TaskStatus(Enum):
    PENDING = 1
    COMPLETE = 2

class TaskResult:
    def __init__(self, task_id: str, task_input: Dict, task_output: Dict):
        self.task_id = task_id
        self.task_input = task_input
        self.task_output = task_output
