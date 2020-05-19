import CaboCha


class Kongming:

    def __init__(self, stopwords=None):
        self.cabocha = CaboCha.Parser()
        self.stopwords = stopwords

    def _get_modifier(self, tree, chunk):
        surface = ''
        for i in range(chunk.token_pos, chunk.token_pos + chunk.head_pos + 1):
            token = tree.token(i)
            features = token.feature.split(',')
            surface += token.surface
        return surface

    def _get_function(self, tree, chunk):
        surface = ''
        for i in range(chunk.token_pos + chunk.head_pos + 1, chunk.token_pos + chunk.token_size):
            token = tree.token(i)
            features = token.feature.split(',')
            if not features[1] in ['読点', '句点']:
                surface += token.surface
        return surface

    def _get_head(self, tree, chunk):
        start = chunk.token_pos
        end = start + chunk.head_pos + 1 if chunk.head_pos != chunk.func_pos else start + chunk.token_size
        surface = ''
        for i in range(start, end):
            token = tree.token(i)
            features = token.feature.split(',')
            if self.stopwords and token.surface in self.stopwords:
                continue
            if features[0] in ['名詞', '形容詞', '記号']:
                surface += token.surface
            elif features[0] == '動詞':
                surface += features[6]
                break
        return surface

    def _extract_arrows(self, tree):
        chunks = {}
        for i in range(0, tree.chunk_size()):
            chunks[i] = tree.chunk(i)

        arrows = []
        for chunk_id, chunk in chunks.items():
            if not chunk.link > 0:
                continue
            modifier = self._get_modifier(tree, chunk)
            function = self._get_function(tree, chunk)
            head_chunk = chunks[chunk.link]
            head = self._get_head(tree, head_chunk)
            arrow = {"modifier": modifier, "function": function, "head": head}
            arrows.append(arrow)
        return arrows

    def collect(self, text):
        tree = self.cabocha.parse(text)
        dependencies = self._extract_arrows(tree)
        return dependencies
