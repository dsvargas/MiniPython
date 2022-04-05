import token
from miParserLexer import *
from miParserParser import *
from TablaSimbolos import *
from ErrorListener import *
from antlr4 import *




class AContextual(TablaSimbolos,miParserParser):
    nivelActual = 0
    tabla = TablaSimbolos();
    listaErrores = []

    def __init__(self,nivelActual,tabla,listaErrores):
        self.nivelActual = nivelActual
        self.tabla = tabla
        self.listaErrores = listaErrores

    def OpenScope(self):
        return self.nivelActual +1

    def CloseScope(self):
        return self.nivelActual-1

    def program(self):
        return super().program()

    def statement(self):
        return super().statement()

    def defStatement(self):
        return super().defStatement()

    def argList(self):
        return super().argList()

    def moreArgs(self):
        return super().moreArgs()

    def ifStatement(self):
        return super().ifStatement()

    def whileStatement(self):
        return super().whileStatement()

    def forStatement(self):
        return super().forStatement()

    def returnStatement(self):
        return super().returnStatement()

    def printStatement(self):
        return super().printStatement()

    def assignStatement(self):
        return super().assignStatement()

    def functionCallStatement(self):
        return super().functionCallStatement()

    def expressionStatement(self):
        return super().expressionStatement()

    def sequence(self):
        return super().sequence()

    def moreStatements(self):
        return super().moreStatements()

    def expression(self):
        return super().expression()

    def comparison(self):
        return super().comparison()

    def additionExpression(self):
        return super().additionExpression()

    def additionFactor(self):
        return super().additionFactor()

    def multiplicationExpression(self):
        return super().multiplicationExpression()

    def multiplicationFactor(self):
        return super().multiplicationFactor()

    def elementExpression(self):
        return super().elementExpression()

    def elementAccess(self):
        return super().elementAccess()

    def expressionList(self):
        return super().expressionList()

    def moreExpressions(self):
        return super().moreExpressions()

    def primitiveExpression(self):
        return super().primitiveExpression()

    def listExpression(self):
        return super().listExpression()


"""

  

        public override object VisitRoot_AST(ParserGrammar.Root_ASTContext context) //done
        {
            Visit(context.topDeclarationList());
            //tabla.imprimirTabla();
            return null;
        }

        public override object VisitTopDeclarationList_AST(ParserGrammar.TopDeclarationList_ASTContext context) //done
        {
            for (int i = 0; i < context.ChildCount; i++)
            {
                if (context.children[i] is ParserGrammar.VariableDeclContext)
                    Visit(context.children[i]);
                else if (context.children[i] is ParserGrammar.TypeDeclContext)
                    Visit(context.children[i]);
                else if (context.children[i] is ParserGrammar.FuncDeclContext)
                    Visit(context.children[i]);
            }
            return null;
        }

        public override object VisitSingleVarDecl_VD_AST(ParserGrammar.SingleVarDecl_VD_ASTContext context)
        {
            Visit(context.singleVarDecl());
            return null;
        }

        public override object VisitMultiVarDecl_VD_AST(ParserGrammar.MultiVarDecl_VD_ASTContext context)
        {
            Visit(context.innerVarDecls());
            return null;
        }

        public override object VisitVarDecl_VD_AST(ParserGrammar.VarDecl_VD_ASTContext context)
        {
            return null;
        }

        public override object VisitInnerVarDecls_AST(ParserGrammar.InnerVarDecls_ASTContext context)
        {
            Visit(context.singleVarDecl(0));
            for (int i = 1; i < context.singleVarDecl().Length; i++)
                Visit(context.singleVarDecl(i));
            return null;
        }

        public override object VisitTypeAsygn_SVD_AST(ParserGrammar.TypeAsygn_SVD_ASTContext context)
        {
            List<IToken> listaID = (List<IToken>) Visit(context.identifierList()); //lista de los token id

            int tipo = (int) Visit(context.declType());

            List<int> listaExp = ((List<int>) Visit(context.expressionList()));

            if (listaExp.Count != listaID.Count)
                listaErrores.addError("Error: Cantidad de identificadores no concuerda con los argumentos . Linea: "+context.ASYGN().Symbol.Line);
            else if (tipo == -1)
                listaErrores.addError("Error: Tipo de dato incorrecto . Linea: "+context.ASYGN().Symbol.Line);
            foreach (int var in listaExp)
            {
                if(var != tipo)
                    listaErrores.addError("Error: Conflicto de tipos: Linea: "+context.ASYGN().Symbol.Line);
            }
            for (int i = 0; i < listaExp.Count; i++)
            {
                TablaSimbolos.Ident res = tabla.InsertVarIdent(listaID[i], tipo, context, nivelActual);
                if(res == null)
                    listaErrores.addError("La variable [ "+listaID[i].Text + " ] ya ha sido declarada. Linea: "+listaID[i].Line);
            }

            return null;
        }

        public override object VisitIdListAsygn_SVD_AST(ParserGrammar.IdListAsygn_SVD_ASTContext context)
        {
            List<IToken> listaID = (List<IToken>) Visit(context.identifierList()); //lista de los token id

            List<int> listaExp = ((List<int>) Visit(context.expressionList()));

            if (listaExp.Count != listaID.Count)
                listaErrores.addError("Error: Cantidad de identificadores no concuerda con los argumentos . Linea: "+context.ASYGN().Symbol.Line);
            else
            {
                for (int i = 0; i < listaExp.Count; i++)
                {
                    TablaSimbolos.Ident res= tabla.InsertVarIdent(listaID[i], listaExp[i], context,nivelActual);
                    if (res == null)
                        listaErrores.addError("La variable [ "+listaID[i].Text+ " ] ya ha sido declarada: Linea: "+listaID[i].Line);
                }
            }
            return null;
        }

        public override object VisitSingleVarDecl_SVD_AST(ParserGrammar.SingleVarDecl_SVD_ASTContext context)
        {
            Visit(context.singleVarDeclNoExps());
            return null;
        }

        public override object VisitSingleVarDeclNoExps_AST(ParserGrammar.SingleVarDeclNoExps_ASTContext context)
        {
            List<IToken> listaID = (List<IToken>) Visit(context.identifierList()); //lista de los token id

            int tipo =(int) Visit(context.declType());

            List<TablaSimbolos.Ident> result = new List<TablaSimbolos.Ident>();

            if (tipo != -1)
            {
                foreach (IToken v in listaID)
                {
                   TablaSimbolos.VarIdent a = tabla.InsertVarIdent(v,tipo,context, nivelActual);
                   if (a != null)
                       result.Add(a);
                   else
                       listaErrores.addError("La variable [ "+v.Text + " ] ya ha sido declarada. Linea: "+v.Line);
                }
            }
            else
            {
                listaErrores.addError("Error: Tipo de dato desconocido");
            }
            return result;
        }
        public override object VisitSingleTypeDecl_TD_AST(ParserGrammar.SingleTypeDecl_TD_ASTContext context)
        {
            Visit(context.singleTypeDecl());
            return null;
        }

        public override object VisitMultiTypeDecl_TD_AST(ParserGrammar.MultiTypeDecl_TD_ASTContext context)
        {
            Visit(context.innerTypeDecls());
            return null;
        }

        public override object VisitTypeDecl_AST(ParserGrammar.TypeDecl_ASTContext context)//done
        {
            return null;
        }

        public override object VisitInnerTypeDecls_AST(ParserGrammar.InnerTypeDecls_ASTContext context)
        {
            Visit(context.singleTypeDecl(0));
            for (int i = 1; i < context.singleTypeDecl().Length; i++)
                Visit(context.singleTypeDecl(i));
            return null;
        }

        public override object VisitSingleTypeDecl_AST(ParserGrammar.SingleTypeDecl_ASTContext context)
        {
            IToken tok= context.ID().Symbol;

            int tipo = (int) Visit(context.declType());

            TablaSimbolos.Ident res = tabla.InsertVarIdent(tok, tipo, context, nivelActual);

            if(res==null)
                listaErrores.addError("La variable [ "+tok.Text+ " ] ya ha sido declara. Linea: " + tok.Line);

            Visit(context.declType());
            return null;
        }

        public override object VisitFuncDecl_AST(ParserGrammar.FuncDecl_ASTContext context)
        {
            Visit(context.funcFrontDecl());
            Visit(context.block());
            return null;
        }

        public override object VisitFuncFrontDecl_AST(ParserGrammar.FuncFrontDecl_ASTContext context)
        {
            IToken token = context.ID().Symbol;
            List<TablaSimbolos.Ident> args = new List<TablaSimbolos.Ident>();
            int tipo = -3;

            if (context.funcArgDecls() != null)
            {
                openScope();
                args = (List<TablaSimbolos.Ident>) Visit(context.funcArgDecls());
                closeScope();
            }

            if (context.declType() != null)
            {
                tipo = (int) Visit(context.declType());
            }

            TablaSimbolos.FuncIdent newFunc= tabla.InsertFuncIdent(token, tipo, context, nivelActual);
            newFunc.setArgs(args);

            return null;
        }

        public override object VisitFuncArgDecls_AST(ParserGrammar.FuncArgDecls_ASTContext context)
        {
            List<TablaSimbolos.Ident> funcArgs = new List<TablaSimbolos.Ident>();
            List<TablaSimbolos.Ident> aux = new List<TablaSimbolos.Ident>();

            for (int i = 0; i < context.singleVarDeclNoExps().Length; i++)
            {
                aux = (List<TablaSimbolos.Ident>) Visit(context.singleVarDeclNoExps(i));
                funcArgs = funcArgs.Concat(aux).ToList();
            }
            return funcArgs;
        }

        public override object VisitDeclType_DT_AST(ParserGrammar.DeclType_DT_ASTContext context)//done
        {
            int tipo = (int) Visit(context.declType());
            return tipo;
        }

        public override object VisitId_DT_AST(ParserGrammar.Id_DT_ASTContext context)//done
        {
            if (context.ID().Symbol.Text.Equals("int"))
                return -9;
            if(context.ID().Symbol.Text.Equals("bool"))
                return -4;
            if (context.ID().Symbol.Text.Equals("string"))
                return -12;
            if (context.ID().Symbol.Text.Equals("float"))
                return -10;
            TablaSimbolos.Ident dato = tabla.repetido(context.ID().Symbol.Text, nivelActual);
            if (dato == null)
            {
                listaErrores.addError("Error: Tipo de dato no ha sido declarado. Linea: "+context.ID().Symbol.Line);
                return -1;
            }
            return dato.GetTipo();
        }

        public override object VisitSliceDecl_DT_AST(ParserGrammar.SliceDecl_DT_ASTContext context)
        {
            return Visit(context.sliceDeclType());
        }

        public override object VisitArrayDecl_DT_AST(ParserGrammar.ArrayDecl_DT_ASTContext context)
        {
            return Visit(context.arrayDeclType());
        }

        public override object VisitStructDecl_DT_AST(ParserGrammar.StructDecl_DT_ASTContext context)
        {
            return Visit(context.structDeclType());
        }

        public override object VisitSliceDeclType_AST(ParserGrammar.SliceDeclType_ASTContext context)
        {
            int tipo =(int) Visit(context.declType());

            if (tipo != -1)
                tabla.InsertSliceIdent(null, tipo, context, nivelActual);
            else
                listaErrores.addError("Error: Tipo de dato incorrecto  Linea: "+ context.BRACKETIZQ().Symbol.Line);
            return -5;
        }

        public override object VisitArrayDeclType_AST(ParserGrammar.ArrayDeclType_ASTContext context)
        {
            int tipo = (int) Visit(context.declType());

            if (tipo != -1)
                tabla.InsertArrayIdent(null, tipo, context, nivelActual, context.INTLITERAL().Symbol.Text);
            else
                listaErrores.addError("Error: El tipo de dato es incorrecto. Linea: "+context.BRACKETIZQ().Symbol.Line);
            return -6;
        }

        public override object VisitStructDeclType_AST(ParserGrammar.StructDeclType_ASTContext context)
        {
            openScope();
            List<TablaSimbolos.Ident> mems = new List<TablaSimbolos.Ident>();
            if (context.structMemDecls() != null)
            {
                mems = (List<TablaSimbolos.Ident>)Visit(context.structMemDecls());
            }
            TablaSimbolos.StructIdent nuevaEntrada= tabla.InsertStructIdent(null, -7, context, nivelActual);
            nuevaEntrada.SetMembers(mems);
            closeScope();
            return -7;
        }

        public override object VisitStructMemDecls_AST(ParserGrammar.StructMemDecls_ASTContext context)
        {
            List<TablaSimbolos.Ident> listaMem = new List<TablaSimbolos.Ident>();
            for(int i=0; i<context.singleVarDeclNoExps().Length;i++)
            {
                List<TablaSimbolos.Ident> aux =(List<TablaSimbolos.Ident>)Visit(context.singleVarDeclNoExps(i));
                listaMem = listaMem.Concat(aux).ToList();
            }
            return listaMem;
        }

        public override object VisitIdDecl_AST(ParserGrammar.IdDecl_ASTContext context)
        {
            List<IToken> lista = new List<IToken>();
            TablaSimbolos.Ident repetido = tabla.repetido(context.ID(0).Symbol.Text, nivelActual);
            if(repetido==null)
                lista.Add(context.ID(0).Symbol);
            else
                listaErrores.addError("Error: El identificador [  " +context.ID(0).Symbol.Text+ " ] ya ha sido declarado "+" Linea: "+context.ID(0).Symbol.Line);
            for (int i = 1; i < context.ID().Length; i++)
            {
                repetido = tabla.repetido(context.ID(i).Symbol.Text, nivelActual);
                if(repetido==null)
                    lista.Add(context.ID(i).Symbol);
                else
                    listaErrores.addError("Error: El identificador [  " +context.ID(i).Symbol.Text+ " ] ya ha sido declarado "+" Linea: "+context.ID(i).Symbol.Line);
            }
            return lista;
        }

        public override object VisitElevado_EXP_AST(ParserGrammar.Elevado_EXP_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            if (exp != -9)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.ELEVADO().Symbol.Text+". Linea: "+context.ELEVADO().Symbol.Line);
                return -1;
            }
            return exp;
        }

        public override object VisitExpsum_EXP_AST(ParserGrammar.Expsum_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            MessageBox.Show("1: " + exp1.ToString());
            MessageBox.Show("2: " + exp2.ToString());
            if (exp1==-9 || exp1==-10 || exp1==-11)
            {
                if (exp2==-9 || exp2==-10 || exp2==-11)
                    return -9;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.SUM().GetText()+" Linea: "+context.SUM().Symbol.Line);
            return -1;
        }

        public override object VisitExpmayor_EXP_AST(ParserGrammar.Expmayor_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 && exp2 ==-9)
                return -4;
            if (exp1 == -10 && exp2 == -10)
                return -4;
            if (exp1 == -11 && exp2 == -11)
                return -4;
            if ((exp1==-12 && exp2 == -12) || (exp1==-12 && exp2 == -13) || (exp1==-13 && exp2 == -12) || (exp1==-13 && exp2 == -13)) // if both are string
            {
                return -4;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.MAYOR().Symbol.Text+". Linea: "+context.MAYOR().Symbol.Line);
            return -1;
        }

        public override object VisitExpand2_EXP_AST(ParserGrammar.Expand2_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -4 || exp2!= -4)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.AND2().Symbol.Text+ ". Linea: "+ context.AND2().Symbol.Line);
                return -1;
            }
            return -4;
        }

        public override object VisitExpmenorigual_EXP_AST(ParserGrammar.Expmenorigual_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 && exp2 ==-9)
                return -4;
            if (exp1 == -10 && exp2 == -10)
                return -4;
            if (exp1 == -11 && exp2 == -11)
                return -4;
            if ((exp1==-12 && exp2 == -12) || (exp1==-12 && exp2 == -13) || (exp1==-13 && exp2 == -12) || (exp1==-13 && exp2 == -13)) // if both are string
            {
                return -4;
            }
            return exp1;
        }

        public override object VisitExpmayorigual_EXP_AST(ParserGrammar.Expmayorigual_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 && exp2 ==-9)
                return -4;
            if (exp1 == -10 && exp2 == -10)
                return -4;
            if (exp1 == -11 && exp2 == -11)
                return -4;
            if ((exp1==-12 && exp2 == -12) || (exp1==-12 && exp2 == -13) || (exp1==-13 && exp2 == -12) || (exp1==-13 && exp2 == -13)) // if both are string
            {
                return -4;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.MAYORIGUAL().Symbol.Text+". Linea: "+context.MAYORIGUAL().Symbol.Line);
            return -1;
        }

        public override object VisitSum_EXP_AST(ParserGrammar.Sum_EXP_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            if (exp == -9)
                return exp;
            if (exp == -10)
                return exp;
            if (exp == -11)
                return exp;
            if (exp == -12)
                return exp;
            if (exp == -13)
                return exp;
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.SUM().GetText());
            return -1;
        }

        public override object VisitExpmul_EXP_AST(ParserGrammar.Expmul_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if ((exp1 & exp2) == -9)
                return -9;
            if (exp1==-9 || exp1 ==-10 || exp1==-11)
            {
                if(exp2==-9 || exp2 ==-10 || exp2==-11)
                    return -10;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.MUL().Symbol.Text+" Linea: "+context.MUL().Symbol.Line);
            return -1;

        }

        public override object VisitExpor2_EXP_AST(ParserGrammar.Expor2_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -4 || exp2 != -4)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador " + context.OR2().Symbol.Text+" Linea: "+context.OR2().Symbol.Line);
                return -1;
            }
            return -4;
        }

        public override object VisitExpdiv_EXP_AST(ParserGrammar.Expdiv_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1==-9 || exp1 ==-10 || exp1==-11)
            {
                if(exp2==-9 || exp2 ==-10 || exp2==-11)
                    return -10;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.DIV().Symbol.Text+" Linea: "+context.DIV().Symbol.Line);
            return -1;
        }

        public override object VisitExpand_EXP_AST(ParserGrammar.Expand_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -9 || exp2 != -9)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.AND().Symbol.Text+". Linea: "+context.AND().Symbol.Line);
                return -1;
            }
            return-9;
        }

        public override object VisitExpres_EXP_AST(ParserGrammar.Expres_EXP_ASTContext context)//done
        {

            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 && exp2 == -9)
                return -9;
            if (exp1 == -9 || exp1 == -10 || exp1 == -11)
            {
                if(exp2 == -9 || exp2 == -10 || exp2 == -11)
                    return -10;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.RES().Symbol.Text+". Linea: "+context.RES().Symbol.Line);
            return -1;
        }

        public override object VisitRes_EXP_AST(ParserGrammar.Res_EXP_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            if (exp == -9)
                return exp;
            if (exp == -10)
                return exp;
            if (exp == -11)
                return exp;
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.RES().GetText());
            return -1;
        }
        public override object VisitExpdoblemenorque_EXP_AST(ParserGrammar.Expdoblemenorque_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 !=-9  || exp2!=-9)

            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.DOBLEMENORQUE().Symbol.Text+". Linea: "+context.DOBLEMENORQUE().Symbol.Line);
                return -1;
            }
            return -9;
        }

        public override object VisitExpelevado_EXP_AST(ParserGrammar.Expelevado_EXP_ASTContext context) //done
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -9 || exp2 != -9)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.ELEVADO().Symbol.Text+". Linea: "+context.ELEVADO().Symbol.Line);
                return -1;
            }
         return -9;
        }

        public override object VisitPrimaryExpression_EXP_AST(ParserGrammar.PrimaryExpression_EXP_ASTContext context)//done
        {
            int tipo =(int) Visit(context.primaryExpression());
            return tipo;
        }

        public override object VisitExpor_EXP_AST(ParserGrammar.Expor_EXP_ASTContext context)//done
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -9 || exp2!= -9)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.OR().Symbol.Text+". Linea: "+context.OR().Symbol.Line);
                return -1;
            }
            return exp1;
        }

        public override object VisitAdmiracion_EXP_AST(ParserGrammar.Admiracion_EXP_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            if (exp != -4)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.ADMIRACION().Symbol.Text+". Linea: "+context.ADMIRACION().Symbol.Line);
                return -1;
            }
            return exp;
        }

        public override object VisitExpequals_EXP_AST(ParserGrammar.Expequals_EXP_ASTContext context) //done
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 || exp1 == -10 || exp1 == -11)
            {
                if(exp2== -9 || exp2 == -10 || exp2 == -11)
                    return -4;
            }
            if ((exp1 == -12 && exp2 == -12) || (exp1 == -12 && exp2 == -13) || (exp1 == -13 && exp2 == -12) || (exp1 == -13 && exp2 == -13)) // if both are string
                return -4;
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.EQUALS().Symbol.Text+". Linea: "+context.EQUALS().Symbol.Line);
            return -1;
        }

        public override object VisitExpdoblemayorque_EXP_AST(ParserGrammar.Expdoblemayorque_EXP_ASTContext context)//done
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1==-9 || exp1 == -10 || exp1 ==-11) // if both are numeric
            {
                if(exp2==-9 || exp2 == -10 || exp2 ==-11)
                    return -9;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.DOBLEMAYORQUE().Symbol.Text+". Linea: "+context.DOBLEMAYORQUE().Symbol.Line);
            return -1;
        }

        public override object VisitExpdif_EXP_AST(ParserGrammar.Expdif_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 || exp1 == -10 || exp1 == -11)
            {
                if(exp2 == -9 || exp2 == -10 || exp2 == -11)
                    return -4;
            }
            if ((exp1 == -12 && exp2 == -12) || (exp1 == -12 && exp2 == -13) || (exp1 == -13 && exp2 == -12) || (exp1 == -13 && exp2 == -13)) // if both are string
                return -4;
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.DIF().Symbol.Text+". Linea: "+context.DIF().Symbol.Line);
            return -1;
        }

        public override object VisitExpmenor_EXP_AST(ParserGrammar.Expmenor_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 == -9 && exp2 ==-9)
                return -4;
            if (exp1 == -10 && exp2 == -10)
                return -4;
            if (exp1 == -11 && exp2 == -11)
                return -4;
            if ((exp1==-12 && exp2 == -12) || (exp1==-12 && exp2 == -13) || (exp1==-13 && exp2 == -12) || (exp1==-13 && exp2 == -13)) // if both are string
            {
                return -4;
            }
            listaErrores.addError("Error: Datos incompatibles para el operador "+context.MENOR().Symbol.Text+". Linea "+context.MENOR().Symbol.Line);
            return -1;
        }

        public override object VisitExpporcentaje_EXP_AST(ParserGrammar.Expporcentaje_EXP_ASTContext context)
        {

            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 !=-9 || exp2 != -9)// if any is not an integer %
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.PORCENTAJE().Symbol.Text+" Linea: "+context.PORCENTAJE().Symbol.Line);
                return -1;
            }
            return -9;

        }

        public override object VisitExpandtecho_EXP_AST(ParserGrammar.Expandtecho_EXP_ASTContext context)
        {
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if (exp1 != -9 || exp2 != -9)
            {
                listaErrores.addError("Error: Datos incompatibles para el operador "+context.ANDTECHO().Symbol.Text+". Linea: "+context.ANDTECHO().Symbol.Line);
                return -1;
            }
            return -9;
        }

        public override object VisitExpressionList_AST(ParserGrammar.ExpressionList_ASTContext context)
        {
            //declarar un list para que retorne la lista
            List<int> listaTipos = new List<int>();
            listaTipos.Add((int) Visit(context.expression(0)));
            for (int i = 1; i < context.expression().Length; i++)
            {
                // cada visit devuelve un tipo que debe ir agregando a la lista
               listaTipos.Add((int) Visit(context.expression(i)));
            }
            //y al final retorna la lista
            return listaTipos;
        }

        public override object VisitLengthExpression_PE_AST(ParserGrammar.LengthExpression_PE_ASTContext context)
        {
            return Visit(context.lengthExpression());
        }

        public override object VisitOperand_PE_AST(ParserGrammar.Operand_PE_ASTContext context)
        {
            return Visit(context.operand());
        }

        public override object VisitAppendExpression_PE_AST(ParserGrammar.AppendExpression_PE_ASTContext context)
        {
            return Visit(context.appendExpression());
        }

        public override object VisitCapExpression_PE_AST(ParserGrammar.CapExpression_PE_ASTContext context)//done
        {
          return Visit(context.capExpression());
        }

        public override object VisitArguments_PE_AST(ParserGrammar.Arguments_PE_ASTContext context)//done
        {
            int primExp = (int) Visit(context.primaryExpression());
            if (primExp != -3)
            {
                listaErrores.addError("Error: La expresión no es un método");
                return -1;
            }
            return 0;
        }

        public override object VisitSelector_PE_AST(ParserGrammar.Selector_PE_ASTContext context)//done
        {
            IToken selector = (IToken) Visit(context.selector());
            int primExp = (int) Visit(context.primaryExpression());
            if (primExp != -1)
            {
                if(primExp == -5 || primExp == -6 || primExp == -7 || primExp == -3)
                    return 0;
                listaErrores.addError("Error: La expresion no tiene selectores. Linea: "+selector.Line);
                return -1;
            }
            listaErrores.addError("Error: El seleccionador [ ."+selector.Text+" ] no se encuentra. Linea: "+selector.Line);
            return -1;
        }

        public override object VisitIndex_PE_AST(ParserGrammar.Index_PE_ASTContext context)//done
        {
            int primExp = (int) Visit(context.primaryExpression());
            int index = (int) Visit(context.index());

            if (index != -1 && primExp!=-1)
            {
                if (primExp == -5 || primExp == -6)
                {
                    if (index == -9)
                        return 0;
                    listaErrores.addError("Error: Se ha encontrado un índice no válido");
                    return -1;
                }
                listaErrores.addError("Error: El elemento no puede ser indexado");
                return -1;
            }
            listaErrores.addError("Error: error de expresiones");
            return -1;
        }

        public override object VisitLiteral_OP_AST(ParserGrammar.Literal_OP_ASTContext context)
        {
            int tipo = (int) Visit(context.literal());
            return tipo;
        }

        public override object VisitId_OP_AST(ParserGrammar.Id_OP_ASTContext context)
        {
            TablaSimbolos.Ident a = null;
            a = tabla.repetido(context.ID().Symbol.Text, nivelActual);

            if (nivelActual != 0 && a==null)
                a = tabla.repetido(context.ID().Symbol.Text, 0);

            if (a == null)
            {
                listaErrores.addError("Error: La expresión [ " + context.ID().Symbol.Text + " ] no ha sido declarada. Linea: " + context.ID().Symbol.Line);
                return -1;
            }
            return a.GetTipo();
        }

        public override object VisitExpression_OP_AST(ParserGrammar.Expression_OP_ASTContext context)//done
        {
            int tipo = (int) Visit(context.expression());
            return tipo;
        }

        public override object VisitIntliteral_LIT_AST(ParserGrammar.Intliteral_LIT_ASTContext context) //done
        {
            return -9;
        }

        public override object VisitFloatliteral_LIT_AST(ParserGrammar.Floatliteral_LIT_ASTContext context) //done
        {
            return -10;
        }

        public override object VisitRuneliteral_LIT_AST(ParserGrammar.Runeliteral_LIT_ASTContext context) //done
        {
            return -11;
        }

        public override object VisitRawstring_LIT_AST(ParserGrammar.Rawstring_LIT_ASTContext context) //done
        {
            return -12;
        }

        public override object VisitInterpretedstring_LIT_AST(ParserGrammar.Interpretedstring_LIT_ASTContext context)
        {
            return -12;
        }

        public override object VisitIndex_AST(ParserGrammar.Index_ASTContext context)
        {
           int tipoexp=(int) Visit(context.expression());
           if (tipoexp != -1)
               return tipoexp;
           listaErrores.addError("Error: Error de expresiones. Linea: "+context.BRACKETIZQ().Symbol.Line);
           return -1;
        }

        public override object VisitArguments_AST(ParserGrammar.Arguments_ASTContext context)//done
        {
            List<int> listaTipos = new List<int>();

            if (context.expressionList() != null)
            {
                listaTipos= (List<int>) Visit(context.expressionList());
            }
            return listaTipos;
        }

        public override object VisitSelector_AST(ParserGrammar.Selector_ASTContext context)
        {
            return context.ID().Symbol;
        }

        public override object VisitAppendExpression_AST(ParserGrammar.AppendExpression_ASTContext context)//done
        {
            int exp1= (int) Visit(context.expression(0));
            int exp2= (int) Visit(context.expression(1));

            if (exp2 == -1)
            {
                listaErrores.addError("Error: La expresion no se encuentra. Linea: "+context.APPEND().Symbol.Line);
                return -1;
            }
            if (exp1 == -5 || exp1 == -6)
                return -14;

            listaErrores.addError("Error: El operado 'Append' no es válido para el elemento seleccionado. Linea: "+context.APPEND().Symbol.Line);
            return -1;
        }

        public override object VisitLengthExpression_AST(ParserGrammar.LengthExpression_ASTContext context)//done
        {
            int exp = (int) Visit(context.expression());
            if (exp == -1)
            {
                listaErrores.addError("Error: La expresion no se encuentra. Linea: "+context.LEN().Symbol.Line);
                return -1;
            }
            if (exp == -5 || exp == -6)
                return -15;

            listaErrores.addError("Error: El operado 'Len' no es válido para el elemento seleccionado. Linea: "+context.LEN().Symbol.Line);
            return -1;
        }

        public override object VisitCapExpression_AST(ParserGrammar.CapExpression_ASTContext context)//done
        {
            int exp= (int) Visit(context.expression());
            if (exp == -1)
            {
                listaErrores.addError("Error: La expresion no se encuentra. Linea: "+context.CAP().Symbol.Line);
                return -1;
            }
            if (exp == -5 || exp == -6)
                return -15;

            listaErrores.addError("Error: El operado 'Cap' no es válido para el elemento seleccionado. Linea: "+context.CAP().Symbol.Line);
            return -1;
        }

        public override object VisitStatementList_AST(ParserGrammar.StatementList_ASTContext context)
        {
            for (int i = 0; i < context.statement().Length; i++)
                Visit(context.statement(i));
            return null;
        }

        public override object VisitBlock_AST(ParserGrammar.Block_ASTContext context)
        {
            openScope();
            Visit(context.statementList());
            closeScope();
            return -17;
        }

        public override object VisitPrint_STAT_AST(ParserGrammar.Print_STAT_ASTContext context)//done
        {
            if (context.expression() != null)
            {
                int exp = (int) Visit(context.expression());
                if (exp == -12 || exp == -13)
                    return 0;
                listaErrores.addError("Error: El tipo de dato no es compatible con la función 'print'. Linea: "+context.PRINT().Symbol.Line);
                return -1;
            }
            return 0;
        }

        public override object VisitPrintln_STAT_AST(ParserGrammar.Println_STAT_ASTContext context)//done
        {
            if (context.expressionList() != null)
            {
                List<int> tiposExp =(List<int>) Visit(context.expressionList());
                for (int i = 0; i < tiposExp.Count; i++)
                {
                    if(tiposExp[i] != -12 && tiposExp[i] != -13)
                        listaErrores.addError("Error: El tipo de dato no es compatible con la función 'println'. Linea: "+context.PRINTLN().Symbol.Line);
                }
            }
            return 0;
        }

        public override object VisitReturn_STAT_AST(ParserGrammar.Return_STAT_ASTContext context)//done
        {
            int tipoExp = -3;
            if (context.expression() != null)
            {
                tipoExp = (int) Visit(context.expression());
            }
            TablaSimbolos.Ident lastFunc = tabla.buscarUltimaFunc(nivelActual);
            if (lastFunc != null)
            {
                if (lastFunc.GetTipo() != tipoExp)
                {
                    listaErrores.addError("Error: El tipo de dato retornado no es el esperado. Linea: "+context.RETURN().Symbol.Line);
                    return -1;
                }
                return 0;
            }
            listaErrores.addError("Error: No se encuentra el tipo a retornar. Linea: "+ context.RETURN().Symbol.Line);
            return null;
        }

        public override object VisitBreak_STAT_AST(ParserGrammar.Break_STAT_ASTContext context)
        {
            return null;
        }

        public override object VisitContinue_STAT_AST(ParserGrammar.Continue_STAT_ASTContext context)
        {
            return null;
        }

        public override object VisitSimpleStatement_STAT_AST(ParserGrammar.SimpleStatement_STAT_ASTContext context)
        {
            return  Visit(context.simpleStatement());
            //Dilana esta haciendo esta cadena
        }

        public override object VisitBlock_STAT_AST(ParserGrammar.Block_STAT_ASTContext context)
        {
            return Visit(context.block());
        }

        public override object VisitSwitch_STAT_AST(ParserGrammar.Switch_STAT_ASTContext context)
        {
            Visit(context.@switch());
            return -16;
        }

        public override object VisitIfStatement_STAT_AST(ParserGrammar.IfStatement_STAT_ASTContext context)
        {
            Visit(context.ifStatement());
            return -18;
        }

        public override object VisitLoop_STAT_AST(ParserGrammar.Loop_STAT_ASTContext context)
        {
            Visit(context.loop());
            return -19;
        }

        public override object VisitTypeDecl_STAT_AST(ParserGrammar.TypeDecl_STAT_ASTContext context)
        {
            Visit(context.typeDecl());
            return null;
        }

        public override object VisitVariableDecl_STAT_AST(ParserGrammar.VariableDecl_STAT_ASTContext context)
        {
            Visit(context.variableDecl());
            return null;
        }

        public override object VisitExpression_SS_AST(ParserGrammar.Expression_SS_ASTContext context)
        {
           int tipoExp= (int) Visit(context.expression());
           if (tipoExp != -1)
           {
               if (tipoExp != -9)
               {
                   listaErrores.addError("Error: La expresión no es autoincrementable / autodecrementable");
                   return -1;
               }
               return 0;
           }
           listaErrores.addError("Error: la expresión no es válida");
           return -1;
        }

        public override object VisitAssignmentStatement_SS_AST(ParserGrammar.AssignmentStatement_SS_ASTContext context)
        {
            return Visit(context.assignmentStatement());
        }

        public override object VisitExplist_SS_AST(ParserGrammar.Explist_SS_ASTContext context)
        {
            List<int> exp1 = (List<int>) Visit(context.expressionList(0));
            List<int> exp2 = (List<int>) Visit(context.expressionList(0));
            if (exp1.Count != exp2.Count)
            {
                listaErrores.addError("Error: La cantidad de variables no concuerda con las definiciones");
                return -1;
            }
            return 0;
        }

        public override object VisitEpsilon_SS_AST(ParserGrammar.Epsilon_SS_ASTContext context)//done
        {
            return 0;
        }

        public override object VisitAsygn_AS_AST(ParserGrammar.Asygn_AS_ASTContext context)
        {
            try
            {
                List<int> exp1 = (List<int>) Visit(context.expressionList(0));
                List<int> exp2 = (List<int>)Visit(context.expressionList(1));
                // si tienen la misma cantidad de elementos
                if (exp2.Count == exp1.Count)
                {
                    for (int i = 0; i < exp1.Count; i++)
                    {
                        if (exp1[i] != exp2[i])
                        {
                            // error de tipos
                            listaErrores.addError("Error: Datos incompatibles los tipos de datos no son iguales 111 ");
                            return -1;
                        }
                    }
                    return 0;
                }
                else
                {
                    //error la cantidad de variales no son iguales a la cantidad de argunentos
                    listaErrores.addError("Error: la cantidad de variales no son iguales a la cantidad de argunentos ");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }
            return null;
        }

        public override object VisitSumigual_AS_AST(ParserGrammar.Sumigual_AS_ASTContext context)
        {
            // '+=' integer, float32, string
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if ((exp1 == -9 && exp2 == -9) || (exp1 == -9 && exp2 == -10) || (exp1 == -10 && exp2 == -9) ||
                (exp1 == -10 && exp2 == -10) || (exp1 == -12 && exp2 == -12))
            {
                if (exp1 == -12)
                    return -12;
                return -9;
            }
            //error de tipos
            listaErrores.addError("Error: Datos incompatibles para el operando +=");
            return -1;
        }

        public override object VisitAndigual_AS_AST(ParserGrammar.Andigual_AS_ASTContext context)
        {
            // '&=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9 )
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles,el operando &= solo acepta enteros  ");
                return -1;
            }
            return -9;
        }

        public override object VisitResigual_AS_AST(ParserGrammar.Resigual_AS_ASTContext context)
        {
            // '-=' integers, float32
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if ((exp1 == -9 && exp2 == -9) || (exp1 == -9 && exp2 == -10) || (exp1 == -10 && exp2 == -9) || (exp1 == -10 && exp2 == -10))
                return -9;
            //error de tipos
            listaErrores.addError("Error: Datos incompatibles, el operando -= solo acepta enteros o flotantes  ");
            return -1;
        }

        public override object VisitOrigual_AS_AST(ParserGrammar.Origual_AS_ASTContext context)
        {
            //'|=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando |= solo acepta enteros ");
                return -1;
            }
            return -9;
        }

        public override object VisitMuligual_AS_AST(ParserGrammar.Muligual_AS_ASTContext context)
        {
            // '*=' integer, float32
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if ((exp1 == -9 && exp2 == -9) || (exp1 == -9 && exp2 == -10) || (exp1 == -10 && exp2 == -9) || (exp1 == -10 && exp2 == -10))
                return -9;
            //error de tipos
            listaErrores.addError("Error: Datos incompatibles, el operando *= solo acepta enteros ");
            return -1;
        }

        public override object VisitElevadoigual_AS_AST(ParserGrammar.Elevadoigual_AS_ASTContext context)
        {
            // '^=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando ^= solo acepta enteros");
                return -1;
            }
            return -9;
        }

        public override object VisitDoblemenorqueigual_AS_AST(ParserGrammar.Doblemenorqueigual_AS_ASTContext context)
        {
            // '<<=' Integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando <<= solo acepta enteros");
                return -1;
            }
            return -9;
        }

        public override object VisitDoblemayorqueigual_AS_AST(ParserGrammar.Doblemayorqueigual_AS_ASTContext context)
        {
            // '>>=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando >>= solo acepta enteros ");
            }
            return -9;
        }

        public override object VisitAndelevadoigual_AS_AST(ParserGrammar.Andelevadoigual_AS_ASTContext context)
        {
            //'&^=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando &^= solo acepta enteros ");
                return -1;
            }
            return -9;
        }

        public override object VisitPorcentaje_AS_AST(ParserGrammar.Porcentaje_AS_ASTContext context)
        {
            // '%=' integer
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if(exp1 != -9 || exp2 != -9)
            {
                //error de tipos
                listaErrores.addError("Error: Datos incompatibles, el operando %= solo acepta enteros ");
                return -1;
            }
            return -9;
        }

        public override object VisitDivigual_AS_AST(ParserGrammar.Divigual_AS_ASTContext context)
        {
            // '/=' integer, float32
            int exp1 = (int) Visit(context.expression(0));
            int exp2 = (int) Visit(context.expression(1));

            if ((exp1 == -9 && exp2 == -9) || (exp1 == -9 && exp2 == -10) || (exp1 == -10 && exp2 == -9) || (exp1 == -10 && exp2 == -10))
                return -10;
            //error de tipos
            listaErrores.addError("Error: Datos incompatibles, el operando /=  solo acepta enteros ");
            return -1 ;
        }

        public override object VisitIfblock_IF_AST(ParserGrammar.Ifblock_IF_ASTContext context)
        {
            Visit(context.expression());
            Visit(context.block());
            return 0;
        }

        public override object VisitIfelseif_IF_AST(ParserGrammar.Ifelseif_IF_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            if(exp==-1)
                listaErrores.addError("Error: Expresion no válida para el operador 'if'. Linea: "+context.IF().Symbol.Line);
            Visit(context.block());
            Visit(context.ifStatement());

            return -18;
        }

        public override object VisitIfelseblock_IF_AST(ParserGrammar.Ifelseblock_IF_ASTContext context)
        {

            int exp= (int)Visit(context.expression());

            if(exp==-1)
                listaErrores.addError("Error: Expresion no válida para el operador 'if'. Linea: "+context.IF().Symbol.Line);
            Visit(context.block(0));
            Visit(context.block(1));
            return -18;
        }

        public override object VisitIfpycomablock_IF_AST(ParserGrammar.Ifpycomablock_IF_ASTContext context)
        {
            Visit(context.simpleStatement());
            int exp = (int)Visit(context.expression());
            if(exp ==-1)
                listaErrores.addError("Error: Expresion no válida para el operador 'if'. Linea: "+context.IF().Symbol.Line);
            Visit(context.block());
            return -18;
        }

        public override object VisitIfpycomablockelseif_IF_AST(ParserGrammar.Ifpycomablockelseif_IF_ASTContext context)
        {
            Visit(context.simpleStatement());
            int exp = (int) Visit(context.expression());
            if(exp==-1)
                listaErrores.addError("Error: Expresion no válida para el operador 'if'. Linea: "+context.IF().Symbol.Line);
            Visit(context.block());
            Visit(context.ifStatement());
            return -18;
        }

        public override object VisitIfpycomablockelseblock_IF_AST(ParserGrammar.Ifpycomablockelseblock_IF_ASTContext context)
        {
            Visit(context.simpleStatement());
            int exp = (int) Visit(context.expression());
            if(exp==-1)
                listaErrores.addError("Error: Expresion no válida para el operador 'if'. Linea: "+context.IF().Symbol.Line);
            Visit(context.block(0));
            Visit(context.block(1));
            return -18;
        }

        public override object VisitForblock_LOOP_AST(ParserGrammar.Forblock_LOOP_ASTContext context)
        {
            Visit(context.block());
            return -19;
        }

        public override object VisitForexpblock_LOOP_AST(ParserGrammar.Forexpblock_LOOP_ASTContext context)
        {
           // FOR expression block
           int exp= (int) Visit(context.expression());
           if (exp == -1)
           {
               listaErrores.addError("Error: La expresión no es válida para la función 'for'. Linea:"+context.FOR().Symbol.Line);
           }
           Visit(context.block());
           return -19;
        }

        public override object VisitForpycomaexp_LOOP_AST(ParserGrammar.Forpycomaexp_LOOP_ASTContext context)
        {
          //  | FOR simpleStatement PyCOMA expression PyCOMA simpleStatement block
            Visit(context.simpleStatement(0));
            int exp = (int) Visit(context.expression());
            if(exp == -1)
                listaErrores.addError("Error: La expresión no es válida para la función 'for'. Linea:"+context.FOR().Symbol.Line);
            Visit(context.simpleStatement(1));
            Visit(context.block());
            return -19;
        }

        public override object VisitForpycomablock_LOOP_AST(ParserGrammar.Forpycomablock_LOOP_ASTContext context)
        {
            // FOR simpleStatement PyCOMA PyCOMA simpleStatement block
            Visit(context.simpleStatement(0));
            Visit(context.simpleStatement(1));
            Visit(context.block());
            return -19;
        }

        public override object VisitSwitchSSexp_SWITCH_AST(ParserGrammar.SwitchSSexp_SWITCH_ASTContext context)
        {
            int statement = (int) Visit(context.simpleStatement());
            int exp = (int) Visit(context.expression());
            Visit(context.expressionCaseClauseList());
            return -16;
        }

        public override object VisitSwitchexp_SWITCH_AST(ParserGrammar.Switchexp_SWITCH_ASTContext context)
        {
            int exp = (int) Visit(context.expression());
            Visit(context.expressionCaseClauseList());
            return -16;
        }

        public override object VisitSwitchSS_SWITCH_AST(ParserGrammar.SwitchSS_SWITCH_ASTContext context)
        {
            Visit(context.simpleStatement());
            Visit(context.expressionCaseClauseList());
            return -16;
        }

        public override object VisitSwitchexpcase_SWITCH_AST(ParserGrammar.Switchexpcase_SWITCH_ASTContext context)
        {
            Visit(context.expressionCaseClauseList());
            return -16;
        }

        public override object VisitExpressionCaseClauseList_AST(ParserGrammar.ExpressionCaseClauseList_ASTContext context)
        {
            Visit(context.expressionCaseClause());
            Visit(context.expressionCaseClauseList());
            return 0;
        }

        public override object VisitEpsilon_EXPCASE_AST(ParserGrammar.Epsilon_EXPCASE_ASTContext context)
        {
            return 0;
        }

        public override object VisitExpressionCaseClause_AST(ParserGrammar.ExpressionCaseClause_ASTContext context)
        {
            Visit(context.expressionSwitchCase());
            Visit(context.statementList());
            return 0;
        }

        public override object VisitCase_EXPSWITCH_AST(ParserGrammar.Case_EXPSWITCH_ASTContext context)
        {
            List<int> tipos= (List<int>)Visit(context.expressionList());
            return 0;
        }

        public override object VisitDefault_EXPSWITCH_AST(ParserGrammar.Default_EXPSWITCH_ASTContext context)
        {
            return 0;
        }
    }
}
"""

