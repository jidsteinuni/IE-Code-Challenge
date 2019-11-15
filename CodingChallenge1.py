#Pacman Code Challenge
#By Jason Idstein

def main():

    print("Hello! Welcome to the Pacman Simulator.\n"
          "To begin please place Pacman on the board with the command \"PLACE X,Y,DIRECTION\""
          "\nProvide coordinates between 0-4 in place of X and Y and give a direction NORTH, SOUTH, EAST or WEST")

    pacman = Pacman(None, None, None, False)
    quitProg = False

    #Continuously loop asking for input until a quit command is entered
    while quitProg is False:
        #Take input from commandline
        args = input()
        quitProg = interpretArgs(args, pacman)


def interpretArgs(args, pacman):

    #Test for MOVE command and then runs the move command on the pacman object
    if args == "MOVE":
        #Check that pacman has been placed on the board
        if pacman.placed is True:
            pacman.move()
        #If pacman hasn't been placed return an error message asking user to place him first
        else:
            print("Please place pacman on the board before trying to move him")
    #Tests for LEFT command and then runs the left command on pacman object
    elif args == "LEFT":
        #Check that pacman has been placed on the board
        if pacman.placed is True:
            pacman.left()
        #If pacman hasn't been placed return an error message asking user to place him first
        else:
            print("Please place pacman on the board before trying to move him")
    #Tests for RIGHT command and then runs the right command on pacman object
    elif args == "RIGHT":
        #Check that pacman has been placed on the board
        if pacman.placed is True:
            pacman.right()
        #If pacman hasn't been placed return an error message asking user to place him first
        else:
            print("Please place pacman on the board before trying to move him")
    #Tests for REPORT command and then runs the report command on pacman object
    elif args == "REPORT":
        #Check that pacman has been placed on the board
        if pacman.placed is True:
            pacman.report()
        #If pacman hasn't been placed return an error message asking user to place him first
        else:
            print("Please place pacman on the board before asking for his position")
    #Tests for QUIT command and then returns True so that the quit variable flag is set to true and ends the input loop
    elif args == 'QUIT':
        return True
    else:
        #Cleans up the input for the PLACE command by removing delimiters and storing arguments in a list
        args = args.replace(',', ' ')
        args = args.split()
        if args[0] == 'PLACE':
            #Checks that the input for place coordinates is valid
            if '0' <= args[1] <= '4' and '0' <= args[2] <= '4':
                #Changes input to integer type for integer operations in pacman class
                args[1] = int(args[1])
                args[2] = int(args[2])
                #Checks that the input for direction is valid
                if args[3] == 'SOUTH' or args[3] == 'NORTH' or args[3] == 'WEST' or args[3] == 'EAST':
                    pacman.place(args[1],args[2],args[3])
                #Error message if invalid direction is given as input
                else:
                    print("Invalid paramter. Please use NORTH, SOUTH, EAST or WEST for direction")
            #Error message if invalid coordinates are given as input
            else:
                print("Invalid parameter. Please enter values between 0 and 4 as coordinates")
        #Error message if no valid input is detected that demonstrates how to use the program
        else:
            print("Invalid Command.\nPlease use one of the following commands:\n"
                  "PLACE X,Y,DIRECTION\nMOVE\nLEFT\nRIGHT\nREPORT\nQUIT\n")


    return False


class Pacman:

    def __init__(self, x, y, direction, placed):
        #initialise pacman object and set position to none until place command is called
        self.posx = x
        self.posy = y
        self.direction = direction
        self.placed = placed

    def place(self, x, y, direction):
        #Place pacman on the board anywhere by setting the coordinates and direction.
        #Set the placed flag to True to allow other pacman operations
        self.direction = direction
        self.posx = x
        self.posy = y
        self.placed = True

    def move(self):

        #move pacman in the direction that he is facing by incrementing or decrementing the x or y coordinate
        if self.direction == 'NORTH' and self.posy < 4:
            self.posy += 1
        elif self.direction == 'SOUTH' and self.posy > 0:
            self.posy -= 1
        elif self.direction == 'EAST' and self.posx < 4:
            self.posx += 1
        elif self.direction == 'WEST' and self.posx > 0:
            self.posx -= 1
        #If pacman is at the edge of the grid and unable to move any further in that direction print an error message and don't move
        else:
            print("Pacman is unable to move any further in direction %s without falling off the board!\nPlease try changing his direction with \"Left\" or \"Right\"" % self.direction)

    def left(self):

        #rotate pacman to the left
        if self.direction == 'NORTH':
            self.direction = 'WEST'
        elif self.direction == 'EAST':
            self.direction = 'NORTH'
        elif self.direction == 'SOUTH':
            self.direction = 'EAST'
        elif self.direction == 'WEST':
            self.direction = 'SOUTH'

    def right(self):

        #rotate pacman to the right
        if self.direction == 'NORTH':
            self.direction = 'EAST'
        elif self.direction == 'EAST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'WEST'
        elif self.direction == 'WEST':
            self.direction = 'NORTH'

    def report(self):
        #print out the coordinates and direction of pacman
        print("Pacman is located at %s,%s facing %s" % (self.posx, self.posy, self.direction))

if __name__ == '__main__':
    main()

