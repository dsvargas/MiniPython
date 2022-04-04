# Generated from C:/Users/dilan/OneDrive - Estudiantes ITCR/Semestre I 2022/Compiladores/Proyecto/Proyecto/MiniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0202\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\7")
        buf.write(";\u0163\n;\f;\16;\u0166\13;\3<\3<\3<\3<\3<\3<\3<\6<\u016f")
        buf.write("\n<\r<\16<\u0170\3<\5<\u0174\n<\3=\3=\7=\u0178\n=\f=\16")
        buf.write("=\u017b\13=\3=\3=\3>\3>\7>\u0181\n>\f>\16>\u0184\13>\3")
        buf.write("?\3?\5?\u0188\n?\3@\3@\3@\5@\u018d\n@\3@\5@\u0190\n@\3")
        buf.write("@\5@\u0193\n@\3@\3@\3@\5@\u0198\n@\5@\u019a\n@\3A\3A\3")
        buf.write("A\3A\3A\3B\5B\u01a2\nB\3B\6B\u01a5\nB\rB\16B\u01a6\3B")
        buf.write("\3B\5B\u01ab\nB\3B\7B\u01ae\nB\fB\16B\u01b1\13B\5B\u01b3")
        buf.write("\nB\3B\3B\3B\5B\u01b8\nB\3B\7B\u01bb\nB\fB\16B\u01be\13")
        buf.write("B\5B\u01c0\nB\3C\3C\3D\3D\5D\u01c6\nD\3D\7D\u01c9\nD\f")
        buf.write("D\16D\u01cc\13D\3E\3E\3E\3E\3F\3F\5F\u01d4\nF\3F\3F\3")
        buf.write("G\3G\3H\5H\u01db\nH\3I\3I\3I\3I\3I\7I\u01e2\nI\fI\16I")
        buf.write("\u01e5\13I\3I\3I\3I\3I\3I\3I\3J\3J\6J\u01ef\nJ\rJ\16J")
        buf.write("\u01f0\3J\3J\3K\3K\3K\3K\3L\5L\u01fa\nL\3L\3L\7L\u01fe")
        buf.write("\nL\fL\16L\u0201\13L\3\u01e3\2M\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091C\u0093D\u0095E\u0097F\3\2\17\n\2$$))^^ddhhpp")
        buf.write("ttvv\6\2\f\f\17\17))^^\5\2\62;CHch\3\2$$\4\2ZZzz\3\2\62")
        buf.write(";\4\2RRrr\4\2--//\4\2GGgg\5\2C\\aac|\4\2\f\f\16\17\6\2")
        buf.write("\13\f\16\17\"\"--\4\2\13\13\"\"\2\u0216\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0091\3\2\2\2\2")
        buf.write("\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099")
        buf.write("\3\2\2\2\5\u009c\3\2\2\2\7\u00a1\3\2\2\2\t\u00a7\3\2\2")
        buf.write("\2\13\u00aa\3\2\2\2\r\u00b0\3\2\2\2\17\u00b4\3\2\2\2\21")
        buf.write("\u00b7\3\2\2\2\23\u00bd\3\2\2\2\25\u00c1\3\2\2\2\27\u00c5")
        buf.write("\3\2\2\2\31\u00cb\3\2\2\2\33\u00cf\3\2\2\2\35\u00d8\3")
        buf.write("\2\2\2\37\u00df\3\2\2\2!\u00e5\3\2\2\2#\u00ed\3\2\2\2")
        buf.write("%\u00f2\3\2\2\2\'\u00f6\3\2\2\2)\u00fd\3\2\2\2+\u0104")
        buf.write("\3\2\2\2-\u0108\3\2\2\2/\u010a\3\2\2\2\61\u010c\3\2\2")
        buf.write("\2\63\u010e\3\2\2\2\65\u0110\3\2\2\2\67\u0113\3\2\2\2")
        buf.write("9\u0115\3\2\2\2;\u0118\3\2\2\2=\u011a\3\2\2\2?\u011d\3")
        buf.write("\2\2\2A\u0120\3\2\2\2C\u0122\3\2\2\2E\u0125\3\2\2\2G\u0128")
        buf.write("\3\2\2\2I\u012a\3\2\2\2K\u012d\3\2\2\2M\u012f\3\2\2\2")
        buf.write("O\u0132\3\2\2\2Q\u0135\3\2\2\2S\u0137\3\2\2\2U\u013a\3")
        buf.write("\2\2\2W\u013c\3\2\2\2Y\u013f\3\2\2\2[\u0141\3\2\2\2]\u0143")
        buf.write("\3\2\2\2_\u0146\3\2\2\2a\u0149\3\2\2\2c\u014b\3\2\2\2")
        buf.write("e\u014e\3\2\2\2g\u0150\3\2\2\2i\u0153\3\2\2\2k\u0155\3")
        buf.write("\2\2\2m\u0157\3\2\2\2o\u0159\3\2\2\2q\u015b\3\2\2\2s\u015d")
        buf.write("\3\2\2\2u\u015f\3\2\2\2w\u0173\3\2\2\2y\u0175\3\2\2\2")
        buf.write("{\u017e\3\2\2\2}\u0187\3\2\2\2\177\u0199\3\2\2\2\u0081")
        buf.write("\u019b\3\2\2\2\u0083\u01bf\3\2\2\2\u0085\u01c1\3\2\2\2")
        buf.write("\u0087\u01c3\3\2\2\2\u0089\u01cd\3\2\2\2\u008b\u01d1\3")
        buf.write("\2\2\2\u008d\u01d7\3\2\2\2\u008f\u01da\3\2\2\2\u0091\u01dc")
        buf.write("\3\2\2\2\u0093\u01ec\3\2\2\2\u0095\u01f4\3\2\2\2\u0097")
        buf.write("\u01f9\3\2\2\2\u0099\u009a\7k\2\2\u009a\u009b\7h\2\2\u009b")
        buf.write("\4\3\2\2\2\u009c\u009d\7g\2\2\u009d\u009e\7n\2\2\u009e")
        buf.write("\u009f\7u\2\2\u009f\u00a0\7g\2\2\u00a0\6\3\2\2\2\u00a1")
        buf.write("\u00a2\7y\2\2\u00a2\u00a3\7j\2\2\u00a3\u00a4\7k\2\2\u00a4")
        buf.write("\u00a5\7n\2\2\u00a5\u00a6\7g\2\2\u00a6\b\3\2\2\2\u00a7")
        buf.write("\u00a8\7f\2\2\u00a8\u00a9\7q\2\2\u00a9\n\3\2\2\2\u00aa")
        buf.write("\u00ab\7d\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7g\2\2\u00ad")
        buf.write("\u00ae\7c\2\2\u00ae\u00af\7m\2\2\u00af\f\3\2\2\2\u00b0")
        buf.write("\u00b1\7h\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7t\2\2\u00b3")
        buf.write("\16\3\2\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6")
        buf.write("\20\3\2\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7g\2\2\u00b9")
        buf.write("\u00ba\7i\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc")
        buf.write("\22\3\2\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7p\2\2\u00bf")
        buf.write("\u00c0\7f\2\2\u00c0\24\3\2\2\2\u00c1\u00c2\7n\2\2\u00c2")
        buf.write("\u00c3\7g\2\2\u00c3\u00c4\7v\2\2\u00c4\26\3\2\2\2\u00c5")
        buf.write("\u00c6\7e\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7p\2\2\u00c8")
        buf.write("\u00c9\7u\2\2\u00c9\u00ca\7v\2\2\u00ca\30\3\2\2\2\u00cb")
        buf.write("\u00cc\7x\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7t\2\2\u00ce")
        buf.write("\32\3\2\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7q\2\2\u00d1")
        buf.write("\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7p\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7\7g\2\2\u00d7")
        buf.write("\34\3\2\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write("\u00db\7v\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\36\3\2\2\2\u00df\u00e0\7r\2\2\u00e0")
        buf.write("\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4 \3\2\2\2\u00e5\u00e6\7r\2\2\u00e6")
        buf.write("\u00e7\7c\2\2\u00e7\u00e8\7e\2\2\u00e8\u00e9\7m\2\2\u00e9")
        buf.write("\u00ea\7c\2\2\u00ea\u00eb\7i\2\2\u00eb\u00ec\7g\2\2\u00ec")
        buf.write("\"\3\2\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7{\2\2\u00ef")
        buf.write("\u00f0\7r\2\2\u00f0\u00f1\7g\2\2\u00f1$\3\2\2\2\u00f2")
        buf.write("\u00f3\7f\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7h\2\2\u00f5")
        buf.write("&\3\2\2\2\u00f6\u00f7\7u\2\2\u00f7\u00f8\7v\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7e\2\2\u00fb")
        buf.write("\u00fc\7v\2\2\u00fc(\3\2\2\2\u00fd\u00fe\7c\2\2\u00fe")
        buf.write("\u00ff\7r\2\2\u00ff\u0100\7r\2\2\u0100\u0101\7g\2\2\u0101")
        buf.write("\u0102\7p\2\2\u0102\u0103\7f\2\2\u0103*\3\2\2\2\u0104")
        buf.write("\u0105\7n\2\2\u0105\u0106\7g\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write(",\3\2\2\2\u0108\u0109\7.\2\2\u0109.\3\2\2\2\u010a\u010b")
        buf.write("\7=\2\2\u010b\60\3\2\2\2\u010c\u010d\7\60\2\2\u010d\62")
        buf.write("\3\2\2\2\u010e\u010f\7<\2\2\u010f\64\3\2\2\2\u0110\u0111")
        buf.write("\7<\2\2\u0111\u0112\7?\2\2\u0112\66\3\2\2\2\u0113\u0114")
        buf.write("\7?\2\2\u01148\3\2\2\2\u0115\u0116\7?\2\2\u0116\u0117")
        buf.write("\7?\2\2\u0117:\3\2\2\2\u0118\u0119\7-\2\2\u0119<\3\2\2")
        buf.write("\2\u011a\u011b\7-\2\2\u011b\u011c\7-\2\2\u011c>\3\2\2")
        buf.write("\2\u011d\u011e\7-\2\2\u011e\u011f\7?\2\2\u011f@\3\2\2")
        buf.write("\2\u0120\u0121\7/\2\2\u0121B\3\2\2\2\u0122\u0123\7/\2")
        buf.write("\2\u0123\u0124\7/\2\2\u0124D\3\2\2\2\u0125\u0126\7/\2")
        buf.write("\2\u0126\u0127\7?\2\2\u0127F\3\2\2\2\u0128\u0129\7\61")
        buf.write("\2\2\u0129H\3\2\2\2\u012a\u012b\7\61\2\2\u012b\u012c\7")
        buf.write("?\2\2\u012cJ\3\2\2\2\u012d\u012e\7,\2\2\u012eL\3\2\2\2")
        buf.write("\u012f\u0130\7,\2\2\u0130\u0131\7?\2\2\u0131N\3\2\2\2")
        buf.write("\u0132\u0133\7#\2\2\u0133\u0134\7?\2\2\u0134P\3\2\2\2")
        buf.write("\u0135\u0136\7#\2\2\u0136R\3\2\2\2\u0137\u0138\7@\2\2")
        buf.write("\u0138\u0139\7?\2\2\u0139T\3\2\2\2\u013a\u013b\7@\2\2")
        buf.write("\u013bV\3\2\2\2\u013c\u013d\7>\2\2\u013d\u013e\7?\2\2")
        buf.write("\u013eX\3\2\2\2\u013f\u0140\7>\2\2\u0140Z\3\2\2\2\u0141")
        buf.write("\u0142\7\'\2\2\u0142\\\3\2\2\2\u0143\u0144\7\'\2\2\u0144")
        buf.write("\u0145\7?\2\2\u0145^\3\2\2\2\u0146\u0147\7(\2\2\u0147")
        buf.write("\u0148\7(\2\2\u0148`\3\2\2\2\u0149\u014a\7(\2\2\u014a")
        buf.write("b\3\2\2\2\u014b\u014c\7~\2\2\u014c\u014d\7~\2\2\u014d")
        buf.write("d\3\2\2\2\u014e\u014f\7~\2\2\u014ff\3\2\2\2\u0150\u0151")
        buf.write("\7~\2\2\u0151\u0152\7?\2\2\u0152h\3\2\2\2\u0153\u0154")
        buf.write("\7*\2\2\u0154j\3\2\2\2\u0155\u0156\7+\2\2\u0156l\3\2\2")
        buf.write("\2\u0157\u0158\7]\2\2\u0158n\3\2\2\2\u0159\u015a\7_\2")
        buf.write("\2\u015ap\3\2\2\2\u015b\u015c\7}\2\2\u015cr\3\2\2\2\u015d")
        buf.write("\u015e\7\177\2\2\u015et\3\2\2\2\u015f\u0164\5\u008fH\2")
        buf.write("\u0160\u0163\5\u008fH\2\u0161\u0163\5\u0085C\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165v\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0167\u0168\7^\2\2\u0168\u0174\t\2\2\2")
        buf.write("\u0169\u016a\7)\2\2\u016a\u016b\n\3\2\2\u016b\u0174\7")
        buf.write(")\2\2\u016c\u016e\7^\2\2\u016d\u016f\7w\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\t\4\2\2")
        buf.write("\u0173\u0167\3\2\2\2\u0173\u0169\3\2\2\2\u0173\u016c\3")
        buf.write("\2\2\2\u0174x\3\2\2\2\u0175\u0179\7$\2\2\u0176\u0178\n")
        buf.write("\5\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017c\u017d\7$\2\2\u017dz\3\2\2\2\u017e")
        buf.write("\u0182\5\u0085C\2\u017f\u0181\5\u0085C\2\u0180\u017f\3")
        buf.write("\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183|\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0188")
        buf.write("\5\177@\2\u0186\u0188\5\u0081A\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188~\3\2\2\2\u0189\u0192\5\u0087D\2\u018a")
        buf.write("\u018c\7\60\2\2\u018b\u018d\5\u0087D\2\u018c\u018b\3\2")
        buf.write("\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u0190")
        buf.write("\5\u008bF\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u0193\5\u008bF\2\u0192\u018a\3\2")
        buf.write("\2\2\u0192\u0191\3\2\2\2\u0193\u019a\3\2\2\2\u0194\u0195")
        buf.write("\7\60\2\2\u0195\u0197\5\u0087D\2\u0196\u0198\5\u008bF")
        buf.write("\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019a")
        buf.write("\3\2\2\2\u0199\u0189\3\2\2\2\u0199\u0194\3\2\2\2\u019a")
        buf.write("\u0080\3\2\2\2\u019b\u019c\7\62\2\2\u019c\u019d\t\6\2")
        buf.write("\2\u019d\u019e\5\u0083B\2\u019e\u019f\5\u0089E\2\u019f")
        buf.write("\u0082\3\2\2\2\u01a0\u01a2\7a\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a5\5")
        buf.write("\u008dG\2\u01a4\u01a1\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01b2\3\2\2\2")
        buf.write("\u01a8\u01af\7\60\2\2\u01a9\u01ab\7a\2\2\u01aa\u01a9\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae")
        buf.write("\5\u008dG\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b3\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b2\u01a8\3\2\2\2\u01b2\u01b3\3")
        buf.write("\2\2\2\u01b3\u01c0\3\2\2\2\u01b4\u01b5\7\60\2\2\u01b5")
        buf.write("\u01bc\5\u008dG\2\u01b6\u01b8\7a\2\2\u01b7\u01b6\3\2\2")
        buf.write("\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\5\u008dG\2\u01ba\u01b7\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c0\3\2\2\2")
        buf.write("\u01be\u01bc\3\2\2\2\u01bf\u01a4\3\2\2\2\u01bf\u01b4\3")
        buf.write("\2\2\2\u01c0\u0084\3\2\2\2\u01c1\u01c2\t\7\2\2\u01c2\u0086")
        buf.write("\3\2\2\2\u01c3\u01ca\t\7\2\2\u01c4\u01c6\7a\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c9\t\7\2\2\u01c8\u01c5\3\2\2\2\u01c9\u01cc\3")
        buf.write("\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u0088")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\t\b\2\2\u01ce")
        buf.write("\u01cf\t\t\2\2\u01cf\u01d0\5\u0087D\2\u01d0\u008a\3\2")
        buf.write("\2\2\u01d1\u01d3\t\n\2\2\u01d2\u01d4\t\t\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d6\5\u0087D\2\u01d6\u008c\3\2\2\2\u01d7\u01d8\t\4")
        buf.write("\2\2\u01d8\u008e\3\2\2\2\u01d9\u01db\t\13\2\2\u01da\u01d9")
        buf.write("\3\2\2\2\u01db\u0090\3\2\2\2\u01dc\u01dd\7$\2\2\u01dd")
        buf.write("\u01de\7$\2\2\u01de\u01df\7$\2\2\u01df\u01e3\3\2\2\2\u01e0")
        buf.write("\u01e2\13\2\2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e5\3\2\2")
        buf.write("\2\u01e3\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e6")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7\7$\2\2\u01e7")
        buf.write("\u01e8\7$\2\2\u01e8\u01e9\7$\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01eb\bI\2\2\u01eb\u0092\3\2\2\2\u01ec\u01ee\7%\2\2\u01ed")
        buf.write("\u01ef\n\f\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\3")
        buf.write("\2\2\2\u01f2\u01f3\bJ\2\2\u01f3\u0094\3\2\2\2\u01f4\u01f5")
        buf.write("\t\r\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\bK\2\2\u01f7")
        buf.write("\u0096\3\2\2\2\u01f8\u01fa\7\17\2\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01ff")
        buf.write("\7\f\2\2\u01fc\u01fe\t\16\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0098\3\2\2\2\u0201\u01ff\3\2\2\2\37\2\u0162\u0164")
        buf.write("\u0170\u0173\u0179\u0182\u0187\u018c\u018f\u0192\u0197")
        buf.write("\u0199\u01a1\u01a6\u01aa\u01af\u01b2\u01b7\u01bc\u01bf")
        buf.write("\u01c5\u01ca\u01d3\u01da\u01e3\u01f0\u01f9\u01ff\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class miParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    WHILE = 3
    DO = 4
    BREAK = 5
    FOR = 6
    IN = 7
    BEGIN = 8
    END = 9
    LET = 10
    CONST = 11
    VAR = 12
    CONTINUE = 13
    RETURN = 14
    PRINT = 15
    PACKAGE = 16
    TYPE = 17
    DEF = 18
    STRUCT = 19
    APPEND = 20
    LEN = 21
    COMA = 22
    PyCOMA = 23
    PUNTO = 24
    DOSPUNTOS = 25
    DOSPUNTOSIGUAL = 26
    ASYGN = 27
    EQUALS = 28
    SUM = 29
    SUM2 = 30
    SUMIGUAL = 31
    RES = 32
    RES2 = 33
    RESIGUAL = 34
    DIV = 35
    DIVIGUAL = 36
    MUL = 37
    MULIGUAL = 38
    DIF = 39
    ADMIRACION = 40
    MAYORIGUAL = 41
    MAYOR = 42
    MENORIGUAL = 43
    MENOR = 44
    PORCENTAJE = 45
    PORCENTAJEIGUAL = 46
    AND2 = 47
    AND = 48
    OR2 = 49
    OR = 50
    ORIGUAL = 51
    PARENTESISIZQ = 52
    PARENTESISDER = 53
    BRACKETIZQ = 54
    BRACKETDER = 55
    LLAVEIZQ = 56
    LLAVEDER = 57
    ID = 58
    CHAR_LITERAL = 59
    RAWSTRINGLITERAL = 60
    INTLITERAL = 61
    FLOATLITERAL = 62
    DECIMAL_FLOAT_LIT = 63
    HEX_FLOAT_LIT = 64
    BLOK_COMMENT = 65
    COMMENT = 66
    WS = 67
    NEWLINE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'do'", "'break'", "'for'", "'in'", 
            "'begin'", "'end'", "'let'", "'const'", "'var'", "'continue'", 
            "'return'", "'print'", "'package'", "'type'", "'def'", "'struct'", 
            "'append'", "'len'", "','", "';'", "'.'", "':'", "':='", "'='", 
            "'=='", "'+'", "'++'", "'+='", "'-'", "'--'", "'-='", "'/'", 
            "'/='", "'*'", "'*='", "'!='", "'!'", "'>='", "'>'", "'<='", 
            "'<'", "'%'", "'%='", "'&&'", "'&'", "'||'", "'|'", "'|='", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "WHILE", "DO", "BREAK", "FOR", "IN", "BEGIN", 
            "END", "LET", "CONST", "VAR", "CONTINUE", "RETURN", "PRINT", 
            "PACKAGE", "TYPE", "DEF", "STRUCT", "APPEND", "LEN", "COMA", 
            "PyCOMA", "PUNTO", "DOSPUNTOS", "DOSPUNTOSIGUAL", "ASYGN", "EQUALS", 
            "SUM", "SUM2", "SUMIGUAL", "RES", "RES2", "RESIGUAL", "DIV", 
            "DIVIGUAL", "MUL", "MULIGUAL", "DIF", "ADMIRACION", "MAYORIGUAL", 
            "MAYOR", "MENORIGUAL", "MENOR", "PORCENTAJE", "PORCENTAJEIGUAL", 
            "AND2", "AND", "OR2", "OR", "ORIGUAL", "PARENTESISIZQ", "PARENTESISDER", 
            "BRACKETIZQ", "BRACKETDER", "LLAVEIZQ", "LLAVEDER", "ID", "CHAR_LITERAL", 
            "RAWSTRINGLITERAL", "INTLITERAL", "FLOATLITERAL", "DECIMAL_FLOAT_LIT", 
            "HEX_FLOAT_LIT", "BLOK_COMMENT", "COMMENT", "WS", "NEWLINE" ]

    ruleNames = [ "IF", "ELSE", "WHILE", "DO", "BREAK", "FOR", "IN", "BEGIN", 
                  "END", "LET", "CONST", "VAR", "CONTINUE", "RETURN", "PRINT", 
                  "PACKAGE", "TYPE", "DEF", "STRUCT", "APPEND", "LEN", "COMA", 
                  "PyCOMA", "PUNTO", "DOSPUNTOS", "DOSPUNTOSIGUAL", "ASYGN", 
                  "EQUALS", "SUM", "SUM2", "SUMIGUAL", "RES", "RES2", "RESIGUAL", 
                  "DIV", "DIVIGUAL", "MUL", "MULIGUAL", "DIF", "ADMIRACION", 
                  "MAYORIGUAL", "MAYOR", "MENORIGUAL", "MENOR", "PORCENTAJE", 
                  "PORCENTAJEIGUAL", "AND2", "AND", "OR2", "OR", "ORIGUAL", 
                  "PARENTESISIZQ", "PARENTESISDER", "BRACKETIZQ", "BRACKETDER", 
                  "LLAVEIZQ", "LLAVEDER", "ID", "CHAR_LITERAL", "RAWSTRINGLITERAL", 
                  "INTLITERAL", "FLOATLITERAL", "DECIMAL_FLOAT_LIT", "HEX_FLOAT_LIT", 
                  "HEX_MANTISSA", "DIGIT", "DECIMALS", "HEX_EXPONENT", "EXPONENT", 
                  "HEX_DIGIT", "LETTER", "BLOK_COMMENT", "COMMENT", "WS", 
                  "NEWLINE" ]

    grammarFileName = "miParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: miParserLexer = lexer

        def pull_token(self):
            return super(miParserLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NEWLINE, miParserParser.INDENT, miParserParser.DEDENT, False)
        return self.denter.next_token()


