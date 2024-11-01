import noises
import gallery

def ascii_art(user_input):
  # Type of the input-make sure string
  # Strip trailing spaces
  animal_array = parse_input(user_input)
  if len(animal_array) == 0:
    wrong_input("nothing", 0)
    return
  for animal in animal_array:
    # If animal is in the gallery
    if animal in gallery.animals:
      print_art(animal)
    elif animal in noises.animal_noises:
      print(print_art(get_noise(animal)))
    else:
      # If animal is not in the gallery
      wrong_input(animal, len(animal_array))

def parse_input(user_input):
  inputs = []
  inputs = user_input.split(" ")
  return inputs

def print_art(animal):
  #match animal with art
  #calls print_noise or wrong_input
  return(gallery.animals.get(animal))

def get_noise(noise):
   #match animal with noise
   return(noises.get(noise))

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
  return