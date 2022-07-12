from expression_tree import ExpressionTree

def build_expression_tree(tokens):
    """return an expresion tree based on a tokenized expression"""

    S = []

    for t in tokens:
        if t in '+-x*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
        #we ignore a left (

    return S.pop()


if __name__ == '__main__':
    test = '(((3+1)x4)/((9-5)+2))'

    t = build_expression_tree(test)

    print(t)
    print(t.evaluate())
