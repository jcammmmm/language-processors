// Generated from c:\Users\jcam\Data\repo-m\language-processors\psicoder\grammar\PsiCoder.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PsiCoderParser}.
 */
public interface PsiCoderListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PsiCoderParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PsiCoderParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#definition}.
	 * @param ctx the parse tree
	 */
	void enterDefinition(PsiCoderParser.DefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#definition}.
	 * @param ctx the parse tree
	 */
	void exitDefinition(PsiCoderParser.DefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(PsiCoderParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(PsiCoderParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#return}.
	 * @param ctx the parse tree
	 */
	void enterReturn(PsiCoderParser.ReturnContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#return}.
	 * @param ctx the parse tree
	 */
	void exitReturn(PsiCoderParser.ReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#structure}.
	 * @param ctx the parse tree
	 */
	void enterStructure(PsiCoderParser.StructureContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#structure}.
	 * @param ctx the parse tree
	 */
	void exitStructure(PsiCoderParser.StructureContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(PsiCoderParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(PsiCoderParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(PsiCoderParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(PsiCoderParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(PsiCoderParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(PsiCoderParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void enterIfThen(PsiCoderParser.IfThenContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#ifThen}.
	 * @param ctx the parse tree
	 */
	void exitIfThen(PsiCoderParser.IfThenContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#for}.
	 * @param ctx the parse tree
	 */
	void enterFor(PsiCoderParser.ForContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#for}.
	 * @param ctx the parse tree
	 */
	void exitFor(PsiCoderParser.ForContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#while}.
	 * @param ctx the parse tree
	 */
	void enterWhile(PsiCoderParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#while}.
	 * @param ctx the parse tree
	 */
	void exitWhile(PsiCoderParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#doWhile}.
	 * @param ctx the parse tree
	 */
	void enterDoWhile(PsiCoderParser.DoWhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#doWhile}.
	 * @param ctx the parse tree
	 */
	void exitDoWhile(PsiCoderParser.DoWhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#switch}.
	 * @param ctx the parse tree
	 */
	void enterSwitch(PsiCoderParser.SwitchContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#switch}.
	 * @param ctx the parse tree
	 */
	void exitSwitch(PsiCoderParser.SwitchContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#case}.
	 * @param ctx the parse tree
	 */
	void enterCase(PsiCoderParser.CaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#case}.
	 * @param ctx the parse tree
	 */
	void exitCase(PsiCoderParser.CaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#default}.
	 * @param ctx the parse tree
	 */
	void enterDefault(PsiCoderParser.DefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#default}.
	 * @param ctx the parse tree
	 */
	void exitDefault(PsiCoderParser.DefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(PsiCoderParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(PsiCoderParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#read}.
	 * @param ctx the parse tree
	 */
	void enterRead(PsiCoderParser.ReadContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#read}.
	 * @param ctx the parse tree
	 */
	void exitRead(PsiCoderParser.ReadContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(PsiCoderParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(PsiCoderParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(PsiCoderParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(PsiCoderParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(PsiCoderParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(PsiCoderParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(PsiCoderParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(PsiCoderParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#funCall}.
	 * @param ctx the parse tree
	 */
	void enterFunCall(PsiCoderParser.FunCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#funCall}.
	 * @param ctx the parse tree
	 */
	void exitFunCall(PsiCoderParser.FunCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(PsiCoderParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(PsiCoderParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link PsiCoderParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(PsiCoderParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PsiCoderParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(PsiCoderParser.TypeContext ctx);
}