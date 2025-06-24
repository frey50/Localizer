from pipeline import uzbek_chatbot_pipeline

print("🌐 Uzbek-English Chatbot | Type 'q' to quit\n")
while True:
    user_input = input("👤 > ")
    if user_input.lower().strip() == 'q':
        break
    uzbek_chatbot_pipeline(user_input)
    print()
