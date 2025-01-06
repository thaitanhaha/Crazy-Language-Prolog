grammar Cra2Pre;

options {
    language=Python3;
}

@lexer::header {
from lexererr import *
}

program	returns [s] 
	: PROGRAM ID SEMICOLON v=var_decl_part f=func_decl_part b=block_stmt DOT EOF
	  {$s = "[[" + $v.s + "],[" + $f.s + "]," + $b.s + "]. " }
	;

var_decl_part returns [s]
	: v=var_decl_list {$s = ",".join($v.results)}
	| {$s = ''}
	;

var_decl_list returns [results]
	: vc1=var_const_decl vl=var_decl_list {$results = [$vc1.s] + $vl.results}
	| vc2=var_const_decl {$results = [$vc2.s]}
	;

var_const_decl returns [s]
	: v=var_decl {$s=$v.s} | c=const_decl {$s=$c.s}
	;

var_decl returns [s]
    : VAR l=id_list COLON t=ctype SEMICOLON 
	{$s = ",".join(f"var({id},{$t.s})" for id in $l.results)}
    ;

id_list returns [results]
    : ID COMMA l=id_list {$results = [$ID.text] + $l.results}
    | ID {$results = [$ID.text]}
    ;

const_decl returns [s]
	: CONST ID EQUAL l=literal SEMICOLON {$s = f"const({$ID.text},{$l.s})"}
	;

func_decl_part returns [s]
	: f=func_decl_list {$s = ",".join($f.results)}
	| {$s = ''}
	;

func_decl_list returns [results]
	: fp1=func_procedure_decl fdl=func_decl_list {$results = [$fp1.s] + $fdl.results}
	| fp2=func_procedure_decl {$results = [$fp2.s]}
	;

func_procedure_decl returns [s]
	: f=func_decl {$s=$f.s} | p=procedure_decl {$s=$p.s}
	;

func_decl returns [s]
	: FUNCTION ID LR pl=param_list RR COLON pt=primitive_type SEMICOLON b=block_stmt SEMICOLON
	{$s = f"func({$ID.text},[{$pl.s}],{$pt.s},{$b.s})"}
	;

procedure_decl returns [s]
	: PROCEDURE ID LR pl=param_list RR SEMICOLON b=block_stmt SEMICOLON
	{$s = f"proc({$ID.text},[{$pl.s}],{$b.s})"}
	;

param_list returns [s]
	: p=params {$s = ",".join($p.results)}
	| {$s = ''}
	;

params returns [results]
	: p1=param SEMICOLON ps=params {$results = [$p1.s] + $ps.results}
	| p2=param {$results = [$p2.s]}
	;

param returns [s]
	: o=one_param {$s=$o.s} | m=mul_param {$s=$m.s}
	;

one_param returns [s]
	: ID COLON t=ctype {$s = f"par({$ID.text},{$t.s})"}
	;

mul_param returns [s]
	: l=id_list COLON t=ctype
	{$s = ",".join(f"par({id},{$t.s})" for id in $l.results)}
	;
	
ctype returns [s] 
	: p=primitive_type {$s = $p.s} | a=array_type {$s = $a.s}
	;

primitive_type returns [s]
	: INTEGER {$s = "integer" }
	| REAL	  {$s = "real" }
	| BOOLEAN {$s = "boolean" }
	| STRING  {$s = "string" }
	;

array_type returns [s] 
	: ARRAY a=array_size_list OF t=primitive_type
	{size = ",".join($a.results)
$s = f"arr([{size}],{$t.s})"}
	;

array_size_list returns [results]
	: as1=array_size asl=array_size_list {$results = [$as1.s] + $asl.results}
	| as2=array_size {$results = [$as2.s]}
	;

array_size returns [s]
	: LS INTEGER_LIT RS {$s = $INTEGER_LIT.text}
	;
	
stmt_list returns [s]
	: st=stmts {$s = ",".join($st.results)}
	| {$s = ''}
	;

stmts returns [results]
	: st1=stmt ss=stmts {$results = [$st1.s] + $ss.results}
	| st2=stmt {$results = [$st2.s]}
	;

stmt returns [s]
	: t1=var_const_decl {$s = $t1.s}
	| t2=assign_stmt {$s = $t2.s}
	| t3=block_stmt {$s = $t3.s}
	| t4=if_stmt {$s = $t4.s}
	| t5=call_stmt {$s = $t5.s}
	| t6=while_stmt {$s = $t6.s}
	| t7=do_while_stmt {$s = $t7.s}
	| t8=loop_do_stmt {$s = $t8.s}
	| t9=break_stmt {$s = $t9.s}
	| t10=continue_stmt {$s = $t10.s}
	;

assign_stmt returns [s] 
	: l=lhs ASSOPE e=expr SEMICOLON 
	{$s = f"assign({$l.s},{$e.s})"}
	;

lhs returns [s]
	: e=expr_8 {$s = $e.s}
	| ID {$s = $ID.text}
	;

block_stmt returns [s]
	: BEGIN st=stmt_list END
	{$s = f"[{$st.s}]"}
	;

if_stmt returns [s] 
	: IF e1=expr THEN s1=stmt ELSE s2=stmt {$s = f"if({$e1.s},{$s1.s},{$s2.s})"}
	| IF e2=expr THEN s3=stmt {$s = f"if({$e2.s},{$s3.s})"}
	;

call_stmt returns [s] 
	: c=call_expr SEMICOLON {$s = $c.s}
	;

call_expr returns [s]
	: ID LR e=expr_list RR {$s = f"call({$ID.text},[{$e.s}])"}
	;

while_stmt returns [s] 
	: WHILE e=expr DO st=stmt {$s = f"while({$e.s},{$st.s})"}
	;

do_while_stmt returns [s] 
	: DO l=stmt_list WHILE e=expr SEMICOLON {$s = f"do([{$l.s}],{$e.s})"}
	;

loop_do_stmt returns [s] 
	: LOOP e=expr DO st=stmt {$s = f"loop({$e.s},{$st.s})"}
	;

break_stmt returns [s] 
	: BREAK SEMICOLON {$s = f"break(null)"}
	;

continue_stmt returns [s] 
	: CONTINUE SEMICOLON {$s = f"continue(null)"}
	;
	
expr_list returns [s]
	: e=exprs {$s = ",".join($e.results)}
	| {$s = ""} 
	;

exprs returns [results]
	: e1=expr COMMA es=exprs {$results = [$e1.s] + $es.results}
	| e2=expr {$results = [$e2.s]} 
	;

expr returns [s]
	: e1=expr (ADD e2=expr2 {$s = f"add({$e1.s},{$e2.s})"} | SUB e2=expr2 {$s = f"sub({$e1.s},{$e2.s})"})
	| e=expr2 {$s = $e.s}
	;

expr2 returns [s]
	: e1=expr2 (MUL e2=expr3 {$s = f"times({$e1.s},{$e2.s})"} | DIVV e2=expr3 {$s = f"rdiv({$e1.s},{$e2.s})"} | DIV e2=expr3 {$s = f"idiv({$e1.s},{$e2.s})"} | MOD e2=expr3 {$s = f"imod({$e1.s},{$e2.s})"}) 
	| e=expr3 {$s = $e.s}
	;

expr3 returns [s]
	: e1=expr3 (EQUAL e2=expr4 {$s = f"eql({$e1.s},{$e2.s})"} | DIFF e2=expr4 {$s = f"ne({$e1.s},{$e2.s})"})
	| e=expr4 {$s = $e.s}
	;

expr4 returns [s]
	: e1=expr4 (LESS e2=expr5 {$s = f"less({$e1.s},{$e2.s})"} | GREATER e2=expr5 {$s = f"greater({$e1.s},{$e2.s})"} | LE e2=expr5 {$s = f"le({$e1.s},{$e2.s})"} | GE e2=expr5 {$s = f"ge({$e1.s},{$e2.s})"})
	| e=expr5 {$s = $e.s}
	;

expr5 returns [s]
	: e1=expr5 OR e2=expr6 {$s = f"bor({$e1.s},{$e2.s})"}
	| e=expr6 {$s = $e.s}
	;

expr6 returns [s]
	: e1=expr6 AND e2=expr7 {$s = f"band({$e1.s},{$e2.s})"}
	| e=expr7 {$s = $e.s}
	;

expr7 returns [s]
	: (SUB e1=expr7 {$s = f"sub({$e1.s})"} | NOT e2=expr7 {$s = f"bnot({$e2.s})"})
	| e=expr8 {$s = $e.s}
	;

expr_8 returns [s]
	: ID i=index_operators 
	{temp = ",".join($i.results)
$s = f"ele({$ID.text},[{temp}])"}
	;

expr8 returns [s]
	: e1=expr_8 {$s = $e1.s}
	| e2=expr9 {$s = $e2.s}
	;

expr9 returns [s]
	: LR e=expr RR {$s = $e.s}
	| l=literal {$s = $l.s}
	| a = array_literal {$s = $a.s}
	| ID {$s = $ID.text}
	| c=call_expr {$s = $c.s}
	;

index_operators returns [results]
	: io=index_op ios=index_operators {$results = [$io.s] + $ios.results}
	| i=index_op {$results = [$i.s]}
	;

index_op returns [s]
	: LS e=expr RS {$s = $e.s}
	;

array_literal returns [s]
	: LS a=array_element_list RS {$s = f"array([{$a.s}])"}
	;

array_element_list returns [s]
	: a=array_elements {$s = ",".join($a.results)}
	;

array_elements returns [results]
	: ae=array_element COMMA aes=array_elements {$results = [$ae.s] + $aes.results}
	| a=array_element {$results = [$a.s]}
	;

array_element returns [s]
	: a=array_literal {$s = $a.s}
	| l=literal {$s = $l.s}
	;

literal returns [s]
	: INTEGER_LIT {$s = $INTEGER_LIT.text} 
	| REAL_LIT {$s = $REAL_LIT.text} 
	| BOOLEAN_LIT{$s = $BOOLEAN_LIT.text} 
	| STRING_LIT 
	{temp = $STRING_LIT.text
res = "\"" + temp.replace("''", "\\\'").replace("\"", "\\\"") + "\""
$s = f"str({res})"
	}
	;

PROGRAM		: 'program' ;
VAR			: 'var';
BEGIN		: 'begin' ;
END			: 'end' ;
BOOLEAN		: 'boolean';
INTEGER		: 'integer' ;
REAL		: 'real' ;
STRING		: 'string';
CONST		: 'const';
AND			: 'and';
CONTINUE	: 'continue';
OF			: 'of';
THEN		: 'then';
ARRAY		: 'array';
DIV			: 'div';
FUNCTION	: 'function';
OR			: 'or';
DO			: 'do';
IF			: 'if';
LOOP		: 'loop';
PROCEDURE	: 'procedure';
BREAK		: 'break';
ELSE		: 'else';
MOD			: 'mod';
WHILE		: 'while';
NOT			: 'not';
ASSOPE		: ':=' ;
EQUAL		: '=' ;
DIFF		: '<>' ;
DOT			: '.' ;
COMMA		: ',' ;
SEMICOLON 	: ';' ;
COLON		: ':' ;
LS			: '[';
RS			: ']';
LR			: '(';
RR			: ')';
ADD			: '+';
SUB			: '-';
MUL			: '*';
DIVV		: '/';
LESS		: '<';
GREATER 	: '>';
LE			: '<=';
GE			: '>=';

fragment DIGIT: [0-9];
fragment DIGIT_S: [1-9];
fragment LOWER_CHAR: [a-z];
fragment UPPER_CHAR: [A-Z];
fragment INT_PART: (DIGIT_S DIGIT*) | '0';
fragment FRAC_PART: '.' (DIGIT* DIGIT_S | '0');
fragment EX_PART: ('e' | 'E') ('-' | )? DIGIT+;
fragment STRING_CHAR: ~[\n\t'\\] | ESCSEQ | [']['];
fragment ESCSEQ: '\\' [nt\\];

INTEGER_LIT: (DIGIT_S DIGIT*) | '0';
REAL_LIT: INT_PART FRAC_PART EX_PART
		| INT_PART FRAC_PART
		| INT_PART EX_PART
        | FRAC_PART EX_PART
        | FRAC_PART
        ;
BOOLEAN_LIT: 'true' | 'false';
STRING_LIT: ['] STRING_CHAR* ['] {self.text = self.text[1:-1]};
ID: LOWER_CHAR (LOWER_CHAR | UPPER_CHAR | DIGIT)*;

LINE_COMMENT: '//' ~[\n]* -> skip;
BLOCK_COMMENT: '/*' ( . )*? '*/' -> skip;
WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: ['] STRING_CHAR* ('\r\n' | '\n' | EOF) {
	if (len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
          raise UncloseString(self.text[0:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[0:-1])
	else:
          raise UncloseString(self.text[0:])
};
fragment ILLEGAL_ESCSEQ: '\\' ~[nt\\];
ILLEGAL_ESCAPE: ['] STRING_CHAR* ILLEGAL_ESCSEQ {raise IllegalEscape(self.text[0:])};
