# AI/LM logic 

from app.models import (
    Category,
    CustomerAnalysis,
    Priority,
    Sentiment,
)

def analyse_customer_message(message: str) -> CustomerAnalysis:
    return CustomerAnalysis(
        category=Category.BILLING,
        priority=Priority.HIGH,
        sentiment=Sentiment.NEGATIVE,
        requires_human=True,
        summary=message,
    )