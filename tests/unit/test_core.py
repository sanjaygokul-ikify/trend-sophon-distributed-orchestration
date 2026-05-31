from packages.core import InferenceEngine, TaskScheduler, TransactionalMemoryStore
import unittest

class TestCore(unittest.TestCase):
    def test_inference_engine(self):
        llm_type = 'Codex'
        engine = InferenceEngine(llm_type)
        task_id = 'test_task'
        task_input = {'input': 'test_input'}
        engine.execute_task(task_id, task_input)
        self.assertEqual(engine.get_task_result(task_id), None)

    def test_task_scheduler(self):
        scheduler = TaskScheduler()
        task_id = 'test_task'
        task_input = {'input': 'test_input'}
        scheduler.schedule_task(task_id, task_input)
        self.assertIn(task_id, scheduler.get_scheduled_tasks())

    def test_transactional_memory_store(self):
        store = TransactionalMemoryStore()
        task_id = 'test_task'
        task_result = {'result': 'test_result'}
        store.write(task_id, task_result)
        self.assertEqual(store.read(task_id), task_result)

if __name__ == '__main__':
    unittest.main()