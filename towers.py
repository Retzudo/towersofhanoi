from functools import total_ordering


class TowerError(Exception):
    pass


@total_ordering
class Piece:
    """A single piece on a rod."""
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

    def __lt__(self, other):
        return self.size < other.size

    def __eq__(self, other):
        return self.size == other.size


class Rod:
    """A rod. A tower consists of a number of rods."""
    def __init__(self, pieces=None):
        if not pieces:
            self.pieces = []
        else:
            self.pieces = pieces

    def push_piece(self, piece):
        """Try to place a piece 'on top'.

        Raise an error if not successul.
        """
        if len(self.pieces) == 0:
            self.pieces.append(piece)
            return

        if piece <= self.pieces[-1]:
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
        """Remove and return the top piece of this rod."""
        return self.pieces.pop()

    def __str__(self):
        return str(self.pieces)

    def __len__(self):
        return len(self.pieces)


class Tower:
    """A tower made of rods rods."""
    def __init__(self, rods=None):
        if not rods:
            self.rods = []
        else:
            self.rods = rods

    def move_piece(self, from_rod_index, to_rod_index):
        """Pop a piece from one rod and try to place it
        on another rod."""
        if from_rod_index == to_rod_index:
            return

        from_rod = self.rods[from_rod_index]
        to_rod = self.rods[to_rod_index]

        piece = from_rod.pop_piece()
        try:
            to_rod.push_piece(piece)
        except TowerError:
            # Revert
            from_rod.push_piece(piece)
            raise


def create_tower(num_of_rods=3, num_of_pieces=3):
    """Return a new Tower object.

    Initialize the tower with the given number of rods and
    the given number of pieces on rod #0.
    """
    if num_of_rods <= 0 or num_of_pieces <= 0:
        raise ValueError('Number of pieces or rods must be > 0')

    tower = Tower()
    tower.rods = [Rod() for rod in range(num_of_rods)]

    # Populate the first rod
    tower.rods[0].pieces = [Piece(num_of_pieces - p) for p in range(num_of_pieces)]

    return tower
