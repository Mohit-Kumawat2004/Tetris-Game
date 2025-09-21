import pygame
import sys
from game import Game
from colors import Colors

pygame.init()
 
# Define fonts and surfaces
title_font = pygame.font.Font(None, 40)
menu_font = pygame.font.Font(None, 60)
title_large_font = pygame.font.Font(None, 100)  # Large font for the game title
creator_font = pygame.font.Font(None, 30)  # Font for the creators' names
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Define rectangles for UI elements
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
button_rect = pygame.Rect(320, 500, 170, 50)  # Close Game button rectangle

# Define difficulty modes
EASY = 300
NORMAL = 200
HARD = 100

# Initialize screen and game
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("TETRIS DASH")
clock = pygame.time.Clock()

# Function to display the menu
def display_menu():
    screen.fill((128, 0, 128))  # Purple background color
    easy_button = pygame.Rect(320, 200, 170, 50)
    normal_button = pygame.Rect(320, 300, 170, 50)
    hard_button = pygame.Rect(320, 400, 170, 50)

    pygame.draw.rect(screen, Colors.light_blue, easy_button, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, normal_button, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, hard_button, 0, 10)

    easy_text = menu_font.render("Easy", True, Colors.white)
    normal_text = menu_font.render("Normal", True, Colors.white)
    hard_text = menu_font.render("Hard", True, Colors.white)

    screen.blit(easy_text, easy_text.get_rect(centerx=easy_button.centerx, centery=easy_button.centery))
    screen.blit(normal_text, normal_text.get_rect(centerx=normal_button.centerx, centery=normal_button.centery))
    screen.blit(hard_text, hard_text.get_rect(centerx=hard_button.centerx, centery=hard_button.centery))

    # Display the game title
    title_text = title_large_font.render("TETRIS DASH", True, (255, 255, 0))  # Yellow color
    screen.blit(title_text, title_text.get_rect(centerx=screen.get_width() / 2, centery=100))

    # Display the Developer names
    creators = ["Mohit Kumawat"]
    for i, creator in enumerate(creators):
        creator_text = creator_font.render(creator, True, (255, 165, 0))  # Orange color
        screen.blit(creator_text, creator_text.get_rect(centerx=screen.get_width() / 2, centery=600 + i * 30))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return EASY
                if normal_button.collidepoint(event.pos):
                    return NORMAL
                if hard_button.collidepoint(event.pos):
                    return HARD

# Get selected mode
selected_mode = display_menu()

game = Game()

# Custom event for game updates
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, selected_mode)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Display final message and score
                print(f"Game finished with score: {game.score}")
                pygame.quit()
                sys.exit()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, 
                                                                  centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # Draw Close Game button
    pygame.draw.rect(screen, Colors.red, button_rect, 0, 10)
    button_text_surface = title_font.render("Close Game", True, Colors.white)
    screen.blit(button_text_surface, button_text_surface.get_rect(centerx=button_rect.centerx, 
                                                                  centery=button_rect.centery))

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)

