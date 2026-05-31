from packages.core import InferenceEngine, TaskScheduler, TransactionalMemoryStore
import unittest

class TestRuntime(unittest.TestCase):
    def test_inference_engine_exception(self):
        llm_type = 'Invalid'
        with self.assertRaises(Exception):
            InferenceEngine(llm_type)

    def test_task_scheduler_exception(self):
        scheduler = TaskScheduler()
        task_id = 'test_task'
        task_input = None
        with self.assertRaises(Exception):
            scheduler.schedule_task(task_id, task_input)

    def test_transactional_memory_store_exception(self):
        store = TransactionalMemoryStore()
        task_id = 'test_task'
        task_result = None
        with self.assertRaises(Exception):
            store.write(task_id, task_result)

if __name__ == '__main__':
    unittest.main()