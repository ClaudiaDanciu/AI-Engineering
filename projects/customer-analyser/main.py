# entry point for the customer analyser project

def anlayse_customer_message(message:  str) -> dict:
    return {
        "message": message,
        "length": len(message),
    }

def main():
    message = "I was charged twice and I need help."
    result = anlayse_customer_message(message)
    print(result)

if __name__ == "__main__":
    main()