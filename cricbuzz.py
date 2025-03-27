import requests
from bs4 import BeautifulSoup

def get_cricbuzz_live_scores():
    url = 'https://www.cricbuzz.com/'
    
    # Send HTTP request to CricBuzz
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error: Failed to retrieve data from CricBuzz")
        return
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract live matches
    live_matches = soup.find_all('div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')
    
    if not live_matches:
        print("No live matches available at the moment.")
        return
    
    print("Live Cricket Matches:\n")
    
    for match in live_matches:
        # Extract match details
        teams = match.find_all('span', class_='cb-ovr-flo')
        if len(teams) == 2:
            team1 = teams[0].text.strip()
            team2 = teams[1].text.strip()
        
        score = match.find('div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr').text.strip()
        
        # Print the match info
        print(f"{team1} vs {team2}")
        print(f"Score: {score}")
        print("-" * 50)

# Call the function to display live cricket scores
get_cricbuzz_live_scores()

