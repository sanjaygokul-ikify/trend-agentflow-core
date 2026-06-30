from dataclasses import dataclass
from typing import Optional

@dataclass
class AgentTask:
    agent_id: int
    task_id: int
    task_data: bytes

@dataclass
class AgentState:
    agent_id: int
    state_data: bytes