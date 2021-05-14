import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Interpreter {

	public static void main(String [] args) throws Exception{
		MyLanguageLexer lexer = new MyLanguageLexer(CharStreams.fromFileName("in/input.txt"));
		CommonTokenStream tokens = new CommonTokenStream(lexer);
		MyLanguageParser parser = new MyLanguageParser(tokens);
		ParseTree tree = parser.commands();

		MyVisitor<Object> loader = new MyVisitor<Object>();
		loader.visit(tree);
	}
}
