# django-blog-website
Learning Django Framwork to create a blog website (Bootstrap as a frontend)
> Source: Django Tutorials of Corey Schafer
## Feature:
1. Authentication
2. Admin Site
3. CRUD Post
4. Update User Profile
5. Pagination
6. Email and Password Reset
7. 

## import post into db
```bash
python manage.py shell
```

```python
import json
from blog.models import Post
with open('posts.json') as f:
    posts_json = json.load(f)
for post in posts_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()
exit()
```

## Set Gmail and password environment to reset password

```bash
set EMAIL_HOST_USER=phanhoaithuabc@gmail.com
set EMAIL_HOST_PASSWORD=***
```

## Create a migration for the project

```bash
python manage.py makemigrations
```

## Migrate database of the project

```bash
python manage.py migrate
```

## Create superuser for admin page

```bash
python manage.py createsuperuser
```

## Run the project

```bash
python manage.py runserver
```