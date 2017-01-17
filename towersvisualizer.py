import sys
if sys.version_info[0] < 3:
    from itertools import izip_longest as zip_longest
else:
    from itertools import zip_longest


class Visualizer:
    def __init__(self, tower=None):
        self.tower = tower

    def _count_pieces(self):
        pieces = 0
        for rod in self.tower.rods:
            pieces += len(rod.pieces)

        return pieces

    def _get_biggest_size(self):
        size = 0
        for rod in self.tower.rods:
            for piece in rod.pieces:
                if piece.size > size:
                    size = piece.size

        return size

    @staticmethod
    def _render_piece(piece):
        return '[{}]'.format('-'*(piece.size*2-1))

    def _render_rod(self, rod):
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
        rendered_rods = []
        for rod in self.tower.rods:
            rendered_rods.append(self._render_rod(rod))


        lines = []
        for line in zip_longest(*rendered_rods):
            lines.append(' '.join(line) + ' ')
        
        lines.append('_'*(len(lines[-1])+1))

        return '\n'.join(lines)
