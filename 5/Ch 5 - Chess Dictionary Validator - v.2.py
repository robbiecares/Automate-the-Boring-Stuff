from string import ascii_lowercase
import pprint

piece_list = {}
print("Let's play chess!\nTo start, we'll need to create some pieces.")
#entire application could be reworked to start from the update menu.

def current_pieces(piece_list):
    print("\nCurrent Pieces")
    for piece, count in piece_list.items():
        print(" " + piece + ": " + str(count))
    #pprint.pprint(piece_list) #pretty print here or "print('Key: ' + k + ' Value: ' + str(v))" trick from lesson

def YNQ(question, tip):
    positive_responses = ["yes", "y", "Yes", "Y"]
    negative_responses = ["no", "N", "No", "n"]
    response = input("\n" + question + "\n")
    while response not in (negative_responses + positive_responses):
        response = input("\n" + tip + "\n")
    if response in positive_responses:
        return True
    else:
        return False

def add_piece(piece_list):
    piece_name = None
    more_pieces = None
    while piece_name is None or more_pieces == True:
        piece_name = input("\nPlease enter a piece name\n")
        while piece_name in piece_list:
            current_pieces(piece_list)
            piece_name = input("\nThat piece is already in the list. Please check the name and re-enter it: ")
        piece_list[piece_name] = ""
        #zero should not be accepted here
        piece_count = None
        while type(piece_count) != int or piece_count < 1:
            piece_count = input("\nHow many '" + piece_name + "s' should each player receive?\n")
            try:
                piece_count = int(piece_count)
                if piece_count < 1:  # if not a positive int print message and ask for input again
                    print("\nPlease input a whole number greater than zero")
                    continue
                break
            except ValueError:
                print("\nPlease input a whole number greater than zero")
    # else all is good, val is >= 1 and an integer
        piece_list[piece_name] = piece_count
        print("\n'" + piece_name + ": " + str(piece_list[piece_name]) + "' added to piece list")
        more_pieces = YNQ("Would you like to add another piece?", "Please confirm if there are more pieces by stating Yes or No")
        if more_pieces == True:
            piece_name = None
            continue
        else:
            return piece_list

def piece_menu(piece_list):
    piece_list_complete  = ""
    pieces = []

    while piece_list_complete is not True:
        update_action = input('''
Piece Menu
 1. View current piece list
 2. Create new piece
 3. Edit piece name
 4. Edit piece count
 5. Remove piece
 6. Un/confirm piece list

Please choose an option: ''')

        if update_action == "1":
            current_pieces(piece_list)

        elif update_action == "2": #add piece
            add_piece(piece_list)

        elif update_action in str(345):
            piece_to_update = input("\nPlease enter the name of the piece\n")
            #test this while loop, should there be a continue statement? If not, then why is there one in the YNQ function?
            while piece_to_update not in piece_list.keys():
                piece_to_update = input("\nPlease check your entry, that piece is not in the list\n")

            if update_action == "3": #change piece name
                new_piece_name = input("\nWhat is the correct name?\n")
                while new_piece_name is None or new_piece_name in piece_list:
                    print("\nPlease ensure that the name is not blank or already in the list\n")
                piece_list[new_piece_name] = piece_list[piece_to_update]
                del piece_list[piece_to_update]
                print("\n'" + piece_to_update + "'" + " updated to '" + new_piece_name + "'")

            elif update_action == "4": #change piece count
                old_count = piece_list[piece_to_update]
                new_count = None
                while type(new_count) != int or new_count < 1:
                    new_count = input("\nHow many '" + piece_name + "s' should each player receive?\n")
                    try:
                        new_count = int(new_count)
                        if new_count < 1:
                            print("\nPlease input a whole number greater than zero")
                            continue
                        break
                    except ValueError:
                        print("\nPlease input a whole number greater than zero")
                piece_list[piece_to_update] = new_count
                print("\n'" + str(old_count) + "' updated to " + "'" + str(new_count) + "' for " + piece_to_update)

            elif update_action == "5": #remove piece
                del piece_list[piece_to_update]
                print("\n'" + piece_to_update + "' removed")

        elif update_action == "6":
            current_pieces(piece_list)
            list_status = ""
            if piece_list_complete == True:
                list_status = "confirmed"
            else:
                list_status = "unconfirmed"
            print("\nThe piece list is currently " + list_status)
            piece_list_complete = YNQ("Are all pieces entered correctly?", "Please confirm if there are more pieces by stating Yes or No")
            if piece_list_complete == True:
                print("\nPiece list confirmed")
            else:
                print("\nPiece list unconfirmed")

        else:
            update_action = input("\nplease choose an option: ")
    colors = 'wb' #define colors
    for color in colors: #add color to piece name
        for item in piece_list.items(): #item is a tuple for each key,value pair of piece_count
            piece, count = item #this line assigns "variables" to the key,value pair of the tuple returned by the call to the dictionary. This was a new lesson for me.
            for i in range(count):
                pieces.append(color + piece)
    return pieces

add_piece(piece_list)
piece_menu(piece_list)