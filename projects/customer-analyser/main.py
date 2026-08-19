# entry point for the customer analyser project
from app.analyser import analyse_customer_message

def main():
    message = "I was charged twice and I need help."
    result = analyse_customer_message(message)
    print(result.model_dump_json(indent=2))

if __name__ == "__main__":
    main()