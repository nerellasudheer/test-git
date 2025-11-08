def greet(name):
    """Prints a greeting message using the provided name."""
    print(f"Hello {name}, welcome!")


def ask_name(name):
    """Calls the greet function and then returns the name."""
    greet(name)  # Pass the name argument to the greet function
    return name


# Call the function, which will first print the greeting, then return 'sudheer'
returned_name = ask_name("Sudheer")
print(f"The name returned from ask_name is: {returned_name}")
