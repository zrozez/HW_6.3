class Hello:

    def __init__(self, name):
        self.name = name
    
    @property
    def hello(self):
        return self.name

print(Hello('Temirlan hi').hello)
