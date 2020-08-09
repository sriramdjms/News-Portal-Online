# NewsPortalOnline
# Django Framework
# Python
# HTML
# CSS
# Javascript
FLOW OF WEB APPLICATION:

# USER:
    Login
    Register
    Select Preferences
    View News
    Make Payments
# Login
    You first enter the login page
# Registraion
    Being a User you first need to register in the site:
    Registration requires USERNAME, EMAIL, PHONENUMBER, and PASSWORD
    These details will be later stored in the database.
# Preferences
    Then Registered User enter Cards Page where you select your preferences.
 # News
    Registered User enter the News Home Page.
    Here By the left and right Arrows he change the news and it shows the Top headlined news at that                                                   
    Specific time the news gets refreshed for every few seconds and displays the Real time news.
    There is also a Search option for the registered user if he intends to search for a particular news.
    
# Admin:
    He acts as a Super User and is responsible for managing the database.
    
# Actions Performed:
    Login Authentication
    News Recommendation
# Login Authentication:
    When the Registered User enters the Username and Password. It searches for the username in the database and checks if the password stored in the database                         matches with the password entered by the user. If it matches it moves further else it displays a dialogue saying “Please check you credentials”.
# News Recommendation
         It is done from “newsapi.org” python package.
         There is an API key required to work with it.
         It contains Title, Article, Description, Content.
         Json.dump, Json.load does the job efficiently for us by cleaning the data display the news Required.
