import java.util.HashMap;

public class MyVisitor<T> extends MyLanguageBaseVisitor<T> {

    HashMap<String, Object> table = new HashMap<>();

    @Override
    public T visitRepeat(MyLanguageParser.RepeatContext ctx) {
        int times = (int)(double)(Double) visitExpr(ctx.expr());
        for(int i = 0; i < times; i++) {
            visitCommands(ctx.commands());
        }
        return null;
    }

    @Override
    public T visitConditional(MyLanguageParser.ConditionalContext ctx) {
        String op = ctx.ROP().getText();
        Double num1  = (Double) visitExpr(ctx.expr(0));
        Double num2  = (Double) visitExpr(ctx.expr(1));
        Boolean ans = null;

        switch (op) {
            case "<":
                ans = num1 < num2;
                break;
            case "<=":
                ans = num1 <= num2;
                break;
            case ">":
                ans = num1 > num2;
                break;
            case ">=":
                ans = num1 >= num2;
                break;
            case "==":
                ans = num1 == num2;
                break;
            case "!=":
                ans = num1 != num2;
                break;
        }
        /**
         * Si quiereo verificar existensia de 'else' debería estar como token, si no,
         * debo verificar si los comandos de ese posible 'else' vienen no nulos.
         */
        if (ans) {
            visitCommands(ctx.commands());
        }

        return null;
    }

    @Override
    public T visitCommand(MyLanguageParser.CommandContext ctx) {
        // el analisis se va por este camino de la regla command
        if(ctx.printexpr() != null){
            Double ans = (Double)visitExpr(ctx.printexpr().expr());
            int aux = (int)Math.floor(ans);

            if(ans-aux < 1e-9){
                System.out.println(aux);
            }else{
                System.out.println(ans);
            }
        // camino de declaracion de variable
        }else if (ctx.VAR() != null){
            String name = ctx.ID().getText();
            if(table.get(name)!=null){
                int line = ctx.ID().getSymbol().getLine();
                int col = ctx.ID().getSymbol().getCharPositionInLine()+1;
                System.err.printf("<%d:%d> Error semantico, la variable con nombre: \"" + name + "\" ya fue declarada.\n",line,col);
                System.exit(-1);
            }else{
                table.put(name, visitExpr(ctx.expr()));
            }
        }else{
            return visitChildren(ctx);
        }

        return super.visitCommand(ctx);
    }

    @Override
    public T visitExpr(MyLanguageParser.ExprContext ctx) {
        if(ctx.DOUBLE() != null){
            Double num = new Double(ctx.DOUBLE().getText());
            //System.out.println(num);
            return (T)num;
        }else if(ctx.PIZQ()!=null){
            return visitExpr(ctx.expr(0));
        }else if(ctx.ID()!=null){
            String name = ctx.ID().getText();
            Object value;
            if( (value=table.get(name))==null){
                int line = ctx.ID().getSymbol().getLine();
                int col = ctx.ID().getSymbol().getCharPositionInLine()+1;
                //Prodría ser en .out tambien.
                System.err.printf("<%d:%d> Error semantico, la variable con nombre \"" + name + "\" no fue declarada.\n",line,col);
                System.exit(-1);
                return null;
            }else{
                return (T)value;
            }
        }else{
            String op = (ctx.MULOP() != null ? ctx.MULOP().getText() : ctx.SUMOP().getText());
            Double num1 = (Double)visitExpr(ctx.expr(0));
            Double num2 = (Double)visitExpr(ctx.expr(1));
            Double ans = null;

            switch(op){
                case "+":
                    ans = num1 + num2;
                    break;
                case "-":
                    ans = num1 - num2;
                    break;
                case "*":
                    ans = num1 * num2;
                    break;
                case "/":
                    ans = num1 / num2;
                    break;
            }
            //System.out.println(ans);
            return (T)(Double)ans;
        }
    }
}
