import random, math

def initial_random_movement(max_value:float, display_height:int):
    a = math.tan(math.degrees(random.randint(1, 120)))

    def module(x):
        return math.sqrt(x**2)

    def f(x:float) -> float:
        function = a * x

        return module(function) + display_height/2

    return f

def check_border_colision_y(func, x:float, incrementer_y:float, screen_size_y:float):
    if not screen_size_y > func(x+incrementer_y) > 0:
        return True

    return False

def check_table_colision(func, tables):
    if table.collidelist(tables) >= 0:
        return True

    return False  
    
