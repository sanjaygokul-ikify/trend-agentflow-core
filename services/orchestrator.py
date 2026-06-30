from packages.core import SpeculationEngine, PersistentMemory


class Orchestrator:
    def __init__(self, persistent_memory: PersistentMemory):
        self.speculation_engine = SpeculationEngine(persistent_memory)

    def run(self, task: AgentTask) -> bool:
        return self.speculation_engine.speculate(task)

    def get_status(self, task: AgentTask) -> str:
        return self.speculation_engine.get_speculation_status(task)
