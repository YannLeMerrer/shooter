import pygame
from game import Game
from projectile import Projectile
from monster import Monster


def create_game_window():
    pygame.init()

    pygame.display.set_caption("Comet Fall Game")
    window = pygame.display.set_mode((2435, 1027))
    return window


screen = create_game_window()
background = pygame.image.load('assets/bg.jpg')
game = Game()

monsters = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
game_is_running = True
game_is_paused = False
max_x = screen.get_width()
min_x = 0


def update_screen():
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    projectiles.draw(screen)
    monsters.draw(screen)
    pygame.display.flip()


def update_player_position():
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < max_x - game.player.rect.width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= min_x:
        game.player.move_left()


def update_projectile_position():
    projectiles.update()


def update_monsters_position():
    monsters.update()
    collisions = pygame.sprite.groupcollide(monsters, projectiles, True, True)
    #for monster in monsters:
     #   if collisions[monster]:
      #      monster.kill()
       #     for projectile in collisions[monster]:
        #        projectile.kill()

def process_keys():
    global game_is_running, projectiles, game_is_paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                projectile = Projectile(game.player.rect.x + 150, game.player.rect.y + 100)
                projectiles.add(projectile)
            if event.key == pygame.K_m:
                mummy = Monster(max_x - 150, game.player.rect.y + 50)
                monsters.add(mummy)
            if event.key == pygame.K_p:
                game_is_paused = not game_is_paused
                print("Pause")
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



def run_game():
    while game_is_running:
        if not game_is_paused:
            update_screen()
            update_player_position()
            update_projectile_position()
            update_monsters_position()
        process_keys()

        


run_game()
