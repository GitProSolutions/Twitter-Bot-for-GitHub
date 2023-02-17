import tweepy
from github import Github
import random
import time

# Authenticate to Twitter
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Authenticate to GitHub
ACCESS_TOKEN_GITHUB = 'YOUR_GITHUB_ACCESS_TOKEN'
g = Github(ACCESS_TOKEN_GITHUB)

# Define the repository and Twitter handle to use
REPO = 'your-repo'
HANDLE = 'your-twitter-handle'

# Define the adjectives and emojis to use in the tweet
ADJECTIVES = ['awesome', 'amazing', 'incredible', 'fantastic', 'mind-blowing']
EMOJIS = ['💥', '🎉', '🚀', '👍', '👏']

# Search for the latest commit in your repository
def get_latest_commit(repo_name):
    repo = g.get_repo(repo_name)
    commits = repo.get_commits()
    latest_commit = commits[0]
    return latest_commit

# Generate the tweet text from the latest commit
def generate_tweet(commit):
    author = commit.author.name
    commit_message = commit.commit.message
    commit_url = commit.html_url
    adjective = random.choice(ADJECTIVES)
    emoji = random.choice(EMOJIS)
    tweet = f'🚨 New commit alert! 🚨\n\n{HANDLE} just pushed an {adjective} update to {REPO}! {emoji}\n\n"{commit_message}" 💻👨‍💻💡\n\nCheck it out here 👉 {commit_url} #coding #github #opensource #webdev'
    return tweet

# Post the tweet to Twitter
def post_tweet(tweet):
    api = tweepy.API(auth)
    api.update_status(tweet)

# Set up a schedule for the bot to run
def run_bot():
    while True:
        latest_commit = get_latest_commit(REPO)
        tweet = generate_tweet(latest_commit)
        post_tweet(tweet)
        print('Tweet posted:', tweet)
        time.sleep(3600) # Run every hour

run_bot()
