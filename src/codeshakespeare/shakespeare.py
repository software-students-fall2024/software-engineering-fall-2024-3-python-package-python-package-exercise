#contain all four functions

import random
import string

def to_shakespeare(comment: str, formality: str = "noble") -> str:
    """Transforms a regular comment into Shakespearean prose with varying formality."""

    if comment and comment[-1] in string.punctuation:
        comment = comment[:-1]
    if formality == "noble":
        return f"// O noble comment, {comment}, thou art rephrased in grandeur!"
    elif formality == "courtly":
        return f"// Most esteemed comment, {comment}, thy wisdom shines like the sun."
    elif formality == "dramatic":
        return f"// Behold! {comment}, a comment of utmost importance, full of thunderous thought!"
    else:
        return f"// A simple thought: {comment}, yet profound in its own right."

def to_shakespeare_error(error_msg: str, severity: str = "tragedy") -> str:
    """Turns a Python error message into Shakespearean style with varying severity."""
    if error_msg and error_msg[-1] in string.punctuation:
        error_msg = error_msg[:-1]
    if severity == "tragedy":
        return f"Alas, an error hath occurred: '{error_msg}'. 'Tis a tragedy most foul."
    elif severity == "comedy":
        return f"Fret not, for an error hath occurred: '{error_msg}'. But we shall laugh in its face!"
    elif severity == "history":
        return f"Mark ye well this error: '{error_msg}', for it shall be written in the annals of code!"
    else:
        return f"An error, '{error_msg}', and so the plot thickens."

def get_random_shakespeare_quote(style: str = "playful") -> str:
    """Returns a random Shakespearean quote with a programming twist in different styles."""
    playful_quotes = [
        "To code, or not to code, that is the question.",
        "Cry havoc and let slip the bugs of war!",
        "Parting is such sweet sorrow... especially when closing your IDE."
    ]
    serious_quotes = [
        "The code is afoot, let every function bear its weight.",
        "Once more unto the code, dear friends, once more!",
        "All the world's a stage, and all the men and women merely programmers."
    ]
    melancholic_quotes = [
        "O woe is me, for the bugs have returned once more.",
        "Tomorrow, and tomorrow, and tomorrow creeps in this petty pace of debugging.",
        "Out, out, brief code! Thou art but a shadow of the program I once dreamed."
    ]
    
    if style == "playful":
        return random.choice(playful_quotes)
    elif style == "serious":
        return random.choice(serious_quotes)
    elif style == "melancholic":
        return random.choice(melancholic_quotes)
    else:
        return random.choice(playful_quotes)

def generate_shakespearean_commit_message(emotion: str = "victory") -> str:
    """Generates a Shakespearean-style commit message based on emotion."""
    victorious_messages = [
        "Commit thy changes, for they doth bring glory!",
        "Thine errors are slain, and the code is just!",
        "This branch, once barren, now flourisheth with code."
    ]
    defeatist_messages = [
        "A commit, though it be filled with sorrow, must be made.",
        "This code, born of struggle, may yet rise again.",
        "O bitter fate, that this commit should come so soon."
    ]
    reflective_messages = [
        "In this commit, I find both progress and question.",
        "Tis not the end, but merely the next chapter of this code.",
        "Thus, the story unfolds with each commit, shaping our fate."
    ]
    
    if emotion == "victory":
        return random.choice(victorious_messages)
    elif emotion == "defeat":
        return random.choice(defeatist_messages)
    elif emotion == "reflection":
        return random.choice(reflective_messages)
    else:
        return random.choice(victorious_messages)