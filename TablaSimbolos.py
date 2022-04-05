import token

from miParserLexer import *
from miParserParser import *
from antlr4 import *


class TablaSimbolos():
    tabla = [] # tabla de simbolos
    token = Token
    tipo = 0
    nivel = 0
    contex = ParserRuleContext

    def __init__(self,tabla, token, tipo, context, nivel):
        self.tabla = []
        self.token = token
        self.tipo = tipo
        self.contex = context
        self.nivel = nivel


    def Ident(self, token, tipo, context, nivelActual):
        self.token = token
        self.tipo = tipo
        self.contex = context
        self.nivel  = nivelActual

    def getNivel(self):
        return self.nivel

    def getToken(self):
        return self.token

    def getTipo(self):
        return self.tipo
#####################################
from antlr4 import *

class TablaSimbolos:

    tabla = []

    nivelActual =0

    class Ident:
        token = None
        type = 0
        nivel = 0
        valor = 0
        #ParserRuleContext declCtx

        def Ident( t, tp, decl):
            tok = None
            type = tp
            valor = 0
            declCtx=decl


        def setValue(v):
            valor = v



    def TablaSimbolos(self):
        tabla = []
        nivelActual=-1;



"""
   

        //*****Classes de las declaraciones*****

        public class VarIdent : Ident  //clase para declaracion de variable
        {
            public VarIdent(IToken id, int type, ParserRuleContext ctx,int nivelActual):base(token:id,type:type,context:ctx,nivelActual:nivelActual)
            { }
        }

        public VarIdent InsertVarIdent(IToken id,int type, ParserRuleContext ctx,int nivelActual)
        {
            VarIdent aux = null;
            Ident auxRepetido = repetido(id.Text,nivelActual);
            if (auxRepetido==null)
            {
                aux = new VarIdent(id, type, ctx,nivelActual);
                tabla.Add(aux);
                return aux;
            }
            return aux;
        }

        public class SliceIdent : Ident
        {
            public SliceIdent(IToken id, int type, ParserRuleContext ctx, int nivel) : base(token: id, type: type,
                context: ctx, nivelActual: nivel)
            {}
        }
        public SliceIdent InsertSliceIdent(IToken id, int tipo, ParserRuleContext context, int nivelActual)
        {
            SliceIdent var = new SliceIdent(id, tipo, context, nivelActual);
            tabla.Add(var);
            return var;
        }

        public class ArrayIdent:Ident
        {
            private string size = null;
            public ArrayIdent(IToken id, int tipo, ParserRuleContext context, int nivelActual,string size) : base(token: id, type: tipo, context: context, nivelActual: nivelActual)
            {
                this.size =  size;
            }
            public string getSize()
            {
                return this.size;
            }
        }

        public ArrayIdent InsertArrayIdent(IToken id, int tipo, ParserRuleContext ctx, int nivelActual, string size)
        {
            ArrayIdent var = new ArrayIdent(id, tipo, ctx, nivelActual, size);
            tabla.Add(var);
            return var;
        }

        public class StructIdent : Ident
        {
            private List<Ident> structMems;

            public StructIdent(IToken id, int tipo, ParserRuleContext ctx, int nivelActual) : base(token: id, type: tipo, context: ctx, nivelActual: nivelActual)
            {
                structMems = new List<Ident>();
            }

            public void SetMembers(List<Ident> members)
            {
                structMems = members;
            }

            public List<Ident> getMembers()
            {
                return structMems;
            }
        }

        public StructIdent InsertStructIdent(IToken id, int tipo, ParserRuleContext ctx, int nivelActual)
        {
            StructIdent var = new StructIdent(id, tipo, ctx, nivelActual);
            tabla.Add(var);
            return var;
        }

        public class FuncIdent: Ident
        {
            private List<Ident> args;
            public FuncIdent(IToken id, int tipo, ParserRuleContext ctx, int nivelActual) : base(token: id, type: tipo, context: ctx, nivelActual: nivelActual)
            {
                args = new List<Ident>();
            }

            public List<Ident> getArgs()
            {
                return args;
            }

            public void setArgs(List<Ident> args)
            {
                this.args = args;
            }

        }

        public FuncIdent InsertFuncIdent(IToken id, int tipo, ParserRuleContext ctx, int nivelActual)
        {
            FuncIdent func = new FuncIdent(id, tipo, ctx, nivelActual);
            tabla.Add(func);
            return func;
        }

        public Ident buscarUltimaFunc(int nivelActual)
        {
            int contador = nivelActual;
            while (contador >= 0)
            {
                for (int i = 0; i < tabla.Count; i++)
                {
                    if (tabla[i] is FuncIdent && tabla[i].GetNivel() == contador)
                        return tabla[i];
                }
                contador--;
            }
            return null;
        }
//----------------------------------------------------

        public void closeScope(int nivelActual)
        {
            for( int i=0; i<tabla.Count;i++)
            {
                if (tabla[i].GetNivel() == nivelActual)
                    tabla.Remove(tabla[i]);
            }
        }

        public Ident repetido(string id, int nivel)
        {
            Ident aux = null;
            foreach (Ident var in tabla)
            {
                if (var.getToken().Text.Equals(id) && var.GetNivel() == nivel)
                    aux= var;
            }
            return aux;
        }

        public void imprimirTabla()
        {
            for (int i = 0; i < tabla.Count; i++)
            {
                IToken s =  (tabla[i].getToken());
                if(s!=null)
                    MessageBox.Show("(VarDecl)  Nombre: " + s.Text +"  Nivel: "+ tabla[i].GetNivel()+"   tipo: "+ tabla[i].GetTipo());
                else
                    MessageBox.Show("(VarDecl)  Nombre: N/A  Nivel: "+ tabla[i].GetNivel()+"   tipo: "+ tabla[i].GetTipo());

            }
        }
    }
}
"""




