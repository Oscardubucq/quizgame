import pgzrun
TITLE = "quiz master"
WIDTH = 800
HEIGHT = 600
marquee_box = Rect(0,0,720,50)
question_box = Rect(0,0,550,130)
timer_box = Rect(0,0,150,130)
skip_box = Rect(0,0,150,300)
answer_box1 = Rect(0,0,250,130)
answer_box2 = Rect(0,0,250,130)
answer_box3 = Rect(0,0,250,130)
answer_box4 = Rect(0,0,250,130)

score = 0
time_left = 10
question_file_name = "questions.txt"
marquee_message = ""
is_game_over = False

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(25,25)
question_box.move_ip(25,100)
timer_box.move_ip(600,100)
skip_box.move_ip(600,280)
answer_box1.move_ip(25,280)
answer_box2.move_ip(320,280)
answer_box3.move_ip(25,450)
answer_box4.move_ip(320,450)

def draw ():
    global marquee_message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(marquee_box,"blue")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_box,"blue")
    for i in answer_boxes :
        screen.draw.filled_rect(i,"orange")

    marquee_message = "welcome to the Quiz Master Game"
    marquee_message = marquee_message + f"Q:{question_index}of{question_count}"

    screen.draw.textbox(marquee_message,marquee_box,color = "white")

    screen.draw.textbox(str(time_left),timer_box,color = "white")

    screen.draw.textbox("SKIP",skip_box,color = "white",angle = -90)

    screen.draw.textbox(question[0].strip(),question_box,color = "white")

    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color = "black")
        index += 1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x -= 2
    if marquee_box.right<0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count,questions
    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()
def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int (question[5]):
                correct_answer()
            else:
                game_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score ,question,time_left,questions
    score += 1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question,time_left,is_game_over
    message = f"GAME OVER!You got {score}out of 11 questions correct!"
    question = [message,"-","-","-","-",5]
    time_left = 0
    is_game_over = True

def skip_question():
    global question,time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(update_time_left,1)







pgzrun.go()
