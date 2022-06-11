from user import User
from post import Post

matt = User("matt.muroya@gmail.com", "Matt Muroya",
            "password", "Software Engineer")

barack = User("barack@obama.com", "Barack Obama",
              "password", "Former President")


matt.get_user_info()

barack.get_user_info()


matts_post = Post("ayy barack lmao sup", matt)

baracks_post = Post("my BOI", barack)


matts_post.get_post_info()

baracks_post.get_post_info()
