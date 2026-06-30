import unittest
from packages.cli.main import main
from packages.core import AgentTask
from packages.services.orchestrator import Orchestrator
from packages.utils.logging import get_logger


class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        # create a test task
        task = AgentTask(agent_id=1, task_id=1, task_data=b'test_data')
        # run the pipeline
        orchestrator = Orchestrator(PersistentMemory())
        logger = get_logger(__name__)
        result = orchestrator.run(task)
        logger.info('Pipeline result', result=result)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
