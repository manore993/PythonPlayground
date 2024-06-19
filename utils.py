def my_sum(a, b):
    return a + b

def reverse_str(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        final_string += initial_string[index - 1]
        index = index - 1
    return final_string

import time 

def request():
    time.sleep(10)
    return 10

def main_function():
    response = request()
    return response

class Player:
    def _init_(self, name, level):
        self.name = name
        self.level = level
    
    def get_info(self):
        infos = {"name" : self.name,
        "level" : self.level}
        return infos
    
def create_player():
    player = Player("Ranga", 100)
    infos = player.get_info()
    return infos

PI = 3.1415

def perimeter(radius):
    return 2 * PI * radius