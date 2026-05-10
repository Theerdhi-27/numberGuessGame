import streamlit as st
import random

st.set_page_config(
    page_title="Guess The Number",
    page_icon="🎯",
    layout="centered"
)

# Title
st.title("🎯 Guess The Secret Number")
st.write("Try to guess the secret number!")

# Difficulty Selection
difficulty = st.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Difficulty Settings
if difficulty == "Easy":
    max_num = 50
    attempts = 10
elif difficulty == "Medium":
    max_num = 100
    attempts = 7
else:
    max_num = 200
    attempts = 5

# Initialize Session State
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, max_num)

if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = attempts

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# User Input
guess = st.number_input(
    f"Enter a number between 1 and {max_num}",
    min_value=1,
    max_value=max_num,
    step=1
)

# Guess Button
if st.button("Guess"):
    
    if not st.session_state.game_over:

        if guess > st.session_state.secret_number:
            st.warning("📈 Too High!")

        elif guess < st.session_state.secret_number:
            st.warning("📉 Too Low!")

        else:
            st.success("🎉 Congratulations! You guessed correctly!")
            st.balloons()
            st.session_state.game_over = True

        st.session_state.attempts_left -= 1

        if st.session_state.attempts_left == 0 and not st.session_state.game_over:
            st.error("😢 Game Over!")
            st.write(
                "Secret Number was:",
                st.session_state.secret_number
            )
            st.session_state.game_over = True

# Display Attempts
st.info(f"Attempts Left: {st.session_state.attempts_left}")

# Restart Button
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, max_num)
    st.session_state.attempts_left = attempts
    st.session_state.game_over = False
    st.rerun()