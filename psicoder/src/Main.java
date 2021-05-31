import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        if (args.length != 0)
            transpilePsicodeSource("../in/t42.psi");
        else {
            String[] samples = {
                "../in/a04.psi", // maximum number
                "../in/a05.psi", // prime number
                "../in/a08.psi", // geometry
                "../in/a19.psi", // students
                "in/00.psi",
                "in/01.psi",
                "in/02.psi",
                "in/03.psi",
                "in/04.psi",
                "in/05.psi",
                "in/06.psi",
                "in/07.psi",
                "in/08.psi",
                "in/09.psi",
                "in/10.psi",
                "in/11.psi",
                "in/12.psi"
            };
            for (String filename : samples) {
                System.out.println("#######################################################");
                System.out.println("#######################################################");
                System.out.println("#######################################################");
                System.out.println("#######################################################");
                System.out.println("#######################################################");
                System.out.println("PSICODER SOURCE: " + filename);
                transpilePsicodeSource(filename);
                Thread.sleep(1000L);
            }
        }
    }

    private static void transpilePsicodeSource(String filename) throws IOException {
        PsiCoderLexer lexer;
        lexer = new PsiCoderLexer(CharStreams.fromFileName(filename));
        CommonTokenStream tokenStream = new CommonTokenStream(lexer);
        PsiCoderParser parser = new PsiCoderParser(tokenStream);
        ParseTree tree = parser.program();
        ParseTreeWalker walker = new ParseTreeWalker();
        PythonTranspiler pythonTranspiler = new PythonTranspiler();
        walker.walk(pythonTranspiler, tree);
        System.out.println(pythonTranspiler.getTranspiledSource());
    }
}