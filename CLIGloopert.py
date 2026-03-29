# Imports
from magic import Magic  # python-magic, reads file signatures
from pyfiglet import Figlet #Creates ASCII text (line 9)
from pathlib import Path #Handles file paths
from tkinter import Tk # Allows for GUI
from tkinter.filedialog import askopenfilename # Opens a file picker dialog box
import hashlib
import sys
# Big Font
f = Figlet(font="big")

# Gloopert Text Art
ascii_art = """                                             gj%      
                                           ]D8@@8W                               
                                           @88@@@@                                
                                          ]M88@@@$W
                                          @Q88@@@@@                              
                                         @VQ88@@@@$W
                                        gYQQ88@@@@@@
                                      ,@~OQQ88@@@@@8@
                                    @TOOOQ888@@@@@@8W
                               ,am%T+<<zOQQ88@@@@@@@@8@p
                          ,am%T}<<<<<<zOOQ888@@@@@@@@@@@$@@,
                      ,m0$>OO<<<<`<>zzOOQQ888@@@@@@@@@@@@@@@@$@%mg,
                   ,m$~OOO<^`` ,,,zzOOOQQ888@@@@@@@@@@@@@@@@@@@@@@@$%m
                 a@<QOO<<`   ,,zzzOOOOQQQ888@@@@@@@@@@@@@@@@@@@@@@@@@@m
               $<QOO<<`` ,,zzzOOOOOOQQQ888@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$m
            gOQQQOOO<<<zzzzOOOOOOO@MT!!TT%@@@@@@@M!     ?@@@@@@@@@@@@@@@@@@@$
           gMQQQQOOOzzzzOOOOOOOQqE         %@@@$   @.   @@@@@@@@@@@@@@@@@@Q@
           DQ88QQQOzOOOOOOOOQQQQ$   @@@W  "@@@@  ]@@@@   @@@@@@@@@@@@@@@@@@@].
          $O8888QQQQQQQQQQQQQQQ8]w  ?0@%"  ]D@@$w  TTT-   @@@@@@@@@@@@@@88@@@].
          $Q8@@88888QQQ88Q8888888$p      ,@%@@@@$%p;,;gm@8@@@@@@@@@@@@@Q<Q@@8$
          ]@$@@@@8888888888888@@@@8$%%@@%8@@@@@@@@@88@@@@@@@@@@@@@@@@@Q^>8@@]M
           @8@@@@@@@@@@@@@@@@@$@@@@@@@@@@@@@@@@@@@@@@@$@%O8$%@@@@@@@@Q<,z@@O@
            "%p8@@@@@@@@@@@@@@$%@gQQQQQO~($$$$}<QQQQQg@@$@@@@@@8QzQ@8O@T
              T%g8%@@@@@@@@@@@@@@$%@@ggQQQQQQQQQQggg@@%8@@@@@@@@@@@@8j                 
              TNgO8%@@@@@@@@@@@@@@@88$$$$$$@$88@@@@@@@@@@@@@88j@M"""


#Sha265 funtion
def get_sha256(UserInput): # Defines SHA-256 hashing function
    BUF_SIZE=65536 # Read file in 64KB chunks for efficiency
    sha256=hashlib.sha256() # Create SHA-256 hash object
    with open(UserInput,"rb") as f: # Open the file in binary mode
        while True: # Continue reading until end of file
            data=f.read(BUF_SIZE) # Read the next block of bytes
            if not data: # If no data was read, we've reached EOF
                break # Exit the loop
            sha256.update(data) # Add the block to the hash
    return sha256.hexdigest() # Return the final hash digest in hexadecimal
        


   

# File picker function, Reuseable function to open a file dialog box
def pick_file():
    root = Tk() #Creates Tkinter main window
    root.withdraw()  # Hides Tkinter main window
    file_path = askopenfilename() #opens file picker and returns selected file path
    root.destroy() # closes the hidden Tk window and file picker box
    return file_path #sends the selected file path to the program

# Clean drag & drop input (handles quotes/spaces)
def clean_input(path_str): #clean input funtion
    return path_str.strip().strip('"').strip("'") # Removes spaces,removesdouble quotes,removes single quotes

# Initialize Magic ONCE (better performance)
m = Magic() #Creates a magic object for file info 
m_mime = Magic(mime=True) # Cretas another magic object for MIME type only

# Display UI
print(f.renderText("Gloopert")) #Prints Figlet tile using f
print(ascii_art) #prints Gloopert ASCII
print(f.renderText('Feed me a file !   >:(')) #Prints Figlet text using f

# Program Loop Starts Here
while True: #Runs until user quits
    print("-" * 120) # Prints devider line

    # User Input
    UserInput = input("Enter File (o = dialog, q to quit): ").strip() # .strip removes any spaces
    
    #Exit condtion
    if UserInput.lower() in ["q", "quit", "exit"]:
        break

    # Open file dialog
    if UserInput.lower() == "o": # Opens file dialog
        UserInput = pick_file()
        if not UserInput: # Checks if dialog box was closed
            print("No file selected.")
            continue # Restarts loop

    # Clean drag/drop input
    UserInput = clean_input(UserInput) # Removes quotes and spces from drag and drop and manual inputs

    # Check file exists
    file_path = Path(UserInput)
    if not file_path.is_file(): #Checks if file exists
        print(f"ERROR: '{UserInput}' does not exist!") # Prints error
        continue # Restarts loop

    #File Info
    try:
        print("File:", file_path.resolve()) # Prints full file path
        print("Size:", file_path.stat().st_size, "bytes") # Gets file size in bytes
        print("File Details:", m.from_file(UserInput)) # Uses python-magic to describe file
        print("File Type:", m_mime.from_file(UserInput)) # Shows MIME type, Example:(text/plain)
        file_hashsha256 = get_sha256(UserInput)
        print(f"SHA256 Hash: {file_hashsha256}")
        

    #Error handling
    except Exception as e: # Catches any error (bad file, permission issues, etc)
        print("ERROR reading file:", e) # Prints error instead of crashing
