from linked_binary_tree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree"""

    def __init__(self, token, left=None, right=None):
        """

        :param token: single form, token is leaf (e.g. '42'), in three form token is an operator
        :param left: expression tree instance
        :param right: expression tree instance
        """

        super().__init__()
        if not isinstance(token, str):
            raise TypeError('token must be a string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be a vaild operator')
            self._attach(p=self.root(), t1=left, t2=right)

    def __str__(self):
        pieces = []
        self._paranthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _paranthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._paranthesize_recur(self.left(p), result)
            result.append(p.element())
            self._paranthesize_recur((self.right(p)), result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur((self.right(p)))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val
