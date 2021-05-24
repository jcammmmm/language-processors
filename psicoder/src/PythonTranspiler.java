import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;

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
        transpiledSource
                .append(TAB.repeat(tabDepth))
                .append(src);
        if (addNewline)
            transpiledSource.append("\n");

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

    @Override
    public void enterProgram(PsiCoderParser.ProgramContext ctx) {

    }

    @Override
    public void exitProgram(PsiCoderParser.ProgramContext ctx) {

    }

    @Override
    public void enterPrincipal(PsiCoderParser.PrincipalContext ctx) {
        appendln("def main():");
        tabDepth++;
        if (ctx.bloque().getChildCount() == 0)
            appendln("pass");
    }

    @Override
    public void exitPrincipal(PsiCoderParser.PrincipalContext ctx) {
        tabDepth--;
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

    }

    @Override
    public void exitBloque(PsiCoderParser.BloqueContext ctx) {

    }

    @Override
    public void enterProposicion(PsiCoderParser.ProposicionContext ctx) {

    }

    @Override
    public void exitProposicion(PsiCoderParser.ProposicionContext ctx) {

    }

    @Override
    public void enterSi(PsiCoderParser.SiContext ctx) {

    }

    @Override
    public void exitSi(PsiCoderParser.SiContext ctx) {

    }

    @Override
    public void enterSiEntonces(PsiCoderParser.SiEntoncesContext ctx) {

    }

    @Override
    public void exitSiEntonces(PsiCoderParser.SiEntoncesContext ctx) {

    }

    @Override
    public void enterPara(PsiCoderParser.ParaContext ctx) {

    }

    @Override
    public void exitPara(PsiCoderParser.ParaContext ctx) {

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

    }

    @Override
    public void enterLeer(PsiCoderParser.LeerContext ctx) {

    }

    @Override
    public void exitLeer(PsiCoderParser.LeerContext ctx) {

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
        for (PsiCoderParser.InicializacionContext inicializacionContext : ctx.inicializacion()) {
            String identifier = inicializacionContext.ID().getText();
            String value = inicializacionContext.valor().getText();
            appendln(identifier + " = " + value);
        }
    }

    @Override
    public void enterInicializacion(PsiCoderParser.InicializacionContext ctx) {

    }

    @Override
    public void exitInicializacion(PsiCoderParser.InicializacionContext ctx) {

    }

    @Override
    public void enterAsignacion(PsiCoderParser.AsignacionContext ctx) {

    }

    @Override
    public void exitAsignacion(PsiCoderParser.AsignacionContext ctx) {

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
