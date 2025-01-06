# Generated from main/crazy/parser/Cra2Pre.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u027f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\177\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0088\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5\u0090\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a0\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00ad\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00b6\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00be\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\5\16\u00da\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00e4\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00ec\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00fe\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u0108\n\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0117\n\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0122")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u012b\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u014b")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0158\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u016d\n\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\5&\u0198\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a2")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01b1\n")
        buf.write("(\7(\u01b3\n(\f(\16(\u01b6\13(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01cd\n)\7")
        buf.write(")\u01cf\n)\f)\16)\u01d2\13)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\5*\u01e1\n*\7*\u01e3\n*\f*\16*\u01e6\13")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u01fd\n+\7+\u01ff\n+\f+\16+\u0202\13+\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\7,\u020d\n,\f,\16,\u0210\13")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u021b\n-\f-\16-\u021e")
        buf.write("\13-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0228\n.\3.\3.\3.\5.\u022d")
        buf.write("\n.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u0239")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u024b\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\5\62\u0254\n\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u026b\n")
        buf.write("\66\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0273\n\67\38\3")
        buf.write("8\38\38\38\38\38\38\58\u027d\n8\38\2\bNPRTVX9\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\2\2\u0280\2p\3\2\2\2\4")
        buf.write("~\3\2\2\2\6\u0087\3\2\2\2\b\u008f\3\2\2\2\n\u0091\3\2")
        buf.write("\2\2\f\u009f\3\2\2\2\16\u00a1\3\2\2\2\20\u00ac\3\2\2\2")
        buf.write("\22\u00b5\3\2\2\2\24\u00bd\3\2\2\2\26\u00bf\3\2\2\2\30")
        buf.write("\u00cb\3\2\2\2\32\u00d9\3\2\2\2\34\u00e3\3\2\2\2\36\u00eb")
        buf.write("\3\2\2\2 \u00ed\3\2\2\2\"\u00f2\3\2\2\2$\u00fd\3\2\2\2")
        buf.write("&\u0107\3\2\2\2(\u0109\3\2\2\2*\u0116\3\2\2\2,\u0118\3")
        buf.write("\2\2\2.\u0121\3\2\2\2\60\u012a\3\2\2\2\62\u014a\3\2\2")
        buf.write("\2\64\u014c\3\2\2\2\66\u0157\3\2\2\28\u0159\3\2\2\2:\u016c")
        buf.write("\3\2\2\2<\u016e\3\2\2\2>\u0172\3\2\2\2@\u0178\3\2\2\2")
        buf.write("B\u017e\3\2\2\2D\u0185\3\2\2\2F\u018b\3\2\2\2H\u018f\3")
        buf.write("\2\2\2J\u0197\3\2\2\2L\u01a1\3\2\2\2N\u01a3\3\2\2\2P\u01b7")
        buf.write("\3\2\2\2R\u01d3\3\2\2\2T\u01e7\3\2\2\2V\u0203\3\2\2\2")
        buf.write("X\u0211\3\2\2\2Z\u022c\3\2\2\2\\\u022e\3\2\2\2^\u0238")
        buf.write("\3\2\2\2`\u024a\3\2\2\2b\u0253\3\2\2\2d\u0255\3\2\2\2")
        buf.write("f\u025a\3\2\2\2h\u025f\3\2\2\2j\u026a\3\2\2\2l\u0272\3")
        buf.write("\2\2\2n\u027c\3\2\2\2pq\7\3\2\2qr\7\64\2\2rs\7\"\2\2s")
        buf.write("t\5\4\3\2tu\5\20\t\2uv\58\35\2vw\7 \2\2wx\7\2\2\3xy\b")
        buf.write("\2\1\2y\3\3\2\2\2z{\5\6\4\2{|\b\3\1\2|\177\3\2\2\2}\177")
        buf.write("\b\3\1\2~z\3\2\2\2~}\3\2\2\2\177\5\3\2\2\2\u0080\u0081")
        buf.write("\5\b\5\2\u0081\u0082\5\6\4\2\u0082\u0083\b\4\1\2\u0083")
        buf.write("\u0088\3\2\2\2\u0084\u0085\5\b\5\2\u0085\u0086\b\4\1\2")
        buf.write("\u0086\u0088\3\2\2\2\u0087\u0080\3\2\2\2\u0087\u0084\3")
        buf.write("\2\2\2\u0088\7\3\2\2\2\u0089\u008a\5\n\6\2\u008a\u008b")
        buf.write("\b\5\1\2\u008b\u0090\3\2\2\2\u008c\u008d\5\16\b\2\u008d")
        buf.write("\u008e\b\5\1\2\u008e\u0090\3\2\2\2\u008f\u0089\3\2\2\2")
        buf.write("\u008f\u008c\3\2\2\2\u0090\t\3\2\2\2\u0091\u0092\7\4\2")
        buf.write("\2\u0092\u0093\5\f\7\2\u0093\u0094\7#\2\2\u0094\u0095")
        buf.write("\5$\23\2\u0095\u0096\7\"\2\2\u0096\u0097\b\6\1\2\u0097")
        buf.write("\13\3\2\2\2\u0098\u0099\7\64\2\2\u0099\u009a\7!\2\2\u009a")
        buf.write("\u009b\5\f\7\2\u009b\u009c\b\7\1\2\u009c\u00a0\3\2\2\2")
        buf.write("\u009d\u009e\7\64\2\2\u009e\u00a0\b\7\1\2\u009f\u0098")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\r\3\2\2\2\u00a1\u00a2")
        buf.write("\7\13\2\2\u00a2\u00a3\7\64\2\2\u00a3\u00a4\7\36\2\2\u00a4")
        buf.write("\u00a5\5n8\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7\b\b\1\2\u00a7")
        buf.write("\17\3\2\2\2\u00a8\u00a9\5\22\n\2\u00a9\u00aa\b\t\1\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00ad\b\t\1\2\u00ac\u00a8\3\2\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\21\3\2\2\2\u00ae\u00af\5\24")
        buf.write("\13\2\u00af\u00b0\5\22\n\2\u00b0\u00b1\b\n\1\2\u00b1\u00b6")
        buf.write("\3\2\2\2\u00b2\u00b3\5\24\13\2\u00b3\u00b4\b\n\1\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b2\3\2\2\2")
        buf.write("\u00b6\23\3\2\2\2\u00b7\u00b8\5\26\f\2\u00b8\u00b9\b\13")
        buf.write("\1\2\u00b9\u00be\3\2\2\2\u00ba\u00bb\5\30\r\2\u00bb\u00bc")
        buf.write("\b\13\1\2\u00bc\u00be\3\2\2\2\u00bd\u00b7\3\2\2\2\u00bd")
        buf.write("\u00ba\3\2\2\2\u00be\25\3\2\2\2\u00bf\u00c0\7\22\2\2\u00c0")
        buf.write("\u00c1\7\64\2\2\u00c1\u00c2\7&\2\2\u00c2\u00c3\5\32\16")
        buf.write("\2\u00c3\u00c4\7\'\2\2\u00c4\u00c5\7#\2\2\u00c5\u00c6")
        buf.write("\5&\24\2\u00c6\u00c7\7\"\2\2\u00c7\u00c8\58\35\2\u00c8")
        buf.write("\u00c9\7\"\2\2\u00c9\u00ca\b\f\1\2\u00ca\27\3\2\2\2\u00cb")
        buf.write("\u00cc\7\27\2\2\u00cc\u00cd\7\64\2\2\u00cd\u00ce\7&\2")
        buf.write("\2\u00ce\u00cf\5\32\16\2\u00cf\u00d0\7\'\2\2\u00d0\u00d1")
        buf.write("\7\"\2\2\u00d1\u00d2\58\35\2\u00d2\u00d3\7\"\2\2\u00d3")
        buf.write("\u00d4\b\r\1\2\u00d4\31\3\2\2\2\u00d5\u00d6\5\34\17\2")
        buf.write("\u00d6\u00d7\b\16\1\2\u00d7\u00da\3\2\2\2\u00d8\u00da")
        buf.write("\b\16\1\2\u00d9\u00d5\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00dc\5\36\20\2\u00dc\u00dd\7\"\2\2")
        buf.write("\u00dd\u00de\5\34\17\2\u00de\u00df\b\17\1\2\u00df\u00e4")
        buf.write("\3\2\2\2\u00e0\u00e1\5\36\20\2\u00e1\u00e2\b\17\1\2\u00e2")
        buf.write("\u00e4\3\2\2\2\u00e3\u00db\3\2\2\2\u00e3\u00e0\3\2\2\2")
        buf.write("\u00e4\35\3\2\2\2\u00e5\u00e6\5 \21\2\u00e6\u00e7\b\20")
        buf.write("\1\2\u00e7\u00ec\3\2\2\2\u00e8\u00e9\5\"\22\2\u00e9\u00ea")
        buf.write("\b\20\1\2\u00ea\u00ec\3\2\2\2\u00eb\u00e5\3\2\2\2\u00eb")
        buf.write("\u00e8\3\2\2\2\u00ec\37\3\2\2\2\u00ed\u00ee\7\64\2\2\u00ee")
        buf.write("\u00ef\7#\2\2\u00ef\u00f0\5$\23\2\u00f0\u00f1\b\21\1\2")
        buf.write("\u00f1!\3\2\2\2\u00f2\u00f3\5\f\7\2\u00f3\u00f4\7#\2\2")
        buf.write("\u00f4\u00f5\5$\23\2\u00f5\u00f6\b\22\1\2\u00f6#\3\2\2")
        buf.write("\2\u00f7\u00f8\5&\24\2\u00f8\u00f9\b\23\1\2\u00f9\u00fe")
        buf.write("\3\2\2\2\u00fa\u00fb\5(\25\2\u00fb\u00fc\b\23\1\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00fa\3\2\2\2")
        buf.write("\u00fe%\3\2\2\2\u00ff\u0100\7\b\2\2\u0100\u0108\b\24\1")
        buf.write("\2\u0101\u0102\7\t\2\2\u0102\u0108\b\24\1\2\u0103\u0104")
        buf.write("\7\7\2\2\u0104\u0108\b\24\1\2\u0105\u0106\7\n\2\2\u0106")
        buf.write("\u0108\b\24\1\2\u0107\u00ff\3\2\2\2\u0107\u0101\3\2\2")
        buf.write("\2\u0107\u0103\3\2\2\2\u0107\u0105\3\2\2\2\u0108\'\3\2")
        buf.write("\2\2\u0109\u010a\7\20\2\2\u010a\u010b\5*\26\2\u010b\u010c")
        buf.write("\7\16\2\2\u010c\u010d\5&\24\2\u010d\u010e\b\25\1\2\u010e")
        buf.write(")\3\2\2\2\u010f\u0110\5,\27\2\u0110\u0111\5*\26\2\u0111")
        buf.write("\u0112\b\26\1\2\u0112\u0117\3\2\2\2\u0113\u0114\5,\27")
        buf.write("\2\u0114\u0115\b\26\1\2\u0115\u0117\3\2\2\2\u0116\u010f")
        buf.write("\3\2\2\2\u0116\u0113\3\2\2\2\u0117+\3\2\2\2\u0118\u0119")
        buf.write("\7$\2\2\u0119\u011a\7\60\2\2\u011a\u011b\7%\2\2\u011b")
        buf.write("\u011c\b\27\1\2\u011c-\3\2\2\2\u011d\u011e\5\60\31\2\u011e")
        buf.write("\u011f\b\30\1\2\u011f\u0122\3\2\2\2\u0120\u0122\b\30\1")
        buf.write("\2\u0121\u011d\3\2\2\2\u0121\u0120\3\2\2\2\u0122/\3\2")
        buf.write("\2\2\u0123\u0124\5\62\32\2\u0124\u0125\5\60\31\2\u0125")
        buf.write("\u0126\b\31\1\2\u0126\u012b\3\2\2\2\u0127\u0128\5\62\32")
        buf.write("\2\u0128\u0129\b\31\1\2\u0129\u012b\3\2\2\2\u012a\u0123")
        buf.write("\3\2\2\2\u012a\u0127\3\2\2\2\u012b\61\3\2\2\2\u012c\u012d")
        buf.write("\5\b\5\2\u012d\u012e\b\32\1\2\u012e\u014b\3\2\2\2\u012f")
        buf.write("\u0130\5\64\33\2\u0130\u0131\b\32\1\2\u0131\u014b\3\2")
        buf.write("\2\2\u0132\u0133\58\35\2\u0133\u0134\b\32\1\2\u0134\u014b")
        buf.write("\3\2\2\2\u0135\u0136\5:\36\2\u0136\u0137\b\32\1\2\u0137")
        buf.write("\u014b\3\2\2\2\u0138\u0139\5<\37\2\u0139\u013a\b\32\1")
        buf.write("\2\u013a\u014b\3\2\2\2\u013b\u013c\5@!\2\u013c\u013d\b")
        buf.write("\32\1\2\u013d\u014b\3\2\2\2\u013e\u013f\5B\"\2\u013f\u0140")
        buf.write("\b\32\1\2\u0140\u014b\3\2\2\2\u0141\u0142\5D#\2\u0142")
        buf.write("\u0143\b\32\1\2\u0143\u014b\3\2\2\2\u0144\u0145\5F$\2")
        buf.write("\u0145\u0146\b\32\1\2\u0146\u014b\3\2\2\2\u0147\u0148")
        buf.write("\5H%\2\u0148\u0149\b\32\1\2\u0149\u014b\3\2\2\2\u014a")
        buf.write("\u012c\3\2\2\2\u014a\u012f\3\2\2\2\u014a\u0132\3\2\2\2")
        buf.write("\u014a\u0135\3\2\2\2\u014a\u0138\3\2\2\2\u014a\u013b\3")
        buf.write("\2\2\2\u014a\u013e\3\2\2\2\u014a\u0141\3\2\2\2\u014a\u0144")
        buf.write("\3\2\2\2\u014a\u0147\3\2\2\2\u014b\63\3\2\2\2\u014c\u014d")
        buf.write("\5\66\34\2\u014d\u014e\7\35\2\2\u014e\u014f\5N(\2\u014f")
        buf.write("\u0150\7\"\2\2\u0150\u0151\b\33\1\2\u0151\65\3\2\2\2\u0152")
        buf.write("\u0153\5\\/\2\u0153\u0154\b\34\1\2\u0154\u0158\3\2\2\2")
        buf.write("\u0155\u0156\7\64\2\2\u0156\u0158\b\34\1\2\u0157\u0152")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0158\67\3\2\2\2\u0159\u015a")
        buf.write("\7\5\2\2\u015a\u015b\5.\30\2\u015b\u015c\7\6\2\2\u015c")
        buf.write("\u015d\b\35\1\2\u015d9\3\2\2\2\u015e\u015f\7\25\2\2\u015f")
        buf.write("\u0160\5N(\2\u0160\u0161\7\17\2\2\u0161\u0162\5\62\32")
        buf.write("\2\u0162\u0163\7\31\2\2\u0163\u0164\5\62\32\2\u0164\u0165")
        buf.write("\b\36\1\2\u0165\u016d\3\2\2\2\u0166\u0167\7\25\2\2\u0167")
        buf.write("\u0168\5N(\2\u0168\u0169\7\17\2\2\u0169\u016a\5\62\32")
        buf.write("\2\u016a\u016b\b\36\1\2\u016b\u016d\3\2\2\2\u016c\u015e")
        buf.write("\3\2\2\2\u016c\u0166\3\2\2\2\u016d;\3\2\2\2\u016e\u016f")
        buf.write("\5> \2\u016f\u0170\7\"\2\2\u0170\u0171\b\37\1\2\u0171")
        buf.write("=\3\2\2\2\u0172\u0173\7\64\2\2\u0173\u0174\7&\2\2\u0174")
        buf.write("\u0175\5J&\2\u0175\u0176\7\'\2\2\u0176\u0177\b \1\2\u0177")
        buf.write("?\3\2\2\2\u0178\u0179\7\33\2\2\u0179\u017a\5N(\2\u017a")
        buf.write("\u017b\7\24\2\2\u017b\u017c\5\62\32\2\u017c\u017d\b!\1")
        buf.write("\2\u017dA\3\2\2\2\u017e\u017f\7\24\2\2\u017f\u0180\5.")
        buf.write("\30\2\u0180\u0181\7\33\2\2\u0181\u0182\5N(\2\u0182\u0183")
        buf.write("\7\"\2\2\u0183\u0184\b\"\1\2\u0184C\3\2\2\2\u0185\u0186")
        buf.write("\7\26\2\2\u0186\u0187\5N(\2\u0187\u0188\7\24\2\2\u0188")
        buf.write("\u0189\5\62\32\2\u0189\u018a\b#\1\2\u018aE\3\2\2\2\u018b")
        buf.write("\u018c\7\30\2\2\u018c\u018d\7\"\2\2\u018d\u018e\b$\1\2")
        buf.write("\u018eG\3\2\2\2\u018f\u0190\7\r\2\2\u0190\u0191\7\"\2")
        buf.write("\2\u0191\u0192\b%\1\2\u0192I\3\2\2\2\u0193\u0194\5L\'")
        buf.write("\2\u0194\u0195\b&\1\2\u0195\u0198\3\2\2\2\u0196\u0198")
        buf.write("\b&\1\2\u0197\u0193\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("K\3\2\2\2\u0199\u019a\5N(\2\u019a\u019b\7!\2\2\u019b\u019c")
        buf.write("\5L\'\2\u019c\u019d\b\'\1\2\u019d\u01a2\3\2\2\2\u019e")
        buf.write("\u019f\5N(\2\u019f\u01a0\b\'\1\2\u01a0\u01a2\3\2\2\2\u01a1")
        buf.write("\u0199\3\2\2\2\u01a1\u019e\3\2\2\2\u01a2M\3\2\2\2\u01a3")
        buf.write("\u01a4\b(\1\2\u01a4\u01a5\5P)\2\u01a5\u01a6\b(\1\2\u01a6")
        buf.write("\u01b4\3\2\2\2\u01a7\u01b0\f\4\2\2\u01a8\u01a9\7(\2\2")
        buf.write("\u01a9\u01aa\5P)\2\u01aa\u01ab\b(\1\2\u01ab\u01b1\3\2")
        buf.write("\2\2\u01ac\u01ad\7)\2\2\u01ad\u01ae\5P)\2\u01ae\u01af")
        buf.write("\b(\1\2\u01af\u01b1\3\2\2\2\u01b0\u01a8\3\2\2\2\u01b0")
        buf.write("\u01ac\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01a7\3\2\2\2")
        buf.write("\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3")
        buf.write("\2\2\2\u01b5O\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8")
        buf.write("\b)\1\2\u01b8\u01b9\5R*\2\u01b9\u01ba\b)\1\2\u01ba\u01d0")
        buf.write("\3\2\2\2\u01bb\u01cc\f\4\2\2\u01bc\u01bd\7*\2\2\u01bd")
        buf.write("\u01be\5R*\2\u01be\u01bf\b)\1\2\u01bf\u01cd\3\2\2\2\u01c0")
        buf.write("\u01c1\7+\2\2\u01c1\u01c2\5R*\2\u01c2\u01c3\b)\1\2\u01c3")
        buf.write("\u01cd\3\2\2\2\u01c4\u01c5\7\21\2\2\u01c5\u01c6\5R*\2")
        buf.write("\u01c6\u01c7\b)\1\2\u01c7\u01cd\3\2\2\2\u01c8\u01c9\7")
        buf.write("\32\2\2\u01c9\u01ca\5R*\2\u01ca\u01cb\b)\1\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01bc\3\2\2\2\u01cc\u01c0\3\2\2\2\u01cc")
        buf.write("\u01c4\3\2\2\2\u01cc\u01c8\3\2\2\2\u01cd\u01cf\3\2\2\2")
        buf.write("\u01ce\u01bb\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d0\u01d1\3\2\2\2\u01d1Q\3\2\2\2\u01d2\u01d0")
        buf.write("\3\2\2\2\u01d3\u01d4\b*\1\2\u01d4\u01d5\5T+\2\u01d5\u01d6")
        buf.write("\b*\1\2\u01d6\u01e4\3\2\2\2\u01d7\u01e0\f\4\2\2\u01d8")
        buf.write("\u01d9\7\36\2\2\u01d9\u01da\5T+\2\u01da\u01db\b*\1\2\u01db")
        buf.write("\u01e1\3\2\2\2\u01dc\u01dd\7\37\2\2\u01dd\u01de\5T+\2")
        buf.write("\u01de\u01df\b*\1\2\u01df\u01e1\3\2\2\2\u01e0\u01d8\3")
        buf.write("\2\2\2\u01e0\u01dc\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01d7")
        buf.write("\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5S\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e8\b+\1\2\u01e8\u01e9\5V,\2\u01e9\u01ea\b+\1\2\u01ea")
        buf.write("\u0200\3\2\2\2\u01eb\u01fc\f\4\2\2\u01ec\u01ed\7,\2\2")
        buf.write("\u01ed\u01ee\5V,\2\u01ee\u01ef\b+\1\2\u01ef\u01fd\3\2")
        buf.write("\2\2\u01f0\u01f1\7-\2\2\u01f1\u01f2\5V,\2\u01f2\u01f3")
        buf.write("\b+\1\2\u01f3\u01fd\3\2\2\2\u01f4\u01f5\7.\2\2\u01f5\u01f6")
        buf.write("\5V,\2\u01f6\u01f7\b+\1\2\u01f7\u01fd\3\2\2\2\u01f8\u01f9")
        buf.write("\7/\2\2\u01f9\u01fa\5V,\2\u01fa\u01fb\b+\1\2\u01fb\u01fd")
        buf.write("\3\2\2\2\u01fc\u01ec\3\2\2\2\u01fc\u01f0\3\2\2\2\u01fc")
        buf.write("\u01f4\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fd\u01ff\3\2\2\2")
        buf.write("\u01fe\u01eb\3\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3")
        buf.write("\2\2\2\u0200\u0201\3\2\2\2\u0201U\3\2\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0203\u0204\b,\1\2\u0204\u0205\5X-\2\u0205\u0206")
        buf.write("\b,\1\2\u0206\u020e\3\2\2\2\u0207\u0208\f\4\2\2\u0208")
        buf.write("\u0209\7\23\2\2\u0209\u020a\5X-\2\u020a\u020b\b,\1\2\u020b")
        buf.write("\u020d\3\2\2\2\u020c\u0207\3\2\2\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020fW\3\2\2")
        buf.write("\2\u0210\u020e\3\2\2\2\u0211\u0212\b-\1\2\u0212\u0213")
        buf.write("\5Z.\2\u0213\u0214\b-\1\2\u0214\u021c\3\2\2\2\u0215\u0216")
        buf.write("\f\4\2\2\u0216\u0217\7\f\2\2\u0217\u0218\5Z.\2\u0218\u0219")
        buf.write("\b-\1\2\u0219\u021b\3\2\2\2\u021a\u0215\3\2\2\2\u021b")
        buf.write("\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021dY\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220\7)\2\2")
        buf.write("\u0220\u0221\5Z.\2\u0221\u0222\b.\1\2\u0222\u0228\3\2")
        buf.write("\2\2\u0223\u0224\7\34\2\2\u0224\u0225\5Z.\2\u0225\u0226")
        buf.write("\b.\1\2\u0226\u0228\3\2\2\2\u0227\u021f\3\2\2\2\u0227")
        buf.write("\u0223\3\2\2\2\u0228\u022d\3\2\2\2\u0229\u022a\5^\60\2")
        buf.write("\u022a\u022b\b.\1\2\u022b\u022d\3\2\2\2\u022c\u0227\3")
        buf.write("\2\2\2\u022c\u0229\3\2\2\2\u022d[\3\2\2\2\u022e\u022f")
        buf.write("\7\64\2\2\u022f\u0230\5b\62\2\u0230\u0231\b/\1\2\u0231")
        buf.write("]\3\2\2\2\u0232\u0233\5\\/\2\u0233\u0234\b\60\1\2\u0234")
        buf.write("\u0239\3\2\2\2\u0235\u0236\5`\61\2\u0236\u0237\b\60\1")
        buf.write("\2\u0237\u0239\3\2\2\2\u0238\u0232\3\2\2\2\u0238\u0235")
        buf.write("\3\2\2\2\u0239_\3\2\2\2\u023a\u023b\7&\2\2\u023b\u023c")
        buf.write("\5N(\2\u023c\u023d\7\'\2\2\u023d\u023e\b\61\1\2\u023e")
        buf.write("\u024b\3\2\2\2\u023f\u0240\5n8\2\u0240\u0241\b\61\1\2")
        buf.write("\u0241\u024b\3\2\2\2\u0242\u0243\5f\64\2\u0243\u0244\b")
        buf.write("\61\1\2\u0244\u024b\3\2\2\2\u0245\u0246\7\64\2\2\u0246")
        buf.write("\u024b\b\61\1\2\u0247\u0248\5> \2\u0248\u0249\b\61\1\2")
        buf.write("\u0249\u024b\3\2\2\2\u024a\u023a\3\2\2\2\u024a\u023f\3")
        buf.write("\2\2\2\u024a\u0242\3\2\2\2\u024a\u0245\3\2\2\2\u024a\u0247")
        buf.write("\3\2\2\2\u024ba\3\2\2\2\u024c\u024d\5d\63\2\u024d\u024e")
        buf.write("\5b\62\2\u024e\u024f\b\62\1\2\u024f\u0254\3\2\2\2\u0250")
        buf.write("\u0251\5d\63\2\u0251\u0252\b\62\1\2\u0252\u0254\3\2\2")
        buf.write("\2\u0253\u024c\3\2\2\2\u0253\u0250\3\2\2\2\u0254c\3\2")
        buf.write("\2\2\u0255\u0256\7$\2\2\u0256\u0257\5N(\2\u0257\u0258")
        buf.write("\7%\2\2\u0258\u0259\b\63\1\2\u0259e\3\2\2\2\u025a\u025b")
        buf.write("\7$\2\2\u025b\u025c\5h\65\2\u025c\u025d\7%\2\2\u025d\u025e")
        buf.write("\b\64\1\2\u025eg\3\2\2\2\u025f\u0260\5j\66\2\u0260\u0261")
        buf.write("\b\65\1\2\u0261i\3\2\2\2\u0262\u0263\5l\67\2\u0263\u0264")
        buf.write("\7!\2\2\u0264\u0265\5j\66\2\u0265\u0266\b\66\1\2\u0266")
        buf.write("\u026b\3\2\2\2\u0267\u0268\5l\67\2\u0268\u0269\b\66\1")
        buf.write("\2\u0269\u026b\3\2\2\2\u026a\u0262\3\2\2\2\u026a\u0267")
        buf.write("\3\2\2\2\u026bk\3\2\2\2\u026c\u026d\5f\64\2\u026d\u026e")
        buf.write("\b\67\1\2\u026e\u0273\3\2\2\2\u026f\u0270\5n8\2\u0270")
        buf.write("\u0271\b\67\1\2\u0271\u0273\3\2\2\2\u0272\u026c\3\2\2")
        buf.write("\2\u0272\u026f\3\2\2\2\u0273m\3\2\2\2\u0274\u0275\7\60")
        buf.write("\2\2\u0275\u027d\b8\1\2\u0276\u0277\7\61\2\2\u0277\u027d")
        buf.write("\b8\1\2\u0278\u0279\7\62\2\2\u0279\u027d\b8\1\2\u027a")
        buf.write("\u027b\7\63\2\2\u027b\u027d\b8\1\2\u027c\u0274\3\2\2\2")
        buf.write("\u027c\u0276\3\2\2\2\u027c\u0278\3\2\2\2\u027c\u027a\3")
        buf.write("\2\2\2\u027do\3\2\2\2(~\u0087\u008f\u009f\u00ac\u00b5")
        buf.write("\u00bd\u00d9\u00e3\u00eb\u00fd\u0107\u0116\u0121\u012a")
        buf.write("\u014a\u0157\u016c\u0197\u01a1\u01b0\u01b4\u01cc\u01d0")
        buf.write("\u01e0\u01e4\u01fc\u0200\u020e\u021c\u0227\u022c\u0238")
        buf.write("\u024a\u0253\u026a\u0272\u027c")
        return buf.getvalue()


class Cra2PreParser ( Parser ):

    grammarFileName = "Cra2Pre.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'var'", "'begin'", "'end'", 
                     "'boolean'", "'integer'", "'real'", "'string'", "'const'", 
                     "'and'", "'continue'", "'of'", "'then'", "'array'", 
                     "'div'", "'function'", "'or'", "'do'", "'if'", "'loop'", 
                     "'procedure'", "'break'", "'else'", "'mod'", "'while'", 
                     "'not'", "':='", "'='", "'<>'", "'.'", "','", "';'", 
                     "':'", "'['", "']'", "'('", "')'", "'+'", "'-'", "'*'", 
                     "'/'", "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "VAR", "BEGIN", "END", "BOOLEAN", 
                      "INTEGER", "REAL", "STRING", "CONST", "AND", "CONTINUE", 
                      "OF", "THEN", "ARRAY", "DIV", "FUNCTION", "OR", "DO", 
                      "IF", "LOOP", "PROCEDURE", "BREAK", "ELSE", "MOD", 
                      "WHILE", "NOT", "ASSOPE", "EQUAL", "DIFF", "DOT", 
                      "COMMA", "SEMICOLON", "COLON", "LS", "RS", "LR", "RR", 
                      "ADD", "SUB", "MUL", "DIVV", "LESS", "GREATER", "LE", 
                      "GE", "INTEGER_LIT", "REAL_LIT", "BOOLEAN_LIT", "STRING_LIT", 
                      "ID", "LINE_COMMENT", "BLOCK_COMMENT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_var_decl_part = 1
    RULE_var_decl_list = 2
    RULE_var_const_decl = 3
    RULE_var_decl = 4
    RULE_id_list = 5
    RULE_const_decl = 6
    RULE_func_decl_part = 7
    RULE_func_decl_list = 8
    RULE_func_procedure_decl = 9
    RULE_func_decl = 10
    RULE_procedure_decl = 11
    RULE_param_list = 12
    RULE_params = 13
    RULE_param = 14
    RULE_one_param = 15
    RULE_mul_param = 16
    RULE_ctype = 17
    RULE_primitive_type = 18
    RULE_array_type = 19
    RULE_array_size_list = 20
    RULE_array_size = 21
    RULE_stmt_list = 22
    RULE_stmts = 23
    RULE_stmt = 24
    RULE_assign_stmt = 25
    RULE_lhs = 26
    RULE_block_stmt = 27
    RULE_if_stmt = 28
    RULE_call_stmt = 29
    RULE_call_expr = 30
    RULE_while_stmt = 31
    RULE_do_while_stmt = 32
    RULE_loop_do_stmt = 33
    RULE_break_stmt = 34
    RULE_continue_stmt = 35
    RULE_expr_list = 36
    RULE_exprs = 37
    RULE_expr = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr_8 = 45
    RULE_expr8 = 46
    RULE_expr9 = 47
    RULE_index_operators = 48
    RULE_index_op = 49
    RULE_array_literal = 50
    RULE_array_element_list = 51
    RULE_array_elements = 52
    RULE_array_element = 53
    RULE_literal = 54

    ruleNames =  [ "program", "var_decl_part", "var_decl_list", "var_const_decl", 
                   "var_decl", "id_list", "const_decl", "func_decl_part", 
                   "func_decl_list", "func_procedure_decl", "func_decl", 
                   "procedure_decl", "param_list", "params", "param", "one_param", 
                   "mul_param", "ctype", "primitive_type", "array_type", 
                   "array_size_list", "array_size", "stmt_list", "stmts", 
                   "stmt", "assign_stmt", "lhs", "block_stmt", "if_stmt", 
                   "call_stmt", "call_expr", "while_stmt", "do_while_stmt", 
                   "loop_do_stmt", "break_stmt", "continue_stmt", "expr_list", 
                   "exprs", "expr", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr_8", "expr8", "expr9", "index_operators", 
                   "index_op", "array_literal", "array_element_list", "array_elements", 
                   "array_element", "literal" ]

    EOF = Token.EOF
    PROGRAM=1
    VAR=2
    BEGIN=3
    END=4
    BOOLEAN=5
    INTEGER=6
    REAL=7
    STRING=8
    CONST=9
    AND=10
    CONTINUE=11
    OF=12
    THEN=13
    ARRAY=14
    DIV=15
    FUNCTION=16
    OR=17
    DO=18
    IF=19
    LOOP=20
    PROCEDURE=21
    BREAK=22
    ELSE=23
    MOD=24
    WHILE=25
    NOT=26
    ASSOPE=27
    EQUAL=28
    DIFF=29
    DOT=30
    COMMA=31
    SEMICOLON=32
    COLON=33
    LS=34
    RS=35
    LR=36
    RR=37
    ADD=38
    SUB=39
    MUL=40
    DIVV=41
    LESS=42
    GREATER=43
    LE=44
    GE=45
    INTEGER_LIT=46
    REAL_LIT=47
    BOOLEAN_LIT=48
    STRING_LIT=49
    ID=50
    LINE_COMMENT=51
    BLOCK_COMMENT=52
    WS=53
    ERROR_CHAR=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.v = None # Var_decl_partContext
            self.f = None # Func_decl_partContext
            self.b = None # Block_stmtContext

        def PROGRAM(self):
            return self.getToken(Cra2PreParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def DOT(self):
            return self.getToken(Cra2PreParser.DOT, 0)

        def EOF(self):
            return self.getToken(Cra2PreParser.EOF, 0)

        def var_decl_part(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_decl_partContext,0)


        def func_decl_part(self):
            return self.getTypedRuleContext(Cra2PreParser.Func_decl_partContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Cra2PreParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(Cra2PreParser.PROGRAM)
            self.state = 111
            self.match(Cra2PreParser.ID)
            self.state = 112
            self.match(Cra2PreParser.SEMICOLON)
            self.state = 113
            localctx.v = self.var_decl_part()
            self.state = 114
            localctx.f = self.func_decl_part()
            self.state = 115
            localctx.b = self.block_stmt()
            self.state = 116
            self.match(Cra2PreParser.DOT)
            self.state = 117
            self.match(Cra2PreParser.EOF)
            localctx.s = "[[" + localctx.v.s + "],[" + localctx.f.s + "]," + localctx.b.s + "]. " 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.v = None # Var_decl_listContext

        def var_decl_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_part" ):
                return visitor.visitVar_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_part(self):

        localctx = Cra2PreParser.Var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_decl_part)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.VAR, Cra2PreParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                localctx.v = self.var_decl_list()
                localctx.s = ",".join(localctx.v.results)
                pass
            elif token in [Cra2PreParser.BEGIN, Cra2PreParser.FUNCTION, Cra2PreParser.PROCEDURE]:
                self.enterOuterAlt(localctx, 2)
                localctx.s = ''
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.vc1 = None # Var_const_declContext
            self.vl = None # Var_decl_listContext
            self.vc2 = None # Var_const_declContext

        def var_const_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_const_declContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = Cra2PreParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl_list)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                localctx.vc1 = self.var_const_decl()
                self.state = 127
                localctx.vl = self.var_decl_list()
                localctx.results = [localctx.vc1.s] + localctx.vl.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                localctx.vc2 = self.var_const_decl()
                localctx.results = [localctx.vc2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.v = None # Var_declContext
            self.c = None # Const_declContext

        def var_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Const_declContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_var_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_decl" ):
                return visitor.visitVar_const_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_const_decl(self):

        localctx = Cra2PreParser.Var_const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_const_decl)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                localctx.v = self.var_decl()
                localctx.s=localctx.v.s
                pass
            elif token in [Cra2PreParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                localctx.c = self.const_decl()
                localctx.s=localctx.c.s
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.l = None # Id_listContext
            self.t = None # CtypeContext

        def VAR(self):
            return self.getToken(Cra2PreParser.VAR, 0)

        def COLON(self):
            return self.getToken(Cra2PreParser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def id_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Id_listContext,0)


        def ctype(self):
            return self.getTypedRuleContext(Cra2PreParser.CtypeContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = Cra2PreParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(Cra2PreParser.VAR)
            self.state = 144
            localctx.l = self.id_list()
            self.state = 145
            self.match(Cra2PreParser.COLON)
            self.state = 146
            localctx.t = self.ctype()
            self.state = 147
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = ",".join(f"var({id},{localctx.t.s})" for id in localctx.l.results)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self._ID = None # Token
            self.l = None # Id_listContext

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def COMMA(self):
            return self.getToken(Cra2PreParser.COMMA, 0)

        def id_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Id_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = Cra2PreParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_list)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                localctx._ID = self.match(Cra2PreParser.ID)
                self.state = 151
                self.match(Cra2PreParser.COMMA)
                self.state = 152
                localctx.l = self.id_list()
                localctx.results = [(None if localctx._ID is None else localctx._ID.text)] + localctx.l.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                localctx._ID = self.match(Cra2PreParser.ID)
                localctx.results = [(None if localctx._ID is None else localctx._ID.text)]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.l = None # LiteralContext

        def CONST(self):
            return self.getToken(Cra2PreParser.CONST, 0)

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def EQUAL(self):
            return self.getToken(Cra2PreParser.EQUAL, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def literal(self):
            return self.getTypedRuleContext(Cra2PreParser.LiteralContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = Cra2PreParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(Cra2PreParser.CONST)
            self.state = 160
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 161
            self.match(Cra2PreParser.EQUAL)
            self.state = 162
            localctx.l = self.literal()
            self.state = 163
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"const({(None if localctx._ID is None else localctx._ID.text)},{localctx.l.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.f = None # Func_decl_listContext

        def func_decl_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_func_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_part" ):
                return visitor.visitFunc_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_part(self):

        localctx = Cra2PreParser.Func_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_func_decl_part)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.FUNCTION, Cra2PreParser.PROCEDURE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                localctx.f = self.func_decl_list()
                localctx.s = ",".join(localctx.f.results)
                pass
            elif token in [Cra2PreParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                localctx.s = ''
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.fp1 = None # Func_procedure_declContext
            self.fdl = None # Func_decl_listContext
            self.fp2 = None # Func_procedure_declContext

        def func_procedure_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Func_procedure_declContext,0)


        def func_decl_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Func_decl_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_func_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_list" ):
                return visitor.visitFunc_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_list(self):

        localctx = Cra2PreParser.Func_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl_list)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                localctx.fp1 = self.func_procedure_decl()
                self.state = 173
                localctx.fdl = self.func_decl_list()
                localctx.results = [localctx.fp1.s] + localctx.fdl.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                localctx.fp2 = self.func_procedure_decl()
                localctx.results = [localctx.fp2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_procedure_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.f = None # Func_declContext
            self.p = None # Procedure_declContext

        def func_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Func_declContext,0)


        def procedure_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Procedure_declContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_func_procedure_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_procedure_decl" ):
                return visitor.visitFunc_procedure_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_procedure_decl(self):

        localctx = Cra2PreParser.Func_procedure_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_procedure_decl)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                localctx.f = self.func_decl()
                localctx.s=localctx.f.s
                pass
            elif token in [Cra2PreParser.PROCEDURE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                localctx.p = self.procedure_decl()
                localctx.s=localctx.p.s
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.pl = None # Param_listContext
            self.pt = None # Primitive_typeContext
            self.b = None # Block_stmtContext

        def FUNCTION(self):
            return self.getToken(Cra2PreParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def LR(self):
            return self.getToken(Cra2PreParser.LR, 0)

        def RR(self):
            return self.getToken(Cra2PreParser.RR, 0)

        def COLON(self):
            return self.getToken(Cra2PreParser.COLON, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(Cra2PreParser.SEMICOLON)
            else:
                return self.getToken(Cra2PreParser.SEMICOLON, i)

        def param_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Param_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(Cra2PreParser.Primitive_typeContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = Cra2PreParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(Cra2PreParser.FUNCTION)
            self.state = 190
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 191
            self.match(Cra2PreParser.LR)
            self.state = 192
            localctx.pl = self.param_list()
            self.state = 193
            self.match(Cra2PreParser.RR)
            self.state = 194
            self.match(Cra2PreParser.COLON)
            self.state = 195
            localctx.pt = self.primitive_type()
            self.state = 196
            self.match(Cra2PreParser.SEMICOLON)
            self.state = 197
            localctx.b = self.block_stmt()
            self.state = 198
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"func({(None if localctx._ID is None else localctx._ID.text)},[{localctx.pl.s}],{localctx.pt.s},{localctx.b.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.pl = None # Param_listContext
            self.b = None # Block_stmtContext

        def PROCEDURE(self):
            return self.getToken(Cra2PreParser.PROCEDURE, 0)

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def LR(self):
            return self.getToken(Cra2PreParser.LR, 0)

        def RR(self):
            return self.getToken(Cra2PreParser.RR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(Cra2PreParser.SEMICOLON)
            else:
                return self.getToken(Cra2PreParser.SEMICOLON, i)

        def param_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Param_listContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_procedure_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_decl" ):
                return visitor.visitProcedure_decl(self)
            else:
                return visitor.visitChildren(self)




    def procedure_decl(self):

        localctx = Cra2PreParser.Procedure_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_procedure_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(Cra2PreParser.PROCEDURE)
            self.state = 202
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 203
            self.match(Cra2PreParser.LR)
            self.state = 204
            localctx.pl = self.param_list()
            self.state = 205
            self.match(Cra2PreParser.RR)
            self.state = 206
            self.match(Cra2PreParser.SEMICOLON)
            self.state = 207
            localctx.b = self.block_stmt()
            self.state = 208
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"proc({(None if localctx._ID is None else localctx._ID.text)},[{localctx.pl.s}],{localctx.b.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.p = None # ParamsContext

        def params(self):
            return self.getTypedRuleContext(Cra2PreParser.ParamsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = Cra2PreParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                localctx.p = self.params()
                localctx.s = ",".join(localctx.p.results)
                pass
            elif token in [Cra2PreParser.RR]:
                self.enterOuterAlt(localctx, 2)
                localctx.s = ''
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.p1 = None # ParamContext
            self.ps = None # ParamsContext
            self.p2 = None # ParamContext

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def param(self):
            return self.getTypedRuleContext(Cra2PreParser.ParamContext,0)


        def params(self):
            return self.getTypedRuleContext(Cra2PreParser.ParamsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = Cra2PreParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                localctx.p1 = self.param()
                self.state = 218
                self.match(Cra2PreParser.SEMICOLON)
                self.state = 219
                localctx.ps = self.params()
                localctx.results = [localctx.p1.s] + localctx.ps.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                localctx.p2 = self.param()
                localctx.results = [localctx.p2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.o = None # One_paramContext
            self.m = None # Mul_paramContext

        def one_param(self):
            return self.getTypedRuleContext(Cra2PreParser.One_paramContext,0)


        def mul_param(self):
            return self.getTypedRuleContext(Cra2PreParser.Mul_paramContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = Cra2PreParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                localctx.o = self.one_param()
                localctx.s=localctx.o.s
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                localctx.m = self.mul_param()
                localctx.s=localctx.m.s
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.t = None # CtypeContext

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def COLON(self):
            return self.getToken(Cra2PreParser.COLON, 0)

        def ctype(self):
            return self.getTypedRuleContext(Cra2PreParser.CtypeContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_one_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_param" ):
                return visitor.visitOne_param(self)
            else:
                return visitor.visitChildren(self)




    def one_param(self):

        localctx = Cra2PreParser.One_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_one_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 236
            self.match(Cra2PreParser.COLON)
            self.state = 237
            localctx.t = self.ctype()
            localctx.s = f"par({(None if localctx._ID is None else localctx._ID.text)},{localctx.t.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.l = None # Id_listContext
            self.t = None # CtypeContext

        def COLON(self):
            return self.getToken(Cra2PreParser.COLON, 0)

        def id_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Id_listContext,0)


        def ctype(self):
            return self.getTypedRuleContext(Cra2PreParser.CtypeContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_mul_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_param" ):
                return visitor.visitMul_param(self)
            else:
                return visitor.visitChildren(self)




    def mul_param(self):

        localctx = Cra2PreParser.Mul_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mul_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            localctx.l = self.id_list()
            self.state = 241
            self.match(Cra2PreParser.COLON)
            self.state = 242
            localctx.t = self.ctype()
            localctx.s = ",".join(f"par({id},{localctx.t.s})" for id in localctx.l.results)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.p = None # Primitive_typeContext
            self.a = None # Array_typeContext

        def primitive_type(self):
            return self.getTypedRuleContext(Cra2PreParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_typeContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_ctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCtype" ):
                return visitor.visitCtype(self)
            else:
                return visitor.visitChildren(self)




    def ctype(self):

        localctx = Cra2PreParser.CtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ctype)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.BOOLEAN, Cra2PreParser.INTEGER, Cra2PreParser.REAL, Cra2PreParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                localctx.p = self.primitive_type()
                localctx.s = localctx.p.s
                pass
            elif token in [Cra2PreParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                localctx.a = self.array_type()
                localctx.s = localctx.a.s
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None

        def INTEGER(self):
            return self.getToken(Cra2PreParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(Cra2PreParser.REAL, 0)

        def BOOLEAN(self):
            return self.getToken(Cra2PreParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(Cra2PreParser.STRING, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = Cra2PreParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primitive_type)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(Cra2PreParser.INTEGER)
                localctx.s = "integer" 
                pass
            elif token in [Cra2PreParser.REAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(Cra2PreParser.REAL)
                localctx.s = "real" 
                pass
            elif token in [Cra2PreParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(Cra2PreParser.BOOLEAN)
                localctx.s = "boolean" 
                pass
            elif token in [Cra2PreParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(Cra2PreParser.STRING)
                localctx.s = "string" 
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.a = None # Array_size_listContext
            self.t = None # Primitive_typeContext

        def ARRAY(self):
            return self.getToken(Cra2PreParser.ARRAY, 0)

        def OF(self):
            return self.getToken(Cra2PreParser.OF, 0)

        def array_size_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_size_listContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(Cra2PreParser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = Cra2PreParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(Cra2PreParser.ARRAY)
            self.state = 264
            localctx.a = self.array_size_list()
            self.state = 265
            self.match(Cra2PreParser.OF)
            self.state = 266
            localctx.t = self.primitive_type()
            size = ",".join(localctx.a.results)
            localctx.s = f"arr([{size}],{localctx.t.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_size_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.as1 = None # Array_sizeContext
            self.asl = None # Array_size_listContext
            self.as2 = None # Array_sizeContext

        def array_size(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_sizeContext,0)


        def array_size_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_size_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_size_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size_list" ):
                return visitor.visitArray_size_list(self)
            else:
                return visitor.visitChildren(self)




    def array_size_list(self):

        localctx = Cra2PreParser.Array_size_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_size_list)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                localctx.as1 = self.array_size()
                self.state = 270
                localctx.asl = self.array_size_list()
                localctx.results = [localctx.as1.s] + localctx.asl.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                localctx.as2 = self.array_size()
                localctx.results = [localctx.as2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._INTEGER_LIT = None # Token

        def LS(self):
            return self.getToken(Cra2PreParser.LS, 0)

        def INTEGER_LIT(self):
            return self.getToken(Cra2PreParser.INTEGER_LIT, 0)

        def RS(self):
            return self.getToken(Cra2PreParser.RS, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = Cra2PreParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(Cra2PreParser.LS)
            self.state = 279
            localctx._INTEGER_LIT = self.match(Cra2PreParser.INTEGER_LIT)
            self.state = 280
            self.match(Cra2PreParser.RS)
            localctx.s = (None if localctx._INTEGER_LIT is None else localctx._INTEGER_LIT.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.st = None # StmtsContext

        def stmts(self):
            return self.getTypedRuleContext(Cra2PreParser.StmtsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = Cra2PreParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt_list)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                localctx.st = self.stmts()
                localctx.s = ",".join(localctx.st.results)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                localctx.s = ''
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.st1 = None # StmtContext
            self.ss = None # StmtsContext
            self.st2 = None # StmtContext

        def stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.StmtContext,0)


        def stmts(self):
            return self.getTypedRuleContext(Cra2PreParser.StmtsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmts" ):
                return visitor.visitStmts(self)
            else:
                return visitor.visitChildren(self)




    def stmts(self):

        localctx = Cra2PreParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmts)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                localctx.st1 = self.stmt()
                self.state = 290
                localctx.ss = self.stmts()
                localctx.results = [localctx.st1.s] + localctx.ss.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                localctx.st2 = self.stmt()
                localctx.results = [localctx.st2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.t1 = None # Var_const_declContext
            self.t2 = None # Assign_stmtContext
            self.t3 = None # Block_stmtContext
            self.t4 = None # If_stmtContext
            self.t5 = None # Call_stmtContext
            self.t6 = None # While_stmtContext
            self.t7 = None # Do_while_stmtContext
            self.t8 = None # Loop_do_stmtContext
            self.t9 = None # Break_stmtContext
            self.t10 = None # Continue_stmtContext

        def var_const_decl(self):
            return self.getTypedRuleContext(Cra2PreParser.Var_const_declContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Assign_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Block_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.If_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Call_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Do_while_stmtContext,0)


        def loop_do_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Loop_do_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.Continue_stmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = Cra2PreParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                localctx.t1 = self.var_const_decl()
                localctx.s = localctx.t1.s
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                localctx.t2 = self.assign_stmt()
                localctx.s = localctx.t2.s
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                localctx.t3 = self.block_stmt()
                localctx.s = localctx.t3.s
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                localctx.t4 = self.if_stmt()
                localctx.s = localctx.t4.s
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
                localctx.t5 = self.call_stmt()
                localctx.s = localctx.t5.s
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 313
                localctx.t6 = self.while_stmt()
                localctx.s = localctx.t6.s
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                localctx.t7 = self.do_while_stmt()
                localctx.s = localctx.t7.s
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 319
                localctx.t8 = self.loop_do_stmt()
                localctx.s = localctx.t8.s
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 322
                localctx.t9 = self.break_stmt()
                localctx.s = localctx.t9.s
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 325
                localctx.t10 = self.continue_stmt()
                localctx.s = localctx.t10.s
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.l = None # LhsContext
            self.e = None # ExprContext

        def ASSOPE(self):
            return self.getToken(Cra2PreParser.ASSOPE, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def lhs(self):
            return self.getTypedRuleContext(Cra2PreParser.LhsContext,0)


        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = Cra2PreParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            localctx.l = self.lhs()
            self.state = 331
            self.match(Cra2PreParser.ASSOPE)
            self.state = 332
            localctx.e = self.expr(0)
            self.state = 333
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"assign({localctx.l.s},{localctx.e.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # Expr_8Context
            self._ID = None # Token

        def expr_8(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr_8Context,0)


        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = Cra2PreParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                localctx.e = self.expr_8()
                localctx.s = localctx.e.s
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                localctx._ID = self.match(Cra2PreParser.ID)
                localctx.s = (None if localctx._ID is None else localctx._ID.text)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.st = None # Stmt_listContext

        def BEGIN(self):
            return self.getToken(Cra2PreParser.BEGIN, 0)

        def END(self):
            return self.getToken(Cra2PreParser.END, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = Cra2PreParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(Cra2PreParser.BEGIN)
            self.state = 344
            localctx.st = self.stmt_list()
            self.state = 345
            self.match(Cra2PreParser.END)
            localctx.s = f"[{localctx.st.s}]"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # ExprContext
            self.s1 = None # StmtContext
            self.s2 = None # StmtContext
            self.e2 = None # ExprContext
            self.s3 = None # StmtContext

        def IF(self):
            return self.getToken(Cra2PreParser.IF, 0)

        def THEN(self):
            return self.getToken(Cra2PreParser.THEN, 0)

        def ELSE(self):
            return self.getToken(Cra2PreParser.ELSE, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Cra2PreParser.StmtContext)
            else:
                return self.getTypedRuleContext(Cra2PreParser.StmtContext,i)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = Cra2PreParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_stmt)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(Cra2PreParser.IF)
                self.state = 349
                localctx.e1 = self.expr(0)
                self.state = 350
                self.match(Cra2PreParser.THEN)
                self.state = 351
                localctx.s1 = self.stmt()
                self.state = 352
                self.match(Cra2PreParser.ELSE)
                self.state = 353
                localctx.s2 = self.stmt()
                localctx.s = f"if({localctx.e1.s},{localctx.s1.s},{localctx.s2.s})"
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(Cra2PreParser.IF)
                self.state = 357
                localctx.e2 = self.expr(0)
                self.state = 358
                self.match(Cra2PreParser.THEN)
                self.state = 359
                localctx.s3 = self.stmt()
                localctx.s = f"if({localctx.e2.s},{localctx.s3.s})"
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.c = None # Call_exprContext

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def call_expr(self):
            return self.getTypedRuleContext(Cra2PreParser.Call_exprContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = Cra2PreParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            localctx.c = self.call_expr()
            self.state = 365
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = localctx.c.s
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.e = None # Expr_listContext

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def LR(self):
            return self.getToken(Cra2PreParser.LR, 0)

        def RR(self):
            return self.getToken(Cra2PreParser.RR, 0)

        def expr_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = Cra2PreParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 369
            self.match(Cra2PreParser.LR)
            self.state = 370
            localctx.e = self.expr_list()
            self.state = 371
            self.match(Cra2PreParser.RR)
            localctx.s = f"call({(None if localctx._ID is None else localctx._ID.text)},[{localctx.e.s}])"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # ExprContext
            self.st = None # StmtContext

        def WHILE(self):
            return self.getToken(Cra2PreParser.WHILE, 0)

        def DO(self):
            return self.getToken(Cra2PreParser.DO, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.StmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = Cra2PreParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(Cra2PreParser.WHILE)
            self.state = 375
            localctx.e = self.expr(0)
            self.state = 376
            self.match(Cra2PreParser.DO)
            self.state = 377
            localctx.st = self.stmt()
            localctx.s = f"while({localctx.e.s},{localctx.st.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.l = None # Stmt_listContext
            self.e = None # ExprContext

        def DO(self):
            return self.getToken(Cra2PreParser.DO, 0)

        def WHILE(self):
            return self.getToken(Cra2PreParser.WHILE, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Stmt_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = Cra2PreParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(Cra2PreParser.DO)
            self.state = 381
            localctx.l = self.stmt_list()
            self.state = 382
            self.match(Cra2PreParser.WHILE)
            self.state = 383
            localctx.e = self.expr(0)
            self.state = 384
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"do([{localctx.l.s}],{localctx.e.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_do_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # ExprContext
            self.st = None # StmtContext

        def LOOP(self):
            return self.getToken(Cra2PreParser.LOOP, 0)

        def DO(self):
            return self.getToken(Cra2PreParser.DO, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(Cra2PreParser.StmtContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_loop_do_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_do_stmt" ):
                return visitor.visitLoop_do_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_do_stmt(self):

        localctx = Cra2PreParser.Loop_do_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_loop_do_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(Cra2PreParser.LOOP)
            self.state = 388
            localctx.e = self.expr(0)
            self.state = 389
            self.match(Cra2PreParser.DO)
            self.state = 390
            localctx.st = self.stmt()
            localctx.s = f"loop({localctx.e.s},{localctx.st.s})"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None

        def BREAK(self):
            return self.getToken(Cra2PreParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = Cra2PreParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(Cra2PreParser.BREAK)
            self.state = 394
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"break(null)"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None

        def CONTINUE(self):
            return self.getToken(Cra2PreParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(Cra2PreParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = Cra2PreParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(Cra2PreParser.CONTINUE)
            self.state = 398
            self.match(Cra2PreParser.SEMICOLON)
            localctx.s = f"continue(null)"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # ExprsContext

        def exprs(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = Cra2PreParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr_list)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.NOT, Cra2PreParser.LS, Cra2PreParser.LR, Cra2PreParser.SUB, Cra2PreParser.INTEGER_LIT, Cra2PreParser.REAL_LIT, Cra2PreParser.BOOLEAN_LIT, Cra2PreParser.STRING_LIT, Cra2PreParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                localctx.e = self.exprs()
                localctx.s = ",".join(localctx.e.results)
                pass
            elif token in [Cra2PreParser.RR]:
                self.enterOuterAlt(localctx, 2)
                localctx.s = ""
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.e1 = None # ExprContext
            self.es = None # ExprsContext
            self.e2 = None # ExprContext

        def COMMA(self):
            return self.getToken(Cra2PreParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = Cra2PreParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exprs)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                localctx.e1 = self.expr(0)
                self.state = 408
                self.match(Cra2PreParser.COMMA)
                self.state = 409
                localctx.es = self.exprs()
                localctx.results = [localctx.e1.s] + localctx.es.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                localctx.e2 = self.expr(0)
                localctx.results = [localctx.e2.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # ExprContext
            self.e = None # Expr2Context
            self.e2 = None # Expr2Context

        def expr2(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr2Context,0)


        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def ADD(self):
            return self.getToken(Cra2PreParser.ADD, 0)

        def SUB(self):
            return self.getToken(Cra2PreParser.SUB, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            localctx.e = self.expr2(0)
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.ExprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 421
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [Cra2PreParser.ADD]:
                        self.state = 422
                        self.match(Cra2PreParser.ADD)
                        self.state = 423
                        localctx.e2 = self.expr2(0)
                        localctx.s = f"add({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.SUB]:
                        self.state = 426
                        self.match(Cra2PreParser.SUB)
                        self.state = 427
                        localctx.e2 = self.expr2(0)
                        localctx.s = f"sub({localctx.e1.s},{localctx.e2.s})"
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr2Context
            self.e = None # Expr3Context
            self.e2 = None # Expr3Context

        def expr3(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr2Context,0)


        def MUL(self):
            return self.getToken(Cra2PreParser.MUL, 0)

        def DIVV(self):
            return self.getToken(Cra2PreParser.DIVV, 0)

        def DIV(self):
            return self.getToken(Cra2PreParser.DIV, 0)

        def MOD(self):
            return self.getToken(Cra2PreParser.MOD, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            localctx.e = self.expr3(0)
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.Expr2Context(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 441
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 458
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [Cra2PreParser.MUL]:
                        self.state = 442
                        self.match(Cra2PreParser.MUL)
                        self.state = 443
                        localctx.e2 = self.expr3(0)
                        localctx.s = f"times({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.DIVV]:
                        self.state = 446
                        self.match(Cra2PreParser.DIVV)
                        self.state = 447
                        localctx.e2 = self.expr3(0)
                        localctx.s = f"rdiv({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.DIV]:
                        self.state = 450
                        self.match(Cra2PreParser.DIV)
                        self.state = 451
                        localctx.e2 = self.expr3(0)
                        localctx.s = f"idiv({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.MOD]:
                        self.state = 454
                        self.match(Cra2PreParser.MOD)
                        self.state = 455
                        localctx.e2 = self.expr3(0)
                        localctx.s = f"imod({localctx.e1.s},{localctx.e2.s})"
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr3Context
            self.e = None # Expr4Context
            self.e2 = None # Expr4Context

        def expr4(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr3Context,0)


        def EQUAL(self):
            return self.getToken(Cra2PreParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(Cra2PreParser.DIFF, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            localctx.e = self.expr4(0)
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.Expr3Context(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 469
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 478
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [Cra2PreParser.EQUAL]:
                        self.state = 470
                        self.match(Cra2PreParser.EQUAL)
                        self.state = 471
                        localctx.e2 = self.expr4(0)
                        localctx.s = f"eql({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.DIFF]:
                        self.state = 474
                        self.match(Cra2PreParser.DIFF)
                        self.state = 475
                        localctx.e2 = self.expr4(0)
                        localctx.s = f"ne({localctx.e1.s},{localctx.e2.s})"
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr4Context
            self.e = None # Expr5Context
            self.e2 = None # Expr5Context

        def expr5(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr4Context,0)


        def LESS(self):
            return self.getToken(Cra2PreParser.LESS, 0)

        def GREATER(self):
            return self.getToken(Cra2PreParser.GREATER, 0)

        def LE(self):
            return self.getToken(Cra2PreParser.LE, 0)

        def GE(self):
            return self.getToken(Cra2PreParser.GE, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            localctx.e = self.expr5(0)
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 510
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.Expr4Context(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 489
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 506
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [Cra2PreParser.LESS]:
                        self.state = 490
                        self.match(Cra2PreParser.LESS)
                        self.state = 491
                        localctx.e2 = self.expr5(0)
                        localctx.s = f"less({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.GREATER]:
                        self.state = 494
                        self.match(Cra2PreParser.GREATER)
                        self.state = 495
                        localctx.e2 = self.expr5(0)
                        localctx.s = f"greater({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.LE]:
                        self.state = 498
                        self.match(Cra2PreParser.LE)
                        self.state = 499
                        localctx.e2 = self.expr5(0)
                        localctx.s = f"le({localctx.e1.s},{localctx.e2.s})"
                        pass
                    elif token in [Cra2PreParser.GE]:
                        self.state = 502
                        self.match(Cra2PreParser.GE)
                        self.state = 503
                        localctx.e2 = self.expr5(0)
                        localctx.s = f"ge({localctx.e1.s},{localctx.e2.s})"
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 512
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr5Context
            self.e = None # Expr6Context
            self.e2 = None # Expr6Context

        def expr6(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr6Context,0)


        def OR(self):
            return self.getToken(Cra2PreParser.OR, 0)

        def expr5(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr5Context,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            localctx.e = self.expr6(0)
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 524
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.Expr5Context(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 517
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 518
                    self.match(Cra2PreParser.OR)
                    self.state = 519
                    localctx.e2 = self.expr6(0)
                    localctx.s = f"bor({localctx.e1.s},{localctx.e2.s})" 
                self.state = 526
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr6Context
            self.e = None # Expr7Context
            self.e2 = None # Expr7Context

        def expr7(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr7Context,0)


        def AND(self):
            return self.getToken(Cra2PreParser.AND, 0)

        def expr6(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr6Context,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Cra2PreParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            localctx.e = self.expr7()
            localctx.s = localctx.e.s
            self._ctx.stop = self._input.LT(-1)
            self.state = 538
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Cra2PreParser.Expr6Context(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 531
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 532
                    self.match(Cra2PreParser.AND)
                    self.state = 533
                    localctx.e2 = self.expr7()
                    localctx.s = f"band({localctx.e1.s},{localctx.e2.s})" 
                self.state = 540
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr7Context
            self.e2 = None # Expr7Context
            self.e = None # Expr8Context

        def SUB(self):
            return self.getToken(Cra2PreParser.SUB, 0)

        def NOT(self):
            return self.getToken(Cra2PreParser.NOT, 0)

        def expr7(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr7Context,0)


        def expr8(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr8Context,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = Cra2PreParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr7)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.NOT, Cra2PreParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [Cra2PreParser.SUB]:
                    self.state = 541
                    self.match(Cra2PreParser.SUB)
                    self.state = 542
                    localctx.e1 = self.expr7()
                    localctx.s = f"sub({localctx.e1.s})"
                    pass
                elif token in [Cra2PreParser.NOT]:
                    self.state = 545
                    self.match(Cra2PreParser.NOT)
                    self.state = 546
                    localctx.e2 = self.expr7()
                    localctx.s = f"bnot({localctx.e2.s})"
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [Cra2PreParser.LS, Cra2PreParser.LR, Cra2PreParser.INTEGER_LIT, Cra2PreParser.REAL_LIT, Cra2PreParser.BOOLEAN_LIT, Cra2PreParser.STRING_LIT, Cra2PreParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                localctx.e = self.expr8()
                localctx.s = localctx.e.s
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._ID = None # Token
            self.i = None # Index_operatorsContext

        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(Cra2PreParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr_8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_8" ):
                return visitor.visitExpr_8(self)
            else:
                return visitor.visitChildren(self)




    def expr_8(self):

        localctx = Cra2PreParser.Expr_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr_8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            localctx._ID = self.match(Cra2PreParser.ID)
            self.state = 557
            localctx.i = self.index_operators()
            temp = ",".join(localctx.i.results)
            localctx.s = f"ele({(None if localctx._ID is None else localctx._ID.text)},[{temp}])"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e1 = None # Expr_8Context
            self.e2 = None # Expr9Context

        def expr_8(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr_8Context,0)


        def expr9(self):
            return self.getTypedRuleContext(Cra2PreParser.Expr9Context,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = Cra2PreParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr8)
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                localctx.e1 = self.expr_8()
                localctx.s = localctx.e1.s
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 563
                localctx.e2 = self.expr9()
                localctx.s = localctx.e2.s
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # ExprContext
            self.l = None # LiteralContext
            self.a = None # Array_literalContext
            self._ID = None # Token
            self.c = None # Call_exprContext

        def LR(self):
            return self.getToken(Cra2PreParser.LR, 0)

        def RR(self):
            return self.getToken(Cra2PreParser.RR, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(Cra2PreParser.LiteralContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_literalContext,0)


        def ID(self):
            return self.getToken(Cra2PreParser.ID, 0)

        def call_expr(self):
            return self.getTypedRuleContext(Cra2PreParser.Call_exprContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = Cra2PreParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr9)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.match(Cra2PreParser.LR)
                self.state = 569
                localctx.e = self.expr(0)
                self.state = 570
                self.match(Cra2PreParser.RR)
                localctx.s = localctx.e.s
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                localctx.l = self.literal()
                localctx.s = localctx.l.s
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 576
                localctx.a = self.array_literal()
                localctx.s = localctx.a.s
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 579
                localctx._ID = self.match(Cra2PreParser.ID)
                localctx.s = (None if localctx._ID is None else localctx._ID.text)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 581
                localctx.c = self.call_expr()
                localctx.s = localctx.c.s
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.io = None # Index_opContext
            self.ios = None # Index_operatorsContext
            self.i = None # Index_opContext

        def index_op(self):
            return self.getTypedRuleContext(Cra2PreParser.Index_opContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(Cra2PreParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = Cra2PreParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_index_operators)
        try:
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                localctx.io = self.index_op()
                self.state = 587
                localctx.ios = self.index_operators()
                localctx.results = [localctx.io.s] + localctx.ios.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                localctx.i = self.index_op()
                localctx.results = [localctx.i.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.e = None # ExprContext

        def LS(self):
            return self.getToken(Cra2PreParser.LS, 0)

        def RS(self):
            return self.getToken(Cra2PreParser.RS, 0)

        def expr(self):
            return self.getTypedRuleContext(Cra2PreParser.ExprContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = Cra2PreParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(Cra2PreParser.LS)
            self.state = 596
            localctx.e = self.expr(0)
            self.state = 597
            self.match(Cra2PreParser.RS)
            localctx.s = localctx.e.s
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.a = None # Array_element_listContext

        def LS(self):
            return self.getToken(Cra2PreParser.LS, 0)

        def RS(self):
            return self.getToken(Cra2PreParser.RS, 0)

        def array_element_list(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_element_listContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = Cra2PreParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(Cra2PreParser.LS)
            self.state = 601
            localctx.a = self.array_element_list()
            self.state = 602
            self.match(Cra2PreParser.RS)
            localctx.s = f"array([{localctx.a.s}])"
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.a = None # Array_elementsContext

        def array_elements(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_list" ):
                return visitor.visitArray_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_element_list(self):

        localctx = Cra2PreParser.Array_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_array_element_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            localctx.a = self.array_elements()
            localctx.s = ",".join(localctx.a.results)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.results = None
            self.ae = None # Array_elementContext
            self.aes = None # Array_elementsContext
            self.a = None # Array_elementContext

        def COMMA(self):
            return self.getToken(Cra2PreParser.COMMA, 0)

        def array_element(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_elementContext,0)


        def array_elements(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = Cra2PreParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_elements)
        try:
            self.state = 616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                localctx.ae = self.array_element()
                self.state = 609
                self.match(Cra2PreParser.COMMA)
                self.state = 610
                localctx.aes = self.array_elements()
                localctx.results = [localctx.ae.s] + localctx.aes.results
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                localctx.a = self.array_element()
                localctx.results = [localctx.a.s]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self.a = None # Array_literalContext
            self.l = None # LiteralContext

        def array_literal(self):
            return self.getTypedRuleContext(Cra2PreParser.Array_literalContext,0)


        def literal(self):
            return self.getTypedRuleContext(Cra2PreParser.LiteralContext,0)


        def getRuleIndex(self):
            return Cra2PreParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = Cra2PreParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_array_element)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                localctx.a = self.array_literal()
                localctx.s = localctx.a.s
                pass
            elif token in [Cra2PreParser.INTEGER_LIT, Cra2PreParser.REAL_LIT, Cra2PreParser.BOOLEAN_LIT, Cra2PreParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                localctx.l = self.literal()
                localctx.s = localctx.l.s
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._INTEGER_LIT = None # Token
            self._REAL_LIT = None # Token
            self._BOOLEAN_LIT = None # Token
            self._STRING_LIT = None # Token

        def INTEGER_LIT(self):
            return self.getToken(Cra2PreParser.INTEGER_LIT, 0)

        def REAL_LIT(self):
            return self.getToken(Cra2PreParser.REAL_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(Cra2PreParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(Cra2PreParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return Cra2PreParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = Cra2PreParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_literal)
        try:
            self.state = 634
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Cra2PreParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                localctx._INTEGER_LIT = self.match(Cra2PreParser.INTEGER_LIT)
                localctx.s = (None if localctx._INTEGER_LIT is None else localctx._INTEGER_LIT.text)
                pass
            elif token in [Cra2PreParser.REAL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                localctx._REAL_LIT = self.match(Cra2PreParser.REAL_LIT)
                localctx.s = (None if localctx._REAL_LIT is None else localctx._REAL_LIT.text)
                pass
            elif token in [Cra2PreParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 630
                localctx._BOOLEAN_LIT = self.match(Cra2PreParser.BOOLEAN_LIT)
                localctx.s = (None if localctx._BOOLEAN_LIT is None else localctx._BOOLEAN_LIT.text)
                pass
            elif token in [Cra2PreParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 632
                localctx._STRING_LIT = self.match(Cra2PreParser.STRING_LIT)
                temp = (None if localctx._STRING_LIT is None else localctx._STRING_LIT.text)
                res = "\"" + temp.replace("''", "\\\'").replace("\"", "\\\"") + "\""
                localctx.s = f"str({res})"
                	
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.expr_sempred
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
        self._predicates[42] = self.expr5_sempred
        self._predicates[43] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




