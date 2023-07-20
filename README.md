# Philosophy-website
This is the skeleton (no database and placeholder text) for the website used to diplay posts and information. The website is intended to be a resource for the philosophy group that I run. After each session, posts are uploaded on the subject spoken about. Additional information such as location, format, time etc. as well as an FAQ page are included.

#### Posts/Sessions
Posts and sessions are created using Django's admin page. Posts and sessions are created separately and a third table called PostsInSession is used to pair the session with the applicable post. Posts can also be created as a draft and published later.

#### Tags
`django-taggit` (https://django-taggit.readthedocs.io/en/latest/) is used to apply tags to posts. When a post is created, a tag can be added, allowing for filtering by subject matter on the sessions page.
