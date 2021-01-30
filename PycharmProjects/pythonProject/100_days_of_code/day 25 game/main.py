import pandas as pd
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":

        # MODIFICATION BASED ON DAY26
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_t_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# If the answer_state is one of the states in the dataframe
    #If the got right
        #Create a turtle to write the name of the state at x, y

# while score < 51:
#     if df.loc[df_states.state.lower() == answer_state.lower()] == True
#         state = df_states.state
#         x = df_states.x
#         y = df_states.y
#         score += 1
#         turtle.penup()
#         turtle.goto(x, y)
#         turtle.write(state)
#     answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state's name?")





# Get x en y coördinates for the click position
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
