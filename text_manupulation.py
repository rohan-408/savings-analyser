# For converting 2D array into 1D list
def flatten(t):
    return [item for sublist in t for item in sublist]

# for Converting a list into a string (for easy to read print statements)
def list_to_string(a):  # for printing a list as single string
  return (", ".join(a))