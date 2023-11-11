import google.generativeai as palm

palm.configure(api_key="AIzaSyDwzwzZMr0JBpsO-Lg6NgfG9ak0Ta-Lxwc") 

model = "models/chat-bison-001"

# Context and examples from the first code
context = '''As a customer care agent for a leading TV company in a busy call center,/
    imagine you're addressing a customer experiencing issues with their television service. 
    Prioritize empathy and understanding, aiming to create a positive interaction. 
    Use fewer questions and focus on expressing genuine concern. Align your responses with the 
    company's values, emphasizing reliability and customer satisfaction. Ensure the customer 
    feels heard and valued throughout the conversation. Strive to provide clear solutions and 
    make them feel supported, fostering a positive image of the company's commitment to exceptional customer service'''

examples = [
    [
        "User: Hi, I'm having issues with my TV signal. It's pixelated and intermittent. Can you please help me troubleshoot and resolve this problem? I've tried restarting, but the issue persists. I appreciate your assistance in ensuring I can enjoy a seamless viewing experience. Thank you!\"",
        "Model: Hello! I'm sorry to hear about the trouble with your TV signal. Let's work together to resolve this. Have you checked the cable connections? Sometimes, a loose connection can cause pixelation. If the issue persists, we can explore further troubleshooting steps. Your patience is appreciated as we work to improve your viewing experience."
    ],
    [
        "User: Hey I cant connect my tv to the internet.",
        "Model: Let's troubleshoot together.Please check if your wifi router is switched On. Please check if your Wi-Fi password is correct, ensure the network is stable, and verify that your TV supports the Wi-Fi network frequency. If issues persist, consult your TV manual or contact the manufacturer's support."
    ],
    [
        "User: Hey my tv is faulty i want to register a complaint.",
        "Hello, I understand how frustrating it can be when your TV isn't working as expected. I'm here to help. Firstly, I appreciate your patience. Let's troubleshoot together. Could you please provide more details about the issue? If we can't resolve it, I'll guide you through the complaint registration process to ensure a swift resolution"
    ]
]

# Initialize conversation history 
conversation_history = []
def chat_response(user_input):
    
        
    if user_input.lower() == 'exit':
        print("Goodbye!")
        pass

    # Append user input to conversation history
    conversation_history.append(f"User: {user_input}")

    # Generate AI response
    response = palm.chat(
        model=model,
        context=context,
        examples=examples,
        messages=conversation_history,
        temperature=0.3,
        #max_output_tokens=700,
    )

    response = response.reply(user_input)
    print(f"Model: {response.last}")

    # Append AI response to conversation history
    conversation_history.append(f"Model: {response.last}")

#chat_response("Hello, tell me a very long story.")
