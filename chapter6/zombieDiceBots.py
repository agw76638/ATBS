import zombiedice, random

class stopTwoBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        brains = 0
        while brains < 2:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            brains += diceRollResults['brains']


class stopTwoShotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        while shotguns < 2:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            shotguns += diceRollResults['shotgun']

class rollRandom:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()

class initDicide:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        init = random.randint(1, 4)
        for i in range(init):
            diceRollResults = zombiedice.roll()
            if shotguns == 2:
                break
            if diceRollResults is None:
                return
            shotguns += diceRollResults['shotgun']

class stopIfMoreShotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        brains = 0
        while shotguns <= brains:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']

zombies = (
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    rollRandom(name='Random'),
    stopTwoBrains(name='Stop at 2 Brains'),
    stopTwoShotguns(name='Stop at 2 Shotguns'),
    initDicide(name='Initialy decide'),
    stopIfMoreShotguns(name='Stop shotgun>brain')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)