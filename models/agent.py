from models.enums import AgentStatus

class agent:
    def __init__(
            self,
            code_name: str,
            real_name: str,
            location: str,
            status: str = 'active',
            missions_completed: int = 0,
            _id:int = None
    ):
        self.code_name:str = code_name
        self.real_name:str = real_name
        self.location:str = location
        self.status:AgentStatus = self.validate_status(status)
        self.missions_completed:int = missions_completed
        self.id:int| None = _id

    @staticmethod
    def validate_status(status: str) -> AgentStatus:
        if not isinstance(status, str):
            raise TypeError(f"Status must be a string, got {type(status).__name__}")
        status_name = status.upper()
        if status_name in AgentStatus.__members__:
            return AgentStatus[status_name]
        else:
            raise ValueError(f"Invalid status '{status}'. Must be one of {list(AgentStatus.__members__.keys())}")

    def __str__(self):
        if self.id is not None:
            return f"Agent({self.id}): {self.code_name} - {self.real_name} at {self.location} with status {self.status}"
        return f"Agent: {self.code_name} - {self.real_name} at {self.location} with status {self.status}"