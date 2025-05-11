class Hello:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}!"
    
    # 小林が担当
    # 機能追加：say_goodbyeメソッドを追加
    def say_goodbye(self):
        return f"Goodbye, {self.name}!"
    
    # 機能追加：how_are_youメソッドを追加
    def how_are_you(self):
        return f"How are you, {self.name}?"
    
    # 機能追加：こんにちは
    def say_konnichiwa(self):
        return f"こんにちは、{self.name}さん！"