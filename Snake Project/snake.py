import consts


class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys  # dictionary keys move like in json file
        self.game = game
        self.cells = [pos]  # snake head
        self.color = color
        self.direction = direction  # first direction
        self.game.add_snake(self)
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        currentHeadPosTuple = self.get_head()
        newHead = [0,0]
        if self.direction == "DOWN":
            if currentHeadPosTuple[1] + 1 > consts.table_size-1:
                newHead[0], newHead[1] = currentHeadPosTuple[0], 0
            else:
                 newHead[0], newHead[1] = currentHeadPosTuple[0], currentHeadPosTuple[1] + 1
        elif self.direction == "UP":
            if currentHeadPosTuple[1] - 1 < 0:
                newHead[0], newHead[1] = currentHeadPosTuple[0], consts.table_size - 1
            else:
                newHead[0], newHead[1] = currentHeadPosTuple[0], currentHeadPosTuple[1] - 1
        elif self.direction == "LEFT":
            if currentHeadPosTuple[0] - 1 < 0:
                newHead[0], newHead[1] = consts.table_size - 1, currentHeadPosTuple[1]
            else:
                newHead[0], newHead[1] = currentHeadPosTuple[0] - 1, currentHeadPosTuple[1]
        elif self.direction == "RIGHT":
            if currentHeadPosTuple[0] + 1 > consts.table_size-1:
                newHead[0], newHead[1] = 0, currentHeadPosTuple[1]
            else:
                newHead[0], newHead[1] = currentHeadPosTuple[0] + 1, currentHeadPosTuple[1]

        if (self.game.get_cell(newHead).color is consts.block_color) or (self.game.get_cell(newHead).color != consts.fruit_color and self.game.get_cell(newHead).color != consts.back_color):
            self.game.kill(self)
        else:
            if self.game.get_cell(newHead).color == consts.fruit_color:
                self.cells.append(newHead)
                self.game.get_cell(newHead).set_color(self.color)
            else:
                pos = self.cells.pop(0)
                self.game.get_cell(pos).set_color(consts.back_color)
                self.cells.append(newHead)
                self.game.get_cell(newHead).set_color(self.color)



    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                value = self.keys[key]
                if value == "RIGHT":
                    if self.direction != "LEFT":
                        self.direction = "RIGHT"
                elif value == "LEFT":
                    if self.direction != "RIGHT":
                        self.direction = "LEFT"
                elif value == "DOWN":
                    if self.direction != "UP":
                        self.direction = "DOWN"
                elif value == "UP":
                    if self.direction != "DOWN":
                        self.direction = "UP"

