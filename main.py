from Game import Game

with open('config.txt', 'r') as f:
    lines = f.readlines()

game = Game("my game",
            int(lines[0].strip('\n')),
            int(lines[1].strip('\n')),
            lines[3].strip('\n'),
            int(lines[2].strip('\n')))
game.run()
