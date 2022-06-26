import pandas
import turtle
from map_tags import Tag


def get_mouse_click_coord(x, y):
    print(x, y)


# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

# Background
screen = turtle.Screen()
screen.title("Us Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Prompt
correct_list = []
score = 0

# DataFrame
game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title=f"{len(correct_list)}/50 states correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    with open("50_states.csv", mode="r") as state_file:
        states_dataframe = pandas.read_csv(state_file)

        for i in states_dataframe.state:
            if answer_state == i:
                correct_list.append(answer_state)
                x_loc = int(states_dataframe.x[states_dataframe.state == answer_state])
                y_loc = int(states_dataframe.y[states_dataframe.state == answer_state])
                print(correct_list)
                tag = Tag(name=answer_state, xcor=x_loc, ycor=y_loc)

# TODO 1: Check if answer_state is in csv file:
# TODO 2: Write correct guess on to the map
# TODO 3: Use a loop to continue guessing
# TODO 4: Keep track of guesses in list and score.


screen.exitonclick()
