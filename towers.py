class TowerError(Exception):
    pass


class Piece:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)


class Rod:
    def __init__(self, pieces=None):
        if not pieces:
            self.pieces = []
        else:
            self.pieces = pieces

    def push_piece(self, piece):
        if len(self.pieces) == 0:
            self.pieces.append(piece)
            return

        if piece.size <= self.pieces[-1].size:
            self.pieces.append(piece)
        else:
            raise TowerError(
                'Can\'t place piece {} on rod {} because the '
                'size of the top piece is {}'.format(
                    piece,
                    self,
                    self.pieces[-1]
                )
            )

    def pop_piece(self):
        return self.pieces.pop()

    def __str__(self):
        return str(self.pieces)
    
    def __len__(self):
        return len(self.pieces)


class Tower:
    def __init__(self, rods=None):
        if not rods:
            self.rods = []
        else:
            self.rods = rods

    def move_piece(self, from_rod_index, to_rod_index):
        if from_rod_index == to_rod_index:
            return
        
        from_rod = self.rods[from_rod_index]
        to_rod = self.rods[to_rod_index]

        piece = from_rod.pop_piece()
        to_rod.push_piece(piece)


def create_tower(num_of_rods, num_of_pieces):
    if num_of_rods <= 0 or num_of_pieces <= 0:
        raise ValueError('Number of pieces or rods must be > 0')

    tower = Tower()
    tower.rods = [Rod() for rod in range(num_of_rods)]

    # Populate the first rod
    tower.rods[0].pieces = [Piece(num_of_pieces-p) for p in range(num_of_pieces)]

    return tower
