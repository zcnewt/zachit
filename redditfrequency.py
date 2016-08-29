"""
reddit frequency.py
token:7saTq39OL_lLSg
secret:-767lr8CMBqPoghX8tZ7FvepJU0
https://github.com/reddit/reddit/wiki/OAuth2
get number of posts over time for a given period of time for a given subreddit

POST https://www.reddit.com/api/login/username?user=[username]&passwd=[password]&api_type=json HTTP/1.1
Response:
{
  "json": {
    "errors": [],
    "data": {
      "need_https": true,
      "modhash": "example",
      "cookie": "another,2016-08-21T19:50:48,example"
    }
  }
}
Use in X-Modhash header:




input: subreddit, time period, granularity

output: datapoints for given granularity specifying number of posts
[<timestamp>:<number of posts>,...]

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_api_link', '_comment_sort', '_comments', '_comments_by_id', '_extract_more_comments', '_get_json_dict', '_has_fetched', '_info_url', '_insert_comment', '_methods', '_orphaned', '_params', '_populate', '_post_populate', '_replaced_more', '_underscore_names', '_uniq', '_update_comments', 'add_comment', 'approve', 'approved_by', 'archived', 'author', 'author_flair_css_class', 'author_flair_text', 'banned_by', 'clear_vote', 'clicked', 'comments', 'created', 'created_utc', 'delete', 'distinguish', 'distinguished', 'domain', 'downs', 'downvote', 'edit', 'edited', 'from', 'from_api_response', 'from_id', 'from_json', 'from_kind', 'from_url', 'fullname', 'get_duplicates', 'get_flair_choices', 'gild', 'gilded', 'has_fetched', 'hidden', 'hide', 'hide_score', 'id', 'ignore_reports', 'is_self', 'json_dict', 'likes', 'link_flair_css_class', 'link_flair_text', 'lock', 'locked', 'mark_as_nsfw', 'media', 'media_embed', 'mod_reports', 'name', 'num_comments', 'num_reports', 'over_18', 'permalink', 'quarantine', 'reddit_session', 'refresh', 'removal_reason', 'remove', 'replace_more_comments', 'report', 'report_reasons', 'save', 'saved', 'score', 'secure_media', 'secure_media_embed', 'select_flair', 'selftext', 'selftext_html', 'set_contest_mode', 'set_flair', 'set_suggested_sort', 'short_link', 'stickied', 'sticky', 'subreddit', 'subreddit_id', 'suggested_sort', 'thumbnail', 'title', 'undistinguish', 'unhide', 'unignore_reports', 'unlock', 'unmark_as_nsfw', 'unsave', 'unset_contest_mode', 'unsticky', 'ups', 'upvote', 'url', 'user_reports', 'visited', 'vote']
"""

import praw
r = praw.Reddit(user_agent='my_cool_application')
#period='day'    'all','year','month','week','day','hour'
submissions = r.get_subreddit('worldnews').get_top(plimit=15,period='day')

while 1:
    submission = next(submissions)
    print(submission.title, submission.ups, submission.downs, sep=",")
    print(dir(submission))
    break