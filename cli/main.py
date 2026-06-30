import argparse
from packages.core import AgentTask
from services.orchestrator import Orchestrator
from packages.utils.logging import get_logger


def main():
    parser = argparse.ArgumentParser(description='Run the orchestrator')
    parser.add_argument('--task-id', type=int, required=True)
    parser.add_argument('--agent-id', type=int, required=True)
    args = parser.parse_args()
    task = AgentTask(agent_id=args.agent_id, task_id=args.task_id, task_data=b'test_data')
    orchestrator = Orchestrator(PersistentMemory())
    logger = get_logger(__name__)
    logger.info('Running orchestrator')
    result = orchestrator.run(task)
    logger.info('Orchestrator result', result=result)

if __name__ == '__main__':
    main()
