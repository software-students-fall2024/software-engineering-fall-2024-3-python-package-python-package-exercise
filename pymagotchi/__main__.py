from time import sleep
from .pet import new_pet

def main():
    pet = new_pet()  

    try:
        while pet.stats["health"] > 0:
            
            pet.status()

           
            print("\nChoose an action:")
            print("1. Feed")
            print("2. Play")
            print("3. Let Sleep")
            print("4. Wait (Do nothing)")
            print("5. Leave (Exit the game)")

            
            choice = input("Enter the number of your choice: ")

           
            if choice == "1":
                pet.feed()
            elif choice == "2":
                pet.play()
            elif choice == "3":
                pet.sleep()
            elif choice == "4":
                print("You chose to wait...")
            elif choice == "5":
                print("You have chosen to leave the game.")
                break  
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

            
            pet.update_stats()
            
           
            sleep(1)

    except KeyboardInterrupt:
        print("\nExiting the simulation.")
    
    print(f"\n{pet.name} has unfortunately reached zero health. Game over.")

if __name__ == "__main__":
    main()