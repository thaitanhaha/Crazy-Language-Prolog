# Generated from Cra2Pre.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by Cra2PreParser#decl_part.
    def enterDecl_part(self, ctx:Cra2PreParser.Decl_partContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#decl_part.
    def exitDecl_part(self, ctx:Cra2PreParser.Decl_partContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#var_decl_part.
    def enterVar_decl_part(self, ctx:Cra2PreParser.Var_decl_partContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#var_decl_part.
    def exitVar_decl_part(self, ctx:Cra2PreParser.Var_decl_partContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#var_decl_list.
    def enterVar_decl_list(self, ctx:Cra2PreParser.Var_decl_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#var_decl_list.
    def exitVar_decl_list(self, ctx:Cra2PreParser.Var_decl_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#var_const_decl.
    def enterVar_const_decl(self, ctx:Cra2PreParser.Var_const_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#var_const_decl.
    def exitVar_const_decl(self, ctx:Cra2PreParser.Var_const_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#var_decl.
    def enterVar_decl(self, ctx:Cra2PreParser.Var_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#var_decl.
    def exitVar_decl(self, ctx:Cra2PreParser.Var_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#id_list.
    def enterId_list(self, ctx:Cra2PreParser.Id_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#id_list.
    def exitId_list(self, ctx:Cra2PreParser.Id_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#const_decl.
    def enterConst_decl(self, ctx:Cra2PreParser.Const_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#const_decl.
    def exitConst_decl(self, ctx:Cra2PreParser.Const_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#func_decl_part.
    def enterFunc_decl_part(self, ctx:Cra2PreParser.Func_decl_partContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#func_decl_part.
    def exitFunc_decl_part(self, ctx:Cra2PreParser.Func_decl_partContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#func_decl_list.
    def enterFunc_decl_list(self, ctx:Cra2PreParser.Func_decl_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#func_decl_list.
    def exitFunc_decl_list(self, ctx:Cra2PreParser.Func_decl_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#func_procedure_decl.
    def enterFunc_procedure_decl(self, ctx:Cra2PreParser.Func_procedure_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#func_procedure_decl.
    def exitFunc_procedure_decl(self, ctx:Cra2PreParser.Func_procedure_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#func_decl.
    def enterFunc_decl(self, ctx:Cra2PreParser.Func_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#func_decl.
    def exitFunc_decl(self, ctx:Cra2PreParser.Func_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#procedure_decl.
    def enterProcedure_decl(self, ctx:Cra2PreParser.Procedure_declContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#procedure_decl.
    def exitProcedure_decl(self, ctx:Cra2PreParser.Procedure_declContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#param_list.
    def enterParam_list(self, ctx:Cra2PreParser.Param_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#param_list.
    def exitParam_list(self, ctx:Cra2PreParser.Param_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#params.
    def enterParams(self, ctx:Cra2PreParser.ParamsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#params.
    def exitParams(self, ctx:Cra2PreParser.ParamsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#param.
    def enterParam(self, ctx:Cra2PreParser.ParamContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#param.
    def exitParam(self, ctx:Cra2PreParser.ParamContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#one_param.
    def enterOne_param(self, ctx:Cra2PreParser.One_paramContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#one_param.
    def exitOne_param(self, ctx:Cra2PreParser.One_paramContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#mul_param.
    def enterMul_param(self, ctx:Cra2PreParser.Mul_paramContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#mul_param.
    def exitMul_param(self, ctx:Cra2PreParser.Mul_paramContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#ctype.
    def enterCtype(self, ctx:Cra2PreParser.CtypeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#ctype.
    def exitCtype(self, ctx:Cra2PreParser.CtypeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#primitive_type.
    def enterPrimitive_type(self, ctx:Cra2PreParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#primitive_type.
    def exitPrimitive_type(self, ctx:Cra2PreParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#int_real_bool_type.
    def enterInt_real_bool_type(self, ctx:Cra2PreParser.Int_real_bool_typeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#int_real_bool_type.
    def exitInt_real_bool_type(self, ctx:Cra2PreParser.Int_real_bool_typeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_type.
    def enterArray_type(self, ctx:Cra2PreParser.Array_typeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_type.
    def exitArray_type(self, ctx:Cra2PreParser.Array_typeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_size_list.
    def enterArray_size_list(self, ctx:Cra2PreParser.Array_size_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_size_list.
    def exitArray_size_list(self, ctx:Cra2PreParser.Array_size_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_size.
    def enterArray_size(self, ctx:Cra2PreParser.Array_sizeContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_size.
    def exitArray_size(self, ctx:Cra2PreParser.Array_sizeContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#stmt_list.
    def enterStmt_list(self, ctx:Cra2PreParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#stmt_list.
    def exitStmt_list(self, ctx:Cra2PreParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#stmts.
    def enterStmts(self, ctx:Cra2PreParser.StmtsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#stmts.
    def exitStmts(self, ctx:Cra2PreParser.StmtsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#stmt.
    def enterStmt(self, ctx:Cra2PreParser.StmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#stmt.
    def exitStmt(self, ctx:Cra2PreParser.StmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#assign_stmt.
    def enterAssign_stmt(self, ctx:Cra2PreParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#assign_stmt.
    def exitAssign_stmt(self, ctx:Cra2PreParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#lhs.
    def enterLhs(self, ctx:Cra2PreParser.LhsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#lhs.
    def exitLhs(self, ctx:Cra2PreParser.LhsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#block_stmt.
    def enterBlock_stmt(self, ctx:Cra2PreParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#block_stmt.
    def exitBlock_stmt(self, ctx:Cra2PreParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#if_stmt.
    def enterIf_stmt(self, ctx:Cra2PreParser.If_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#if_stmt.
    def exitIf_stmt(self, ctx:Cra2PreParser.If_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#call_stmt.
    def enterCall_stmt(self, ctx:Cra2PreParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#call_stmt.
    def exitCall_stmt(self, ctx:Cra2PreParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#call_expr.
    def enterCall_expr(self, ctx:Cra2PreParser.Call_exprContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#call_expr.
    def exitCall_expr(self, ctx:Cra2PreParser.Call_exprContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#while_stmt.
    def enterWhile_stmt(self, ctx:Cra2PreParser.While_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#while_stmt.
    def exitWhile_stmt(self, ctx:Cra2PreParser.While_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:Cra2PreParser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:Cra2PreParser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#loop_do_stmt.
    def enterLoop_do_stmt(self, ctx:Cra2PreParser.Loop_do_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#loop_do_stmt.
    def exitLoop_do_stmt(self, ctx:Cra2PreParser.Loop_do_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#break_stmt.
    def enterBreak_stmt(self, ctx:Cra2PreParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#break_stmt.
    def exitBreak_stmt(self, ctx:Cra2PreParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#continue_stmt.
    def enterContinue_stmt(self, ctx:Cra2PreParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#continue_stmt.
    def exitContinue_stmt(self, ctx:Cra2PreParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr_list.
    def enterExpr_list(self, ctx:Cra2PreParser.Expr_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr_list.
    def exitExpr_list(self, ctx:Cra2PreParser.Expr_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#exprs.
    def enterExprs(self, ctx:Cra2PreParser.ExprsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#exprs.
    def exitExprs(self, ctx:Cra2PreParser.ExprsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr.
    def enterExpr(self, ctx:Cra2PreParser.ExprContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr.
    def exitExpr(self, ctx:Cra2PreParser.ExprContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr2.
    def enterExpr2(self, ctx:Cra2PreParser.Expr2Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr2.
    def exitExpr2(self, ctx:Cra2PreParser.Expr2Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr3.
    def enterExpr3(self, ctx:Cra2PreParser.Expr3Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr3.
    def exitExpr3(self, ctx:Cra2PreParser.Expr3Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr4.
    def enterExpr4(self, ctx:Cra2PreParser.Expr4Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr4.
    def exitExpr4(self, ctx:Cra2PreParser.Expr4Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr5.
    def enterExpr5(self, ctx:Cra2PreParser.Expr5Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr5.
    def exitExpr5(self, ctx:Cra2PreParser.Expr5Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr6.
    def enterExpr6(self, ctx:Cra2PreParser.Expr6Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr6.
    def exitExpr6(self, ctx:Cra2PreParser.Expr6Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr7.
    def enterExpr7(self, ctx:Cra2PreParser.Expr7Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr7.
    def exitExpr7(self, ctx:Cra2PreParser.Expr7Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr8.
    def enterExpr8(self, ctx:Cra2PreParser.Expr8Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr8.
    def exitExpr8(self, ctx:Cra2PreParser.Expr8Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#expr9.
    def enterExpr9(self, ctx:Cra2PreParser.Expr9Context):
        pass

    # Exit a parse tree produced by Cra2PreParser#expr9.
    def exitExpr9(self, ctx:Cra2PreParser.Expr9Context):
        pass


    # Enter a parse tree produced by Cra2PreParser#index_operation.
    def enterIndex_operation(self, ctx:Cra2PreParser.Index_operationContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#index_operation.
    def exitIndex_operation(self, ctx:Cra2PreParser.Index_operationContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#index_operators.
    def enterIndex_operators(self, ctx:Cra2PreParser.Index_operatorsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#index_operators.
    def exitIndex_operators(self, ctx:Cra2PreParser.Index_operatorsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_literal.
    def enterArray_literal(self, ctx:Cra2PreParser.Array_literalContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_literal.
    def exitArray_literal(self, ctx:Cra2PreParser.Array_literalContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_element_list.
    def enterArray_element_list(self, ctx:Cra2PreParser.Array_element_listContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_element_list.
    def exitArray_element_list(self, ctx:Cra2PreParser.Array_element_listContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_elements.
    def enterArray_elements(self, ctx:Cra2PreParser.Array_elementsContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_elements.
    def exitArray_elements(self, ctx:Cra2PreParser.Array_elementsContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#array_element.
    def enterArray_element(self, ctx:Cra2PreParser.Array_elementContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#array_element.
    def exitArray_element(self, ctx:Cra2PreParser.Array_elementContext):
        pass


    # Enter a parse tree produced by Cra2PreParser#literal.
    def enterLiteral(self, ctx:Cra2PreParser.LiteralContext):
        pass

    # Exit a parse tree produced by Cra2PreParser#literal.
    def exitLiteral(self, ctx:Cra2PreParser.LiteralContext):
        pass



del Cra2PreParser