from services.orchestrator import Orchestrator
import argparse
import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Distributed Multi-Agent Orchestration Framework')
    parser.add_argument('--llm-type', type=str, required=True, help='LLM type')
    parser.add_argument('--task-id', type=str, required=True, help='Task ID')
    parser.add_argument('--task-input', type=str, required=True, help='Task input')
    args = parser.parse_args()

    orchestrator = Orchestrator(args.llm_type)
    orchestrator.execute_task(args.task_id, {'input': args.task_input})
