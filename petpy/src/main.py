import pet
import petpy

def main():
    print("Welcome to the Pet-py o.O!")
    
    available_pet_types = list(pet.Pet.PET_EMOJIS.keys())
    print("Available pet types:", ", ".join(available_pet_types))
    
    pet_name = input("Namee your pet: ")
    pet_type = input("Which pet did you pick from the list above? ").strip().lower()
    
    while pet_type not in available_pet_types:
        print("Invalid pet type! Please choose a pet from the list.")
        pet_type = input("Please pick a pet that is available: ").strip().lower()
    
    my_pet = pet.create_pet(pet_name, pet_type)
    print(f"Congrats! You've adopted {my_pet.name} the {my_pet.type} {my_pet.emoji}.")

    available_foods = list(pet.Pet.FOOD_MENU.keys())
    print("\nAvailable foods for your pet:", ", ".join(available_foods))

    while True:
        print("What would you like to do with your pet...")
        print("1. Feed your pet")
        print("2. Check your pet's stats")
        print("3. Check your pet's mood")
        print("4. Check your pet's health")
        print("5. Check your pet's level")
        print("6. Release your pet and exit\n")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            food = input("What would you like to feed your pet? Pick from the list above: ").strip().lower()
            while food not in available_foods:
                print("Invalid food choice! Please choose food from the list.")
                food = input("Pick a food item available: ").strip().lower()
            print(petpy.feed(my_pet, food))
        elif choice == '2':
            print(petpy.get_pet_stats(my_pet, pet_name))
        elif choice == '3':
            print(petpy.get_pet_mood(my_pet))
        elif choice == '4':
            print(petpy.get_pet_health(my_pet))
        elif choice == '5':
            print(petpy.get_pet_level(my_pet))
        elif choice == '6':
            petpy.release_pet(my_pet.name)
            print(f"{my_pet.name}: Thank you, sensei. See you never >:(\n")
            break
        else:
            print("Invalid choice, please try again.")
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()
