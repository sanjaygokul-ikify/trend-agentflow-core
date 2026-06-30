import unittest
from packages.core import AgentState


class TestRuntime(unittest.TestCase):
    def test_agent_state(self):
        agent_state = AgentState(agent_id=1, state_data=b'test_state')
        self.assertEqual(agent_state.agent_id, 1)
        self.assertEqual(agent_state.state_data, b'test_state')

if __name__ == '__main__':
    unittest.main()
