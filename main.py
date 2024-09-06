from typing import Literal

from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()


def computer_choice() -> str:
    choices = ["Камень", "Ножницы", "Бумага"]
    return random.choice(choices)


@app.get("/choice")
def user_choice(user: Literal["Камень", "Ножницы", "Бумага"]):
    computer = computer_choice()

    if user == computer:
        return f"Ничья. Компьютер выбрал {computer}"
    elif (
        (user == "Камень" and computer == "Ножницы")
        or (user == "Бумага" and computer == "Камень")
        or (user == "Ножницы" and computer == "Бумага")
    ):
        return f"Вы выиграли! Компьютер выбрал {computer}"

    return f"Вы проиграли:( Компьютер выбрал {computer}"


