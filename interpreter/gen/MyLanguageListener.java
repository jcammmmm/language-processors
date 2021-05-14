// Generated from C:/Users/jcam/Data/repo-m/language-processors/interpreter/grammar\MyLanguage.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MyLanguageParser}.
 */
public interface MyLanguageListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#commands}.
	 * @param ctx the parse tree
	 */
	void enterCommands(MyLanguageParser.CommandsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#commands}.
	 * @param ctx the parse tree
	 */
	void exitCommands(MyLanguageParser.CommandsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(MyLanguageParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(MyLanguageParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#conditional}.
	 * @param ctx the parse tree
	 */
	void enterConditional(MyLanguageParser.ConditionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#conditional}.
	 * @param ctx the parse tree
	 */
	void exitConditional(MyLanguageParser.ConditionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#repeat}.
	 * @param ctx the parse tree
	 */
	void enterRepeat(MyLanguageParser.RepeatContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#repeat}.
	 * @param ctx the parse tree
	 */
	void exitRepeat(MyLanguageParser.RepeatContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#printexpr}.
	 * @param ctx the parse tree
	 */
	void enterPrintexpr(MyLanguageParser.PrintexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#printexpr}.
	 * @param ctx the parse tree
	 */
	void exitPrintexpr(MyLanguageParser.PrintexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MyLanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MyLanguageParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MyLanguageParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MyLanguageParser.ExprContext ctx);
}