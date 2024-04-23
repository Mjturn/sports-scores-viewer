from bs4 import BeautifulSoup
import requests

mlb_url = "https://www.mlb.com/scores"
nfl_url = "https://www.nfl.com/scores"
nba_url = "https://www.nba.com/games"
nhl_url = "https://www.nhl.com/scores"

mlb = requests.get(mlb_url)
nfl = requests.get(nfl_url)
nba = requests.get(nba_url)
nhl = requests.get(nhl_url)

mlb_document = BeautifulSoup(mlb.text, "html.parser")
nfl_document = BeautifulSoup(nfl.text, "html.parser")
nba_document = BeautifulSoup(nba.text, "html.parser")
nhl_document = BeautifulSoup(nhl.text, "html.parser")

mlb_teams = mlb_document.find_all(class_="TeamWrappersstyle__DesktopTeamWrapper-sc-uqs6qh-0 fdaoCu")
nfl_teams = nfl_document.find_all(class_="css-text-146c3p1 r-color-1khnkhu r-fontFamily-1fdbu1n r-fontSize-ubezar")
nba_teams = nba_document.find_all(class_="MatchupCardTeamName_teamName__9YaBA")
nhl_teams = nhl_document.find_all(class_="sc-fUcwZz bJNkqN team-name")

while True:
    print("Which league would you like to view scores from?")
    print("1. MLB")
    print("2. NFL")
    print("3. NBA")
    print("4. NHL")
    print("Type \"quit\" to exit the program.")
    user_input = input()

    if user_input == "1":
        print("MLB Scores:")

    elif user_input == "2":
        print("NFL Scores:")

    elif user_input == "3":
        print("NBA Scores:")

    elif user_input == "4":
        print("NHL Scores:")

    elif user_input.lower() == "quit":
        break

    else:
        print("Sorry, what you've entered is invalid. Please try again.")
