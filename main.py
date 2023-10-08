from funcion import *

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("космічний шутер")


def run():
    game = True


    hero = Hero(setting_win["WIDTH"] // 2 - setting_hero["WIDTH"] // 2,
        setting_win["HEIGHT"] - setting_hero["HEIGHT"] - 10,
        setting_hero["WIDTH"],
        setting_hero["HEIGHT"] )
    clock = pygame.time.Clock()


    while game:
        window.fill((0,0,200))
        hero.move(window)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False




        clock.tick(60)
        pygame.display.flip()

run()