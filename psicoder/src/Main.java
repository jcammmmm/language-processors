import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        PsiCoderLexer lexer;
        if (args.length > 0)
            lexer = new PsiCoderLexer(CharStreams.fromFileName(args[0]));
        else
            lexer = new PsiCoderLexer(CharStreams.fromStream(System.in));

        CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        PsiCoderParser parser = new PsiCoderParser(tokenStream);
        ParseTree tree = parser.program();
        ParseTreeWalker walker = new ParseTreeWalker();
        PythonTranspiler pythonTranspiler = new PythonTranspiler();
        walker.walk(pythonTranspiler, tree);
        System.out.println(pythonTranspiler.getTranspiledSource());
    }
}