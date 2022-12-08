import asyncio
import random


class Colors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'


class Main:
    def __init__(self):
        self.name = None

        self.points = 0
        self.cpu_points = 0

        self.list_of_choices = [
            "rock",
            "paper",
            "scissors"
        ]
        """
        0 : rock-rock, paper-paper, scissors-scissors

        1: rock-paper
        2: rock-scissors
        3: scissors-paper
        4: border
        """
        self.list_of_answers = [
            "{}That's a tie!{}".format(Colors.green, Colors.end),

            "{}Shift!, {} opened their hand and feasted on {}.{}",
            "{}Baam!, {} got crushed by {}.{}",
            "{}Swift!, {} injured {} to bits and pieces.{}",
            "-------------------------------"
        ]

    async def start(self):

        if self.name is None:
            print(self.list_of_answers[4])
            await self.input_name()
            await asyncio.sleep(1)

        print(self.list_of_answers[4])
        print("{} got {} points!\n{} got {} points.".format(self.name, self.points, "CPU", self.cpu_points))

        print(self.list_of_answers[4])
        choices = await self.get_choices()
        await asyncio.sleep(1)

        if not choices:
            await asyncio.sleep(1)
            return await self.start()

        await asyncio.sleep(1)
        answer = await self.justify(choices)

        print(self.list_of_answers[4])
        print(answer)
        await asyncio.sleep(1)

        return await self.start()

    async def justify(self, choices):
        # Huge hardcoded block.

        user = choices[0].lower()
        cpu = choices[1].lower()

        print(self.list_of_answers[4])
        print(f"{Colors.cyan}{self.name} Chosen {user}{Colors.end}")

        print(self.list_of_answers[4])
        await asyncio.sleep(1)

        print(f"{Colors.cyan}CPU Chosen {cpu}{Colors.end}")

        await asyncio.sleep(1)

        if user == "rock":
            # tie
            if cpu == "rock":
                return self.list_of_answers[0]
            # lose
            if cpu == "paper":
                self.cpu_points += 1
                return self.list_of_answers[1].format(Colors.red, "CPU", self.name, Colors.end)
            # win
            if cpu == "scissors":
                self.points += 1
                return self.list_of_answers[2].format(Colors.blue, "CPU", self.name, Colors.end)

        if user == "paper":
            # win
            if cpu == "rock":
                self.points += 1
                return self.list_of_answers[1].format(Colors.blue, "CPU", self.name, Colors.end)
            # tie
            if cpu == "paper":
                return self.list_of_answers[0]
            # lose
            if cpu == "scissors":
                self.cpu_points += 1
                return self.list_of_answers[3].format(Colors.red, "CPU", self.name, Colors.end)

        if user == "scissors":
            # lose
            if cpu == "rock":
                self.cpu_points += 1
                return self.list_of_answers[2].format(Colors.red, self.name, "CPU", Colors.end)
            # win
            if cpu == "paper":
                self.points += 1
                return self.list_of_answers[3].format(Colors.blue, self.name, "CPU", Colors.end)
            # tie
            if cpu == "scissors":
                return self.list_of_answers[0]

    async def get_choices(self):
        user_choice = input("{}Choose an option from the following: {} Or type quit.{}\n".format(
            Colors.green,
            self.list_of_choices,
            Colors.end)
        )

        if user_choice.lower() not in self.list_of_choices:
            if user_choice.lower() == "quit":
                print(f"{Colors.green}Thank you for playing this game! {Colors.end}")
                return quit()

            print(f"{Colors.red}You need to choose an option from the list.{Colors.end}")
            return False

        cpu_choice = random.choice(self.list_of_choices)

        # 0: user, 1: CPU
        return [user_choice, cpu_choice]

    async def input_name(self):
        name = input(f"{Colors.green}Please insert your name here:{Colors.end}\n")

        while len(name) == 0 or len(name) > 16:
            print(f"{Colors.red}Your name cannot be empty or more than 16 characters.{Colors.end}")

        self.name = name
        return True


game = Main()
asyncio.run(game.start())
