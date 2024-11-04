from oracle.petting_zoo import get_random_pet, get_pet
from oracle.vibe_check import get_vibe_check
from oracle.eight_ball import get_eight_ball
from oracle.fortune_cookie import get_fortune

# Get a fortune based on mood
optimistic_fortune = get_fortune("optimistic")
realistic_fortune = get_fortune("realistic")
unfortunate_fortune = get_fortune("unfortunate")

print(optimistic_fortune)  # Outputs a random optimistic fortune

# Get multiple decisions
decisions = get_eight_ball(3)

print(decisions)  # Outputs random decision(s)

# Check different vibes
good_vibe = get_vibe_check("good")
bad_vibe = get_vibe_check("bad")
random_vibe = get_vibe_check("random")

print(random_vibe)  # Outputs a random vibe

# Check different vibes
dog = get_pet("dog")
cat = get_pet("cat")
rabbit = get_pet("rabbit")
hamster = get_pet("hamster")
goat = get_pet("goat")
sheep = get_pet("sheep")
bird = get_pet("bird")
frog = get_pet("frog")
bear = get_pet("bear")
fox = get_pet("fox")

print(fox) #prints fox pet
print(get_random_pet())  # Outputs a random pet