# -*- coding: utf-8 -*-

# ENGLISH

neutral = [
    "It works on my machine, but maybe the server environment is different.",
]

javascript = [
    "The CSS is fighting with JavaScript again.",
    "It's probably because the code's running in sloppy mode instead of strict mode.",
]

python = [
    "It must be a Python 2 vs. Python 3 issue.",
    "The virtual environment must be acting up.",
    "It worked when I ran it without pytest.",
]

matlab = [ 
    "It's a rounding error—MATLAB loves its floating-point precision.",
    "It might be a matrix dimension mismatch. MATLAB is picky about that.",
    "I think MATLAB's licensing server must be down again.",
]

jokes_en = {
    "neutral": neutral,
    "python": python,
    "javascript": javascript,
    "matlab": matlab,
    "all": neutral + javascript + python + matlab,
}

