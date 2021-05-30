import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.misc.Interval;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.TerminalNode;

import java.util.ArrayList;
import java.util.List;

public class PythonTranspiler implements  PsiCoderListener {

    private static final String TAB = "  ";

    private final StringBuilder transpiledSource;
    private final boolean enableDebugOutput;
    private int tabDepth;

    public PythonTranspiler() {
        transpiledSource = new StringBuilder();
        enableDebugOutput = false;
        tabDepth = 0;
    }

    public void appendToTranspiledSrc(String src, boolean addNewline) {
        if (addNewline) {
            transpiledSource
                    .append(TAB.repeat(tabDepth))
                    .append(src)
                    .append("\n");
        } else {
            transpiledSource.append(src);
        }

        if (enableDebugOutput)
            System.out.println(src);
    }

    public void append(String src) {
        appendToTranspiledSrc(src, false);
    }

    public void appendln(String src) {
        appendToTranspiledSrc(src, true);
    }

    public String getTranspiledSource() {
        return transpiledSource.toString();
    }

    public String getExpression(PsiCoderParser.ExpresionContext exprCtx) {
        int ini = exprCtx.getStart().getStartIndex();
        int end = exprCtx.getStop().getStopIndex();
        Interval ival = new Interval(ini, end);
        return exprCtx.start.getInputStream().getText(ival);
    }

    public String replaceBooleanOps(String src) {
        src = src.replace("||", " or ");
        src = src.replace("&&", " and ");
        return src;
    }

                                @Override
    public void enterProgram(PsiCoderParser.ProgramContext ctx) {

    }

    @Override
    public void exitProgram(PsiCoderParser.ProgramContext ctx) {

    }

    @Override
    public void enterPrincipal(PsiCoderParser.PrincipalContext ctx) {
        appendln("def main():");
        if (ctx.bloque().getChildCount() == 0)
            appendln("pass");
    }

    @Override
    public void exitPrincipal(PsiCoderParser.PrincipalContext ctx) {
        appendln("");
        appendln("if __name__ == '__main__':");
        appendln(TAB + "main()");
    }

    @Override
    public void enterDefinition(PsiCoderParser.DefinitionContext ctx) {
    }

    @Override
    public void exitDefinition(PsiCoderParser.DefinitionContext ctx) {

    }

    @Override
    public void enterFuncion(PsiCoderParser.FuncionContext ctx) {

    }

    @Override
    public void exitFuncion(PsiCoderParser.FuncionContext ctx) {

    }

    @Override
    public void enterRetornar(PsiCoderParser.RetornarContext ctx) {

    }

    @Override
    public void exitRetornar(PsiCoderParser.RetornarContext ctx) {

    }

    @Override
    public void enterEstructura(PsiCoderParser.EstructuraContext ctx) {

    }

    @Override
    public void exitEstructura(PsiCoderParser.EstructuraContext ctx) {

    }

    @Override
    public void enterBloque(PsiCoderParser.BloqueContext ctx) {
        tabDepth++;
    }

    @Override
    public void exitBloque(PsiCoderParser.BloqueContext ctx) {
        tabDepth--;
    }

    @Override
    public void enterProposicion(PsiCoderParser.ProposicionContext ctx) {

    }

    @Override
    public void exitProposicion(PsiCoderParser.ProposicionContext ctx) {
    }

    @Override
    public void enterSi(PsiCoderParser.SiContext ctx) {
        StringBuilder ifSrc = new StringBuilder("if ");
        ifSrc.append(ctx.expresion().getText());
        ifSrc.append(":");
        appendln(ifSrc.toString());
    }

    @Override
    public void exitSi(PsiCoderParser.SiContext ctx) {

    }

    @Override
    public void enterSiEntonces(PsiCoderParser.SiEntoncesContext ctx) {
        if (ctx.getChild(0).getText().equals("si_no"))
            appendln("else:");
    }

    @Override
    public void exitSiEntonces(PsiCoderParser.SiEntoncesContext ctx) {

    }

    @Override
    public void enterPara(PsiCoderParser.ParaContext ctx) {
        appendln(ctx.inicio().ID().getText() + " = " + ctx.valor().getText());
        StringBuilder forSrc = new StringBuilder();
        forSrc.append("while (");
        forSrc.append(replaceBooleanOps(ctx.expresion().get(0).getText()));
        forSrc.append("):");
        appendln(forSrc.toString());
    }

    @Override
    public void exitPara(PsiCoderParser.ParaContext ctx) {
        tabDepth++; // at this point we are outside of any block
        String identifier = ctx.inicio().ID().getText();
        if (ctx.valor() != null) { // if the step is given by an already computed value
            appendln(identifier + "+=" + ctx.valor().getText());
        } else { // if value is an expression
            appendln(identifier + "+=" + ctx.expresion(1).getText());
        }
        tabDepth--; // restore depth
    }

    @Override
    public void enterInicio(PsiCoderParser.InicioContext ctx) {

    }

    @Override
    public void exitInicio(PsiCoderParser.InicioContext ctx) {

    }

    @Override
    public void enterMientras(PsiCoderParser.MientrasContext ctx) {

    }

    @Override
    public void exitMientras(PsiCoderParser.MientrasContext ctx) {

    }

    @Override
    public void enterHacerMientras(PsiCoderParser.HacerMientrasContext ctx) {

    }

    @Override
    public void exitHacerMientras(PsiCoderParser.HacerMientrasContext ctx) {

    }

    @Override
    public void enterSeleccionar(PsiCoderParser.SeleccionarContext ctx) {

    }

    @Override
    public void exitSeleccionar(PsiCoderParser.SeleccionarContext ctx) {

    }

    @Override
    public void enterCaso(PsiCoderParser.CasoContext ctx) {

    }

    @Override
    public void exitCaso(PsiCoderParser.CasoContext ctx) {

    }

    @Override
    public void enterDefecto(PsiCoderParser.DefectoContext ctx) {

    }

    @Override
    public void exitDefecto(PsiCoderParser.DefectoContext ctx) {

    }

    @Override
    public void enterImprimir(PsiCoderParser.ImprimirContext ctx) {

    }

    @Override
    public void exitImprimir(PsiCoderParser.ImprimirContext ctx) {
        StringBuilder printTemplate = new StringBuilder("print('");
        StringBuilder printParams = new StringBuilder(".format(");
        for(PsiCoderParser.ValorContext valCtx: ctx.valor()) {
            printTemplate.append("{} ");
            printParams.append(valCtx.getText() + ", ");
        }
        printTemplate.deleteCharAt(printTemplate.length() - 1); // space
        printTemplate.append("')");
        printParams.deleteCharAt(printParams.length() - 1); // space
        printParams.deleteCharAt(printParams.length() - 1); // comma
        printParams.append(")");
        appendln(printTemplate.toString() + printParams.toString());
    }

    @Override
    public void enterLeer(PsiCoderParser.LeerContext ctx) {

    }

    @Override
    public void exitLeer(PsiCoderParser.LeerContext ctx) {
        String identifier = ctx.ID().getText();
        appendln(identifier + " = input()");
    }

    @Override
    public void enterDeclaracion(PsiCoderParser.DeclaracionContext ctx) {
    }

    /**
     * Quiere decir que un sentencia de declarcion de variable acaba de procesarse
     * completamente sin errores sintacticos (ni lexicos).
     * @param ctx the parse tree
     */
    @Override
    public void exitDeclaracion(PsiCoderParser.DeclaracionContext ctx) {
        String type = ctx.tipo().getText();
        String initValue = "";
        switch (type) {
            case "entero":
                initValue = "0";
                break;
            case "real":
                initValue = "0.0";
                break;
            case "booleano":
                initValue = "True";
                break;
            case "caracter":
                initValue = "''";
                break;
            case "cadena":
                initValue = "\"\"";
                break;
            default:
                initValue = "null";
        }
        for (TerminalNode termNode : ctx.ID())
            appendln(termNode.getText() + " = " + initValue);
    }

    @Override
    public void enterInicializacion(PsiCoderParser.InicializacionContext ctx) {

    }

    @Override
    public void exitInicializacion(PsiCoderParser.InicializacionContext ctx) {
        String id = ctx.ID().getText();
        String value = ctx.valor().getText();
        appendln(id + " = " + value);
    }

    @Override
    public void enterAsignacion(PsiCoderParser.AsignacionContext ctx) {

    }

    @Override
    public void exitAsignacion(PsiCoderParser.AsignacionContext ctx) {
        String id = ctx.ID().getText();
        String value = ctx.valor().getText();
        appendln(id + " = " + value);
    }

    @Override
    public void enterValor(PsiCoderParser.ValorContext ctx) {

    }

    @Override
    public void exitValor(PsiCoderParser.ValorContext ctx) {

    }

    @Override
    public void enterExpresion(PsiCoderParser.ExpresionContext ctx) {

    }

    @Override
    public void exitExpresion(PsiCoderParser.ExpresionContext ctx) {

    }

    @Override
    public void enterFunLlamado(PsiCoderParser.FunLlamadoContext ctx) {

    }

    @Override
    public void exitFunLlamado(PsiCoderParser.FunLlamadoContext ctx) {
        if (!(ctx.getParent() instanceof PsiCoderParser.ValorContext))
            appendln(ctx.getText());
    }

    @Override
    public void enterLiteral(PsiCoderParser.LiteralContext ctx) {

    }

    @Override
    public void exitLiteral(PsiCoderParser.LiteralContext ctx) {

    }

    @Override
    public void enterTipo(PsiCoderParser.TipoContext ctx) {

    }

    @Override
    public void exitTipo(PsiCoderParser.TipoContext ctx) {

    }

    @Override
    public void visitTerminal(TerminalNode terminalNode) {

    }

    @Override
    public void visitErrorNode(ErrorNode errorNode) {

    }

    @Override
    public void enterEveryRule(ParserRuleContext parserRuleContext) {

    }

    @Override
    public void exitEveryRule(ParserRuleContext parserRuleContext) {

    }
}
