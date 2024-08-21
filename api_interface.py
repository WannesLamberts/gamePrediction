import requests
from urllib.parse import urlencode
import settings
from utils import convert_to_epoch_time

def get_summoner_puuid(gameName,tagLine):
    """
    Retrieves the PUUID (Player Universally Unique Identifier) of a summoner from the Riot Games API.

    Parameters:
    -----------
    gameName : str
        The game name (Riot ID) of the summoner. This name is used to identify the summoner in the API request.

    tagLine : str
        The tag line associated with the summoner's account. This tag is used in combination with `gameName` to identify the summoner.

    Returns:
    --------
    str or None
        The PUUID of the summoner if the request is successful. Returns `None` if there is an error or if the request fails.
    """

    call = f"https://{settings.REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={settings.API}"

    try:
        response = requests.get(call)
        response.raise_for_status()
        return response.json()["puuid"]
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong with getting puuid error details:\n{e}")
        return None

def get_match_ids(puuid,start,count,start_time):
    """
    Retrieves a list of match IDs for a given PUUID from the Riot Games API.

    Parameters:
    -----------
    puuid : str
        The PUUID (Player Universally Unique Identifier) of the summoner whose match IDs are to be retrieved.

    start : int
        The starting index for the match list retrieval.

    count : int
        The number of match IDs to retrieve. Specifies how many match IDs should be returned.

    start_time : str
        The earliest timestamp (in milliseconds since Unix epoch) for the matches to be included in the response.
        must be in the following format "%Y-%m-%d %H:%M:%S"

    Returns:
    --------
    list or None
        A list of match IDs if the request is successful. Each item in the list is a string representing a match ID.
        Returns `None` if there is an error or if the request fails.
    """

    start_time = convert_to_epoch_time(start_time)
    call = f"https://{settings.REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?startTime={start_time}&start={start}&count={count}&api_key={settings.API}"

    try:
        response = requests.get(call)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong with getting match ids error details:\n{e}")
        return None
def get_match_info(match_id):
    """
    Retrieves detailed information about a specific match from the Riot Games API.

    Parameters:
    -----------
    match_id : str
        The unique identifier of the match for which information is to be retrieved.

    Returns:
    --------
    dict or None
        A dictionary containing detailed information about the match if the request is successful. The structure of the dictionary
        follows the format provided by the Riot Games API, including match details such as participants, game duration, and more.
        Returns `None` if there is an error or if the request fails.
    """

    call = f"https://{settings.REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={settings.API}"

    try:
        response = requests.get(call)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong with getting match info error details:\n{e}")
        return None