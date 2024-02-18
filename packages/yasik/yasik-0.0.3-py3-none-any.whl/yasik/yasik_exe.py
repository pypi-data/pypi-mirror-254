#!/usr/bin/env python3

from antlr4 import InputStream, CommonTokenStream
from yasik_interpreter import YasikEvaluator
from parser_generated.YasikLexer import YasikLexer
from parser_generated.YasikParser import YasikParser


def main():
    print("Hey!!!!")
    for expression in ["lar",
                       "lar(5)",
                       "lar(5,6)",
                       "cat.lar",
                       "cat.lar(5)",
                       "cat.lar(5,6)",
                       "lar(5:16)",
                       "lar(5:16,7:18)",
                       "cat.lar(5:16)",
                       "cat.lar(5:16,7:18)",
                       "lar(5:)",
                       "lar(5:,7:)",
                       "cat.lar(5:)",
                       "cat.lar(5:,7:)",
                       "lar(:16)",
                       "lar(:16,:18)",
                       "cat.lar(:16)",
                       "cat.lar(:16,:18)",
                       "lar += cat.lar(5:)",
                       "lar = cat.lar(5:)",
                       "lar = lar(1,2); lar(1,1) = lar(1,3)",
                       "var1 = lar(1,2); lar(1,1) = var1"]:
        input_stream = InputStream(expression)
        lexer = YasikLexer(input=input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = YasikParser(token_stream)
        evaluator = YasikEvaluator()
        parser.addParseListener(evaluator)
        tree = parser.code()
        print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main()
