// Generated from C:/Users/jcam/Data/repo-m/language-processors/interpreter/grammar\MyLanguage.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MyLanguageParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MyLanguageVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#commands}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommands(MyLanguageParser.CommandsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommand(MyLanguageParser.CommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#conditional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConditional(MyLanguageParser.ConditionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#repeat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRepeat(MyLanguageParser.RepeatContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#printexpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintexpr(MyLanguageParser.PrintexprContext ctx);
	/**
	 * Visit a parse tree produced by {@link MyLanguageParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(MyLanguageParser.ExprContext ctx);
}