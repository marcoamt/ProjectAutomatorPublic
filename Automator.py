import sys
from github import Github

#save commands in /Users/{username}/.my_custom_commands.sh

def auto():
  #take the params passed by the custom commands
  folderName = str(sys.argv[2])

  username = "{git user}"
  password = "{password}"
  login = Github(username, password)

  #git login
  user = login.get_user()
  #create repo on github
  user.create_repo(folderName)
  
if __name__ == "__main__":
    auto()
