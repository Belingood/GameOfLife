import random
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width=25, height=25):
        self.__width = width
        self.__height = height
        self.world = self.generate_universe()
        self.counter = 0

    def form_new_generation(self):
        universe = self.world
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                lv = self.__get_near(universe, [i, j])
                res_lv = (lv < 2, lv == 2, lv == 3, lv > 3).index(True)
                new_world[i][j] = {1: {0: -1, 1: 1, 2: 1, 3: -1},
                                   -1: {0: 0, 1: 0, 2: 1, 3: 0},
                                   0: {0: 0, 1: 0, 2: 1, 3: 0}}[universe[i][j]][res_lv]

        self.world = new_world
        self.counter += 1

    def generate_universe(self):
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    @staticmethod
    def __get_near(universe, pos, system=None):
        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])]:
                count += 1
        return count
