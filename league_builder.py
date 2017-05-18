# Script to pull soccer league players from csv file
# Divide players into 3 different groups evenly by soccer experience level 
# Print a text file of the three teams including player info.
  
def read_file(filegiven):  
  import csv
  #open and read the csv into a list of dictionaries for each player with each field defined for each dictionary within the list of players
  with open (filegiven, newline = '') as csvfile:
    fieldnames = ['Name','Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
    sportreader = csv.DictReader(csvfile, delimiter = ",", fieldnames = fieldnames)
    player_list = list(sportreader)
    return player_list
  
def divide_players(participants):    
  # divide the list of participant players into two lists of dictionaries for experienced and no experience players
  exp =[]
  noexp =[]
    
  # iterate through pulled list of dicitonaries (participants list) to place players into two groups       
  for players in participants[1:19]:
      if players['Soccer Experience'] == 'YES':
        exp.append(players)
      else:
        noexp.append(players)
  return exp, noexp
  print("divide")

def assign_roster(participants):        
  # add players (player's dictionary) evenly into three seperate teams i.e. lists of dictionaries, which are 1,2,3. 
  
  exp, noexp = divide_players(participants)
  
  for team in Roster:
    for i in range (0,3):
      team.append(exp.pop())
      team.append(noexp.pop())
  return Roster    

def create_txt(Roster):
  # write player info (from list of player dictionaries) into a team roster .txt file 
  
  # open file and create list for team names
  team_names = ["Sharks", "Dragons", "Raptors"]
  
  with open("teams.txt", "a") as file:  
  #create a counter for team names when writing to the txt file  
    g=0
  # iterate through Roster and team_names to print team names and variables in txt file  
    for team in Roster:
      file.write(("\n"+"{}"+"\n"+"-"*10+"\n"+"-"*10+"\n").format(team_names[g]))
      g +=1
      for i in range (0,6):
        file.write(("{}, {}, {} \n").format(team[i]['Name'], team[i]['Soccer Experience'], team[i]['Guardian Name(s)']))

def player_filename(name):
  # create lowercase .txt file names for each player in the soccer league
      file_name=(name.lower().replace(" ", "_")+".txt")
      return file_name

def guardian_letter(Roster):
  
  team_names = ["Sharks", "Dragons", "Raptors"]
  
  letter = ("\nDear {}, \nCongrats on {} joining this season's soccer league as part of the {} team.  Go {}!"+
           "\nThe first practice will be on May 20, 2017 at 8:30 am sharp. Please don't be late."+
           "\nRegards,"+
           "\nSoccer League Coach\n")

  #create a counter for team names when writing to the txt file  
  g=0
  # iterate through Roster and team_names to print team names and variables in txt file  
  for team in Roster:
    for i in range (0,6):
      filename = player_filename(team[i]['Name'])
      with open(filename, "a") as file:
        file.write(letter.format(team[i]['Guardian Name(s)'], team[i]['Name'], team_names[g], team_names[g]))
    g += 1

# prevent code from running when imported
if __name__ == '__main__':

# create list of dictionaries for three teams and Roster list holding 3 team lists  
  Sharks =  []
  Dragons = []
  Raptors = []
  Roster = [Sharks, Dragons, Raptors]
  
# run fucntions to generate team roster text file and guardian letters text files 
  participants = read_file('soccer_players.csv')
  divide_players(participants)
  assign_roster(participants)
  create_txt(Roster)
  guardian_letter(Roster)
  