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