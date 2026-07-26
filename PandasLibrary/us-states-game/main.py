import turtle as tt
import pandas as pd

screen = tt.Screen()
screen.title("Us State Game")
image = "PandasLibrary/us-states-game/blank_states_img.gif"
screen.addshape(image)
tt.shape(image)


data = pd.read_csv("PandasLibrary/us-state-game/50_states.csv")
allStates = data.state.to_list()

answer = screen.textinput(title = "Guess the state", prompt = "What's another state").lower()
print(answer)

if answer in allStates:
    t = tt.Turtle()