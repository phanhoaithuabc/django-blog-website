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
    posts_json = json.load()
for post in posts_json:
    post = Post(title=post['title'], content=posts['content], author_id=post['user_id'])
    post.save()
exit()
```
