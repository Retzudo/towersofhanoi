import unittest


class PieceTestCase(unittest.TestCase):
    def test_init(self):
        from towers import Piece

        piece = Piece(123)
        self.assertEqual(piece.size, 123)


class RodTestCase(unittest.TestCase):
    def test_init(self):
        from towers import Rod

        rod = Rod()
        self.assertEqual(len(rod.pieces), 0)

        pieces = [1, 2, 3]
        rod = Rod(pieces)
        self.assertEqual(rod.pieces, pieces)

    def test_push_piece(self):
        from towers import Rod, Piece

        rod = Rod()
        big_piece = Piece(10)
        small_piece = Piece(1)
        
        rod.push_piece(big_piece)
        rod.push_piece(small_piece)

        self.assertEqual(len(rod.pieces), 2)

    def test_push_invalid_piece(self):
        from towers import Rod, Piece, TowerError

        rod = Rod()
        small_piece = Piece(1)
        big_piece = Piece(10)

        with self.assertRaises(TowerError):
            rod.push_piece(small_piece)
            rod.push_piece(big_piece)

    def test_pop_piece(self):
        from towers import Rod, Piece

        rod = Rod()
        piece = Piece(1)

        rod.pieces.append(piece)

        popped_piece = rod.pop_piece()
        self.assertEqual(popped_piece, piece)

    def test_pop_piece_empty(self):
        from towers import Rod, Piece, TowerError

        rod = Rod()
        with self.assertRaises(IndexError):
            rod.pop_piece()


class TowerTestCase(unittest.TestCase):
    def test_init(self):
        from towers import Tower

        rods = [1, 2, 3]
        tower = Tower(rods)
        self.assertEqual(tower.rods, rods)

    def test_move_piece(self):
        from towers import Tower, Rod, Piece

        tower = Tower()
        tower.rods = [Rod() for i in range(3)]

        tower.rods[0].pieces = [Piece(3-i) for i in range(3)]

        tower.move_piece(0, 2)
        self.assertEqual(len(tower.rods[0].pieces), 2)
        self.assertEqual(len(tower.rods[2].pieces), 1)

        tower.move_piece(2, 0)
        self.assertEqual(len(tower.rods[0].pieces), 3)
        self.assertEqual(len(tower.rods[2].pieces), 0)

    def test_invalid_move_piece(self):
        from towers import Tower, Rod, Piece, TowerError

        tower = Tower()
        tower.rods = [Rod() for i in range(3)]

        tower.rods[0].pieces = [Piece(3-i) for i in range(3)]
        tower.rods[1].pieces = [Piece(4)]
        
        with self.assertRaises(TowerError):
            tower.move_piece(1, 0)


class CreateTowerTestCase(unittest.TestCase):
    def test_create_tower(self):
        from towers import create_tower

        tower = create_tower(3, 3)

        self.assertEqual(len(tower.rods), 3)
        self.assertEqual(len(tower.rods[0].pieces), 3)


if __name__ == '__main__':
    unittest.main()
