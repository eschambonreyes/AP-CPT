# import the pygame module
import pygame
#import the random library to generate a random message at the end of the game
import random
#import library to add a pause
import time
#initialize the pygame features
pygame.init()

#screen dimensions
WIDTH = 800
HEIGHT = 600

#window title
pygame.display.set_caption("Football Mini-Game")

#color variables
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = ("WHITE")

#ball properties
#ball size
ball_radius = 20
#ball color
ball_color = RED
#ball stating position(the middle of the field)
ball_pos = [400, 220]
#ball speed at all times of the game when the ball is in play
ball_speed = 5
#ball velocity is the position of the ball at x and y coordinates
ball_velocity = [0, 0]  # Initial velocity

# Character 1 properties
char_size = 50
#char 1 start position
char_pos = [500, 200]
#char 1 color
char_color = BLACK
#char speed at all times of the game when the ball is in play
char_speed = 5

#character 2 properties
char_2_size = 50
#char 2 start position
char_2_pos = [WIDTH // 3 - char_2_size // 2, 200]
#char 2 color
char_2_color = WHITE
#char 2 speed when the ball is in play
char_2_speed = 5

#goal lines properties (thickness)
left_goalline_thickness = 5
right_goalline_thickness = 5

#wall parameters(thickness)
wall_thickness = 3

# pygame window setup
screen = pygame.display.set_mode((800, 500))

#initial player scores
player_1_score=0
player_2_score=0

#game instructions text 
game_instructions = pygame.font.Font(None, 20)#font, size
#code for defining the properties of the game instructions text 
game_instructions_surface = game_instructions.render("Black movement controls: w,a,s,d    White movement controls: arrow keys", True, [0, 0, 255])

#if black wins
black_results_text = pygame.font.Font(None, 50)
#text will say black wins in black
black_results_surface = black_results_text.render("Black Wins", True, [0, 0, 0])

#if white wins
white_results_text = pygame.font.Font(None, 50)
#code will say white wins in white text
white_results_surface = white_results_text.render("White Wins", True, [255, 255, 255])

#list of phrases that are said to the user after they stop playing
messages_list = ["Thank you for playing.", "Hope you enjoyed.", "Until next time."]

#function for when the user wants to stop playing
def end_message():
    #make the screen white
    screen.fill("white")
    quit_text = pygame.font.Font(None, 30)
    #random.choice is the command for picking a random element from messages_list
    quit_surface = quit_text.render(random.choice(messages_list), True, [0, 0, 0])
    # .blit is the command for drawing a surface onto another surface
    screen.blit(quit_surface, (20, 250))
    #Message will be drawn on next update in main loop

#function to continue the game
def continue_play():
    #set these variables to global so it applies to the entire code to make sure it is displayed
    global player_1_score
    global player_2_score
    #set scores to zero
    player_1_score = 0
    player_2_score = 0
    global char_speed
    global char_2_speed
    #reset the character speeds
    char_speed = 5
    char_2_speed = 5
    

#a function for when the game ends
def game_end():
    #return a true if user want to end the game
    status = False
    
    play_again_text = pygame.font.Font(None, 30)
    play_again_surface = play_again_text.render("Would you like to play again?", True, [0, 0, 0])
    screen.blit(play_again_surface, (500, 400))# the drawing, the coordinates for the text
    
    #the text of the option for continuing the game
    yes_text = pygame.font.Font(None, 30)
    yes_surface = yes_text.render("Yes(y)", True, [255, 255, 255])
    screen.blit(yes_surface, (500, 450))
    
    #the option for ending the game
    no_text = pygame.font.Font(None, 30)
    no_surface = no_text.render("No(n)", True, [255, 0, 0])
    screen.blit(no_surface, (580, 450))
    
    if keys[pygame.K_y]:#if the y key is pressed, the continue_play function is called up
        continue_play()
    elif keys[pygame.K_n]:#if the n key is pressed the end_message function is called up
        end_message()
        status = True
    #return bool value of true if the user wants to quit game    
    return status

#function to display the score
def display_score():
    score_text = pygame.font.Font(None, 50)
    #str() command converts the values of player_scores into string data types (words etc)
    score_surface = score_text.render("Score: " + str(player_1_score) + " - " + str(player_2_score), True, [255, 0, 0])
    screen.blit(score_surface, (100, 10))   

#set running to true to commence game
running = True

#while true 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        #if event type is pygame.QUIT, the user has closed the window by clicking 'x'
        if event.type == pygame.QUIT:
            running = False
    
    #the different keys
    keys = pygame.key.get_pressed()
    
    # initialize the green screen for the field
    screen.fill("green")
    
    #always have the score displayed
    display_score()
    
    #always display the instructions
    screen.blit(game_instructions_surface, (10, 390))
    
    #draw the field
    pygame.draw.rect(screen, "white", [100, 75, 600, 300], 7)
    #center line
    pygame.draw.line(screen, "white", [400, 370],[400,80], 7)
    #goals
    pygame.draw.rect(screen, "white", [20, 160, 87, 120], 7)
    pygame.draw.rect(screen, "white", [693, 160, 87, 120], 7)
    #center circle
    pygame.draw.ellipse(screen, "white", [350, 170, 100, 100], 7)
    
    #draw walls
    pygame.draw.rect(screen, WHITE, pygame.Rect(100, 75, 500, wall_thickness))#top wall
    pygame.draw.rect(screen, WHITE, pygame.Rect(100, 75 , wall_thickness, 302))#left wall
    pygame.draw.rect(screen, WHITE, pygame.Rect(700 - wall_thickness, 75, wall_thickness, 302))#right wall
    pygame.draw.rect(screen, WHITE, pygame.Rect(100, 378 - wall_thickness, 600, wall_thickness))#bottom wall
    
    #character 1 movement
    if keys[pygame.K_w]:#if w is pressed
        char_pos[1] -= char_speed#the y coordinate value of the character's speed is negated (causing it to go up)
    if keys[pygame.K_s]:
        char_pos[1] += char_speed#the character speed goes in a positive direction across the y axis 
    if keys[pygame.K_a]:
        char_pos[0] -= char_speed#the character speed is negated across the x axis (causing it to go left)
    if keys[pygame.K_d]:
        char_pos[0] += char_speed#the character speed is kept positive across the x axis

    #character 2(white) movement controls
        #up, down, left, right represent the arrow keys
    if keys[pygame.K_UP]:
        char_2_pos[1] -= char_2_speed
    if keys[pygame.K_DOWN]:
        char_2_pos[1] += char_2_speed
    if keys[pygame.K_LEFT]:
        char_2_pos[0] -= char_2_speed
    if keys[pygame.K_RIGHT]:
        char_2_pos[0] += char_2_speed

    #update ball position
    #ball moves across the x axis according to the velocity of the x value
    ball_pos[0] += ball_velocity[0]
    #ball moves across the y axis according to the velocity of the y value
    ball_pos[1] += ball_velocity[1]


    #draw ball and characters
    char_rect = pygame.Rect(char_pos[0], char_pos[1], char_size, char_size)#making all of the game components relative sizes
    ball_rect = pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)
    char_2_rect = pygame.Rect(char_2_pos[0], char_2_pos[1], char_2_size, char_2_size)
    
    #goal lines
    left_goalline = pygame.draw.rect(screen, "green", pygame.Rect(102, 168, left_goalline_thickness, 105))
    right_goalline = pygame.draw.rect(screen, "green", pygame.Rect(693, 168, right_goalline_thickness, 105))
    
    #walls
    left_wall_rect = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 75 , wall_thickness, 302))
    top_wall_rect = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 75, 600, wall_thickness))
    right_wall_rect = pygame.draw.rect(screen, WHITE, pygame.Rect(700 - wall_thickness, 75, wall_thickness, 302))
    bottom_wall_rect = pygame.draw.rect(screen, WHITE, pygame.Rect(100, 378 - wall_thickness, 600, wall_thickness))
    
    #coding for the collisions with character 1
    if char_rect.colliderect(ball_rect):
        if char_pos[0] < ball_pos[0]:#checking if char 1 is positioned to the left of the ball
            
            ball_velocity[0] = ball_speed #giving the ball a positive speed (ball goes to the right)
        elif char_pos[0] > ball_pos[0]: #is char 1 to the right of the ball?
            ball_velocity[0] = -ball_speed
        if char_pos[1] < ball_pos[1]: #is char 1 above the ball?
            ball_velocity[1] = ball_speed
        elif char_pos[1] > ball_pos[1]: #is char 1 below the ball?
            ball_velocity[-1] = -ball_speed
    
    #coding for the collisions with character 2
    if char_2_rect.colliderect(ball_rect):
        if char_2_pos[0] < ball_pos[0]: #is char 2 to the left of the ball?
            ball_velocity[0] = ball_speed
        elif char_2_pos[0] > ball_pos[0]: #is char 2 to the right of the ball?
            ball_velocity[0] = -ball_speed
        if char_2_pos[1] < ball_pos[1]: #is char 2 above the ball?
            ball_velocity[1] = ball_speed
        elif char_2_pos[1] > ball_pos[1]: #is char 2 below the ball?
            ball_velocity[-1] = -ball_speed
            
    #code for the collisions of the ball with the walls
    if ball_rect.colliderect(left_wall_rect):
        ball_velocity[1] *= 1#when the ball hits the left wall, reverse the x axis value to make it bounce
        ball_velocity[0] *= -1
    elif ball_rect.colliderect(top_wall_rect):
        ball_velocity[1] *= -1#when the ball hits the top wall, make the y value positive to make the ball go down
        ball_velocity[0] *= 1
    elif ball_rect.colliderect(right_wall_rect):
        ball_velocity[1] *= 1#when the ball hits the right wall, negate the x value to make the ball go backwards
        ball_velocity[0] *= -1
    elif ball_rect.colliderect(bottom_wall_rect):
        ball_velocity[1] *= -1#when the ball hits the bottom wall, negate the y value to make the ball go up
        ball_velocity[0] *= 1
    
    #code when player 1 scores
    if ball_rect.colliderect(left_goalline):
        player_1_score += 1#increase score
        ball_velocity[1] = 0 #make the ball stop moving up and down
        ball_velocity[0] = 0 #make the ball stop moving left and right
        ball_pos = [400,220]#restart the ball position
        char_pos = [500, 200]#reset both character positions
        char_2_pos = [WIDTH // 3 - char_2_size // 2, 200]
    #code when player 2 scores
    if ball_rect.colliderect(right_goalline):
        player_2_score += 1
        ball_velocity[1] = 0 #make the ball stop moving up and down
        ball_velocity[0] = 0 #make the ball stop moving left and right
        ball_pos = [400,220]
        char_pos = [500, 200]
        char_2_pos = [WIDTH // 3 - char_2_size // 2, 200]
       
    #draw ball and character
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    pygame.draw.rect(screen, char_color, pygame.Rect(char_pos[0], char_pos[1], char_size, char_size))
    pygame.draw.rect(screen, char_2_color, pygame.Rect(char_2_pos[0], char_2_pos[1], char_2_size, char_2_size))

    #when player 1 wins
    if player_1_score == 5:
        black_results_text.render("Black Wins", True, [0, 0, 0])
        screen.blit(black_results_surface, (500, 10))
        char_speed = 0 #stop the speed of the characters to stop pause the game
        char_2_speed = 0
        user_decision = game_end()#run function to end the game and return result
        if user_decision == True:#if the return of game_next is True, then change running variable to False to end the main loop
            running = False
        
    elif player_2_score == 5:
        white_results_text.render("White Wins", True, [255, 255, 255])
        screen.blit(white_results_surface, (500, 10))
        char_speed = 0
        char_2_speed = 0
        user_decision = game_end()
        if user_decision == True:
            running = False
        
   #update the drawings
    pygame.display.update()

#pause to display end of game message for 3 seconds    
time.sleep(3)    
pygame.quit()



