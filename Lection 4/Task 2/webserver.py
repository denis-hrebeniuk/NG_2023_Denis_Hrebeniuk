from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)

GAME_FIELD_HEIGHT = 10
GAME_FIELD_WIDTH = 100


def update_game_field(player_pos):
    game_field = ""

    """
    player_pos_y - index of the line on which the player's character is located
    It is necessary to get only the integer part, as you only need to know the number of the line the player wants to jump to.

    player_pos_x - index of the player's character in the row
    The line number is used to get only the index of the player in the line
    """
    player_pos_y = int(player_pos / GAME_FIELD_WIDTH)
    player_pos_x = player_pos - (GAME_FIELD_WIDTH * player_pos_y)

    for line in range(GAME_FIELD_HEIGHT):
        for symbol_index in range(GAME_FIELD_WIDTH if line == player_pos_y else GAME_FIELD_WIDTH + 3): # Extends the line so that it is no different from where the player is (fixing the length of the player symbol)
            if symbol_index == player_pos_x and line == player_pos_y:
                game_field += "@"
            else:
                game_field += "."
        game_field += "<br>"

    return Markup(game_field)


@app.route("/")
def index():
    return render_template("index.html", player_pos=0, game_field=update_game_field(0))


@app.route("/doaction")
def do_action():
    player_pos = int(request.args.get("player_pos"))
    action = request.args.get("action")

    match action:
        case "left":
            player_pos -= 1
        case "up":
            player_pos -= GAME_FIELD_WIDTH # The length of the entire line is subtracted to get the position of the player on the previous line
        case "down":
            player_pos += GAME_FIELD_WIDTH # The length of the entire line is added to get the player's position on the next line
        case "right":
            player_pos += 1

    if player_pos < 0 or player_pos >= GAME_FIELD_WIDTH * GAME_FIELD_HEIGHT: # Checking if a player has left the field of play
        player_pos = 0

    return render_template(
        "index.html", player_pos=player_pos, game_field=update_game_field(player_pos)
    )


app.run(host="0.0.0.0", port=8080)
