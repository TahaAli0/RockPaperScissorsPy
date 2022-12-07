import asyncio
import random


class Main:
    def __init__(self):
        self.name = None
        self.list_of_choices = [
            "rock",
            "paper",
            "scissors"
        ]
        """
        0 : rock-rock, paper-paper, scissors-scissors

        1: rock-paper
        2: rock-scissors
        4: scissors-paper
        """
        self.list_of_answers = [
            "That's a tie!",

            "Shift!, {} opened their hand and feasted on {}.",
            "Baam!, {} got crushed by {}.",
            "Swift!, {} injured {} to bits and pieces."
        ]

    async def start(self):

        if self.name is None:
            await self.input_name()

        choices = await self.get_choices()

        if not choices:
            return await self.start()

        answer = await self.justify(choices)

        print(answer)

        return await self.start()

    async def justify(self, choices):
        # Huge hardcoded block.

        user = choices[0].lower()
        cpu = choices[1].lower()

        if user == "rock":
            # tie
            if cpu == "rock":
                return self.list_of_answers[0]
            # lose
            if cpu == "paper":
                return self.list_of_answers[1].format(self.name, "CPU")
            # win
            if cpu == "scissors":
                return self.list_of_answers[2].format("CPU", self.name)

        if user == "paper":
            # win
            if cpu == "rock":
                return self.list_of_answers[1].format("CPU", self.name)
            # tie
            if cpu == "paper":
                return self.list_of_answers[0]
            # lose
            if cpu == "scissors":
                return self.list_of_answers[3].format("CPU", self.name)

        if user == "scissors":
            # lose
            if cpu == "rock":
                return self.list_of_answers[2].format(self.name, "CPU")
            # win
            if cpu == "paper":
                return self.list_of_answers[3].format(self.name, "CPU")
            # tie
            if cpu == "scissors":
                return self.list_of_answers[0]

    async def get_choices(self):
        user_choice = input("Choose an option from the following: {}\n".format(self.list_of_choices))
        if user_choice not in self.list_of_choices:
            print("You need to choose an option from the list.")
            return False

        cpu_choice = random.choice(self.list_of_choices)

        # 0: user, 1: CPU
        return [user_choice, cpu_choice]

    async def input_name(self):
        name = input("Please insert your name here:\n")

        while len(name) == 0 or len(name) > 16:
            print("Your name cannot be empty or more than 16 characters.")

        self.name = name
        return True


game = Main()
asyncio.run(game.start())
