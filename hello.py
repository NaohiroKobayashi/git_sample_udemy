class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"
    
    # 小林が担当
    # 機能追加：say_goodbyeメソッドを追加
    def say_goodbye(self):
        return f"Goodbye, {self.name}!"