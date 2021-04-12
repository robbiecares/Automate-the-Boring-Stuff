#line 52 - make the else work

board_state = { 'a1': 'wrook', 'a2': 'wpawn', 'a7': 'bpawn', 'a8': 'brook',
                'b1': 'wknight', 'b2': 'wpawn', 'b7': 'bpawn', 'b8': 'bknight',
                'c1': 'wbishop', 'c2': 'wpawn', 'c7': 'bpawn', 'c8': 'bbishop',
                'd1': 'wqueen', 'd2': 'wpawn', 'd7': 'bpawn', 'd8': 'bqueen',
                'e1': 'wking', 'e2': 'wpawn', 'e7': 'bpawn', 'e8': 'bking',
                'f1': 'wbishop', 'f2': 'wpawn', 'f7': 'bpawn', 'f8': 'bbishop',
                'g1': 'wknight', 'g2': 'wpawn', 'g7': 'bpawn', 'g8': 'bknight',
                'h1': 'wrook', 'h2': 'wpawn', 'h7': 'bpawn', 'h8': 'brook'}
#a dict with key of space name & value of piece name

def invalid(reason):
    print("board not valid: " + reason)
    return False

#invalid("test")


def Chess_Board_Validator(board_state):
    if "wking" not in board_state.values() or "bking" not in board_state.values():
        invalid("a king is missing so the game must be over")

    colors = "wb"
    total_color_check = []
    for piece in board_state.values():
        color = piece[0]
        if color not in colors:
            invalid("'" + piece + "' is not w or b")
        total_color_check.append(color)

        name = piece[1:]
        piece_names = ["king", "queen", "knight", "bishop", "rook", "pawn"]
        if name not in piece_names:
            invalid("'" + piece + "' is not a valid piece name")

    for colour in colors:
        if total_color_check.count(colour) > 16:
            invalid("you have too many " + colour + " pieces on the board")

    pawns = []
    for piece in board_state.values():
        if piece[1:] == "pawn":
            pawns.append(piece)

    if len(pawns) > 8:
        if pawns.count("bpawn") > 8 or pawns.count("wpawn") > 8:
            invalid("more than eight pawns for one side")

    for location, piece in board_state.items():
        if location[0] not in "abcdefgh" or location[1] not in "12345678":
            invalid("The piece '" + piece + "' shows an invalid location of '" + location+"'")

Chess_Board_Validator(board_state)