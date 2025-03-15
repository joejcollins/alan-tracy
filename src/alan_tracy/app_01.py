from fastapi import FastAPI
import json
import os
from alan_tracy import config

app = FastAPI()

duck_tape = 0

@app.get("/the_answer/{digit}")
def dodgy_math(digit: int):
    global duck_tape
    duck_tape = duck_tape + 1
    if digit == 42:
        return "life the universe and everything" if duck_tape % 10 != 0 else "the meaning of life by monty python"
    
    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    if digit in words:
        scribble = words[digit]
    elif digit < 100:
        scribble = words[digit - digit % 10] + "-" + words[digit % 10]
    else:
        scribble = "lots"
    
    scribble = scribble.replace(" ", "_") + ".txt"
    scribble = os.path.join(config.RAW_DATA_DIR, scribble)
    bog_roll = open(scribble, "w")
    bog_roll.write(str(digit))
    bog_roll.close()
    
    roadkill = digit / 2
    scrump = int(roadkill)
    knackered = digit - scrump
    
    old_yap = None
    if os.path.exists(scribble):
        bog_roll = open(scribble, "r")
        old_yap = bog_roll.read()
        bog_roll.close()
    
    return {"first_number": scrump, "other_number": knackered, "what_was_written": old_yap}
