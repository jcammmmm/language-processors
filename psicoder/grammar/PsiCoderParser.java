// Generated from c:\Users\jcam\Data\repo-m\language-processors\psicoder\grammar\PsiCoder.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PsiCoderParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, COMMENT=36, LINE_COMMENT=37, WS=38, 
		LIT_NUM=39, LIT_BUL=40, LIT_CAD=41, LIT_CHR=42, ID=43, BIN_OP=44, UNA_OP=45, 
		SMCOLON=46;
	public static final int
		RULE_program = 0, RULE_definition = 1, RULE_function = 2, RULE_return = 3, 
		RULE_structure = 4, RULE_block = 5, RULE_statement = 6, RULE_if = 7, RULE_ifThen = 8, 
		RULE_for = 9, RULE_while = 10, RULE_doWhile = 11, RULE_switch = 12, RULE_case = 13, 
		RULE_default = 14, RULE_print = 15, RULE_read = 16, RULE_declaration = 17, 
		RULE_assignment = 18, RULE_value = 19, RULE_expression = 20, RULE_funCall = 21, 
		RULE_literal = 22, RULE_type = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "definition", "function", "return", "structure", "block", 
			"statement", "if", "ifThen", "for", "while", "doWhile", "switch", "case", 
			"default", "print", "read", "declaration", "assignment", "value", "expression", 
			"funCall", "literal", "type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'funcion_principal'", "'fin_principal'", "'funcion'", "'('", "','", 
			"')'", "'hacer'", "'fin_funcion'", "'retornar'", "'estructura'", "'fin_estructura'", 
			"'si'", "'entonces'", "'fin_si'", "'si_no'", "'para'", "'fin_para'", 
			"'mientras'", "'fin_mientras'", "'seleccionar'", "'entre'", "'fin_seleccionar'", 
			"'caso'", "':'", "'romper;'", "'defecto'", "'imprimir'", "'leer'", "'='", 
			"'()'", "'entero'", "'real'", "'cadena'", "'booleano'", "'caracter'", 
			null, null, null, null, null, null, null, null, null, "'!'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"COMMENT", "LINE_COMMENT", "WS", "LIT_NUM", "LIT_BUL", "LIT_CAD", "LIT_CHR", 
			"ID", "BIN_OP", "UNA_OP", "SMCOLON"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PsiCoder.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PsiCoderParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<DefinitionContext> definition() {
			return getRuleContexts(DefinitionContext.class);
		}
		public DefinitionContext definition(int i) {
			return getRuleContext(DefinitionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==T__9) {
				{
				{
				setState(48);
				definition();
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
			match(T__0);
			setState(55);
			block();
			setState(56);
			match(T__1);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==T__9) {
				{
				{
				setState(57);
				definition();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefinitionContext extends ParserRuleContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public StructureContext structure() {
			return getRuleContext(StructureContext.class,0);
		}
		public DefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterDefinition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitDefinition(this);
		}
	}

	public final DefinitionContext definition() throws RecognitionException {
		DefinitionContext _localctx = new DefinitionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_definition);
		try {
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				function();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				structure();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(PsiCoderParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PsiCoderParser.ID, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ReturnContext return() {
			return getRuleContext(ReturnContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__2);
			setState(68);
			type();
			setState(69);
			match(ID);
			setState(70);
			match(T__3);
			{
			setState(71);
			type();
			setState(72);
			match(ID);
			}
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(74);
				match(T__4);
				setState(75);
				type();
				setState(76);
				match(ID);
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			match(T__5);
			setState(84);
			match(T__6);
			setState(87);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(85);
				block();
				}
				break;
			case 2:
				{
				setState(86);
				return();
				}
				break;
			}
			setState(89);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnContext extends ParserRuleContext {
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterReturn(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitReturn(this);
		}
	}

	public final ReturnContext return() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(T__8);
			setState(94);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(92);
				expression();
				}
				break;
			case 2:
				{
				setState(93);
				match(ID);
				}
				break;
			}
			setState(96);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public StructureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structure; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterStructure(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitStructure(this);
		}
	}

	public final StructureContext structure() throws RecognitionException {
		StructureContext _localctx = new StructureContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_structure);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__9);
			setState(99);
			match(ID);
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << ID))) != 0)) {
				{
				{
				setState(100);
				declaration();
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(T__10);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(108);
					statement();
					}
					} 
				}
				setState(113);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public FunCallContext funCall() {
			return getRuleContext(FunCallContext.class,0);
		}
		public IfContext if() {
			return getRuleContext(IfContext.class,0);
		}
		public ForContext for() {
			return getRuleContext(ForContext.class,0);
		}
		public WhileContext while() {
			return getRuleContext(WhileContext.class,0);
		}
		public DoWhileContext doWhile() {
			return getRuleContext(DoWhileContext.class,0);
		}
		public SwitchContext switch() {
			return getRuleContext(SwitchContext.class,0);
		}
		public ReturnContext return() {
			return getRuleContext(ReturnContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(115);
				assignment();
				setState(116);
				match(SMCOLON);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(118);
				print();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(119);
				read();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(120);
				funCall();
				setState(121);
				match(SMCOLON);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(123);
				if();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(124);
				for();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(125);
				while();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(126);
				doWhile();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(127);
				switch();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(128);
				return();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfThenContext ifThen() {
			return getRuleContext(IfThenContext.class,0);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterIf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitIf(this);
		}
	}

	public final IfContext if() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_if);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			match(T__11);
			setState(132);
			match(T__3);
			setState(133);
			expression();
			setState(134);
			match(T__5);
			setState(135);
			match(T__12);
			setState(136);
			block();
			setState(137);
			ifThen();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfThenContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfThenContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifThen; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterIfThen(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitIfThen(this);
		}
	}

	public final IfThenContext ifThen() throws RecognitionException {
		IfThenContext _localctx = new IfThenContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ifThen);
		try {
			setState(144);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				match(T__13);
				}
				break;
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				match(T__14);
				setState(141);
				block();
				setState(142);
				match(T__13);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> SMCOLON() { return getTokens(PsiCoderParser.SMCOLON); }
		public TerminalNode SMCOLON(int i) {
			return getToken(PsiCoderParser.SMCOLON, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ForContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterFor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitFor(this);
		}
	}

	public final ForContext for() throws RecognitionException {
		ForContext _localctx = new ForContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(T__15);
			setState(147);
			match(T__3);
			setState(152);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(148);
				declaration();
				}
				break;
			case 2:
				{
				setState(149);
				assignment();
				setState(150);
				match(SMCOLON);
				}
				break;
			}
			setState(154);
			expression();
			setState(155);
			match(SMCOLON);
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(156);
				value();
				}
				break;
			case 2:
				{
				setState(157);
				expression();
				}
				break;
			}
			setState(160);
			match(T__5);
			setState(161);
			match(T__6);
			setState(162);
			block();
			setState(163);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterWhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitWhile(this);
		}
	}

	public final WhileContext while() throws RecognitionException {
		WhileContext _localctx = new WhileContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			match(T__17);
			setState(166);
			match(T__3);
			setState(167);
			expression();
			setState(168);
			match(T__5);
			setState(169);
			match(T__6);
			setState(170);
			block();
			setState(171);
			match(T__18);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DoWhileContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public DoWhileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doWhile; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterDoWhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitDoWhile(this);
		}
	}

	public final DoWhileContext doWhile() throws RecognitionException {
		DoWhileContext _localctx = new DoWhileContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_doWhile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(T__6);
			setState(174);
			block();
			setState(175);
			match(T__17);
			setState(176);
			match(T__3);
			setState(177);
			expression();
			setState(178);
			match(T__5);
			setState(179);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SwitchContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public DefaultContext default() {
			return getRuleContext(DefaultContext.class,0);
		}
		public List<CaseContext> case() {
			return getRuleContexts(CaseContext.class);
		}
		public CaseContext case(int i) {
			return getRuleContext(CaseContext.class,i);
		}
		public SwitchContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switch; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterSwitch(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitSwitch(this);
		}
	}

	public final SwitchContext switch() throws RecognitionException {
		SwitchContext _localctx = new SwitchContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_switch);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(T__19);
			setState(182);
			match(T__3);
			setState(183);
			match(ID);
			setState(184);
			match(T__5);
			setState(185);
			match(T__20);
			setState(192);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(187); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(186);
					case();
					}
					}
					setState(189); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==T__22 || _la==T__25 );
				}
				break;
			case 2:
				{
				setState(191);
				default();
				}
				break;
			}
			setState(194);
			match(T__21);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CaseContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DefaultContext default() {
			return getRuleContext(DefaultContext.class,0);
		}
		public CaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterCase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitCase(this);
		}
	}

	public final CaseContext case() throws RecognitionException {
		CaseContext _localctx = new CaseContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_case);
		int _la;
		try {
			setState(209);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__22:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(T__22);
				setState(197);
				literal();
				setState(198);
				match(T__23);
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__8) | (1L << T__11) | (1L << T__15) | (1L << T__17) | (1L << T__19) | (1L << T__26) | (1L << T__27) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << ID))) != 0)) {
					{
					{
					setState(199);
					statement();
					}
					}
					setState(204);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__24) {
					{
					setState(205);
					match(T__24);
					}
				}

				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 2);
				{
				setState(208);
				default();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefaultContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public DefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterDefault(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitDefault(this);
		}
	}

	public final DefaultContext default() throws RecognitionException {
		DefaultContext _localctx = new DefaultContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_default);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(T__25);
			setState(212);
			match(T__23);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__8) | (1L << T__11) | (1L << T__15) | (1L << T__17) | (1L << T__19) | (1L << T__26) | (1L << T__27) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << ID))) != 0)) {
				{
				{
				setState(213);
				statement();
				}
				}
				setState(218);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__24) {
				{
				setState(219);
				match(T__24);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitPrint(this);
		}
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(T__26);
			setState(223);
			match(T__3);
			setState(224);
			value();
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(225);
				match(T__4);
				setState(226);
				value();
				}
				}
				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(232);
			match(T__5);
			setState(233);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterRead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitRead(this);
		}
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(T__27);
			setState(236);
			match(T__3);
			setState(237);
			match(ID);
			setState(238);
			match(T__5);
			setState(239);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode SMCOLON() { return getToken(PsiCoderParser.SMCOLON, 0); }
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public List<TerminalNode> ID() { return getTokens(PsiCoderParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PsiCoderParser.ID, i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			type();
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(242);
				assignment();
				}
				break;
			case 2:
				{
				setState(243);
				match(ID);
				}
				break;
			}
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(246);
				match(T__4);
				setState(249);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(247);
					assignment();
					}
					break;
				case 2:
					{
					setState(248);
					match(ID);
					}
					break;
				}
				}
				}
				setState(255);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(256);
			match(SMCOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(ID);
			setState(259);
			match(T__28);
			setState(260);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public FunCallContext funCall() {
			return getRuleContext(FunCallContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				setState(262);
				match(ID);
				}
				break;
			case 2:
				{
				setState(263);
				literal();
				}
				break;
			case 3:
				{
				setState(264);
				expression();
				}
				break;
			case 4:
				{
				setState(265);
				funCall();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<TerminalNode> BIN_OP() { return getTokens(PsiCoderParser.BIN_OP); }
		public TerminalNode BIN_OP(int i) {
			return getToken(PsiCoderParser.BIN_OP, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expression);
		try {
			int _alt;
			setState(288);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(270);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LIT_NUM:
				case LIT_BUL:
				case LIT_CAD:
				case LIT_CHR:
					{
					setState(268);
					literal();
					}
					break;
				case ID:
					{
					setState(269);
					match(ID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(272);
				match(BIN_OP);
				setState(273);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(274);
				match(T__3);
				setState(275);
				expression();
				setState(276);
				match(T__5);
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(277);
						match(BIN_OP);
						setState(278);
						expression();
						}
						} 
					}
					setState(283);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
				}
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(286);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LIT_NUM:
				case LIT_BUL:
				case LIT_CAD:
				case LIT_CHR:
					{
					setState(284);
					literal();
					}
					break;
				case ID:
					{
					setState(285);
					match(ID);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public FunCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funCall; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterFunCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitFunCall(this);
		}
	}

	public final FunCallContext funCall() throws RecognitionException {
		FunCallContext _localctx = new FunCallContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_funCall);
		int _la;
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(290);
				match(ID);
				setState(291);
				match(T__29);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
				match(ID);
				setState(293);
				match(T__3);
				setState(294);
				value();
				setState(299);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(295);
					match(T__4);
					setState(296);
					value();
					}
					}
					setState(301);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(302);
				match(T__5);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode LIT_BUL() { return getToken(PsiCoderParser.LIT_BUL, 0); }
		public TerminalNode LIT_CAD() { return getToken(PsiCoderParser.LIT_CAD, 0); }
		public TerminalNode LIT_NUM() { return getToken(PsiCoderParser.LIT_NUM, 0); }
		public TerminalNode LIT_CHR() { return getToken(PsiCoderParser.LIT_CHR, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LIT_NUM) | (1L << LIT_BUL) | (1L << LIT_CAD) | (1L << LIT_CHR))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PsiCoderParser.ID, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PsiCoderListener ) ((PsiCoderListener)listener).exitType(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << ID))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60\u0139\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\7\2\64\n\2\f\2\16\2\67\13\2\3\2\3\2\3\2\3\2\7\2=\n\2\f\2\16\2@\13"+
		"\2\3\3\3\3\5\3D\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4Q\n"+
		"\4\f\4\16\4T\13\4\3\4\3\4\3\4\3\4\5\4Z\n\4\3\4\3\4\3\5\3\5\3\5\5\5a\n"+
		"\5\3\5\3\5\3\6\3\6\3\6\7\6h\n\6\f\6\16\6k\13\6\3\6\3\6\3\7\7\7p\n\7\f"+
		"\7\16\7s\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\5\b\u0084\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n"+
		"\5\n\u0093\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009b\n\13\3\13\3\13"+
		"\3\13\3\13\5\13\u00a1\n\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\6\16\u00be\n\16\r\16\16\16\u00bf\3\16\5\16\u00c3\n\16\3\16\3\16"+
		"\3\17\3\17\3\17\3\17\7\17\u00cb\n\17\f\17\16\17\u00ce\13\17\3\17\5\17"+
		"\u00d1\n\17\3\17\5\17\u00d4\n\17\3\20\3\20\3\20\7\20\u00d9\n\20\f\20\16"+
		"\20\u00dc\13\20\3\20\5\20\u00df\n\20\3\21\3\21\3\21\3\21\3\21\7\21\u00e6"+
		"\n\21\f\21\16\21\u00e9\13\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3"+
		"\22\3\23\3\23\3\23\5\23\u00f7\n\23\3\23\3\23\3\23\5\23\u00fc\n\23\7\23"+
		"\u00fe\n\23\f\23\16\23\u0101\13\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\5\25\u010d\n\25\3\26\3\26\5\26\u0111\n\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\7\26\u011a\n\26\f\26\16\26\u011d\13\26\3\26\3"+
		"\26\5\26\u0121\n\26\5\26\u0123\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\7\27\u012c\n\27\f\27\16\27\u012f\13\27\3\27\3\27\5\27\u0133\n\27\3\30"+
		"\3\30\3\31\3\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \""+
		"$&(*,.\60\2\4\3\2),\4\2!%--\2\u014b\2\65\3\2\2\2\4C\3\2\2\2\6E\3\2\2\2"+
		"\b]\3\2\2\2\nd\3\2\2\2\fq\3\2\2\2\16\u0083\3\2\2\2\20\u0085\3\2\2\2\22"+
		"\u0092\3\2\2\2\24\u0094\3\2\2\2\26\u00a7\3\2\2\2\30\u00af\3\2\2\2\32\u00b7"+
		"\3\2\2\2\34\u00d3\3\2\2\2\36\u00d5\3\2\2\2 \u00e0\3\2\2\2\"\u00ed\3\2"+
		"\2\2$\u00f3\3\2\2\2&\u0104\3\2\2\2(\u010c\3\2\2\2*\u0122\3\2\2\2,\u0132"+
		"\3\2\2\2.\u0134\3\2\2\2\60\u0136\3\2\2\2\62\64\5\4\3\2\63\62\3\2\2\2\64"+
		"\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3\2\2\289\7"+
		"\3\2\29:\5\f\7\2:>\7\4\2\2;=\5\4\3\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3"+
		"\2\2\2?\3\3\2\2\2@>\3\2\2\2AD\5\6\4\2BD\5\n\6\2CA\3\2\2\2CB\3\2\2\2D\5"+
		"\3\2\2\2EF\7\5\2\2FG\5\60\31\2GH\7-\2\2HI\7\6\2\2IJ\5\60\31\2JK\7-\2\2"+
		"KR\3\2\2\2LM\7\7\2\2MN\5\60\31\2NO\7-\2\2OQ\3\2\2\2PL\3\2\2\2QT\3\2\2"+
		"\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\7\b\2\2VY\7\t\2\2WZ\5\f\7"+
		"\2XZ\5\b\5\2YW\3\2\2\2YX\3\2\2\2Z[\3\2\2\2[\\\7\n\2\2\\\7\3\2\2\2]`\7"+
		"\13\2\2^a\5*\26\2_a\7-\2\2`^\3\2\2\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7"+
		"\60\2\2c\t\3\2\2\2de\7\f\2\2ei\7-\2\2fh\5$\23\2gf\3\2\2\2hk\3\2\2\2ig"+
		"\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7\r\2\2m\13\3\2\2\2np\5\16\b"+
		"\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\r\3\2\2\2sq\3\2\2\2t\u0084"+
		"\5$\23\2uv\5&\24\2vw\7\60\2\2w\u0084\3\2\2\2x\u0084\5 \21\2y\u0084\5\""+
		"\22\2z{\5,\27\2{|\7\60\2\2|\u0084\3\2\2\2}\u0084\5\20\t\2~\u0084\5\24"+
		"\13\2\177\u0084\5\26\f\2\u0080\u0084\5\30\r\2\u0081\u0084\5\32\16\2\u0082"+
		"\u0084\5\b\5\2\u0083t\3\2\2\2\u0083u\3\2\2\2\u0083x\3\2\2\2\u0083y\3\2"+
		"\2\2\u0083z\3\2\2\2\u0083}\3\2\2\2\u0083~\3\2\2\2\u0083\177\3\2\2\2\u0083"+
		"\u0080\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0082\3\2\2\2\u0084\17\3\2\2"+
		"\2\u0085\u0086\7\16\2\2\u0086\u0087\7\6\2\2\u0087\u0088\5*\26\2\u0088"+
		"\u0089\7\b\2\2\u0089\u008a\7\17\2\2\u008a\u008b\5\f\7\2\u008b\u008c\5"+
		"\22\n\2\u008c\21\3\2\2\2\u008d\u0093\7\20\2\2\u008e\u008f\7\21\2\2\u008f"+
		"\u0090\5\f\7\2\u0090\u0091\7\20\2\2\u0091\u0093\3\2\2\2\u0092\u008d\3"+
		"\2\2\2\u0092\u008e\3\2\2\2\u0093\23\3\2\2\2\u0094\u0095\7\22\2\2\u0095"+
		"\u009a\7\6\2\2\u0096\u009b\5$\23\2\u0097\u0098\5&\24\2\u0098\u0099\7\60"+
		"\2\2\u0099\u009b\3\2\2\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009b"+
		"\u009c\3\2\2\2\u009c\u009d\5*\26\2\u009d\u00a0\7\60\2\2\u009e\u00a1\5"+
		"(\25\2\u009f\u00a1\5*\26\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1"+
		"\u00a2\3\2\2\2\u00a2\u00a3\7\b\2\2\u00a3\u00a4\7\t\2\2\u00a4\u00a5\5\f"+
		"\7\2\u00a5\u00a6\7\23\2\2\u00a6\25\3\2\2\2\u00a7\u00a8\7\24\2\2\u00a8"+
		"\u00a9\7\6\2\2\u00a9\u00aa\5*\26\2\u00aa\u00ab\7\b\2\2\u00ab\u00ac\7\t"+
		"\2\2\u00ac\u00ad\5\f\7\2\u00ad\u00ae\7\25\2\2\u00ae\27\3\2\2\2\u00af\u00b0"+
		"\7\t\2\2\u00b0\u00b1\5\f\7\2\u00b1\u00b2\7\24\2\2\u00b2\u00b3\7\6\2\2"+
		"\u00b3\u00b4\5*\26\2\u00b4\u00b5\7\b\2\2\u00b5\u00b6\7\60\2\2\u00b6\31"+
		"\3\2\2\2\u00b7\u00b8\7\26\2\2\u00b8\u00b9\7\6\2\2\u00b9\u00ba\7-\2\2\u00ba"+
		"\u00bb\7\b\2\2\u00bb\u00c2\7\27\2\2\u00bc\u00be\5\34\17\2\u00bd\u00bc"+
		"\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0"+
		"\u00c3\3\2\2\2\u00c1\u00c3\5\36\20\2\u00c2\u00bd\3\2\2\2\u00c2\u00c1\3"+
		"\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7\30\2\2\u00c5\33\3\2\2\2\u00c6"+
		"\u00c7\7\31\2\2\u00c7\u00c8\5.\30\2\u00c8\u00cc\7\32\2\2\u00c9\u00cb\5"+
		"\16\b\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc"+
		"\u00cd\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\7\33"+
		"\2\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2"+
		"\u00d4\5\36\20\2\u00d3\u00c6\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\35\3\2"+
		"\2\2\u00d5\u00d6\7\34\2\2\u00d6\u00da\7\32\2\2\u00d7\u00d9\5\16\b\2\u00d8"+
		"\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2"+
		"\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00df\7\33\2\2\u00de"+
		"\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\37\3\2\2\2\u00e0\u00e1\7\35\2"+
		"\2\u00e1\u00e2\7\6\2\2\u00e2\u00e7\5(\25\2\u00e3\u00e4\7\7\2\2\u00e4\u00e6"+
		"\5(\25\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7"+
		"\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\7\b"+
		"\2\2\u00eb\u00ec\7\60\2\2\u00ec!\3\2\2\2\u00ed\u00ee\7\36\2\2\u00ee\u00ef"+
		"\7\6\2\2\u00ef\u00f0\7-\2\2\u00f0\u00f1\7\b\2\2\u00f1\u00f2\7\60\2\2\u00f2"+
		"#\3\2\2\2\u00f3\u00f6\5\60\31\2\u00f4\u00f7\5&\24\2\u00f5\u00f7\7-\2\2"+
		"\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00ff\3\2\2\2\u00f8\u00fb"+
		"\7\7\2\2\u00f9\u00fc\5&\24\2\u00fa\u00fc\7-\2\2\u00fb\u00f9\3\2\2\2\u00fb"+
		"\u00fa\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fe\u0101\3\2"+
		"\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2\u0101"+
		"\u00ff\3\2\2\2\u0102\u0103\7\60\2\2\u0103%\3\2\2\2\u0104\u0105\7-\2\2"+
		"\u0105\u0106\7\37\2\2\u0106\u0107\5(\25\2\u0107\'\3\2\2\2\u0108\u010d"+
		"\7-\2\2\u0109\u010d\5.\30\2\u010a\u010d\5*\26\2\u010b\u010d\5,\27\2\u010c"+
		"\u0108\3\2\2\2\u010c\u0109\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2"+
		"\2\2\u010d)\3\2\2\2\u010e\u0111\5.\30\2\u010f\u0111\7-\2\2\u0110\u010e"+
		"\3\2\2\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7.\2\2\u0113"+
		"\u0123\5*\26\2\u0114\u0115\7\6\2\2\u0115\u0116\5*\26\2\u0116\u011b\7\b"+
		"\2\2\u0117\u0118\7.\2\2\u0118\u011a\5*\26\2\u0119\u0117\3\2\2\2\u011a"+
		"\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u0123\3\2"+
		"\2\2\u011d\u011b\3\2\2\2\u011e\u0121\5.\30\2\u011f\u0121\7-\2\2\u0120"+
		"\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0110\3\2"+
		"\2\2\u0122\u0114\3\2\2\2\u0122\u0120\3\2\2\2\u0123+\3\2\2\2\u0124\u0125"+
		"\7-\2\2\u0125\u0133\7 \2\2\u0126\u0127\7-\2\2\u0127\u0128\7\6\2\2\u0128"+
		"\u012d\5(\25\2\u0129\u012a\7\7\2\2\u012a\u012c\5(\25\2\u012b\u0129\3\2"+
		"\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e"+
		"\u0130\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7\b\2\2\u0131\u0133\3\2"+
		"\2\2\u0132\u0124\3\2\2\2\u0132\u0126\3\2\2\2\u0133-\3\2\2\2\u0134\u0135"+
		"\t\2\2\2\u0135/\3\2\2\2\u0136\u0137\t\3\2\2\u0137\61\3\2\2\2 \65>CRY`"+
		"iq\u0083\u0092\u009a\u00a0\u00bf\u00c2\u00cc\u00d0\u00d3\u00da\u00de\u00e7"+
		"\u00f6\u00fb\u00ff\u010c\u0110\u011b\u0120\u0122\u012d\u0132";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}