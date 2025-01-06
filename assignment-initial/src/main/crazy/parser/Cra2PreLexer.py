# Generated from main/crazy/parser/Cra2Pre.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\7\63\u014d\n\63")
        buf.write("\f\63\16\63\u0150\13\63\3\63\5\63\u0153\n\63\3\64\3\64")
        buf.write("\7\64\u0157\n\64\f\64\16\64\u015a\13\64\3\64\3\64\5\64")
        buf.write("\u015e\n\64\3\65\3\65\3\65\5\65\u0163\n\65\3\65\6\65\u0166")
        buf.write("\n\65\r\65\16\65\u0167\3\66\3\66\3\66\3\66\5\66\u016e")
        buf.write("\n\66\3\67\3\67\3\67\38\38\78\u0175\n8\f8\168\u0178\13")
        buf.write("8\38\58\u017b\n8\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\59\u018b\n9\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0196\n")
        buf.write(":\3;\3;\7;\u019a\n;\f;\16;\u019d\13;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\7<\u01a6\n<\f<\16<\u01a9\13<\3=\3=\3=\3=\7=\u01af")
        buf.write("\n=\f=\16=\u01b2\13=\3=\3=\3>\3>\3>\3>\7>\u01ba\n>\f>")
        buf.write("\16>\u01bd\13>\3>\3>\3>\3>\3>\3?\6?\u01c5\n?\r?\16?\u01c6")
        buf.write("\3?\3?\3@\3@\3@\3A\3A\7A\u01d0\nA\fA\16A\u01d3\13A\3A")
        buf.write("\3A\3A\5A\u01d8\nA\3A\3A\3B\3B\3B\3C\3C\7C\u01e1\nC\f")
        buf.write("C\16C\u01e4\13C\3C\3C\3C\3\u01bb\2D\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2")
        buf.write("a\2c\2e\2g\2i\2k\2m\2o\60q\61s\62u\63w\64y\65{\66}\67")
        buf.write("\1778\u00819\u0083\2\u0085:\3\2\r\3\2\62;\3\2\63;\3\2")
        buf.write("c|\3\2C\\\4\2GGgg\5\2\13\f))^^\3\2))\5\2^^ppvv\3\2\f\f")
        buf.write("\5\2\13\f\17\17\"\"\3\3\f\f\2\u01f7\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2")
        buf.write("\2\2\3\u0087\3\2\2\2\5\u008f\3\2\2\2\7\u0093\3\2\2\2\t")
        buf.write("\u0099\3\2\2\2\13\u009d\3\2\2\2\r\u00a5\3\2\2\2\17\u00ad")
        buf.write("\3\2\2\2\21\u00b2\3\2\2\2\23\u00b9\3\2\2\2\25\u00bf\3")
        buf.write("\2\2\2\27\u00c3\3\2\2\2\31\u00cc\3\2\2\2\33\u00cf\3\2")
        buf.write("\2\2\35\u00d4\3\2\2\2\37\u00da\3\2\2\2!\u00de\3\2\2\2")
        buf.write("#\u00e7\3\2\2\2%\u00ea\3\2\2\2\'\u00ed\3\2\2\2)\u00f0")
        buf.write("\3\2\2\2+\u00f5\3\2\2\2-\u00ff\3\2\2\2/\u0105\3\2\2\2")
        buf.write("\61\u010a\3\2\2\2\63\u010e\3\2\2\2\65\u0114\3\2\2\2\67")
        buf.write("\u0118\3\2\2\29\u011b\3\2\2\2;\u011d\3\2\2\2=\u0120\3")
        buf.write("\2\2\2?\u0122\3\2\2\2A\u0124\3\2\2\2C\u0126\3\2\2\2E\u0128")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012c\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0130\3\2\2\2O\u0132\3\2\2\2Q\u0134\3\2\2\2S\u0136\3")
        buf.write("\2\2\2U\u0138\3\2\2\2W\u013a\3\2\2\2Y\u013c\3\2\2\2[\u013f")
        buf.write("\3\2\2\2]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2")
        buf.write("c\u0148\3\2\2\2e\u0152\3\2\2\2g\u0154\3\2\2\2i\u015f\3")
        buf.write("\2\2\2k\u016d\3\2\2\2m\u016f\3\2\2\2o\u017a\3\2\2\2q\u018a")
        buf.write("\3\2\2\2s\u0195\3\2\2\2u\u0197\3\2\2\2w\u01a1\3\2\2\2")
        buf.write("y\u01aa\3\2\2\2{\u01b5\3\2\2\2}\u01c4\3\2\2\2\177\u01ca")
        buf.write("\3\2\2\2\u0081\u01cd\3\2\2\2\u0083\u01db\3\2\2\2\u0085")
        buf.write("\u01de\3\2\2\2\u0087\u0088\7r\2\2\u0088\u0089\7t\2\2\u0089")
        buf.write("\u008a\7q\2\2\u008a\u008b\7i\2\2\u008b\u008c\7t\2\2\u008c")
        buf.write("\u008d\7c\2\2\u008d\u008e\7o\2\2\u008e\4\3\2\2\2\u008f")
        buf.write("\u0090\7x\2\2\u0090\u0091\7c\2\2\u0091\u0092\7t\2\2\u0092")
        buf.write("\6\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095\7g\2\2\u0095")
        buf.write("\u0096\7i\2\2\u0096\u0097\7k\2\2\u0097\u0098\7p\2\2\u0098")
        buf.write("\b\3\2\2\2\u0099\u009a\7g\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\u009c\7f\2\2\u009c\n\3\2\2\2\u009d\u009e\7d\2\2\u009e")
        buf.write("\u009f\7q\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7n\2\2\u00a1")
        buf.write("\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7p\2\2\u00a4")
        buf.write("\f\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7p\2\2\u00a7")
        buf.write("\u00a8\7v\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7i\2\2\u00aa")
        buf.write("\u00ab\7g\2\2\u00ab\u00ac\7t\2\2\u00ac\16\3\2\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7c\2\2\u00b0")
        buf.write("\u00b1\7n\2\2\u00b1\20\3\2\2\2\u00b2\u00b3\7u\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6\7k\2\2\u00b6")
        buf.write("\u00b7\7p\2\2\u00b7\u00b8\7i\2\2\u00b8\22\3\2\2\2\u00b9")
        buf.write("\u00ba\7e\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7p\2\2\u00bc")
        buf.write("\u00bd\7u\2\2\u00bd\u00be\7v\2\2\u00be\24\3\2\2\2\u00bf")
        buf.write("\u00c0\7c\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7f\2\2\u00c2")
        buf.write("\26\3\2\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5")
        buf.write("\u00c6\7p\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7p\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\30\3\2\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7h\2\2\u00ce")
        buf.write("\32\3\2\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7j\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\u00d3\7p\2\2\u00d3\34\3\2\2\2\u00d4")
        buf.write("\u00d5\7c\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7t\2\2\u00d7")
        buf.write("\u00d8\7c\2\2\u00d8\u00d9\7{\2\2\u00d9\36\3\2\2\2\u00da")
        buf.write("\u00db\7f\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7x\2\2\u00dd")
        buf.write(" \3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("\u00e1\7p\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7v\2\2\u00e3")
        buf.write("\u00e4\7k\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\"\3\2\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7t\2\2\u00e9")
        buf.write("$\3\2\2\2\u00ea\u00eb\7f\2\2\u00eb\u00ec\7q\2\2\u00ec")
        buf.write("&\3\2\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7h\2\2\u00ef")
        buf.write("(\3\2\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2")
        buf.write("\u00f3\7q\2\2\u00f3\u00f4\7r\2\2\u00f4*\3\2\2\2\u00f5")
        buf.write("\u00f6\7r\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7q\2\2\u00f8")
        buf.write("\u00f9\7e\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7f\2\2\u00fb")
        buf.write("\u00fc\7w\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe")
        buf.write(",\3\2\2\2\u00ff\u0100\7d\2\2\u0100\u0101\7t\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104\7m\2\2\u0104")
        buf.write(".\3\2\2\2\u0105\u0106\7g\2\2\u0106\u0107\7n\2\2\u0107")
        buf.write("\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109\60\3\2\2\2\u010a")
        buf.write("\u010b\7o\2\2\u010b\u010c\7q\2\2\u010c\u010d\7f\2\2\u010d")
        buf.write("\62\3\2\2\2\u010e\u010f\7y\2\2\u010f\u0110\7j\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7n\2\2\u0112\u0113\7g\2\2\u0113")
        buf.write("\64\3\2\2\2\u0114\u0115\7p\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write("\u0117\7v\2\2\u0117\66\3\2\2\2\u0118\u0119\7<\2\2\u0119")
        buf.write("\u011a\7?\2\2\u011a8\3\2\2\2\u011b\u011c\7?\2\2\u011c")
        buf.write(":\3\2\2\2\u011d\u011e\7>\2\2\u011e\u011f\7@\2\2\u011f")
        buf.write("<\3\2\2\2\u0120\u0121\7\60\2\2\u0121>\3\2\2\2\u0122\u0123")
        buf.write("\7.\2\2\u0123@\3\2\2\2\u0124\u0125\7=\2\2\u0125B\3\2\2")
        buf.write("\2\u0126\u0127\7<\2\2\u0127D\3\2\2\2\u0128\u0129\7]\2")
        buf.write("\2\u0129F\3\2\2\2\u012a\u012b\7_\2\2\u012bH\3\2\2\2\u012c")
        buf.write("\u012d\7*\2\2\u012dJ\3\2\2\2\u012e\u012f\7+\2\2\u012f")
        buf.write("L\3\2\2\2\u0130\u0131\7-\2\2\u0131N\3\2\2\2\u0132\u0133")
        buf.write("\7/\2\2\u0133P\3\2\2\2\u0134\u0135\7,\2\2\u0135R\3\2\2")
        buf.write("\2\u0136\u0137\7\61\2\2\u0137T\3\2\2\2\u0138\u0139\7>")
        buf.write("\2\2\u0139V\3\2\2\2\u013a\u013b\7@\2\2\u013bX\3\2\2\2")
        buf.write("\u013c\u013d\7>\2\2\u013d\u013e\7?\2\2\u013eZ\3\2\2\2")
        buf.write("\u013f\u0140\7@\2\2\u0140\u0141\7?\2\2\u0141\\\3\2\2\2")
        buf.write("\u0142\u0143\t\2\2\2\u0143^\3\2\2\2\u0144\u0145\t\3\2")
        buf.write("\2\u0145`\3\2\2\2\u0146\u0147\t\4\2\2\u0147b\3\2\2\2\u0148")
        buf.write("\u0149\t\5\2\2\u0149d\3\2\2\2\u014a\u014e\5_\60\2\u014b")
        buf.write("\u014d\5]/\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0153\3\2\2\2")
        buf.write("\u0150\u014e\3\2\2\2\u0151\u0153\7\62\2\2\u0152\u014a")
        buf.write("\3\2\2\2\u0152\u0151\3\2\2\2\u0153f\3\2\2\2\u0154\u015d")
        buf.write("\7\60\2\2\u0155\u0157\5]/\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015e\5")
        buf.write("_\60\2\u015c\u015e\7\62\2\2\u015d\u0158\3\2\2\2\u015d")
        buf.write("\u015c\3\2\2\2\u015eh\3\2\2\2\u015f\u0162\t\6\2\2\u0160")
        buf.write("\u0163\7/\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3")
        buf.write("\2\2\2\u0164\u0166\5]/\2\u0165\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("j\3\2\2\2\u0169\u016e\n\7\2\2\u016a\u016e\5m\67\2\u016b")
        buf.write("\u016c\t\b\2\2\u016c\u016e\t\b\2\2\u016d\u0169\3\2\2\2")
        buf.write("\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016el\3\2\2")
        buf.write("\2\u016f\u0170\7^\2\2\u0170\u0171\t\t\2\2\u0171n\3\2\2")
        buf.write("\2\u0172\u0176\5_\60\2\u0173\u0175\5]/\2\u0174\u0173\3")
        buf.write("\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u017b\3\2\2\2\u0178\u0176\3\2\2\2\u0179")
        buf.write("\u017b\7\62\2\2\u017a\u0172\3\2\2\2\u017a\u0179\3\2\2")
        buf.write("\2\u017bp\3\2\2\2\u017c\u017d\5e\63\2\u017d\u017e\5g\64")
        buf.write("\2\u017e\u017f\5i\65\2\u017f\u018b\3\2\2\2\u0180\u0181")
        buf.write("\5e\63\2\u0181\u0182\5g\64\2\u0182\u018b\3\2\2\2\u0183")
        buf.write("\u0184\5e\63\2\u0184\u0185\5i\65\2\u0185\u018b\3\2\2\2")
        buf.write("\u0186\u0187\5g\64\2\u0187\u0188\5i\65\2\u0188\u018b\3")
        buf.write("\2\2\2\u0189\u018b\5g\64\2\u018a\u017c\3\2\2\2\u018a\u0180")
        buf.write("\3\2\2\2\u018a\u0183\3\2\2\2\u018a\u0186\3\2\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018br\3\2\2\2\u018c\u018d\7v\2\2\u018d")
        buf.write("\u018e\7t\2\2\u018e\u018f\7w\2\2\u018f\u0196\7g\2\2\u0190")
        buf.write("\u0191\7h\2\2\u0191\u0192\7c\2\2\u0192\u0193\7n\2\2\u0193")
        buf.write("\u0194\7u\2\2\u0194\u0196\7g\2\2\u0195\u018c\3\2\2\2\u0195")
        buf.write("\u0190\3\2\2\2\u0196t\3\2\2\2\u0197\u019b\t\b\2\2\u0198")
        buf.write("\u019a\5k\66\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2")
        buf.write("\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\3")
        buf.write("\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\t\b\2\2\u019f\u01a0")
        buf.write("\b;\2\2\u01a0v\3\2\2\2\u01a1\u01a7\5a\61\2\u01a2\u01a6")
        buf.write("\5a\61\2\u01a3\u01a6\5c\62\2\u01a4\u01a6\5]/\2\u01a5\u01a2")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8x\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7\61\2")
        buf.write("\2\u01ab\u01ac\7\61\2\2\u01ac\u01b0\3\2\2\2\u01ad\u01af")
        buf.write("\n\n\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b3\u01b4\b=\3\2\u01b4z\3\2\2\2")
        buf.write("\u01b5\u01b6\7\61\2\2\u01b6\u01b7\7,\2\2\u01b7\u01bb\3")
        buf.write("\2\2\2\u01b8\u01ba\13\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\7")
        buf.write(",\2\2\u01bf\u01c0\7\61\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2")
        buf.write("\b>\3\2\u01c2|\3\2\2\2\u01c3\u01c5\t\13\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\b?\3\2")
        buf.write("\u01c9~\3\2\2\2\u01ca\u01cb\13\2\2\2\u01cb\u01cc\b@\4")
        buf.write("\2\u01cc\u0080\3\2\2\2\u01cd\u01d1\t\b\2\2\u01ce\u01d0")
        buf.write("\5k\66\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d7\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d4\u01d5\7\17\2\2\u01d5\u01d8")
        buf.write("\7\f\2\2\u01d6\u01d8\t\f\2\2\u01d7\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\bA\5\2")
        buf.write("\u01da\u0082\3\2\2\2\u01db\u01dc\7^\2\2\u01dc\u01dd\n")
        buf.write("\t\2\2\u01dd\u0084\3\2\2\2\u01de\u01e2\t\b\2\2\u01df\u01e1")
        buf.write("\5k\66\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e6\5\u0083B\2\u01e6\u01e7")
        buf.write("\bC\6\2\u01e7\u0086\3\2\2\2\27\2\u014e\u0152\u0158\u015d")
        buf.write("\u0162\u0167\u016d\u0176\u017a\u018a\u0195\u019b\u01a5")
        buf.write("\u01a7\u01b0\u01bb\u01c6\u01d1\u01d7\u01e2\7\3;\2\b\2")
        buf.write("\2\3@\3\3A\4\3C\5")
        return buf.getvalue()


class Cra2PreLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM = 1
    VAR = 2
    BEGIN = 3
    END = 4
    BOOLEAN = 5
    INTEGER = 6
    REAL = 7
    STRING = 8
    CONST = 9
    AND = 10
    CONTINUE = 11
    OF = 12
    THEN = 13
    ARRAY = 14
    DIV = 15
    FUNCTION = 16
    OR = 17
    DO = 18
    IF = 19
    LOOP = 20
    PROCEDURE = 21
    BREAK = 22
    ELSE = 23
    MOD = 24
    WHILE = 25
    NOT = 26
    ASSOPE = 27
    EQUAL = 28
    DIFF = 29
    DOT = 30
    COMMA = 31
    SEMICOLON = 32
    COLON = 33
    LS = 34
    RS = 35
    LR = 36
    RR = 37
    ADD = 38
    SUB = 39
    MUL = 40
    DIVV = 41
    LESS = 42
    GREATER = 43
    LE = 44
    GE = 45
    INTEGER_LIT = 46
    REAL_LIT = 47
    BOOLEAN_LIT = 48
    STRING_LIT = 49
    ID = 50
    LINE_COMMENT = 51
    BLOCK_COMMENT = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'program'", "'var'", "'begin'", "'end'", "'boolean'", "'integer'", 
            "'real'", "'string'", "'const'", "'and'", "'continue'", "'of'", 
            "'then'", "'array'", "'div'", "'function'", "'or'", "'do'", 
            "'if'", "'loop'", "'procedure'", "'break'", "'else'", "'mod'", 
            "'while'", "'not'", "':='", "'='", "'<>'", "'.'", "','", "';'", 
            "':'", "'['", "']'", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
            "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "VAR", "BEGIN", "END", "BOOLEAN", "INTEGER", "REAL", 
            "STRING", "CONST", "AND", "CONTINUE", "OF", "THEN", "ARRAY", 
            "DIV", "FUNCTION", "OR", "DO", "IF", "LOOP", "PROCEDURE", "BREAK", 
            "ELSE", "MOD", "WHILE", "NOT", "ASSOPE", "EQUAL", "DIFF", "DOT", 
            "COMMA", "SEMICOLON", "COLON", "LS", "RS", "LR", "RR", "ADD", 
            "SUB", "MUL", "DIVV", "LESS", "GREATER", "LE", "GE", "INTEGER_LIT", 
            "REAL_LIT", "BOOLEAN_LIT", "STRING_LIT", "ID", "LINE_COMMENT", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "PROGRAM", "VAR", "BEGIN", "END", "BOOLEAN", "INTEGER", 
                  "REAL", "STRING", "CONST", "AND", "CONTINUE", "OF", "THEN", 
                  "ARRAY", "DIV", "FUNCTION", "OR", "DO", "IF", "LOOP", 
                  "PROCEDURE", "BREAK", "ELSE", "MOD", "WHILE", "NOT", "ASSOPE", 
                  "EQUAL", "DIFF", "DOT", "COMMA", "SEMICOLON", "COLON", 
                  "LS", "RS", "LR", "RR", "ADD", "SUB", "MUL", "DIVV", "LESS", 
                  "GREATER", "LE", "GE", "DIGIT", "DIGIT_S", "LOWER_CHAR", 
                  "UPPER_CHAR", "INT_PART", "FRAC_PART", "EX_PART", "STRING_CHAR", 
                  "ESCSEQ", "INTEGER_LIT", "REAL_LIT", "BOOLEAN_LIT", "STRING_LIT", 
                  "ID", "LINE_COMMENT", "BLOCK_COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCSEQ", "ILLEGAL_ESCAPE" ]

    grammarFileName = "Cra2Pre.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[57] = self.STRING_LIT_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if (len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
                      raise UncloseString(self.text[0:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[0:-1])
            	else:
                      raise UncloseString(self.text[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[0:])
     


