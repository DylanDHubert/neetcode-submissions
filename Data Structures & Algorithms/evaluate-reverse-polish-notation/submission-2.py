class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for tok in tokens:
            if tok not in "+ - * /":
                operands.append(int(tok))
            else:  # FOUND OPERATOR
                op2 = operands.pop()
                op1 = operands.pop()

                match tok: # TOKEN IS OPERATOR
                    case "+":
                        result = op1 + op2
                    case "-":
                        result = op1 - op2
                    case "*":
                        result = op1 * op2
                    case "/":
                        result = int(op1 / op2)
                operands.append(result)

        return operands[0]      


