def create_pieces():
    piece_list = []
    piece_count = {'pawn':8, 'knight':2, 'bishop':2, 'rook':2, 'queen':1, 'king':1}
    colors = 'wb' #define colors
    for color in colors: #add color to piece name
        for item in piece_count.items(): #item is a tuple for each key,value pair of piece_count
            piece, count = item #this line assigns "variables" to the key,value pair of the tuple returned by the call to the dictionary. This was a new lesson for me.
            for i in range(count):
                piece_list.append(color + piece)

    #print(pieces)
    return piece_list
#create_pieces()

def starting_location(pieces):
    board_layout = {}

    for piece in pieces:
        if piece in board_layout.values():
            continue
        else:
            name = piece[1:]
            color = piece[0]
            if color == "w":
                rows = 1
            else:
                rows = 8
            if name == "rook":
                columns = "ah"
            elif name == "knight":
                columns = "bg"
            elif name == "bishop":
                columns = "cf"
            elif name == "queen":
                columns = "d"
            elif name == "king":
                columns = "e"
            else:
                columns = "abcdefgh"
                if color == "w":
                    rows = 2
                else:
                    rows = 7

            for column in columns:
                location = column+str(rows)
                board_layout[location] = piece


   #sort on key for clarity when reading
    a_board_layout = board_layout.items()
    sorted_items = sorted(a_board_layout)
    dict(sorted_items)
    print(dict(sorted_items))
    #return sorted_items

starting_location(create_pieces())

