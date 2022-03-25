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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\7;\u0161")
        buf.write("\n;\f;\16;\u0164\13;\3<\3<\3<\3<\3<\3<\3<\6<\u016d\n<")
        buf.write("\r<\16<\u016e\3<\5<\u0172\n<\3=\3=\7=\u0176\n=\f=\16=")
        buf.write("\u0179\13=\3=\3=\3>\3>\7>\u017f\n>\f>\16>\u0182\13>\3")
        buf.write("?\3?\3?\5?\u0187\n?\3?\5?\u018a\n?\3?\5?\u018d\n?\3?\3")
        buf.write("?\3?\5?\u0192\n?\5?\u0194\n?\3@\3@\5@\u0198\n@\3A\3A\3")
        buf.write("A\3A\3A\3B\5B\u01a0\nB\3B\6B\u01a3\nB\rB\16B\u01a4\3B")
        buf.write("\3B\5B\u01a9\nB\3B\7B\u01ac\nB\fB\16B\u01af\13B\5B\u01b1")
        buf.write("\nB\3B\3B\3B\5B\u01b6\nB\3B\7B\u01b9\nB\fB\16B\u01bc\13")
        buf.write("B\5B\u01be\nB\3C\3C\3D\3D\5D\u01c4\nD\3D\7D\u01c7\nD\f")
        buf.write("D\16D\u01ca\13D\3E\3E\3E\3E\3F\3F\5F\u01d2\nF\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\7I\u01dc\nI\fI\16I\u01df\13I\3I\3I\3")
        buf.write("J\3J\3J\3J\3K\5K\u01e8\nK\3K\3K\7K\u01ec\nK\fK\16K\u01ef")
        buf.write("\13K\2\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091C\u0093D\u0095")
        buf.write("E\3\2\17\n\2$$))^^ddhhppttvv\6\2\f\f\17\17))^^\5\2\62")
        buf.write(";CHch\3\2$$\4\2ZZzz\3\2\62;\4\2RRrr\4\2--//\4\2GGgg\6")
        buf.write("\2C\\aac|\u0082\u0101\4\2\f\f\16\17\6\2\13\f\17\17\"\"")
        buf.write("--\4\2\13\13\"\"\2\u0203\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2")
        buf.write("\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u009a\3\2\2\2\7\u009f")
        buf.write("\3\2\2\2\t\u00a5\3\2\2\2\13\u00a8\3\2\2\2\r\u00ae\3\2")
        buf.write("\2\2\17\u00b2\3\2\2\2\21\u00b5\3\2\2\2\23\u00bb\3\2\2")
        buf.write("\2\25\u00bf\3\2\2\2\27\u00c3\3\2\2\2\31\u00c9\3\2\2\2")
        buf.write("\33\u00cd\3\2\2\2\35\u00d6\3\2\2\2\37\u00dd\3\2\2\2!\u00e3")
        buf.write("\3\2\2\2#\u00eb\3\2\2\2%\u00f0\3\2\2\2\'\u00f4\3\2\2\2")
        buf.write(")\u00fb\3\2\2\2+\u0102\3\2\2\2-\u0106\3\2\2\2/\u0108\3")
        buf.write("\2\2\2\61\u010a\3\2\2\2\63\u010c\3\2\2\2\65\u010e\3\2")
        buf.write("\2\2\67\u0111\3\2\2\29\u0114\3\2\2\2;\u0116\3\2\2\2=\u0119")
        buf.write("\3\2\2\2?\u011c\3\2\2\2A\u011e\3\2\2\2C\u0121\3\2\2\2")
        buf.write("E\u0124\3\2\2\2G\u0126\3\2\2\2I\u0129\3\2\2\2K\u012b\3")
        buf.write("\2\2\2M\u012e\3\2\2\2O\u0130\3\2\2\2Q\u0133\3\2\2\2S\u0135")
        buf.write("\3\2\2\2U\u0138\3\2\2\2W\u013a\3\2\2\2Y\u013d\3\2\2\2")
        buf.write("[\u013f\3\2\2\2]\u0141\3\2\2\2_\u0144\3\2\2\2a\u0147\3")
        buf.write("\2\2\2c\u0149\3\2\2\2e\u014c\3\2\2\2g\u014e\3\2\2\2i\u0151")
        buf.write("\3\2\2\2k\u0153\3\2\2\2m\u0155\3\2\2\2o\u0157\3\2\2\2")
        buf.write("q\u0159\3\2\2\2s\u015b\3\2\2\2u\u015d\3\2\2\2w\u0171\3")
        buf.write("\2\2\2y\u0173\3\2\2\2{\u017c\3\2\2\2}\u0193\3\2\2\2\177")
        buf.write("\u0197\3\2\2\2\u0081\u0199\3\2\2\2\u0083\u01bd\3\2\2\2")
        buf.write("\u0085\u01bf\3\2\2\2\u0087\u01c1\3\2\2\2\u0089\u01cb\3")
        buf.write("\2\2\2\u008b\u01cf\3\2\2\2\u008d\u01d5\3\2\2\2\u008f\u01d7")
        buf.write("\3\2\2\2\u0091\u01d9\3\2\2\2\u0093\u01e2\3\2\2\2\u0095")
        buf.write("\u01e7\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099")
        buf.write("\4\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c\7n\2\2\u009c")
        buf.write("\u009d\7u\2\2\u009d\u009e\7g\2\2\u009e\6\3\2\2\2\u009f")
        buf.write("\u00a0\7y\2\2\u00a0\u00a1\7j\2\2\u00a1\u00a2\7k\2\2\u00a2")
        buf.write("\u00a3\7n\2\2\u00a3\u00a4\7g\2\2\u00a4\b\3\2\2\2\u00a5")
        buf.write("\u00a6\7f\2\2\u00a6\u00a7\7q\2\2\u00a7\n\3\2\2\2\u00a8")
        buf.write("\u00a9\7d\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7g\2\2\u00ab")
        buf.write("\u00ac\7c\2\2\u00ac\u00ad\7m\2\2\u00ad\f\3\2\2\2\u00ae")
        buf.write("\u00af\7h\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write("\16\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7p\2\2\u00b4")
        buf.write("\20\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7\7g\2\2\u00b7")
        buf.write("\u00b8\7i\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7p\2\2\u00ba")
        buf.write("\22\3\2\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7p\2\2\u00bd")
        buf.write("\u00be\7f\2\2\u00be\24\3\2\2\2\u00bf\u00c0\7n\2\2\u00c0")
        buf.write("\u00c1\7g\2\2\u00c1\u00c2\7v\2\2\u00c2\26\3\2\2\2\u00c3")
        buf.write("\u00c4\7e\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7p\2\2\u00c6")
        buf.write("\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8\30\3\2\2\2\u00c9")
        buf.write("\u00ca\7x\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7t\2\2\u00cc")
        buf.write("\32\3\2\2\2\u00cd\u00ce\7e\2\2\u00ce\u00cf\7q\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\34\3\2\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\36\3\2\2\2\u00dd\u00de\7r\2\2\u00de")
        buf.write("\u00df\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1")
        buf.write("\u00e2\7v\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7r\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7e\2\2\u00e6\u00e7\7m\2\2\u00e7")
        buf.write("\u00e8\7c\2\2\u00e8\u00e9\7i\2\2\u00e9\u00ea\7g\2\2\u00ea")
        buf.write("\"\3\2\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7{\2\2\u00ed")
        buf.write("\u00ee\7r\2\2\u00ee\u00ef\7g\2\2\u00ef$\3\2\2\2\u00f0")
        buf.write("\u00f1\7f\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7h\2\2\u00f3")
        buf.write("&\3\2\2\2\u00f4\u00f5\7u\2\2\u00f5\u00f6\7v\2\2\u00f6")
        buf.write("\u00f7\7t\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7e\2\2\u00f9")
        buf.write("\u00fa\7v\2\2\u00fa(\3\2\2\2\u00fb\u00fc\7c\2\2\u00fc")
        buf.write("\u00fd\7r\2\2\u00fd\u00fe\7r\2\2\u00fe\u00ff\7g\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\u0101\7f\2\2\u0101*\3\2\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7g\2\2\u0104\u0105\7p\2\2\u0105")
        buf.write(",\3\2\2\2\u0106\u0107\7.\2\2\u0107.\3\2\2\2\u0108\u0109")
        buf.write("\7=\2\2\u0109\60\3\2\2\2\u010a\u010b\7\60\2\2\u010b\62")
        buf.write("\3\2\2\2\u010c\u010d\7<\2\2\u010d\64\3\2\2\2\u010e\u010f")
        buf.write("\7<\2\2\u010f\u0110\7?\2\2\u0110\66\3\2\2\2\u0111\u0112")
        buf.write("\7?\2\2\u0112\u0113\7?\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115:\3\2\2\2\u0116\u0117\7-\2\2\u0117\u0118")
        buf.write("\7-\2\2\u0118<\3\2\2\2\u0119\u011a\7-\2\2\u011a\u011b")
        buf.write("\7?\2\2\u011b>\3\2\2\2\u011c\u011d\7-\2\2\u011d@\3\2\2")
        buf.write("\2\u011e\u011f\7/\2\2\u011f\u0120\7/\2\2\u0120B\3\2\2")
        buf.write("\2\u0121\u0122\7/\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2")
        buf.write("\2\u0124\u0125\7/\2\2\u0125F\3\2\2\2\u0126\u0127\7\61")
        buf.write("\2\2\u0127\u0128\7?\2\2\u0128H\3\2\2\2\u0129\u012a\7\61")
        buf.write("\2\2\u012aJ\3\2\2\2\u012b\u012c\7,\2\2\u012c\u012d\7?")
        buf.write("\2\2\u012dL\3\2\2\2\u012e\u012f\7,\2\2\u012fN\3\2\2\2")
        buf.write("\u0130\u0131\7#\2\2\u0131\u0132\7?\2\2\u0132P\3\2\2\2")
        buf.write("\u0133\u0134\7#\2\2\u0134R\3\2\2\2\u0135\u0136\7@\2\2")
        buf.write("\u0136\u0137\7?\2\2\u0137T\3\2\2\2\u0138\u0139\7@\2\2")
        buf.write("\u0139V\3\2\2\2\u013a\u013b\7>\2\2\u013b\u013c\7?\2\2")
        buf.write("\u013cX\3\2\2\2\u013d\u013e\7>\2\2\u013eZ\3\2\2\2\u013f")
        buf.write("\u0140\7\'\2\2\u0140\\\3\2\2\2\u0141\u0142\7\'\2\2\u0142")
        buf.write("\u0143\7?\2\2\u0143^\3\2\2\2\u0144\u0145\7(\2\2\u0145")
        buf.write("\u0146\7(\2\2\u0146`\3\2\2\2\u0147\u0148\7(\2\2\u0148")
        buf.write("b\3\2\2\2\u0149\u014a\7~\2\2\u014a\u014b\7~\2\2\u014b")
        buf.write("d\3\2\2\2\u014c\u014d\7~\2\2\u014df\3\2\2\2\u014e\u014f")
        buf.write("\7~\2\2\u014f\u0150\7?\2\2\u0150h\3\2\2\2\u0151\u0152")
        buf.write("\7*\2\2\u0152j\3\2\2\2\u0153\u0154\7+\2\2\u0154l\3\2\2")
        buf.write("\2\u0155\u0156\7]\2\2\u0156n\3\2\2\2\u0157\u0158\7_\2")
        buf.write("\2\u0158p\3\2\2\2\u0159\u015a\7}\2\2\u015ar\3\2\2\2\u015b")
        buf.write("\u015c\7\177\2\2\u015ct\3\2\2\2\u015d\u0162\5\u008fH\2")
        buf.write("\u015e\u0161\5\u008fH\2\u015f\u0161\5\u0085C\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163v\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0166\7^\2\2\u0166\u0172\t\2\2\2")
        buf.write("\u0167\u0168\7)\2\2\u0168\u0169\n\3\2\2\u0169\u0172\7")
        buf.write(")\2\2\u016a\u016c\7^\2\2\u016b\u016d\7w\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\t\4\2\2")
        buf.write("\u0171\u0165\3\2\2\2\u0171\u0167\3\2\2\2\u0171\u016a\3")
        buf.write("\2\2\2\u0172x\3\2\2\2\u0173\u0177\7$\2\2\u0174\u0176\n")
        buf.write("\5\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u017a\u017b\7$\2\2\u017bz\3\2\2\2\u017c")
        buf.write("\u0180\5\u0085C\2\u017d\u017f\5\u0085C\2\u017e\u017d\3")
        buf.write("\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181|\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u018c")
        buf.write("\5\u0087D\2\u0184\u0186\7\60\2\2\u0185\u0187\5\u0087D")
        buf.write("\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189")
        buf.write("\3\2\2\2\u0188\u018a\5\u008bF\2\u0189\u0188\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u018d\5\u008b")
        buf.write("F\2\u018c\u0184\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u0194")
        buf.write("\3\2\2\2\u018e\u018f\7\60\2\2\u018f\u0191\5\u0087D\2\u0190")
        buf.write("\u0192\5\u008bF\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2")
        buf.write("\2\2\u0192\u0194\3\2\2\2\u0193\u0183\3\2\2\2\u0193\u018e")
        buf.write("\3\2\2\2\u0194~\3\2\2\2\u0195\u0198\5}?\2\u0196\u0198")
        buf.write("\5\u0081A\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u0080\3\2\2\2\u0199\u019a\7\62\2\2\u019a\u019b\t\6\2")
        buf.write("\2\u019b\u019c\5\u0083B\2\u019c\u019d\5\u0089E\2\u019d")
        buf.write("\u0082\3\2\2\2\u019e\u01a0\7a\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\5")
        buf.write("\u008dG\2\u01a2\u019f\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01b0\3\2\2\2")
        buf.write("\u01a6\u01ad\7\60\2\2\u01a7\u01a9\7a\2\2\u01a8\u01a7\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac")
        buf.write("\5\u008dG\2\u01ab\u01a8\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01b0\u01a6\3\2\2\2\u01b0\u01b1\3")
        buf.write("\2\2\2\u01b1\u01be\3\2\2\2\u01b2\u01b3\7\60\2\2\u01b3")
        buf.write("\u01ba\5\u008dG\2\u01b4\u01b6\7a\2\2\u01b5\u01b4\3\2\2")
        buf.write("\2\u01b5\u01b6\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b9")
        buf.write("\5\u008dG\2\u01b8\u01b5\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2")
        buf.write("\u01bc\u01ba\3\2\2\2\u01bd\u01a2\3\2\2\2\u01bd\u01b2\3")
        buf.write("\2\2\2\u01be\u0084\3\2\2\2\u01bf\u01c0\t\7\2\2\u01c0\u0086")
        buf.write("\3\2\2\2\u01c1\u01c8\t\7\2\2\u01c2\u01c4\7a\2\2\u01c3")
        buf.write("\u01c2\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c7\t\7\2\2\u01c6\u01c3\3\2\2\2\u01c7\u01ca\3")
        buf.write("\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u0088")
        buf.write("\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\t\b\2\2\u01cc")
        buf.write("\u01cd\t\t\2\2\u01cd\u01ce\5\u0087D\2\u01ce\u008a\3\2")
        buf.write("\2\2\u01cf\u01d1\t\n\2\2\u01d0\u01d2\t\t\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("\u01d4\5\u0087D\2\u01d4\u008c\3\2\2\2\u01d5\u01d6\t\4")
        buf.write("\2\2\u01d6\u008e\3\2\2\2\u01d7\u01d8\t\13\2\2\u01d8\u0090")
        buf.write("\3\2\2\2\u01d9\u01dd\7%\2\2\u01da\u01dc\n\f\2\2\u01db")
        buf.write("\u01da\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01dd\3")
        buf.write("\2\2\2\u01e0\u01e1\bI\2\2\u01e1\u0092\3\2\2\2\u01e2\u01e3")
        buf.write("\t\r\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\bJ\2\2\u01e5")
        buf.write("\u0094\3\2\2\2\u01e6\u01e8\7\17\2\2\u01e7\u01e6\3\2\2")
        buf.write("\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ed")
        buf.write("\7\f\2\2\u01ea\u01ec\t\16\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u0096\3\2\2\2\u01ef\u01ed\3\2\2\2\35\2\u0160\u0162")
        buf.write("\u016e\u0171\u0177\u0180\u0186\u0189\u018c\u0191\u0193")
        buf.write("\u0197\u019f\u01a4\u01a8\u01ad\u01b0\u01b5\u01ba\u01bd")
        buf.write("\u01c3\u01c8\u01d1\u01dd\u01e7\u01ed\3\b\2\2")
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
    EQUALS = 27
    ASYGN = 28
    SUM2 = 29
    SUMIGUAL = 30
    SUM = 31
    RES2 = 32
    RESIGUAL = 33
    RES = 34
    DIVIGUAL = 35
    DIV = 36
    MULIGUAL = 37
    MUL = 38
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
    DECIMAL_FLOAT_LIT = 62
    FLOATLITERAL = 63
    HEX_FLOAT_LIT = 64
    COMMENT = 65
    WS = 66
    NEWLINE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'while'", "'do'", "'break'", "'for'", "'in'", 
            "'begin'", "'end'", "'let'", "'const'", "'var'", "'continue'", 
            "'return'", "'print'", "'package'", "'type'", "'def'", "'struct'", 
            "'append'", "'len'", "','", "';'", "'.'", "':'", "':='", "'=='", 
            "'='", "'++'", "'+='", "'+'", "'--'", "'-='", "'-'", "'/='", 
            "'/'", "'*='", "'*'", "'!='", "'!'", "'>='", "'>'", "'<='", 
            "'<'", "'%'", "'%='", "'&&'", "'&'", "'||'", "'|'", "'|='", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "WHILE", "DO", "BREAK", "FOR", "IN", "BEGIN", 
            "END", "LET", "CONST", "VAR", "CONTINUE", "RETURN", "PRINT", 
            "PACKAGE", "TYPE", "DEF", "STRUCT", "APPEND", "LEN", "COMA", 
            "PyCOMA", "PUNTO", "DOSPUNTOS", "DOSPUNTOSIGUAL", "EQUALS", 
            "ASYGN", "SUM2", "SUMIGUAL", "SUM", "RES2", "RESIGUAL", "RES", 
            "DIVIGUAL", "DIV", "MULIGUAL", "MUL", "DIF", "ADMIRACION", "MAYORIGUAL", 
            "MAYOR", "MENORIGUAL", "MENOR", "PORCENTAJE", "PORCENTAJEIGUAL", 
            "AND2", "AND", "OR2", "OR", "ORIGUAL", "PARENTESISIZQ", "PARENTESISDER", 
            "BRACKETIZQ", "BRACKETDER", "LLAVEIZQ", "LLAVEDER", "ID", "CHAR_LITERAL", 
            "RAWSTRINGLITERAL", "INTLITERAL", "DECIMAL_FLOAT_LIT", "FLOATLITERAL", 
            "HEX_FLOAT_LIT", "COMMENT", "WS", "NEWLINE" ]

    ruleNames = [ "IF", "ELSE", "WHILE", "DO", "BREAK", "FOR", "IN", "BEGIN", 
                  "END", "LET", "CONST", "VAR", "CONTINUE", "RETURN", "PRINT", 
                  "PACKAGE", "TYPE", "DEF", "STRUCT", "APPEND", "LEN", "COMA", 
                  "PyCOMA", "PUNTO", "DOSPUNTOS", "DOSPUNTOSIGUAL", "EQUALS", 
                  "ASYGN", "SUM2", "SUMIGUAL", "SUM", "RES2", "RESIGUAL", 
                  "RES", "DIVIGUAL", "DIV", "MULIGUAL", "MUL", "DIF", "ADMIRACION", 
                  "MAYORIGUAL", "MAYOR", "MENORIGUAL", "MENOR", "PORCENTAJE", 
                  "PORCENTAJEIGUAL", "AND2", "AND", "OR2", "OR", "ORIGUAL", 
                  "PARENTESISIZQ", "PARENTESISDER", "BRACKETIZQ", "BRACKETDER", 
                  "LLAVEIZQ", "LLAVEDER", "ID", "CHAR_LITERAL", "RAWSTRINGLITERAL", 
                  "INTLITERAL", "DECIMAL_FLOAT_LIT", "FLOATLITERAL", "HEX_FLOAT_LIT", 
                  "HEX_MANTISSA", "DIGIT", "DECIMALS", "HEX_EXPONENT", "EXPONENT", 
                  "HEX_DIGIT", "LETTER", "COMMENT", "WS", "NEWLINE" ]

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


