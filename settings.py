import pygame
class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализируем настройки игры"""
        #Параметры игры
        self.game_active = False
        self.counter = 0 #Используй для подстчета очков, пока нигде не используется
        #Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1000
        self.bg_color = (200,200,230)

        #Параметры попугая
        self.defolt_speed = 17
        self.decrease_speed = 1

        #Параметры колонны
        self.column_start_speed = 7
        self.column_hole = 400
        self.spawn_time = 2000
        self.image_bot = pygame.image.load('images/Top_column.png')
        self.image_top = pygame.transform.rotate(self.image_bot, 180)
        self.image_mid = pygame.image.load('images/longlong_mid.png')

    def _reset(self):
        """Выводим все к начальным настройкам"""
        #Параметры игры
        self.game_active = False
        self.counter = 0
        #Параметры попугая
        self.defolt_speed = 17
        self.decrease_speed = 1

        #Параметры колонны
        self.column_start_speed = 7
        self.column_hole = 400
        self.spawn_time = 2000
