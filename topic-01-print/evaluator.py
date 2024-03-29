binary_operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

unary_operations = {
    "-": lambda x: -x,
   
}


def evaluate_binary_operation(op, x, y):
    assert op in binary_operations
    x = evaluate(x)
    y = evaluate(y)
    return binary_operations[op](x,y)
def evaluate_unary_operation(op,x):
    assert op in unary_operations
    x = evaluate(x)
    return unary_operations[op](x)
def evaluate_print(x):
    print(x)

def evaluate(tree):
    if type(tree) is list:
        op = tree[0]
        if op == "NUMBER":
            return tree[1]
        if op == "program":
            for statement in tree[1]:
                evaluate(statement)
        if op == "print":
            return evaluate_print(evaluate(tree[1]))
        if(len(tree) == 3):
            if op in binary_operations:
                return evaluate_binary_operation(op, tree[1], tree[2])
        if(len(tree)== 2):
            if op in unary_operations:
                return evaluate_unary_operation(op, tree[1])
    else:
        raise Exception(f"Unknown content in AST={tree}")

def test_evaluate_operations():
    print("test evaluate operations")
    print(evaluate(["+", ["NUMBER",1], ["NUMBER",2]]))
    assert evaluate(["+", ["NUMBER",1], ["NUMBER",2]]) == 3
    assert evaluate(["-", ["NUMBER",9], ["NUMBER",2]]) == 7
    assert evaluate(["*", ["NUMBER",4], ["NUMBER",2]]) == 8
    assert evaluate(["/", ["NUMBER",9], ["NUMBER",3]]) == 3

def test_evaluate_print():
    evaluate(["print",["+",["NUMBER",9],["NUMBER",12]]])

def test_evaluate_negation():
    print("test evaluate negation")
    assert evaluate((["-", ["NUMBER",1]])) == -1
    print(evaluate(['print', ['-', ['-',['NUMBER', 5]], ['NUMBER', 2]]]))
    assert evaluate(['-', ['-',['NUMBER', 5]], ['NUMBER', 2]]) == -7
    #assert evaluate(['+',['+', [['NUMBER', 3]], ['*',['-',['NUMBER', 4]], ['NUMBER', 3]]], ['-', ['*',['NUMBER', 4]], ['NUMBER', 5]]]) == -29
if __name__ == "__main__":
    test_evaluate_operations()
    test_evaluate_print()
    #print(evaluate(['-', ['NUMBER', 5], ['NUMBER', 2]]))
    #evaluate(['print', ['-', ['NUMBER', 5], ['NUMBER', 2]]])
    #evaluate(['print', ['*', ['NUMBER', 4.0], ['-', ['NUMBER', 5], ['NUMBER', 2]]]])
    #evaluate(['print', ['+', ['NUMBER', 3.0], ['*', ['NUMBER', 4.0], ['-', ['NUMBER', 5], ['NUMBER', 2]]]]])
    #evaluate(['program', [['print', ['+', ['NUMBER', 3.0], ['*', ['NUMBER', 4.0], ['-', ['NUMBER', 5], ['NUMBER', 2]]]]]]])
    test_evaluate_negation()
