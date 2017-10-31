**tweetbot Version 1.1 10/31/2017**

**General Description:**
____________________

tweetbot is a python program which can be used to handle multiple twitter accounts. 

By design tweetbot performs four actions.

1. Tweet a random quote from a quote API
2. Tweet line by line from a line separated text file (ASCII characters) 
   with a hash tag passed as argument.
3. Retweet another tweet with the same hash tag which was passed earlier
4. Retweet a tweet with a random hash tag of a particular interest.
  
By design,  all the four activities will spawn as separate processes and 
some are limited by hard coded numbers (~50) and the time period between 
adjacent cycles of the above actions are also hard coded.  In the future 
versions,   I would  work on making it more configurable.  Till then the 
sleep values can be modified to a larger value in  code so that  Twitter 
wouldn't flag your account and take it down for abusing their automation
API.
  
**Usage Information:**
__________________

Usage:
`    ./tweetbot -c [CREDENTIALS_FILE] -f [TWEET_FILE] -h [HASHTAG]`

Example:
`    ./tweetbot -c credentials.csv -f tweets.txt -h hereyougo `
    
Sample credentials file can be seen in the repository.  The tokens and 
keys required in the same can be  generated by creating a twitter app.
>> https://apps.twitter.com/

**Disclaimer:**
___________
The author shall not be responsible or cannot be held liable for any 
unauthorised use of the tool. Be wise is the advice.
