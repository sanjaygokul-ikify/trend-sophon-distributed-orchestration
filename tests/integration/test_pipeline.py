from cli.main import main
import unittest
import logging

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        logging.basicConfig(level=logging.INFO)
        parser = main.parser
        args = parser.parse_args(['--llm-type', 'Codex', '--task-id', 'test_task', '--task-input', 'test_input'])
        main.main(args)

if __name__ == '__main__':
    unittest.main()