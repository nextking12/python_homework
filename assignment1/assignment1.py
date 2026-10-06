#TASK 1
def hello():
    return "Hello!"
   
 #TASK 2
def greet(name):
    return f"Hello, {name}!"

#TASK 3
def calc(a, b, c = "multiply"):
    try:
        match c:
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "add":
                return a + b
            case "subtract":
                    return a - b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b 
            case "power":
                return a ** b

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#TASK 4
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "int":
                return int(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
         
#TASK 5
def grade(*args):
   try:
        if sum(args) / len(args) >= 90:
            return "A"
        elif sum(args) / len(args) >=80:
            return "B"
        elif sum(args) / len(args) >= 70:
            return "C"
        elif sum(args) / len(args) >= 60:
            return "D"
        elif sum(args) / len(args) < 60:
            return "F"
   except TypeError:
       return "Invalid data was provided."
    
#TASK 6
def repeat (string, count):
    result = ""
    for c in range(count):
        result += string
    return result
            
#TASK 7
def student_scores(mode, **kwargs):
    if mode == "mean":
        total = 0
        for key, value in kwargs.items():
            total += value
        return total / len(kwargs)

    elif mode == "best":
        best_name = None
        best_score = -1
        for key, value in kwargs.items():
            if value > best_score:
                best_score = value
                best_name = key
        return best_name

#TASK 8
#TASK 8
def titleize(s):
    little = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = s.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    return " ".join(words) 

#TASK 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

#TASK 10
def pig_latin(sentence):
    vowels = "aeiou"
    out = []
    for word in sentence.split():
        if word[0] in vowels:
            out.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i] == "q" and i + 1 < len(word) and word[i+1] == "u":
                    i += 2
                    break
                i += 1
            out.append(word[i:] + word[:i] + "ay")
    return " ".join(out)

