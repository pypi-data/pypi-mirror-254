from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class UserFlowStep:
    user_uid: str
    step_identifier: str
    step_data: str
    timestamp: datetime.datetime
    
    uid: Optional[str] = None