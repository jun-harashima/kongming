import unittest
from kongming.main import Kongming


class TestKongming(unittest.TestCase):

    def assertModifierEqual(self, tree, chunk_id, modifier):
        _modifier = self.kongming._get_modifier(tree, tree.chunk(chunk_id))
        self.assertEqual(_modifier, modifier)

    def assertFunctionEqual(self, tree, chunk_id, function):
        _function = self.kongming._get_function(tree, tree.chunk(chunk_id))
        self.assertEqual(_function, function)

    def assertHeadEqual(self, tree, chunk_id, head):
        _head = self.kongming._get_head(tree, tree.chunk(chunk_id))
        self.assertEqual(_head, head)

    def setUp(self):
        self.kongming = Kongming(stopword=["。"])
        self.text1 = '鶏肉が揚がったら香味ソースをかけて出来上がり！'
        self.text2 = '鶏のもも肉を適当な大きさに切って、酒・醤油に漬けておく。（1時間）'
        self.text3 = 'すると出来上り。'

    # we don't care about the last chunk because it doesn't modify other chunks
    def test_get_modifier(self):
        tree = self.kongming.cabocha.parse(self.text1)
        self.assertModifierEqual(tree, 0, '鶏肉')
        self.assertModifierEqual(tree, 1, '揚がっ')
        self.assertModifierEqual(tree, 2, '香味ソース')
        self.assertModifierEqual(tree, 3, 'かけ')

        tree = self.kongming.cabocha.parse(self.text2)
        self.assertModifierEqual(tree, 0, '鶏')
        self.assertModifierEqual(tree, 1, 'もも肉')
        self.assertModifierEqual(tree, 2, '適当')
        self.assertModifierEqual(tree, 3, '大きさ')
        self.assertModifierEqual(tree, 4, '切っ')
        self.assertModifierEqual(tree, 5, '酒・醤油')
        self.assertModifierEqual(tree, 6, '漬け')

    # we don't care about the last chunk because it doesn't modify other chunks
    def test_get_function(self):
        tree = self.kongming.cabocha.parse(self.text1)
        self.assertFunctionEqual(tree, 0, 'が')
        self.assertFunctionEqual(tree, 1, 'たら')
        self.assertFunctionEqual(tree, 2, 'を')
        self.assertFunctionEqual(tree, 3, 'て')

        tree = self.kongming.cabocha.parse(self.text2)
        self.assertFunctionEqual(tree, 0, 'の')
        self.assertFunctionEqual(tree, 1, 'を')
        self.assertFunctionEqual(tree, 2, 'な')
        self.assertFunctionEqual(tree, 3, 'に')
        self.assertFunctionEqual(tree, 4, 'て')
        self.assertFunctionEqual(tree, 5, 'に')
        self.assertFunctionEqual(tree, 6, 'ておく')

    # we don't care about the first chunk because it isn't modified by other chunks
    def test_get_head(self):
        tree = self.kongming.cabocha.parse(self.text1)
        self.assertHeadEqual(tree, 1, '揚がる')
        self.assertHeadEqual(tree, 2, '香味ソース')
        self.assertHeadEqual(tree, 3, 'かける')
        self.assertHeadEqual(tree, 4, '出来上がる')

        tree = self.kongming.cabocha.parse(self.text2)
        self.assertHeadEqual(tree, 1, 'もも肉')
        self.assertHeadEqual(tree, 2, '適当')
        self.assertHeadEqual(tree, 3, '大きさ')
        self.assertHeadEqual(tree, 4, '切る')
        self.assertHeadEqual(tree, 5, '酒・醤油')
        self.assertHeadEqual(tree, 6, '漬ける')
        self.assertHeadEqual(tree, 7, '（1時間）')

        tree = self.kongming.cabocha.parse(self.text3)
        self.assertHeadEqual(tree, 1, '出来上り')

if __name__ == "__main__":
    unittest.main()
