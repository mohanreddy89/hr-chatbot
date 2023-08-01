import streamlit as st
import regex as re 

# A simple dictionary to store responses for different keywords
responses = {
    "payroll": "Your payroll is processed on a monthly basis.",
    "salary slips": "You can access your salary slips through our employee portal.",
    "attendance logs": "We maintain attendance logs using our biometric system.",
    "employee status": "To check your employee status, please provide your employee ID.",
    "expenses": "You can submit your expense report to the finance department.",
}

def find_response(user_input):
    for keyword, response in responses.items():
        if re.search(rf"\b{keyword}\b", user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't have information on that topic."

def main():
    st.title("HR Chatbot")
    user_input = st.text_input("Ask your question here...")

    if st.button("Send"):
        if user_input.strip():
            st.markdown("**You:** " + user_input)
            response = find_response(user_input)
            st.markdown("**HR Bot:** " + response)

if __name__ == "__main__":
    main()
