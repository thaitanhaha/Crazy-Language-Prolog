# Generated from main/crazy/parser/Cra2Pre.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Cra2PreParser import Cra2PreParser
else:
    from Cra2PreParser import Cra2PreParser

# This class defines a complete generic visitor for a parse tree produced by Cra2PreParser.

class Cra2PreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Cra2PreParser#program.
    def visitProgram(self, ctx:Cra2PreParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#var_decl_part.
    def visitVar_decl_part(self, ctx:Cra2PreParser.Var_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#var_decl_list.
    def visitVar_decl_list(self, ctx:Cra2PreParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#var_const_decl.
    def visitVar_const_decl(self, ctx:Cra2PreParser.Var_const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#var_decl.
    def visitVar_decl(self, ctx:Cra2PreParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#id_list.
    def visitId_list(self, ctx:Cra2PreParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#const_decl.
    def visitConst_decl(self, ctx:Cra2PreParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#func_decl_part.
    def visitFunc_decl_part(self, ctx:Cra2PreParser.Func_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#func_decl_list.
    def visitFunc_decl_list(self, ctx:Cra2PreParser.Func_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#func_procedure_decl.
    def visitFunc_procedure_decl(self, ctx:Cra2PreParser.Func_procedure_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#func_decl.
    def visitFunc_decl(self, ctx:Cra2PreParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#procedure_decl.
    def visitProcedure_decl(self, ctx:Cra2PreParser.Procedure_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#param_list.
    def visitParam_list(self, ctx:Cra2PreParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#params.
    def visitParams(self, ctx:Cra2PreParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#param.
    def visitParam(self, ctx:Cra2PreParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#one_param.
    def visitOne_param(self, ctx:Cra2PreParser.One_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#mul_param.
    def visitMul_param(self, ctx:Cra2PreParser.Mul_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#ctype.
    def visitCtype(self, ctx:Cra2PreParser.CtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#primitive_type.
    def visitPrimitive_type(self, ctx:Cra2PreParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_type.
    def visitArray_type(self, ctx:Cra2PreParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_size_list.
    def visitArray_size_list(self, ctx:Cra2PreParser.Array_size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_size.
    def visitArray_size(self, ctx:Cra2PreParser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#stmt_list.
    def visitStmt_list(self, ctx:Cra2PreParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#stmts.
    def visitStmts(self, ctx:Cra2PreParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#stmt.
    def visitStmt(self, ctx:Cra2PreParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#assign_stmt.
    def visitAssign_stmt(self, ctx:Cra2PreParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#lhs.
    def visitLhs(self, ctx:Cra2PreParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#block_stmt.
    def visitBlock_stmt(self, ctx:Cra2PreParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#if_stmt.
    def visitIf_stmt(self, ctx:Cra2PreParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#call_stmt.
    def visitCall_stmt(self, ctx:Cra2PreParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#call_expr.
    def visitCall_expr(self, ctx:Cra2PreParser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#while_stmt.
    def visitWhile_stmt(self, ctx:Cra2PreParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:Cra2PreParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#loop_do_stmt.
    def visitLoop_do_stmt(self, ctx:Cra2PreParser.Loop_do_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#break_stmt.
    def visitBreak_stmt(self, ctx:Cra2PreParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#continue_stmt.
    def visitContinue_stmt(self, ctx:Cra2PreParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr_list.
    def visitExpr_list(self, ctx:Cra2PreParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#exprs.
    def visitExprs(self, ctx:Cra2PreParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr.
    def visitExpr(self, ctx:Cra2PreParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr2.
    def visitExpr2(self, ctx:Cra2PreParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr3.
    def visitExpr3(self, ctx:Cra2PreParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr4.
    def visitExpr4(self, ctx:Cra2PreParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr5.
    def visitExpr5(self, ctx:Cra2PreParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr6.
    def visitExpr6(self, ctx:Cra2PreParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr7.
    def visitExpr7(self, ctx:Cra2PreParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr_8.
    def visitExpr_8(self, ctx:Cra2PreParser.Expr_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr8.
    def visitExpr8(self, ctx:Cra2PreParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#expr9.
    def visitExpr9(self, ctx:Cra2PreParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#index_operators.
    def visitIndex_operators(self, ctx:Cra2PreParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#index_op.
    def visitIndex_op(self, ctx:Cra2PreParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_literal.
    def visitArray_literal(self, ctx:Cra2PreParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_element_list.
    def visitArray_element_list(self, ctx:Cra2PreParser.Array_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_elements.
    def visitArray_elements(self, ctx:Cra2PreParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#array_element.
    def visitArray_element(self, ctx:Cra2PreParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Cra2PreParser#literal.
    def visitLiteral(self, ctx:Cra2PreParser.LiteralContext):
        return self.visitChildren(ctx)



del Cra2PreParser