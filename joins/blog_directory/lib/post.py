class Post:
    def __init__(self, id, title, post_content, comments=None):
        self.id = id
        self.title = title
        self.post_content = post_content
        self.comments = comments or []

    def __repr__(self):
        return f"Post({self.id}, {self.title}, " + \
            f"{self.post_content}, comments={self.comments})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__