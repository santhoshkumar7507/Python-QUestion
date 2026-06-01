def analyze_text(text):
    upper = 0
    lower = 0
    words = 0
    
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    words = len(text.split())
    total_chars = len(text)

    return upper, lower, total_chars, words


# Test cases
inputs = [
    "Functions could have no parameters",
    "FUNCTIONS COULD HAVE NO RETURN VALUE",
    "Functions Could Have Multiple Return Statements, But The Moment The First Return Is Executed, Control Exits From The Function",
    "FUNCTIONS have to be Defined before THEY are called. the function Call cannot come before the DEFINITION",
    "FUNCTION CALLS COULD BE USED IN EXPRESSIONS"
]

for line in inputs:
    result = analyze_text(line)
    print(*result)