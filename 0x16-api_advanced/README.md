#0x16. API advanced

##Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

###Resources

[Reddit API Documentation](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA)
[Query String](https://intranet.alxswe.com/rltoken/luFn_zrgmAQ0OAO_PEI9bA)

## Learning Objectives

### General

* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

| Tasks  | File | Function |
| -----  | ---- | -------- |
|0. How many subs? | [0-subs.py](./0-subs.py) |function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0. 
Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.|
|1. Top Ten| [1-top_ten.py](./1-top_ten.py) | Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.|
| 2. Recurse it! | [2-recurse.py](./2-recurse.py) | a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None. |
