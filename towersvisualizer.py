class Visualizer:
    def __init__(self, tower=None):
        self.tower = tower

    def _count_pieces(self):
        """Return the number of total pieces in this tower."""
        pieces = 0
        for rod in self.tower.rods:
            pieces += len(rod.pieces)

        return pieces

    def _get_biggest_size(self):
        """Return the size of the biggest piece in this tower."""
        size = 0
        for rod in self.tower.rods:
            for piece in rod.pieces:
                if piece.size > size:
                    size = piece.size

        return size

    @staticmethod
    def _render_piece(piece):
        """Return a string representation of a single piece."""
        return '[{}]'.format('-'*(piece.size*2-1))

    def _render_rod(self, rod):
        """Return a list of strings that represent a rod.

        Render each individual piece and pad the list with '|'
        for empty spots. Also add an additional '|' to every rod
        and padding around each line for aesthetic purpose.
        """
        biggest_size = self._get_biggest_size()
        rendered_rod = []
        for piece in rod.pieces:
            rendered_rod.append(
                '{sym:^{width}}'.format(sym=self._render_piece(piece), width=biggest_size*2+1)
            )

        while len(rendered_rod) <= self._count_pieces():
            rendered_rod.append('{sym:^{width}}'.format(sym='|', width=biggest_size*2+1))

        return rendered_rod[::-1]

    def visualize(self):
        """Render the whole tower to a string."""
        rendered_rods = []
        for rod in self.tower.rods:
            rendered_rods.append(self._render_rod(rod))


        lines = []
        for line in zip(*rendered_rods):
            lines.append(' '.join(line) + ' ')
        
        lines.append('_'*(len(lines[-1])))

        return '\n'.join(lines)
