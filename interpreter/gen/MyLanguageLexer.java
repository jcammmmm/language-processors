// Generated from C:/Users/jcam/Data/repo-m/language-processors/interpreter/grammar\MyLanguage.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MyLanguageLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, COMMENT=9, 
		LINE_COMMENT=10, WS=11, VAR=12, PIZQ=13, PDER=14, ROP=15, SMCOLON=16, 
		MULOP=17, SUMOP=18, DOUBLE=19, ID=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "COMMENT", 
			"LINE_COMMENT", "WS", "VAR", "PIZQ", "PDER", "ROP", "SMCOLON", "MULOP", 
			"SUMOP", "DOUBLE", "ID"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'as'", "'if'", "'then'", "'endif'", "'repeat'", "'times'", "'endrepeat'", 
			"'print'", null, null, null, "'var'", "'('", "')'", null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "COMMENT", "LINE_COMMENT", 
			"WS", "VAR", "PIZQ", "PDER", "ROP", "SMCOLON", "MULOP", "SUMOP", "DOUBLE", 
			"ID"
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


	public MyLanguageLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyLanguage.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26\u00a8\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n^\n\n\f\n\16\na\13\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\13\3\13\3\13\3\13\7\13l\n\13\f\13\16\13o\13\13\3\13\3\13\3\f\6\ft\n"+
		"\f\r\f\16\fu\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u008c\n\20\3\21\3\21\3\22\3\22"+
		"\3\23\3\23\3\24\6\24\u0095\n\24\r\24\16\24\u0096\3\24\3\24\3\24\6\24\u009c"+
		"\n\24\r\24\16\24\u009d\5\24\u00a0\n\24\3\25\3\25\7\25\u00a4\n\25\f\25"+
		"\16\25\u00a7\13\25\3_\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26\3\2\n\4\2\f\f\17"+
		"\17\5\2\13\f\17\17\"\"\4\2,,\61\61\4\2--//\3\2\62;\3\2\60\60\4\2C\\c|"+
		"\6\2\62;C\\aac|\2\u00b3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2"+
		"\2\5.\3\2\2\2\7\61\3\2\2\2\t\66\3\2\2\2\13<\3\2\2\2\rC\3\2\2\2\17I\3\2"+
		"\2\2\21S\3\2\2\2\23Y\3\2\2\2\25g\3\2\2\2\27s\3\2\2\2\31y\3\2\2\2\33}\3"+
		"\2\2\2\35\177\3\2\2\2\37\u008b\3\2\2\2!\u008d\3\2\2\2#\u008f\3\2\2\2%"+
		"\u0091\3\2\2\2\'\u0094\3\2\2\2)\u00a1\3\2\2\2+,\7c\2\2,-\7u\2\2-\4\3\2"+
		"\2\2./\7k\2\2/\60\7h\2\2\60\6\3\2\2\2\61\62\7v\2\2\62\63\7j\2\2\63\64"+
		"\7g\2\2\64\65\7p\2\2\65\b\3\2\2\2\66\67\7g\2\2\678\7p\2\289\7f\2\29:\7"+
		"k\2\2:;\7h\2\2;\n\3\2\2\2<=\7t\2\2=>\7g\2\2>?\7r\2\2?@\7g\2\2@A\7c\2\2"+
		"AB\7v\2\2B\f\3\2\2\2CD\7v\2\2DE\7k\2\2EF\7o\2\2FG\7g\2\2GH\7u\2\2H\16"+
		"\3\2\2\2IJ\7g\2\2JK\7p\2\2KL\7f\2\2LM\7t\2\2MN\7g\2\2NO\7r\2\2OP\7g\2"+
		"\2PQ\7c\2\2QR\7v\2\2R\20\3\2\2\2ST\7r\2\2TU\7t\2\2UV\7k\2\2VW\7p\2\2W"+
		"X\7v\2\2X\22\3\2\2\2YZ\7\61\2\2Z[\7,\2\2[_\3\2\2\2\\^\13\2\2\2]\\\3\2"+
		"\2\2^a\3\2\2\2_`\3\2\2\2_]\3\2\2\2`b\3\2\2\2a_\3\2\2\2bc\7,\2\2cd\7\61"+
		"\2\2de\3\2\2\2ef\b\n\2\2f\24\3\2\2\2gh\7\61\2\2hi\7\61\2\2im\3\2\2\2j"+
		"l\n\2\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2"+
		"pq\b\13\2\2q\26\3\2\2\2rt\t\3\2\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2"+
		"\2\2vw\3\2\2\2wx\b\f\2\2x\30\3\2\2\2yz\7x\2\2z{\7c\2\2{|\7t\2\2|\32\3"+
		"\2\2\2}~\7*\2\2~\34\3\2\2\2\177\u0080\7+\2\2\u0080\36\3\2\2\2\u0081\u008c"+
		"\7>\2\2\u0082\u0083\7>\2\2\u0083\u008c\7?\2\2\u0084\u0085\7@\2\2\u0085"+
		"\u008c\7?\2\2\u0086\u008c\7@\2\2\u0087\u0088\7?\2\2\u0088\u008c\7?\2\2"+
		"\u0089\u008a\7#\2\2\u008a\u008c\7?\2\2\u008b\u0081\3\2\2\2\u008b\u0082"+
		"\3\2\2\2\u008b\u0084\3\2\2\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2\u008b"+
		"\u0089\3\2\2\2\u008c \3\2\2\2\u008d\u008e\7=\2\2\u008e\"\3\2\2\2\u008f"+
		"\u0090\t\4\2\2\u0090$\3\2\2\2\u0091\u0092\t\5\2\2\u0092&\3\2\2\2\u0093"+
		"\u0095\t\6\2\2\u0094\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2"+
		"\2\2\u0096\u0097\3\2\2\2\u0097\u009f\3\2\2\2\u0098\u00a0\3\2\2\2\u0099"+
		"\u009b\t\7\2\2\u009a\u009c\t\6\2\2\u009b\u009a\3\2\2\2\u009c\u009d\3\2"+
		"\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f"+
		"\u0098\3\2\2\2\u009f\u0099\3\2\2\2\u00a0(\3\2\2\2\u00a1\u00a5\t\b\2\2"+
		"\u00a2\u00a4\t\t\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3"+
		"\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6*\3\2\2\2\u00a7\u00a5\3\2\2\2\13\2_"+
		"mu\u008b\u0096\u009d\u009f\u00a5\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}