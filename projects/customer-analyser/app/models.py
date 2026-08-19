# Pydantic input/output models 

from enum import Enum
from pydantic import BaseModel

class Category(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    OTHER = "other"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"

class CustomerAnalysis(BaseModel):
    category: Category
    priority: Priority
    sentiment: Sentiment
    requires_human: bool
    summary: str