from packages.core import InferenceEngine, TaskScheduler, TransactionalMemoryStore
import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self, llm_type: LLMType):
        self.inference_engine = InferenceEngine(llm_type)
        self.task_scheduler = TaskScheduler()
        self.memory_store = TransactionalMemoryStore()

    def execute_task(self, task_id: str, task_input: Dict) -> None:
        self.task_scheduler.schedule_task(task_id, task_input)
        self.inference_engine.execute_task(task_id, task_input)
        task_result = self.inference_engine.get_task_result(task_id)
        self.memory_store.write(task_id, task_result)
