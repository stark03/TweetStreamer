# Tweet Streamer

### A Django REST API for storing/fethching tweets for a high traffic event

The API is used to stream tweets for a recent high trafiic event and stores these tweets in a SQLite databse for later 
access and analysis.

#### API Provides :-

* Endpoints to start/stop streaming.
* Time limit based streaming.
* Ordering of tweets based on particular fields.
* Searching of words/text in tweets.
* CSV export support

### Setup and Installation :-

1. Clone the git repository.
2. Make sure python3.5+ is installed.
3. Install the requirements listed in requirements.txt

### Twitter Authentication :-

1. Open file **private.py** in subdirectory **Streamer**
2. Replace your-keys* , your-tokens* with your authentication keys and access tokens.

### Creating Database and establishing the server
Open the terminal and enter:- 

```emacs
$ cd TweetStreamer
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### API Endpoints :-

#### 1. To start/trigger streaming :-

#### GET /keyword/{any-keyword}/{time-limit}/

here replace {any-keyword} by keyword you want to search,
             {time-limit} by an integer value in seconds stating the time limit for which you want to stream the tweets.
             
**Note :-** Streaming can be also be stooped by using **GET /tweets/**

#### 2. To fetch the tweets :-

#### GET /tweets/

#### 3. To fetch the users :-

#### GET /users/

#### 4. To search in tweets :-

#### GET /tweets/?search=______

here replace ______ by the aprropriate words you want to search for

#### 5. To sort/order the tweets with respect to a particular field :-

#### GET /tweets/?ordering=________

for ascending :- replace ______ by field-name and 
for descending :- replace _______ by -field-name

#### 6. To search and sort both:-

#### GET /tweets/?ordering=_______&search=________

#### 7. To export tweets data as CSV:-

#### GET /csv/

### Technologies used :-

1. Python 3.5
2. Django Rest Framework
3. Django Filters
4. Tweepy (twitter streaming library in python)

### Features to be added :-

1. Multiple-keyword search
2. Use of NoSQL databases
3. More personalized filters like (greater than, less than) for integer fields.
