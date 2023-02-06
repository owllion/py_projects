import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# TODO: 1.check answer if it's in the list / 2.track the score/
# TODO: 3. if wrong,then nothing happen.

guess_list = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# 超重要!這邊一定要轉成list才可以用 if xx in list語法

while len(guess_list) < 50:
    answer_state = screen.textinput(
        title=f"{len(guess_list)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()
    # title -> make first letter capitalized

    if answer_state == "Exit":
        # 記得是"Exit"，因為answer_state有用title()

        missing_states_list = []
        for state in all_states:
            if state not in guess_list: missing_states_list.append(state)
        new_data = pandas.DataFrame(missing_states_list)
        new_data.to_csv("state_to_learn")

        break

    if answer_state in all_states:
        guess_list.append(answer_state)

        # 要創建新的turtle實體，上面的是image實體的
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
