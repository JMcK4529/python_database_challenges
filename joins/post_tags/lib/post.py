class Post:
    def __init__(self, id, title, tags=None):
        self.id = id
        self.title = title
        self.tags = tags or []

    def __repr__(self):
        return f"Post({self.id}, {self.title}, tags={self.tags})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__