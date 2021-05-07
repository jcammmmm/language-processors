public class Traductor extends SampleGrammarBaseListener {
    @Override
    public void enterInicio(SampleGrammarParser.InicioContext ctx) {
        System.out.println("buahahahaha!");
    }

    @Override
    public void exitInicio(SampleGrammarParser.InicioContext ctx) {
        System.out.println(ctx.ID(0));
    }
}
