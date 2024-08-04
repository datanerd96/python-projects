import random  # Import the random module to generate random numbers

# Define the name and question
name = "Jedidja"
question = "Are you going to pass the exam?"

# Initialize the answer variable
answer = ""

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Print the random number for debugging purposes (currently commented out)
#print(random_number)

# Determine the Magic 8-Ball's answer based on the random number
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Print the question and the Magic 8-Ball's answer
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)

# Check if name or question are empty and print appropriate messages
if name == "":
    print(question)
else:
    print(name + " asks: " + question)

if question == "":
    print("Ask a question.")
else: 
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)

