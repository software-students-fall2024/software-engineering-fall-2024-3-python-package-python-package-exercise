import petpy

MAIN_MENU = 0
PET_MENU = 1

current_menu = MAIN_MENU
current_pet = None

def adopt_pet():
    available_pet_types = list(petpy.Pet.PET_EMOJIS.keys())
    print("Available pet types:", ", ".join(available_pet_types))
    
    pet_name = input("Name your pet: ")
    pet_type = input("Which pet did you pick from the list above? ").strip().lower()
    
    while pet_type not in available_pet_types:
        print("Invalid pet type! Please choose a pet from the list.")
        pet_type = input("Please pick a pet that is available: ").strip().lower()
    
    my_pet = petpy.create_pet(pet_name, pet_type)
    print(f"Congrats! You've adopted {my_pet.name} the {my_pet.type} {my_pet.emoji}.")

def feed_pet():
    available_foods = list(petpy.Pet.FOOD_MENU.keys())
    print("\nAvailable foods for your pet:", ", ".join(available_foods))
    food = input("What would you like to feed your pet? Pick from the list above: ").strip().lower()

    while food not in available_foods:
        print("Invalid food choice! Please choose food from the list.")
        food = input("Pick a food item available: ").strip().lower()

    return food

def main_menu():
    global current_pet
    global current_menu

    print("\n" + "=" * 20 + "MAIN MENU" + "=" * 20)
    print("Your pets:")
    for pet in petpy.pets.values():
        print(f"- {pet.name} the {pet.type} {pet.emoji}")
    
    print("\nWhat would you like to do?")
    print("1. Interact with a pet")
    print("2. Adopt another pet")
    print("3. Exit")

    choice = input("\nEnter the number of your choice: ")
    if choice == '1':
        print("Which pet would you like to interact with? ")

        while True:
            choice_pet = input("Enter the name of your pet: ")
            if choice_pet in petpy.pets.keys():
                current_pet = petpy.pets.get(choice_pet)
                current_menu = PET_MENU
                break
            else:
                print("Pet not found. Please try again.\n")
    elif choice == '2':
        adopt_pet()
    elif choice == '3':
        print("Hope to see you again soon!")
        exit()
    else:
        print("Invalid choice, please try again.\n")

def pet_menu(pet):
    global current_menu 
    global current_pet

    print("\n" + "=" * 20 + "PET MENU" + "=" * 20)
    print(f"What would you like to do with {pet.name} the {pet.type} {pet.emoji}?")
    print("1. Feed your pet")
    print("2. Train your pet")
    print("3. Fight")
    print("4. Check your pet's stats")
    print("5. Check your pet's mood")
    print("6. Check your pet's health")
    print("7. Check your pet's level")
    print("8. Release your pet \n")
    print("9. Go back to main menu")
    
    choice = input("\nEnter the number of your choice: ")
    if choice == '1':
        food = feed_pet()
        print(petpy.feed(pet, food))
        input("\nPress Enter to continue...\n")
    elif choice == '2':
        petpy.train_pet(pet)
        input("\nPress Enter to continue...\n")
    elif choice == '3':
        petpy.fight(pet)
        input("\nPress Enter to continue...\n")
    elif choice == '4':
        print(petpy.get_pet_stats(pet, pet.name))
        input("\nPress Enter to continue...\n")
    elif choice == '5':
        print(petpy.get_pet_mood(pet))
        input("\nPress Enter to continue...\n")
    elif choice == '6':
        print(petpy.get_pet_health(pet))
        input("\nPress Enter to continue...\n")
    elif choice == '7':
        print(petpy.get_pet_level(pet))
        input("\nPress Enter to continue...\n")
    elif choice == '8':
        petpy.release_pet(pet.name)
        print(f"{pet.name}: Thank you, sensei. See you never >:(\n")
        current_pet = None
    elif choice == '9':
        current_menu = MAIN_MENU
    else:
        print("Invalid choice, please try again.\n")
    print("\n" + "-" * 50 + "\n")


def main():
    global current_menu
    global current_pet
    print("Welcome to Pet-py o.O!\n")

    while True:
        prev_pet_count = len(petpy.pets)
        
        if not petpy.pets:
            current_menu = MAIN_MENU
            print("You have no pets. Please adopt one first.")
            adopt_pet()
        else:
            if current_menu == MAIN_MENU:
                main_menu()
            elif current_menu == PET_MENU:
                if current_pet is None:
                    print("No pet selected. Returning to main menu.")
                    current_menu = MAIN_MENU
                    continue
                else:
                    pet_menu(current_pet)

        if len(petpy.pets) < prev_pet_count:
            print(f"{current_pet.name} has left you")
            current_pet = None
            current_menu = MAIN_MENU




if __name__ == "__main__":
    main()
