from IPython.display import clear_output

previous_output = ""

while True:
    user_input = input("Enter something: ")
    clear_output(wait=True)  # Clear the previous output
    
    # Combine the new input with the previous output
    output_to_display = f"You entered: {user_input}"
    print(output_to_display)
    
    # Update the previous output with the current output
    previous_output = output_to_display