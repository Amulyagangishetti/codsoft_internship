import random

# Define a dictionary of rules and responses
dl_definitions = {

    "Deep Learning": "A subset of machine learning that uses artificial neural networks to model and understand complex patterns in data with the goal of making accurate predictions.",

    "Neural Network":"A computational model inspired by the structure of the human brain, consisting of interconnected nodes (neurons) organized in layers that process and transmit information.",

    "Artificial Neuron": "A computational unit in a neural network that receives inputs, applies weights and biases, and computes an output using an activation function.",

    "Activation Function": "A mathematical function that determines the output of a neuron, allowing neural networks to learn complex patterns by introducing non-linearities into the model.",

    "Training Data": "The data used to train a deep learning model, typically labeled with the correct output or target values, enabling the model to learn the patterns and relationships within the data.",

    "Loss Function": "A measure of the inconsistency between the predicted output of a model and the actual target output, guiding the model to make adjustments during training to minimize errors.",

    "Backpropagation": "A key algorithm in training neural networks that calculates the gradients of the loss function with respect to the network's weights, allowing the model to adjust its parameters to minimize the loss.",

    "Gradient Descent": "An optimization algorithm used to minimize the loss function by adjusting the parameters in the direction of the steepest descent of the loss.",

    "Overfitting": "A phenomenon where a model learns the training data too well, capturing noise or random fluctuations, leading to poor generalization and performance on unseen data.",

    "Underfitting": "A condition where a model is too simple to capture the underlying patterns in the data, resulting in poor performance on both the training and test data.",

    "Epoch": "One complete pass through the entire training dataset during the training of a deep learning model.",

    "Batch Size": "The number of training examples utilized in one iteration of the gradient descent algorithm.",

    "Learning Rate": "A hyperparameter that determines the step size at each iteration while moving toward a minimum of the loss function during the training of the model.",

    "Dropout": "A technique used to prevent overfitting in neural networks by randomly disabling a fraction of the neurons during training.",

    "Convolutional Neural Network (CNN)": "A type of deep learning architecture particularly effective for processing grid-like data, such as images, using convolutional layers to automatically learn hierarchical representations.",

    "Recurrent Neural Network (RNN)": "A type of neural network designed to work with sequence data by maintaining an internal state, allowing it to exhibit temporal dynamic behavior and learn dependencies over time.",
    






}

# Define a function to generate responses based on user input
def get_response(user_input):
    user_input = user_input.strip()
    for rule, response in dl_definitions.items():
        if user_input.lower() == rule.lower():
            return response
    return "I'm sorry, I don't have information on that specific topic. Please ask about a different aspect of AI."

# Main loop to interact with the chatbot
print("AI Guide Chatbot: Hello! How can I assist you with information about AI?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI Guide Chatbot: Goodbye! If you have more questions in the future, feel free to return.")
        break
    response = get_response(user_input)
    print("AI Guide Chatbot:", response)