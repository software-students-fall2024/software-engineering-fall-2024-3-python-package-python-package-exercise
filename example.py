from petpy import create_pet, feed, get_pet_mood, get_pet_level, get_pet_health, get_pet_stats, fight, train_pet, release_pet

# Create a new pet
my_pet = create_pet("Buddy", "dog")

# Feed the pet
print(feed(my_pet, "kfc"))

# Check mood, level, and health
print(get_pet_mood(my_pet))
print(get_pet_level(my_pet))
print(get_pet_health(my_pet))

# Train the pet
train_pet(my_pet)

# Engage in a fight
fight(my_pet)

# Check full stats
print(get_pet_stats(my_pet, "Buddy"))

# Release the pet
print(release_pet("Buddy"))
