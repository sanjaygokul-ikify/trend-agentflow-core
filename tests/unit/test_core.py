from packages.core import SpeculationEngine, AgentTask, PersistentMemory, SpeculationError
import unittest


class TestSpeculationEngine(unittest.TestCase):
    def test_speculate(self):
        persistent_memory = PersistentMemory()
        speculation_engine = SpeculationEngine(persistent_memory)
        task = AgentTask(agent_id=1, task_id=1, task_data=b'test_data')
        result = speculation_engine.speculate(task)
        self.assertTrue(result)

    def test_speculate_failure(self):
        persistent_memory = PersistentMemory()
        speculation_engine = SpeculationEngine(persistent_memory)
        task = AgentTask(agent_id=1, task_id=1, task_data=b'test_data')
        with self.assertRaises(SpeculationError):
            speculation_engine.speculate(task)

if __name__ == '__main__':
    unittest.main()
