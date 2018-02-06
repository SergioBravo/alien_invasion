#!/usr/bin/python3
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #Инициализация pygame, settings и создание объекта экрана
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("ALien Invasion")

    #Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")

    #Создание экземпляра для хранения игровой статистики и счета
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Назначение цвета фона
    bg_color = (230, 230, 230)

    #Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)

    bullets = Group()

    aliens = Group()

    #Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            #print(len(bullets))

            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        #При каждом проходе цикла перерисовываем экран
        gf.update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button)

run_game()
