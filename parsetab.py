
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIN COMA COMILLA COS DIV DLLAVE ELSE EQUALS EXP FLOAT FROM GET IF ILLAVE IMPORT IN INPUT KEYS LCORCH LPAREN MATH MINUS NAME NUMBER PLUS POINT PRINT RCORCH RETURN RPAREN SIN SQRT TIMES TWOPOINTopt : assign\n            | if\n            | else\n            | funcionReturn\n            | funcionFrom\n            | sentenciaPrintassign : var string\n            | var diccionario\n            | var input\n            | var cargarDatoDiccionario\n            | var restaLongitudAltitud\n            | var funcionCalcularA\n            | var funcionCalcularC\n            | var funcionCalcularKminput : INPUT LPAREN string RPARENdiccionario : ILLAVE info DLLAVE info : keys TWOPOINT lista\n            | keys TWOPOINT lista COMA infokeys : string\n            | number\n            | floatlista : LCORCH contenido RCORCHcontenido : items\n                | items COMA contenidoitems : string\n            | number\n            | float\n            | listavar : text EQUALStext : NAMEstring : COMILLA text COMILLAfloat : FLOATnumber : NUMBERcargarDatoDiccionario :  obtencionValorDiccionario obtencionIndexobtencionValorDiccionario : text POINT GET LPAREN text RPARENobtencionIndex : LCORCH number RCORCHsentenciaPrint : PRINT LPAREN string RPAREN\n                | PRINT LPAREN string COMA text RPAREN\n                | PRINT LPAREN text RPARENif : IF LPAREN condicion RPAREN TWOPOINT\n                | IF condicion TWOPOINTelse : ELSE TWOPOINTcondicion : text IN funcionItems AND text IN funcionItemsfuncionItems : text POINT KEYS LPAREN RPARENrestaLongitudAltitud : text MINUS textfuncionCalcularA : funcionSinGeneral TIMES funcionSin2funcionSinGeneral : funcionSin1 PLUS funcionCosfuncionSin1 : SIN LPAREN text DIV number RPAREN EXP number funcionSin2 : SIN LPAREN text DIV number RPAREN EXP number funcionCos : COS LPAREN text RPAREN TIMES COS LPAREN text RPARENfuncionCalcularC : number TIMES ASIN LPAREN SQRT LPAREN text RPAREN RPARENfuncionCalcularKm : number TIMES textfuncionReturn : RETURN textfuncionFrom : FROM MATH IMPORT TIMES'
    
_lr_action_items = {'IF':([0,],[9,]),'ELSE':([0,],[10,]),'RETURN':([0,],[11,]),'FROM':([0,],[13,]),'PRINT':([0,],[14,]),'NAME':([0,8,9,11,24,34,39,41,43,55,57,60,83,85,90,92,96,118,122,136,],[15,15,15,15,15,15,-29,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'$end':([1,2,3,4,5,6,7,15,16,17,18,19,20,21,22,23,32,37,38,52,59,64,65,67,71,74,81,82,84,88,89,94,112,135,137,],[0,-1,-2,-3,-4,-5,-6,-30,-7,-8,-9,-10,-11,-12,-13,-14,-33,-42,-53,-34,-41,-31,-45,-16,-46,-52,-54,-37,-39,-15,-36,-40,-38,-51,-49,]),'COMILLA':([8,15,26,39,41,42,51,87,99,116,],[24,-30,24,-29,24,64,24,24,24,24,]),'ILLAVE':([8,39,],[26,-29,]),'INPUT':([8,39,],[27,-29,]),'NUMBER':([8,26,39,53,87,93,99,116,117,127,134,],[32,32,-29,32,32,32,32,32,32,32,32,]),'SIN':([8,39,54,],[33,-29,72,]),'LPAREN':([9,14,27,33,66,72,73,76,107,110,132,],[34,41,51,57,85,90,91,92,118,121,136,]),'TWOPOINT':([10,32,35,46,47,48,49,50,64,78,128,129,],[37,-33,59,68,-19,-20,-21,-32,-31,94,-44,-43,]),'EQUALS':([12,15,],[39,-30,]),'MATH':([13,],[40,]),'MINUS':([15,25,],[-30,43,]),'POINT':([15,25,79,],[-30,44,95,]),'IN':([15,36,111,],[-30,60,122,]),'RPAREN':([15,32,58,62,63,64,69,97,98,108,109,121,124,125,128,129,131,138,],[-30,-33,78,82,84,-31,88,112,113,119,120,128,130,131,-44,-43,135,139,]),'DIV':([15,77,106,],[-30,93,117,]),'FLOAT':([26,87,99,116,],[50,50,50,50,]),'LCORCH':([28,68,87,113,116,],[53,87,87,-35,87,]),'TIMES':([29,30,32,61,75,119,139,],[54,55,-33,81,-47,126,-50,]),'PLUS':([31,32,133,],[56,-33,-48,]),'RCORCH':([32,50,64,70,100,101,102,103,104,105,115,123,],[-33,-32,-31,89,115,-23,-25,-26,-27,-28,-22,-24,]),'COMA':([32,50,62,64,86,101,102,103,104,105,115,],[-33,-32,83,-31,99,116,-25,-26,-27,-28,-22,]),'IMPORT':([40,],[61,]),'GET':([44,],[66,]),'DLLAVE':([45,86,114,115,],[67,-17,-18,-22,]),'ASIN':([55,],[73,]),'COS':([56,126,],[76,132,]),'AND':([80,128,],[96,-44,]),'SQRT':([91,],[107,]),'KEYS':([95,],[110,]),'EXP':([120,130,],[127,134,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'opt':([0,],[1,]),'assign':([0,],[2,]),'if':([0,],[3,]),'else':([0,],[4,]),'funcionReturn':([0,],[5,]),'funcionFrom':([0,],[6,]),'sentenciaPrint':([0,],[7,]),'var':([0,],[8,]),'text':([0,8,9,11,24,34,41,43,55,57,60,83,85,90,92,96,118,122,136,],[12,25,36,38,42,36,63,65,74,77,79,97,98,106,108,111,125,79,138,]),'string':([8,26,41,51,87,99,116,],[16,47,62,69,102,47,102,]),'diccionario':([8,],[17,]),'input':([8,],[18,]),'cargarDatoDiccionario':([8,],[19,]),'restaLongitudAltitud':([8,],[20,]),'funcionCalcularA':([8,],[21,]),'funcionCalcularC':([8,],[22,]),'funcionCalcularKm':([8,],[23,]),'obtencionValorDiccionario':([8,],[28,]),'funcionSinGeneral':([8,],[29,]),'number':([8,26,53,87,93,99,116,117,127,134,],[30,48,70,103,109,48,103,124,133,137,]),'funcionSin1':([8,],[31,]),'condicion':([9,34,],[35,58,]),'info':([26,99,],[45,114,]),'keys':([26,99,],[46,46,]),'float':([26,87,99,116,],[49,104,49,104,]),'obtencionIndex':([28,],[52,]),'funcionSin2':([54,],[71,]),'funcionCos':([56,],[75,]),'funcionItems':([60,122,],[80,129,]),'lista':([68,87,116,],[86,105,105,]),'contenido':([87,116,],[100,123,]),'items':([87,116,],[101,101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> opt","S'",1,None,None,None),
  ('opt -> assign','opt',1,'p_option','Parser.py',10),
  ('opt -> if','opt',1,'p_option','Parser.py',11),
  ('opt -> else','opt',1,'p_option','Parser.py',12),
  ('opt -> funcionReturn','opt',1,'p_option','Parser.py',13),
  ('opt -> funcionFrom','opt',1,'p_option','Parser.py',14),
  ('opt -> sentenciaPrint','opt',1,'p_option','Parser.py',15),
  ('assign -> var string','assign',2,'p_assign','Parser.py',19),
  ('assign -> var diccionario','assign',2,'p_assign','Parser.py',20),
  ('assign -> var input','assign',2,'p_assign','Parser.py',21),
  ('assign -> var cargarDatoDiccionario','assign',2,'p_assign','Parser.py',22),
  ('assign -> var restaLongitudAltitud','assign',2,'p_assign','Parser.py',23),
  ('assign -> var funcionCalcularA','assign',2,'p_assign','Parser.py',24),
  ('assign -> var funcionCalcularC','assign',2,'p_assign','Parser.py',25),
  ('assign -> var funcionCalcularKm','assign',2,'p_assign','Parser.py',26),
  ('input -> INPUT LPAREN string RPAREN','input',4,'p_input','Parser.py',30),
  ('diccionario -> ILLAVE info DLLAVE','diccionario',3,'p_diccionario','Parser.py',34),
  ('info -> keys TWOPOINT lista','info',3,'p_info','Parser.py',38),
  ('info -> keys TWOPOINT lista COMA info','info',5,'p_info','Parser.py',39),
  ('keys -> string','keys',1,'p_keys','Parser.py',46),
  ('keys -> number','keys',1,'p_keys','Parser.py',47),
  ('keys -> float','keys',1,'p_keys','Parser.py',48),
  ('lista -> LCORCH contenido RCORCH','lista',3,'p_lista','Parser.py',52),
  ('contenido -> items','contenido',1,'p_contenido','Parser.py',56),
  ('contenido -> items COMA contenido','contenido',3,'p_contenido','Parser.py',57),
  ('items -> string','items',1,'p_items','Parser.py',64),
  ('items -> number','items',1,'p_items','Parser.py',65),
  ('items -> float','items',1,'p_items','Parser.py',66),
  ('items -> lista','items',1,'p_items','Parser.py',67),
  ('var -> text EQUALS','var',2,'p_var','Parser.py',71),
  ('text -> NAME','text',1,'p_text','Parser.py',76),
  ('string -> COMILLA text COMILLA','string',3,'p_string','Parser.py',80),
  ('float -> FLOAT','float',1,'p_float','Parser.py',84),
  ('number -> NUMBER','number',1,'p_number','Parser.py',88),
  ('cargarDatoDiccionario -> obtencionValorDiccionario obtencionIndex','cargarDatoDiccionario',2,'p_cargarDatoDiccionario','Parser.py',92),
  ('obtencionValorDiccionario -> text POINT GET LPAREN text RPAREN','obtencionValorDiccionario',6,'p_obtencionValorDiccionario','Parser.py',97),
  ('obtencionIndex -> LCORCH number RCORCH','obtencionIndex',3,'p_obtencionIndex','Parser.py',101),
  ('sentenciaPrint -> PRINT LPAREN string RPAREN','sentenciaPrint',4,'p_sentenciaPrint','Parser.py',105),
  ('sentenciaPrint -> PRINT LPAREN string COMA text RPAREN','sentenciaPrint',6,'p_sentenciaPrint','Parser.py',106),
  ('sentenciaPrint -> PRINT LPAREN text RPAREN','sentenciaPrint',4,'p_sentenciaPrint','Parser.py',107),
  ('if -> IF LPAREN condicion RPAREN TWOPOINT','if',5,'p_if','Parser.py',114),
  ('if -> IF condicion TWOPOINT','if',3,'p_if','Parser.py',115),
  ('else -> ELSE TWOPOINT','else',2,'p_else','Parser.py',122),
  ('condicion -> text IN funcionItems AND text IN funcionItems','condicion',7,'p_condicion','Parser.py',126),
  ('funcionItems -> text POINT KEYS LPAREN RPAREN','funcionItems',5,'p_funcionItems','Parser.py',131),
  ('restaLongitudAltitud -> text MINUS text','restaLongitudAltitud',3,'p_restaLongitudAltitud','Parser.py',135),
  ('funcionCalcularA -> funcionSinGeneral TIMES funcionSin2','funcionCalcularA',3,'p_funcionCalcularA','Parser.py',139),
  ('funcionSinGeneral -> funcionSin1 PLUS funcionCos','funcionSinGeneral',3,'p_funcionSinGeneral','Parser.py',143),
  ('funcionSin1 -> SIN LPAREN text DIV number RPAREN EXP number','funcionSin1',8,'p_funcionSin1','Parser.py',147),
  ('funcionSin2 -> SIN LPAREN text DIV number RPAREN EXP number','funcionSin2',8,'p_funcionSin2','Parser.py',152),
  ('funcionCos -> COS LPAREN text RPAREN TIMES COS LPAREN text RPAREN','funcionCos',9,'p_funcionCos','Parser.py',157),
  ('funcionCalcularC -> number TIMES ASIN LPAREN SQRT LPAREN text RPAREN RPAREN','funcionCalcularC',9,'p_funcionCalcularC','Parser.py',162),
  ('funcionCalcularKm -> number TIMES text','funcionCalcularKm',3,'p_funcionCalcularKm','Parser.py',167),
  ('funcionReturn -> RETURN text','funcionReturn',2,'p_funcionReturn','Parser.py',172),
  ('funcionFrom -> FROM MATH IMPORT TIMES','funcionFrom',4,'p_funcionFrom','Parser.py',176),
]
