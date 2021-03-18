# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# The Original Code is Copyright (C) 2020 Voxell Technologies.
# All rights reserved.

import re
import ast
import operator as op

PRIORITY = 8

def handle(text, Mic, Agent):
    remove_words = ["count ", "calculator ", "what is "]
    for rw in remove_words:
        text = text.replace(rw, "")

    # supported operators for Evaluation below
    operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
                ast.USub: op.neg}

    #Used to evaluate Strings
    #I do not use eval() because there is some security issues reported by many people.
    def eval_expr(expr):
        return eval_(ast.parse(expr, mode='eval').body)

    def eval_(node):
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)


    #Find String words to be converted into Math Symbols/Operators
    keywords= ["divided by", "x", "multiply", "times", "divide", "add","plus","minus"]
    for words in keywords:
        realkey=re.findall(r"\bdivided by|divide|x|multiply|times|add|plus|minus|power of\b",text)
        realkey= str(realkey)

    rep = {"divided by": "/", "divide by": "/", "divide": "/", "x": "*", "multiply": "*", "times":"*", "add": "+", "plus": "+", "minus": "-", "power of": "**"} # define desired replacements here

    #Execute the replacement of Strings into Math Symbols/Operators
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)

    answer= eval_expr(text)

    Mic.say(f"The answer is {answer}")


def isValid(text):
  # check if text is valid
  return (bool(re.search(r"\bcalculator|count|what is\b", text, re.IGNORECASE)))



if __name__ == "__main__":
  print(isValid("How is eveything going?"))
