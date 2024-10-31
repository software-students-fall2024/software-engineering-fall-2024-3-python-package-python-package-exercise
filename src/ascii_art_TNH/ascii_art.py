import gallery

def parse_input(user_input):
    # Type of the input-make sure string
    # Strip trailing spaces
    while(True):
      if user_input.strip()!="":
        animal = user_input.split(" ")
        #calls print_art or print_noise
        if animal in gallery.animals:
          print_art(animal)

      # getting animal name from the user
      user_input = input("Enter an animal or exit : ")
      
      if user_input == "exit":
        break

def print_art(animal):
  #match animal with art
  #calls print_noise or wrong_input
  return(gallery.animals.get(animal))

def print_noise(animal):
   #match animal with noise
   noises = {}

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