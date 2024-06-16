
def response_generator(chain, prompt):
    try:
        return chain.invoke(prompt)['text']
    except Exception as e:
        print(f"Error occured at response_generator {e}")
        return "Sorry i could not process your request"