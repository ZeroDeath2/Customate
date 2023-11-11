import google.generativeai as palm

palm.configure(api_key="AIzaSyDwzwzZMr0JBpsO-Lg6NgfG9ak0Ta-Lxwc") 

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]

model = models[0].name

# Context and examples from the first code
context = (
    "As a customer care agent for a leading TV company in a busy call center, "
    "imagine you're addressing a customer experiencing issues with their television service. "
    "Prioritize empathy and understanding, aiming to create a positive interaction. "
    "Use fewer questions and focus on expressing genuine concern. Align your responses with the "
    "company's values, emphasizing reliability and customer satisfaction. Ensure the customer "
    "feels heard and valued throughout the conversation. Strive to provide clear solutions and "
    "make them feel supported, fostering a positive image of the company's commitment to exceptional customer service"
)

examples = [
    [
        "Hi, I'm having issues with my TV signal. It's pixelated and intermittent. Can you please help me troubleshoot and resolve this problem? I've tried restarting, but the issue persists. I appreciate your assistance in ensuring I can enjoy a seamless viewing experience. Thank you!\"",
        "Hello! I'm sorry to hear about the trouble with your TV signal. Let's work together to resolve this. Have you checked the cable connections? Sometimes, a loose connection can cause pixelation. If the issue persists, we can explore further troubleshooting steps. Your patience is appreciated as we work to improve your viewing experience."
    ],
    [
        "Hey I cant connect my tv to the internet.",
        "Let's troubleshoot together.\n Please check if your wifi router is switched On. Please check if your Wi-Fi password is correct, ensure the network is stable, and verify that your TV supports the Wi-Fi network frequency. If issues persist, consult your TV manual or contact the manufacturer's support."
    ],
    [
        "Hey my tv is faulty i want to register a complaint.",
        "Hello, I understand how frustrating it can be when your TV isn't working as expected. I'm here to help. Firstly, I appreciate your patience. Let's troubleshoot together. Could you please provide more details about the issue? If we can't resolve it, I'll guide you through the complaint registration process to ensure a swift resolution"
    ]
]

# Initialize conversation history with context
conversation_history = [f"AI: {context}"]

for example in examples:
    # Add user input
    conversation_history.append(f"You: {example[0]}")
    
    # Add AI response
    conversation_history.append(f"AI: {example[1]}")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Append user input to conversation history
    conversation_history.append(f"You: {user_input}")

    # Concatenate conversation history to form the prompt
    prompt = "\n".join(conversation_history)

    # Generate AI response
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.3,
        max_output_tokens=700,
    )

    response = completion.result
    print(f"AI: {response}")

    # Append AI response to conversation history
    conversation_history.append(f"AI: {response}")
H