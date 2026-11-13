import json


previous_guesses = []
def validate_guess(guess, previous_guesses):
    """
    Validate the player's country guess by checking the country
    database, identifying possible misspellings, and preventing
    repeated guesses. If the country isn't an exact match, compare
    it against existing country names to suggest the closest valid match.

    Sequence:
        Normalize the input, search the database, check previous
        guesses, and return the result.

    Iteration:
        Loop through country names to identify exact or similar matches.

    Conditional:
        Determine whether the guess is valid, misspelled,
        repeated, or unrecognized.
    """
    with open("flag_game_countries.json", "r", encoding="utf-8") as f:
        country_database = json.load(f)  # loads the json into country_database
        
    n_guess = guess.strip().lower() # normalizes the guess

    for country in country_database:
        if n_guess == country["country"].lower():
            if n_guess not in previous_guesses:
                previous_guesses.append(n_guess)
                return country["country"]
            else:
                return "Already Guessed lol"
    return "Country not found"

def eliminate_countries(possible_countries, previous_feedback):
    """
    Narrow down the list of possible countries using feedback from
    previous guesses. Compare each remaining country against the known
    color and continent clues, removing countries that contradict the
    feedback.

    Sequence:
        Retrieve previous feedback, evaluate possible countries,
        eliminate incompatible countries, and return the remaining list.

    Iteration:
        Loop through countries and previous clues to check compatibility.

    Conditional:
        Eliminate countries that contradict known color or continent
        information and keep those that satisfy all clues.
    """
    pass

def guess_count(guesses_used: int,
                max_guesses: int = 10) -> dict:
    """
    Updates the number of guesses a player has used and checks whether the
    player has any tries left in the game.

    The function adds the player's latest guess to the number of guesses used
    so far and compares it with the maximum number of tries allowed. The
    result can be used to show the player how many guesses remain and to end
    the game once the 10 tries limit has been reached.

    Args:
        guesses_used (int): the number of guesses the player has already made
            before the current guess.
        max_guesses (int): the maximum number of guesses the player is
            allowed to make. (Default: 10)

    Returns:
        dict: a dictionary containing the updated number of guesses used, the
            number of guesses remaining, and whether the player has run out of
            guesses.

    Raises:
        ValueError: if guesses_used is negative or if max_guesses is less
            than 1.
    """
    pass


def process_guess(guess_info, country_info):
    """
    Compare the player's guessed country against the target country using 
    flag colors and continent information. Generate feedback showing which 
    colors are shared and whether the continent matches.
    Tracks the player's attempts and determine whether they have won or lost.
    
    Sequence: Retrieve country Information, compare colors and continents,
        update attempts, and generate feedback.
    
    Iteration: Loop thorugh the flag colors to compare them against the target
        flag
    COnditional: Check for matching colors, matching continents, correct guesses
        and the 10 attempt limit.
        
    Args:
        guess_info (dict): a dictionary containing the updated number of 
            guesses used, the number of guesses remaining, and whether the 
            player has run out of guesses.
        
        country_info (dict): a dictionary containing country info.
        
    Returns: remaining (list): a list of the remaining possible countries. 
            
    
    """
    
    
def calculate_rankings(game_results, player_records):
    """
    Calculate player scores based on difficulty level, number of attempts, and 
    whether the player successfully guessed the country. Update player records, 
    track their best scores, and organize players into a leaderboard.
    
    Sequence: Retrieve player records, calculate scores, update records, compare
    player performances, and generate rankings.
    
    Iteration: Loop through game results to calculate scores and through player 
    records to determine rankings.
    
    Conditional: Award points based on wins, attempts, and difficulty; update 
    personal bests when scores improve; handle ties between players.

    Args:
        game_results (list): a list of dictionaries, containing player's names,
        the difficulty level, the number of attempts used, and whether the 
        player guessed the country correctly.
        player_records (dict): a dictionary with player's names, their total 
        scores, best score, and number of games they have played.
        
    Returns:
        rankings (list): a list of scores from highest to lowest. 
    """
    pass
     