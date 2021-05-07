import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayInitLexer lexer;
        if (args.length > 0)
            lexer = new ArrayInitLexer(CharStreams.fromFileName(args[0]));
        else
            lexer = new ArrayInitLexer(CharStreams.fromStream(System.in));

        CommonTokenStream tokens = new CommonTokenStream(lexer);
        ArrayInitParser parser = new ArrayInitParser(tokens);
        ParseTree tree = parser.init();
        ParseTreeWalker walker = new ParseTreeWalker();
        walker.walk(new ShortToUnicodeString(), tree);
        System.out.println();
        // System.out.println(tree.toStringTree(parser));
    }
}
