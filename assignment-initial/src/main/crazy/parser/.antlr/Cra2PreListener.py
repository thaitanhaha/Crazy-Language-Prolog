# Generated from c://Users//hp450//Desktop//assignment1-initial//src//main//crazy//parser//Cra2Pre.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Cra2PreParser import Cra2PreParser
else:
    from Cra2PreParser import Cra2PreParser

# This class defines a complete listener for a parse tree produced by Cra2PreParser.
class Cra2PreListener(ParseTreeListener):

    # Enter a parse tree produced by Cra2PreParser#program.
    def enterProgram(self, ctx:Cra2PreParser.ProgramContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#program.
    def exitProgram(self, ctx:Cra2PreParser.ProgramContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#var_decl.
    def enterVar_decl(self, ctx:Cra2PreParser.Var_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#var_decl.
    def exitVar_decl(self, ctx:Cra2PreParser.Var_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#ctype.
    def enterCtype(self, ctx:Cra2PreParser.CtypeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#ctype.
    def exitCtype(self, ctx:Cra2PreParser.CtypeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#comp_stmt.
    def enterComp_stmt(self, ctx:Cra2PreParser.Comp_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#comp_stmt.
    def exitComp_stmt(self, ctx:Cra2PreParser.Comp_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#stmt.
    def enterStmt(self, ctx:Cra2PreParser.StmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#stmt.
    def exitStmt(self, ctx:Cra2PreParser.StmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#assi_stmt.
    def enterAssi_stmt(self, ctx:Cra2PreParser.Assi_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#assi_stmt.
    def exitAssi_stmt(self, ctx:Cra2PreParser.Assi_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr.
    def enterExpr(self, ctx:Cra2PreParser.ExprContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr.
    def exitExpr(self, ctx:Cra2PreParser.ExprContext):
        pass



del Cra2PreParser