from user import User
from post import Post

app_user_one = User("olayemi@come.com", "Olayemi", "pass1", "Cloud")
app_user_one.get_user_info()

app_user_one.change_job_title("Cloud Architect")
app_user_one.get_user_info()

new_post = Post("on a secret mission today", app_user_one.name)
new_post.get_post_info()
