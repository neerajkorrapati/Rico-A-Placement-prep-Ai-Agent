from pydantic import BaseModel
from typing import List

class InterviewRound(BaseModel):
    round_number: int
    round_name: str
    format: str
    focus_area: List[str]
class CompanyProfile(BaseModel):
    company_name: str
    tech_stack: List[str]
    difficulty_rating: str
    interview_rounds: List[InterviewRound]