# deurl

Ever wanted to have a customised url for a site?
Or the url is to big to remember and share.

this application takes input of a url and a customised name(optional) to give url hash
which is to be used for redirection purpose.


## Functionalities:

### For frontend users:
1) unique redirection hash for a website
2) customised hash
3) model abstraction
4) only user specific data to be shown (privacy purpose)

### For backend maintaniers
1) admin panel search functionalities
2) model inline function with other model
3) custom search
4) dissolved anonymous user problem


## Working on a local server
You need to provide:
1) a db.sqlite3
2) a .env file which includes :
    1) SECRET_KEY
    2) DEBUG (0 for false, 1 for true)
    

### Site is live at:
https://deurl.herokuapp.com/