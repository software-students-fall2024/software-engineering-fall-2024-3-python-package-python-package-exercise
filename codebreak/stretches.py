import random

def stretch_exercise(time_limit):
    """
    Suggests a random stretching exercise based on the time available.
    
    Parameters:
    time_limit (str): The amount of time available for the stretch ('short', 'medium', 'long').
    
    Returns:
    str: A random stretch suggestion.
    """
    stretches = {
        "short": [
            "Neck Stretch: Slowly tilt your head from side to side.",
            "Shoulder Shrug: Raise your shoulders up to your ears and release.",
            "Wrist Stretch: Extend your arm and gently pull your fingers back.",
            "Ankle Circles: Rotate your ankles clockwise and counterclockwise.",
            "Arm Circles: Extend your arms and make small circles.",
            "Chest Stretch: Place your hands behind your back and squeeze shoulder blades together.",
            "Seated Forward Bend: Reach towards your toes while seated.",
            "Finger Stretch: Spread your fingers wide, then squeeze into a fist.",
            "Shoulder Rolls: Roll your shoulders forward and backward.",
            "Seated Cat-Cow: Arch and round your back while sitting up straight."
        ],
        "medium": [
            "Standing Forward Bend: Bend forward and reach for your toes.",
            "Chest Opener: Clasp hands behind your back and stretch.",
            "Seated Twist: Sit up straight, and twist gently to each side.",
            "Side Stretch: Reach one arm overhead and lean to the side.",
            "Figure Four Stretch: Cross one ankle over the opposite knee and lean forward.",
            "Tricep Stretch: Raise one arm and bend it behind your head, gently pulling with the other hand.",
            "Hip Flexor Stretch: Step one foot forward into a lunge and stretch the hip.",
            "Quad Stretch: Stand and pull one foot towards your buttock.",
            "Calf Stretch: Place hands on a wall and stretch your calf by pushing your heel back.",
            "Seated Hamstring Stretch: Extend one leg forward and reach towards your toes."
        ],
        "long": [
            "Downward Dog: Get on all fours and raise your hips into the air.",
            "Child's Pose: Sit back on your heels and stretch your arms forward.",
            "Pigeon Pose: Bring one knee forward and extend the other leg back.",
            "Reclining Twist: Lie on your back, bring one knee across your body, and turn your head in the opposite direction.",
            "Cobra Pose: Lie on your stomach and push up with your hands.",
            "Butterfly Stretch: Sit with the soles of your feet together and gently press your knees down.",
            "Happy Baby Pose: Lie on your back and grab your feet, pulling your knees towards the ground.",
            "Lying Quad Stretch: Lie on your side and pull one foot towards your buttock.",
            "Supine Hamstring Stretch: Lie on your back and lift one leg, holding it with your hands.",
            "Cat-Cow: Get on all fours, arch your back, then round it."
        ]
    }
    
    # Get the list of stretches based on the time limit
    available_stretches = stretches.get(time_limit.lower(), [])
    
    # Select a random stretch from the list if there are options available
    if available_stretches:
        return random.choice(available_stretches)
    else:
        return "Invalid time limit. Please choose 'short', 'medium', or 'long'."

# Example usage
print(stretch_exercise("short"))
print(stretch_exercise("medium"))
print(stretch_exercise("long"))
