import logging
from typing import Dict, List
from packages.core.engine import InferenceEngine
from packages.core.types import LLMType, TaskStatus
from packages.core.exceptions import EngineInitializationError

logger = logging.getLogger(__name__)

class RuntimeExecutor:
    def __init__(self, llm_type: LLMType):
        self.llm_type = llm_type
        self.inference_engine = InferenceEngine(llm_type)

    def execute_task(self, task_id: str, task_input: Dict):
        logger.info(f"Executing task {task_id} with input: {task_input}")
        try:
            self.inference_engine.execute_task(task_id, task_input)
        except EngineInitializationError as e:
            logger.error(f"Error executing task {task_id}: {e}")
        except Exception as e:
            logger.error(f"Error executing task {task_id}: {e}")
            raise
        else:
            logger.info(f"Task {task_id} execution complete")

    def get_task_result(self, task_id: str):
        logger.info(f"Getting result for task {task_id}")
        try:
            task_result = self.inference_engine.get_task_result(task_id)
        except EngineInitializationError as e:
            logger.error(f"Error getting result for task {task_id}: {e}")
        except Exception as e:
            logger.error(f"Error getting result for task {task_id}: {e}")
            raise
        else:
            logger.info(f"Result for task {task_id}: {task_result}")
            return task_result

    def __str__(self):
        return f"RuntimeExecutor(llm_type={self.llm_type}, inference_engine={self.inference_engine})"