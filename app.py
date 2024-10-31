def parse_input(user_input):
    # Type of the input-make sure string
    # Strip trailing spaces
    while(True):
      if user_input.strip():
        animals = user_input.split(" ")
        #calls print_art or print_noise

        for animal in animals:
          print_art(animal.strip()) # Calls print_art and, subsequently, print_noise
        else: 
          print ("Please enter a valid animal name.")
    

      # getting animal name from the user
      user_input = input("Enter an animal or type 'exit' : ")
      
      if user_input.lower() == "exit":
        break

def print_art(animal):
  #match animal with art
  #calls print_noise or wrong_input
  arts = {
        "cow": r"""
         (__)
         (oo)
   /------\/
  / |    ||
 *  ||---||
        """,
        "cat": r"""
 /\_/\  
( o.o ) 
 > ^ <  
        """,
        "dog": r"""
 / \__
(    @\____
 /         O
        """,
        "duck": r"""
 __
<(o )___
 (  ._> /
   `---'  
        """
    }
  if animal in arts:
    print(arts[animal])
    print_noise(animal)
  else:
    wrong_input(animal, length = 1)

def print_noise(animal):
   """
    Prints the sound of a given animal after displaying its ASCII art.
    
    Parameters:
    - animal_name (str): The parsed animal name.
    """
   #match animal with noise
   noises = {
     "cow": "Moo!",
     "cat": "Meow!",
     "dog": "Woof!",
     "duck": "Quack!"
     
     }
   if animal in noises:
     print(f"Sound:{noises[animal]}")
   else:
     print("Sorry, we don't have a sound for that animal.")

def wrong_input(animals, length):
  #if multiple animals were inputed, print flowers
  #if one animal, print flower
  # reference: https://www.asciiart.eu/plants/flowers
  flowers = r"""
        ,,,                      ,,,
       {{{}}    ,,,             {{{}}    ,,,
    ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
   {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
    ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
    \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
    \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
    \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
    \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  """
  flower = r""" 
               .-.'  '.-.
          .-(   \  /   )-.
         /   '..oOOo..'   \
 ,       \.--.oOOOOOOo.--./
 |\  ,   (   :oOOOOOOo:   )
_\.\/|   /'--'oOOOOOOo'--'\
'-.. ;/| \   .''oOOo''.   /
.--`'. :/|'-(   /  \   )-'
 '--. `. / //'-'.__.'-;
   `'-,_';//      ,  /|
        '((       |\/./_
          \\  . |\; ..-'
           \\ |\: .'`--.
            \\, .' .--'
             ))'_,-'`
       jgs  //-'
           // 
          //
         |/
  """
  print("Sorry we do not have", animals)
  if(length>1):
    print(flowers)
  else:
    print(flower)
  

  

def main():
  # getting animal name from the user
  user_input = input("Enter an animal: ")
  parse_input(user_input)



  



if __name__ == "__main__":
  main()