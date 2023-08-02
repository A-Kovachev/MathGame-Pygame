import pygame
from sys import exit
import random
from deadline import Deadline
from problemBox import Problem
from score_level import Score
from buttom import Button
from endScreen import EndScreen
from winScreen import WinScreen
from startScreen import StartScreen

pygame.init()
screen = pygame.display.set_mode((490,700))
pygame.display.set_caption('Quick Math')
clock = pygame.time.Clock()


color_background = (191,239,255)
backfround_surf = pygame.Surface((490,700))
backfround_surf.fill(color_background)

box_speed = 1 
min_value = 5 
max_value = 20 
op_arr_closing_index = 2
winScreen = WinScreen()
endScreen = EndScreen()
deadline = Deadline()
startScreen = StartScreen()
result = Score()
clicked = False
create_new_phase = False
game_over = False
game_won = False
game_start = True

def SolveProblem(value_1, value_2, operator) -> int:

    answer = 0

    if operator == "+":
        answer = value_1 + value_2
    elif operator == "-":
        answer = value_1 - value_2
    elif operator == "x":
        answer = value_1*value_2
    elif operator == "/":
        answer = value_1/value_2

    return answer

def CreateRandomAnswers(value_1, value_2, operator) -> str:
   
    answer = 0
    random_operators = ["+","-"]
    op = random_operators[random.randrange(1,2)]
    arr = [value_1,value_2]
    randomising_values = random.randrange(1,4)
    random_index = random.randrange(1,2)

    if op == "+":
        arr[random_index] += randomising_values
    else:
        arr[random_index] -= randomising_values

    value_1 = arr[0]
    value_2 = arr[1]

    if operator == "+":
        answer = value_1 + value_2
    elif operator == "-":
        answer = value_1 - value_2
    elif operator == "x":
        answer = value_1*value_2
    elif operator == "/":
        answer = value_1/value_2

    return str(answer)

def SetUpMaxValue(level, value) -> int:

    max_value = value

    if level == 2:
        max_value = 100
    elif level == 3:
        max_value = 150
    elif level == 4:
        max_value = 400
    elif level == 5:
        max_value = 600    
    elif level == 6:
        max_value = 700

    return max_value

def SetOperations(level, operation) -> int:

    op = operation

    if level == 2:
        op = 2
    elif level == 4:
        op = 3
    elif level == 5:
        op = 4

    return op
        
def PickProblemValues(max_value) -> int:
    
    min_value = 5
    values_arr = [i for i in range(min_value, max_value + 1)]
    value = values_arr[random.randrange(0, len(values_arr)-1)]
    return value

def PickOperation(arr_end_index) -> str:
    operations_arr = ["+","-","x","/"]
    return operations_arr[random.randrange(0,arr_end_index)]

while True:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            exit()
    
    if create_new_phase:

    
        value_1 = PickProblemValues(max_value)
        value_2 = PickProblemValues(max_value)
        operation = PickOperation(op_arr_closing_index)
        output_problem = str(value_1) + operation + str(value_2)
    
        problem_box = Problem(120,-100,output_problem)
    
        buttons_pos = [10,170,330] 
    
        random_index = random.randrange(0,len(buttons_pos)-1)
        answer = str(SolveProblem(value_1,value_2,operation))
        button_correct = Button(buttons_pos[random_index],answer)
        buttons_pos.pop(random_index)
    
        random_index = random.randint(0,1)
        fake_answer_1 = CreateRandomAnswers(value_1,value_2,operation)
    
        button_wrong_1 = Button(buttons_pos[random_index],fake_answer_1)
    
        buttons_pos.pop(random_index)
    
        fake_answer_2 = CreateRandomAnswers(value_1,value_2,operation)
        while fake_answer_1 == fake_answer_2:
            fake_answer_2 = CreateRandomAnswers(value_1,value_2,operation)
        button_wrong_2 = Button(buttons_pos[0],fake_answer_2)
    
        create_new_phase = False
    if game_start:
        start = startScreen.Draw(screen)
        if start:
            create_new_phase = True
            game_start = False
        pygame.display.update()
        
        clock.tick(60)
    elif game_won:
        winScreen.Draw(screen)
        pygame.display.update()
        clock.tick(60)
    elif game_over == False:
        
        screen.blit(backfround_surf,(0,0))
        deadline.Draw(screen) 
        result.Draw(screen)
        problem_box.Draw(screen,box_speed)
        button_correct.Draw(screen)
        button_wrong_1.Draw(screen)
        button_wrong_2.Draw(screen)
        
        if problem_box.rect_border.colliderect(deadline.deadline_rect): game_over = True
        
        pygame.event.get()
        
        mouse_pos = pygame.mouse.get_pos() 
        
        left_mouse_button = pygame.mouse.get_pressed()

        if button_correct.rect.collidepoint(mouse_pos) and \
        left_mouse_button[0] == 1 and clicked == False:

            clicked = True
            
            create_new_phase = True

            result.score += 1
            if result.score % 10 == 0:
                result.level += 1

                if result.level == 10: 
                    game_won = True
                    continue

                max_value = SetUpMaxValue(result.level,max_value)

                op_arr_closing_index = SetOperations(result.level,op_arr_closing_index)

                result.score = 0

                if not box_speed == 2:
                    box_speed = round(box_speed + 0.2,2)

        elif ((button_wrong_1.rect.collidepoint(mouse_pos) and left_mouse_button[0] == 1) or \
            (button_wrong_2.rect.collidepoint(mouse_pos) and left_mouse_button[0] == 1)) and clicked == False:

                clicked = True

                create_new_phase = True
                result.score -= 1
                if result.score < 0 and result.level == 0:
                    game_over = True

                elif result.score < 0:
                    result.level -= 1
                    max_value = SetUpMaxValue(result.level,max_value)
                    op_arr_closing_index = SetOperations(result.level,op_arr_closing_index)

                    result.score = 19

                    if not box_speed == 1:
                        box_speed = round(box_speed - 0.2,2)

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        pygame.display.update()
        clock.tick(60)
    else: 

        endScreen.Draw(screen,result.level,result.score)

        if endScreen.exit_rect.collidepoint(pygame.mouse.get_pos()) and \
            pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                clicked = True
                exit()

        elif endScreen.retry_rect.collidepoint(pygame.mouse.get_pos()) and \
            pygame.mouse.get_pressed()[0] == 1 and clicked == False:
              clicked = True
              result.level = 0
              result.score = 1
              game_over = False
              create_new_phase = True
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False

        pygame.display.update()
        clock.tick(60)