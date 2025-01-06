%main program
go :- 	open('input.txt',read,Stream),
		read_term(Stream,Y,[]),
		close(Stream),
		open('output.txt',write,Stream1),
		set_output(Stream1),
		catch(reduce_prog(Y),Exception,process(Exception))
		,close(Stream1).
% The first three predicates are used to do type checking while the last two do executing the input program
reduce_prog([Var,Func,Body]) :-
		create_env(Var,env([],0,0),Env),
		type_check_func(Env,Func,Env1),
		%type_check_body(Env1,Body),
		type_check_body_main(Env1,Body),
		create_runtime_env(Env1,REnv),
		reduce_stmt(config(Body,REnv),_).

set_global_env_length(Value) :- assert(global_env(Value)).
get_global_env_length(Value) :- global_env(Value).
get_global_env(_, 0, []).
get_global_env(env(List,X,Y),L,env(Result,X,Y)) :- L>0, length(List,TL), Start is TL-L, sublist(List,Start,Result).
sublist(List, StartIndex, Result) :- length(Prefix, StartIndex), append(Prefix, Result, List).

:- dynamic loop_depth/1.
loop_depth(0).
enter_loop_context :- (retract(loop_depth(D)) -> D1 is D + 1; D1 = 1), assert(loop_depth(D1)).
exit_loop_context :- (retract(loop_depth(D)), D > 1 -> D1 is D - 1, assert(loop_depth(D1)); true).
in_loop_context(break(null)) :- loop_depth(D), (D > 0 -> true; throw(break_not_in_loop(break(null)))).
in_loop_context(continue(null)) :- loop_depth(D), (D > 0 -> true; throw(continue_not_in_loop(continue(null)))).

%For type checking

% Error handling

% Type checking

process(type_mismatch(X)):- write('Type mismatch: '),write(X),!. 
process(undeclare_identifier(X)):- write('Undeclared identifier: '),write(X),!. 
process(wrong_number_of_argument(X)):- write('Wrong number of arguments: '),write(X),!.
process(redeclare_identifier(X)):- write('Redeclared identifier: '),write(X),!. 
process(redeclare_function(X)):- write('Redeclared function: '),write(X),!. 
process(redeclare_procedure(X)):- write('Redeclared procedure: '),write(X),!. 
process(undeclare_function(X)):- write('Undeclared function: '),write(X),!. 
process(undeclare_procedure(X)):- write('Undeclared procedure: '),write(X),!. 
process(break_not_in_loop(X)):- write('Break not in a loop: '),write(X),!. 
process(continue_not_in_loop(X)):- write('Continue not in a loop: '),write(X),!. 
process(cannot_assign(X)) :- write('Cannot assign to a constant: '),write(X),!.

% Runtime error
process(outofbound(X)):- write('Index out of bound: '),write(X),!.
process(invalid_expression(X)):- write('Invalid expression: '),write(X),!.

%lookup(symbol table,id,entry)
lookup(env([],_,_),X,_) :- throw(undeclare_identifier(X)).
lookup(env([id(X,Y,Z,V)|_],_,_),X,id(X,Y,Z,V)) :- !.
lookup(env([id(X,Y,Z1,V)|_],_,_),X,id(X,Y,Z2,V)) :- Z1 \= Z2,!,fail.
lookup(env([_|L],B,T),X,Y) :- lookup(env(L,B,T),X,Y).

lookup_func(env([],_,_),X,_,Params) :- throw(undeclare_function(call(X,Params))).
lookup_func(env([id(X,Y,Z,V)|_],_,_),X,id(X,Y,Z,V),_) :- !.
lookup_func(env([id(X,Y,Z1,V)|_],_,_),X,id(X,Y,Z2,V),_) :- Z1 \= Z2,!,fail.
lookup_func(env([_|L],B,T),X,Y,Params) :- lookup_func(env(L,B,T),X,Y,Params).

lookup_proc(env([],_,_),X,_,Params) :- throw(undeclare_procedure(call(X,Params))).
lookup_proc(env([id(X,Y,Z,V)|_],_,_),X,id(X,Y,Z,V),_) :- !.
lookup_proc(env([id(X,Y,Z1,V)|_],_,_),X,id(X,Y,Z2,V),_) :- Z1 \= Z2,!,fail.
lookup_proc(env([_|L],B,T),X,Y,Params) :- lookup_proc(env(L,B,T),X,Y,Params).

%atom1 check X is an identifier in the input program
atom1(true) :- !,fail.
atom1(false) :- !,fail.
atom1([]) :- !,fail.
atom1(X) :- atom(X).

%check X is a boolean constant
boolean(true).
boolean(false).


%get type of expression Y based on the symbol table Env. T is the return type
%Get the type of an expression: ensures the expected type matches

get_type_expression(_,call(readInt,[]),integer) :- !.
get_type_expression(_,call(readReal,[]),real) :- !.
get_type_expression(_,call(readBool,[]),boolean) :- !.
get_type_expression(Env,Y,T) :- atom1(Y),!,lookup(Env,Y,id(Y,_,T,_)).
get_type_expression(_,Y,integer) :- integer(Y),!.
get_type_expression(_,Y,real) :- float(Y),!.
get_type_expression(_,str(_),string).
get_type_expression(_,Y,boolean) :- boolean(Y),!.

get_type_expression(Env,add(X,Y),Type) :- get_type_expression(Env,X,TypeX), get_type_expression(Env,Y,TypeY),
											((TypeX = integer, TypeY = integer, Type = integer); 
											((TypeX = integer; TypeX = real), (TypeY = integer; TypeY = real), Type = real)),!.
get_type_expression(_,add(X,Y),_) :- throw(type_mismatch(add(X,Y))).

get_type_expression(Env,sub(X,Y),Type) :- get_type_expression(Env,X,TypeX), get_type_expression(Env,Y,TypeY),
											((TypeX = integer, TypeY = integer, Type = integer); 
											((TypeX = integer; TypeX = real), (TypeY = integer; TypeY = real), Type = real)),!.
get_type_expression(_,sub(X,Y),_) :- throw(type_mismatch(sub(X,Y))).

get_type_expression(Env,times(X,Y),Type) :- get_type_expression(Env,X,TypeX), get_type_expression(Env,Y,TypeY),
											((TypeX = integer, TypeY = integer, Type = integer); 
											((TypeX = integer; TypeX = real), (TypeY = integer; TypeY = real), Type = real)),!.
get_type_expression(_,times(X,Y),_) :- throw(type_mismatch(times(X,Y))).

get_type_expression(Env,rdiv(X,Y),real) :- get_type_expression(Env,X,TypeX), get_type_expression(Env,Y,TypeY), 
											((TypeX = integer; TypeX = real), (TypeY = integer; TypeY = real)),!.
get_type_expression(_,rdiv(X,Y),_) :- throw(type_mismatch(rdiv(X,Y))).

get_type_expression(Env,idiv(X,Y),integer) :- get_type_expression(Env,X,integer),get_type_expression(Env,Y,integer),!.
get_type_expression(_,idiv(X,Y),_) :- throw(type_mismatch(idiv(X,Y))).
get_type_expression(Env,imod(X,Y),integer) :- get_type_expression(Env,X,integer),get_type_expression(Env,Y,integer),!.
get_type_expression(_,imod(X,Y),_) :- throw(type_mismatch(imod(X,Y))).

get_type_expression(Env,bnot(X),boolean) :- get_type_expression(Env,X,boolean),!.
get_type_expression(_,bnot(X,Y),_) :- throw(type_mismatch(bnot(X,Y))).
get_type_expression(Env,band(X,Y),boolean) :- get_type_expression(Env,X,boolean),get_type_expression(Env,Y,boolean),!.
get_type_expression(_,band(X,Y),_) :- throw(type_mismatch(band(X,Y))).
get_type_expression(Env,bor(X,Y),boolean) :- get_type_expression(Env,X,boolean),get_type_expression(Env,Y,boolean),!.
get_type_expression(_,bor(X,Y),_) :- throw(type_mismatch(bor(X,Y))).

get_type_expression(Env,greater(X,Y),boolean) :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = real),!.
get_type_expression(_,greater(X,Y),_) :- throw(type_mismatch(greater(X,Y))).
get_type_expression(Env,less(X,Y),boolean)    :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = real),!.
get_type_expression(_,less(X,Y),_) :- throw(type_mismatch(less(X,Y))).
get_type_expression(Env,ge(X,Y),boolean)      :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = real),!.
get_type_expression(_,ge(X,Y),_) :- throw(type_mismatch(ge(X,Y))).
get_type_expression(Env,le(X,Y),boolean)      :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = real),!.
get_type_expression(_,le(X,Y),_) :- throw(type_mismatch(le(X,Y))).

get_type_expression(Env,eql(X,Y),boolean) :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = boolean),!.
get_type_expression(_,eql(X,Y),_) :- throw(type_mismatch(eql(X,Y))).
get_type_expression(Env,ne(X,Y),boolean)  :- get_type_expression(Env,X,Type), get_type_expression(Env,Y,Type), (Type = integer; Type = boolean),!.
get_type_expression(_,ne(X,Y),_) :- throw(type_mismatch(ne(X,Y))).

get_type_expression(Env,ele(X,I),Type) :- lookup(Env,X,T), lookup_to_type(T,TY), TY = arr(_,Type), indices_all_int(Env,I), !.
get_type_expression(_,ele(X,I),_) :- throw(type_mismatch(ele(X,I))).

get_type_expression(_,array(_),_) :- !.

get_type_expression(Env,call(Name,Params),Type) :- 
	lookup_func(Env,Name,T,Params), lookup_to_type(T,TY), TY = func(_,Return,_), Type = Return.

indices_all_int(_, []).
indices_all_int(Env,[H|T]) :- get_type_expression(Env,H,integer), indices_all_int(Env,T).

% TODO
lookup_to_type(id(_, _, TY, _), TY).
type_check_assignment(Env,T,Y) :- lookup_to_type(T,TY), TY = func(_,Return,_), get_type_expression(Env,Y,Return).
type_check_assignment(Env,T,Y) :- lookup_to_type(T,TY), get_type_expression(Env,Y,TY).

type_to_stmts(proc(_, Stmts), Stmts).
type_to_stmts(func(_, _, Stmts), Stmts).
type_to_params(proc(Params, _), Params).
type_to_params(func(Params, _, _), Params).

check_params_length(Name, TY, Params_Called) :- 
	type_to_params(TY, Params), length(Params, L1), length(Params_Called, L2),
    (L1 == L2 -> true; throw(wrong_number_of_argument(call(Name,Params_Called)))).

check_params_types(Env, Name, TY, Params_Called) :- 
	type_to_params(TY, Params), check_types(Env,Name,Params,Params_Called,Params_Called).	
check_types(_,_,[],[],_).
check_types(Env, Name, [par(_,Type1)|Rest1], [Name2|Rest2], Params_Called) :- 
	get_type_expression(Env,Name2,Type2),
	(Type1 == Type2 -> check_types(Env,Name,Rest1,Rest2,Params_Called); throw(type_mismatch(call(Name,Params_Called)))). 


% type checking one statement

type_check_stmt(Env,X,Env) :- is_list(X), create_local_env(Env,Env1), type_check_body(Env1,X), !.
type_check_stmt(Env,var(X,T),Env2) :- create_env([var(X,T)],Env,Env2), !.
type_check_stmt(Env,const(X,Y),Env2) :- create_env([const(X,Y)],Env,Env2), !.
type_check_stmt(Env,assign(ele(X,I),Y),Env) :- 
	get_type_expression(Env,ele(X,I),Type), get_type_expression(Env,Y,TypeY), 
	(Type == TypeY -> true; throw(type_mismatch(assign(ele(X,I),Y)))), !.
type_check_stmt(Env,assign(X,Y),Env) :- lookup(Env,X,T), 
	(T=id(_,const,_,_) -> throw(cannot_assign(assign(X,Y))); type_check_assignment(Env,T,Y)), !.
type_check_stmt(Env,if(X,Y),Env) :- 
	get_type_expression(Env,X,Type),
	(Type == boolean -> type_check_stmt(Env,Y,Env); throw(type_mismatch(if(X,Y)))).
type_check_stmt(Env,if(X,Y,Z),Env) :- 
	get_type_expression(Env,X,Type),
	(Type == boolean -> type_check_stmt(Env,Y,Env),type_check_stmt(Env,Z,_); throw(type_mismatch(if(X,Y,Z)))).
type_check_stmt(Env, while(Cond, Body), Env) :-
    get_type_expression(Env, Cond, Type),
    (Type == boolean ->
        (enter_loop_context,
         type_check_stmt(Env, Body, _),
         exit_loop_context);
        throw(type_mismatch(while(Cond, Body)))
    ).

type_check_stmt(Env, do(Body, Cond), Env) :-
    get_type_expression(Env, Cond, Type),
    (Type == boolean ->
        (enter_loop_context,
         type_check_stmt(Env, Body, _),
         exit_loop_context);
        throw(type_mismatch(do(Body, Cond)))
    ).

type_check_stmt(Env, loop(Count, Body), Env) :- 
    get_type_expression(Env, Count, Type),
    (Type == integer ->
        (enter_loop_context,
         type_check_stmt(Env, Body, _),
         exit_loop_context);
        throw(type_mismatch(loop(Count, Body)))
    ).

type_check_stmt(Env, break(null), Env) :- in_loop_context(break(null)), !.
type_check_stmt(Env, continue(null), Env) :- in_loop_context(continue(null)), !.


type_check_stmt(Env,call(writeInt,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeInt,[X|Tail]))), !.
type_check_stmt(Env,call(writeInt,[X]),Env) :- get_type_expression(Env,X,integer), !.

type_check_stmt(Env,call(writeIntLn,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeIntLn,[X|Tail]))), !.
type_check_stmt(Env,call(writeIntLn,[X]),Env) :- get_type_expression(Env,X,integer), !.

type_check_stmt(Env,call(writeReal,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeReal,[X|Tail]))), !.
type_check_stmt(Env,call(writeReal,[X]),Env) :- get_type_expression(Env,X,real), !.

type_check_stmt(Env,call(writeRealLn,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeRealLn,[X|Tail]))), !.
type_check_stmt(Env,call(writeRealLn,[X]),Env) :- get_type_expression(Env,X,real), !.

type_check_stmt(Env,call(writeBool,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeBool,[X|Tail]))), !.
type_check_stmt(Env,call(writeBool,[X]),Env) :- get_type_expression(Env,X,boolean), !.

type_check_stmt(Env,call(writeBoolLn,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeBoolLn,[X|Tail]))), !.
type_check_stmt(Env,call(writeBoolLn,[X]),Env) :- get_type_expression(Env,X,boolean), !.

type_check_stmt(Env,call(writeStr,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeStr,[X|Tail]))), !.
type_check_stmt(Env,call(writeStr,[X]),Env) :- get_type_expression(Env,X,string), !.

type_check_stmt(Env,call(writeStrLn,[X|Tail]),Env) :- 
	Tail \= [], throw(wrong_number_of_argument(call(writeStrLn,[X|Tail]))), !.
type_check_stmt(Env,call(writeStrLn,[X]),Env) :- get_type_expression(Env,X,string), !.

type_check_stmt(Env,call(writeLn,[X]),Env) :- 
	X \= [], throw(wrong_number_of_argument(call(writeLn,[X]))), !.
type_check_stmt(Env,call(writeLn,[]),Env) :- true, !.

type_check_stmt(Env,call(Name,Params),Env) :- 
	lookup_proc(Env,Name,T,Params), lookup_to_type(T,TY),
	check_params_length(Name,TY,Params), check_params_types(Env,Name,TY,Params),!.


%type check one block
type_check_body(_,[]).
%type_check_body(env([L|_],_),[var(X,Y)|_]) :- has_declared(X,L,_),!,throw(redeclare_identifier(var(X,Y))).
%type_check_body(env([L|L2],T),[var(X,Y)|L1]) :- type_check_body(env([[id(X,var,Y,_)|L]|L2],T),L1),!.
type_check_body(Env,[X|L]) :- type_check_stmt(Env,X,Env2), type_check_body(Env2,L).
type_check_body_main(Env,[X|L]) :- create_local_env(Env,Env1), type_check_body(Env1,[X|L]).

%type checking a procedure
type_check_one_func(Env,proc(_,Y,Z)):- create_local_env(Env,Env1),
										create_env(Y,Env1,env(L,_,T)), type_check_body(env(L,0,T),Z).
type_check_one_func(Env,func(_,Y,_,Z)):- create_local_env(Env,Env1),
										create_env(Y,Env1,env(L,_,T)), type_check_body(env(L,0,T),Z).

%type checking a list of procedures
type_check_func(Env,[],Env).
type_check_func(_,[proc(X,_,_)|_],_) :- is_builtin(X),!,throw(redeclare_procedure(X)).
type_check_func(Env,[proc(X,_,_)|_],_) :- has_declared(X,Env),!,throw(redeclare_procedure(X)).
type_check_func(env(Env,B,T),[proc(X,Y,Z)|L],Env1) :- T1 is T+1,
											type_check_one_func(env([id(X,proc,proc(Y,Z),_)|Env],T1,T1),proc(X,Y,Z)), !,
											type_check_func(env([id(X,proc,proc(Y,Z),_)|Env],B,T1),L,Env1).

type_check_func(_,[func(X,_,_,_)|_],_) :- is_builtin(X),!,throw(redeclare_function(X)).
type_check_func(Env,[func(X,_,_,_)|_],_) :- has_declared(X,Env),!,throw(redeclare_function(X)).
type_check_func(env(Env,B,T),[func(X,Y,Return,Z)|L],Env1) :- T1 is T+1,
											type_check_one_func(env([id(X,func,func(Y,Return,Z),_)|Env],T1,T1),func(X,Y,Return,Z)), !,
											type_check_func(env([id(X,func,func(Y,Return,Z),_)|Env],B,T1),L,Env1).
											
%check if X has been declared in the symbol table from B+1 to T
has_declared(X,env([id(X,_,_,_)|_],B,T)):- T > B ,!.
has_declared(X,env([_|L],B,T)) :- T1 is T - 1, has_declared(X,env(L,B,T1)).

%create a symbol table from the list of variable or constant declarations
%As a suggestion, we may implement a symbol table as the functor env(list,bottom,top)
%where list contains the list of entries id(identifier,kind,type), 
%bottom is the index of the first element in the current scope minus 1, 
%bottom is the index-1 of the first element in the current scope, 
%top is the index of the last element in the current scope. 
%We have the right to implement the symbol table in a different way.
create_env([],L,L).
create_env([var(X,Y)|_],env(_,0,_),_) :- is_builtin(X),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|_],L1,_) :- has_declared(X,L1),!,throw(redeclare_identifier(var(X,Y))).
create_env([var(X,Y)|L],env(L1,B,T),L2) :- T1 is T+1, create_env(L,env([id(X,var,Y,_)|L1],B,T1),L2).
create_env([const(X,str(V))|L],env(L1,B,T),L2) :- T1 is T+1, create_env(L,env([id(X,const,string,V)|L1],B,T1),L2).
create_env([const(X,Y)|L],env(L1,B,T),L2) :- 
	(integer(Y) -> Type=integer; float(Y) -> Type=real; (Y==true ; Y==false) -> Type=boolean), 
	T1 is T+1, create_env(L,env([id(X,const,Type,Y)|L1],B,T1),L2).
create_env([par(X,Y)|L],env(L1,B,T),L2) :- T1 is T+1, create_env(L,env([id(X,par,Y,_)|L1],B,T1),L2).
create_local_env(env(L1,_,_), env(L1,0,0)).

is_builtin(readInt).
is_builtin(writeIntLn).
is_builtin(writeInt).
is_builtin(readReal).
is_builtin(writeRealLn).
is_builtin(writeReal).
is_builtin(readBool).
is_builtin(writeBoolLn).
is_builtin(writeBool).
is_builtin(writeLn).
is_builtin(writeStrLn).
is_builtin(writeStr).

% For runtime
%TODO
%create_runtime_env(X,X).
%create_runtime_env(env(L,B,T),env(L,0,0)) :- set_global_env_length(env(L,B,T)).
create_runtime_env(env(L,_,T),env(L,0,0)) :- set_global_env_length(T).

reduce(config(add(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1+V2.

reduce(config(sub(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1-V2.

reduce(config(times(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1*V2.

reduce(config(rdiv(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1/V2.

reduce(config(idiv(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1 div V2.

reduce(config(imod(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)), R is V1 mod V2.

reduce(config(bnot(E1),Env),config(R,Env1)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), (V1 == true -> R = false; R = true).

reduce(config(band(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 == true, V2 == true -> R = true; R = false).

reduce(config(bor(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 == true; V2 = true -> R = true; R = false).

reduce(config(greater(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 > V2 -> R = true; R = false).

reduce(config(less(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 < V2 -> R = true; R = false).

reduce(config(ge(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 >= V2 -> R = true; R = false).

reduce(config(le(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 =< V2 -> R = true; R = false).

reduce(config(eql(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 == V2 -> R = true; R = false).

reduce(config(ne(E1,E2),Env),config(R,Env2)) :-
		reduce_all(config(E1,Env),config(V1,Env1)), reduce_all(config(E2,Env1),config(V2,Env2)),
		(V1 \= V2 -> R = true; R = false).

reduce(config(ele(E1,L2),Env),config(R,Env2)) :- 
		reduce(config(E1,Env),config(L1,Env1)),
		reduce_params(L2,Env1,ReducedL2,Env2),
		get_element_arr(L1,ReducedL2,V,E1,L2), (var(V) -> throw(invalid_expression(ele(E1,L2))); R = V).

reduce(config(call(readInt,[]),Env),config(R,Env)) :-
	read(V), integer(V), R is V.
reduce(config(call(readReal,[]),Env),config(R,Env)) :-
	read(V), float(V), R is V.
reduce(config(call(readBool,[]),Env),config(R,Env)) :-
	read(V), boolean(V), R is V.

reduce(config(call(Name,Params),Env),config(R,Env3)) :-
	reduce_params(Params,Env,ReducedParams,Env0),
	lookup(Env0,Name,T), lookup_to_type(T,TY), type_to_stmts(TY,Stmts),
	type_to_params(TY,P), params_to_ids(P,ReducedParams,Ids), prepend(Ids,Env0,Env1),
	reduce_stmt(config(Stmts,Env1),Env2),
	env_to_list(Env,EnvList), env_to_list(Env2,EnvList2), 
	update_env_proc_list(EnvList,EnvList2,EnvList3), update_env_proc(Env,EnvList3,Env3),
	member(id(Name,func,_,ReturnValue),EnvList3), R is ReturnValue.

reduce(config(X,Env),config(V,Env)) :-
	Env = env(Vars,_,_), 
	member(id(X,_,T,Value),Vars),
	(var(Value), T \= arr(_,_) -> throw(invalid_expression(X)); (T = arr(L,_), create_value(L,Value); true)),
	V = Value.

get_element_arr([Elem|_], [0], Elem, _,_).
get_element_arr([Elem|_], [0|Indices], Result, Name,L2) :- get_element_arr(Elem, Indices, Result, Name,L2).
get_element_arr([_|Rest], [Index|Indices], Result, Name,L2) :-
    Index > 0, Index1 is Index - 1, get_element_arr(Rest, [Index1|Indices], Result, Name,L2).
get_element_arr(_, _, _, Name,L2) :- throw(outofbound(ele(Name,L2))).


reduce_all(config(V,Env),config(V,Env)):- integer(V),!.
reduce_all(config(V,Env),config(V,Env)):- float(V),!.
reduce_all(config(V,Env),config(V,Env)):- boolean(V),!.
reduce_all(config(V,Env),config(V,Env)):- string(V),!.
reduce_all(config(str(V),Env),config(V,Env)):- !.
reduce_all(config(V,Env),config(V,Env)):- is_list(V),!.
reduce_all(config(E,Env),config(E2,Env2)):-
	reduce(config(E,Env),config(E1,Env1)),!,
	reduce_all(config(E1,Env1),config(E2,Env2)).

reduce_params([], X, [], X).
reduce_params([Param|Rest],Env,[ReducedParam|ReducedRest],FinalEnv) :- 
    reduce_all(config(Param,Env),config(ReducedParam,Env2)), 
    reduce_params(Rest,Env2,ReducedRest,FinalEnv).

reduce_stmt_loop(config(S,Env),FinalEnv) :- 
	Env = env(_,B,T), create_local_env(Env,Env1),
	reduce_stmt(config(S,Env1),Env2), !,
	Env2 = env(L,_,T2), cut_env(L,T2,L2), FinalEnv = env(L2,B,T).
reduce_stmt(config([], Env), Env) :- !.
reduce_stmt(config([S|Rest],Env),FinalEnv) :- 
    reduce_single_stmt(config(S,Env),NewEnv), !,
    reduce_stmt(config(Rest,NewEnv),FinalEnv).

cut_env(L, 0, L) :- !.
cut_env([_|Tail], T, L2) :- T > 0, T1 is T - 1, cut_env(Tail, T1, L2), !.

update_env(env(Vars,N,M),X,V,env(NewVars,N,M)) :- update_var(Vars,X,V,NewVars), !.
update_var([],_,_,[]) :- !.
update_var([id(X,Kind,Type,_)|Rest],X,V,[id(X,Kind,Type,V)|Rest]) :- !.
update_var([Var|Rest],X,V,[Var|NewRest]) :- update_var(Rest,X,V,NewRest).

update_arr([_|Rest], [0], NewValue, [NewValue|Rest], _,_).
update_arr([Elem|Rest], [0|Indices], NewValue, [UpdatedElem|Rest], Name,I) :- update_arr(Elem,Indices,NewValue,UpdatedElem,Name,I).
update_arr([Elem|Rest], [Index|Indices], NewValue, [Elem|UpdatedRest], Name,I) :-
    Index > 0, Index1 is Index - 1, update_arr(Rest, [Index1|Indices], NewValue, UpdatedRest, Name,I).
update_arr(_, _, _, _, Name,I) :- throw(outofbound(ele(Name,I))).

create_value([], _).
create_value([N | Rest], Value) :-
    create_list(N, Rest, Value).
create_list(0, _, []).
create_list(N, Rest, [SubList|Tail]) :- N > 0, create_value(Rest,SubList), N1 is N-1, create_list(N1,Rest,Tail).

reduce_single_stmt(config(L,Env),Env2) :- 
	is_list(L), reduce_stmt_loop(config(L,Env),Env2), !.

reduce_single_stmt(config(var(X,T),Env),Env2) :- 
    create_env([var(X,T)],Env,Env2), !.

reduce_single_stmt(config(const(X,Y),Env),Env2) :- 
    create_env([const(X,Y)],Env,Env2), !.

reduce_single_stmt(config(assign(ele(X,I),Y),Env),Env2) :- 
	Env = env(Vars,_,_), 
	member(id(X,_,arr(L,_),Value),Vars),
    (var(Value) -> create_value(L,Value); true),
    reduce_all(config(Y,Env),config(V,Env1)),
	reduce_params(I,Env1,ReducedI,Env15),
	update_arr(Value,ReducedI,V,V1,X,I), update_env(Env15,X,V1,Env2), !.

reduce_single_stmt(config(assign(X,array(Y)),Env),Env2) :- 
	reduce_array_literal(array(Y),Y1),
	reduce_params(Y1,Env,V,Env1),
    update_env(Env1,X,V,Env2), !.

reduce_single_stmt(config(assign(X,Y),Env),Env2) :- 
    reduce_all(config(Y,Env),config(V,Env1)),
    update_env(Env1,X,V,Env2), !.

reduce_single_stmt(config(if(X,Y),Env),Env2) :-
    reduce_all(config(X,Env),config(V,Env1)),
	(V == true -> reduce_single_stmt(config(Y,Env1),Env2) ; Env2 = Env).

reduce_single_stmt(config(if(X,Y,Z),Env),Env2) :-
    reduce_all(config(X,Env),config(V,Env1)),
	(V == true -> reduce_single_stmt(config(Y,Env1),Env2) ; reduce_single_stmt(config(Z,Env1),Env2)).

reduce_single_stmt(config(while(X,Y),Env),Env3) :-
    enter_loop_context,
    (catch(
         (reduce_all(config(X,Env),config(V,Env1)),
          (V == true ->
              (catch(reduce_single_stmt(config(Y,Env1),Env2),
                     continue_signal(EnvCont),
                     Env2 = EnvCont),
               reduce_single_stmt(config(while(X,Y),Env2),Env3))
              ; Env3 = Env)),
         break_signal(EnvBreak),
         (Env3 = EnvBreak))),
    exit_loop_context.

reduce_single_stmt(config(do(X,Y),Env),Env3) :-
    enter_loop_context,
    (catch(
         (reduce_single_stmt(config(X,Env),Env1), reduce_all(config(Y,Env1),config(V,Env2)),
          (V == true ->
              (catch(reduce_single_stmt(config(do(X,Y),Env2),Env3),
                     continue_signal(EnvCont),
                     reduce_single_stmt(config(do(X,Y),EnvCont),Env3)))
              ; Env3 = Env2)),
         break_signal(EnvBreak),
         (Env3 = EnvBreak))),
    exit_loop_context.

reduce_single_stmt(config(loop(0,_),Env),Env) :- !.
reduce_single_stmt(config(loop(X,Y),Env),Env3) :-
    reduce_all(config(X,Env),config(V,Env1)),
    enter_loop_context,
    (catch(
         (V > 0 ->
              (catch(reduce_single_stmt(config(Y,Env1),Env2),
                     continue_signal(EnvCont),
                     (Env2 = EnvCont)),
               V1 is V - 1,
               reduce_single_stmt(config(loop(V1,Y),Env2),Env3))
              ; Env3 = Env),
         break_signal(EnvBreak),
         (Env3 = EnvBreak))),
    exit_loop_context.

reduce_single_stmt(config(break(null),Env),Env) :- throw(break_signal(Env)).
reduce_single_stmt(config(continue(null),Env),Env) :- throw(continue_signal(Env)).

reduce_single_stmt(config(call(writeInt,[X]),Env),Env1) :- 
	reduce_all(config(X,Env),config(V,Env1)), write(V), !.

reduce_single_stmt(config(call(writeIntLn,[X]),Env),Env1) :-
    reduce_all(config(X,Env),config(V,Env1)), write(V), nl, !.

reduce_single_stmt(config(call(writeReal,[X]),Env),Env1) :-
    reduce_all(config(X,Env),config(V,Env1)), write(V), !.

reduce_single_stmt(config(call(writeRealLn,[X]),Env),Env1) :-
    reduce_all(config(X,Env),config(V,Env1)), write(V), nl, !.

reduce_single_stmt(config(call(writeBool,[X]),Env),Env1) :-
    reduce_all(config(X,Env),config(V,Env1)), write(V), !.

reduce_single_stmt(config(call(writeBoolLn,[X]),Env),Env1) :-
	reduce_all(config(X,Env),config(V,Env1)), write(V), nl, !.

reduce_single_stmt(config(call(writeStr,[X]),Env),Env1) :- 
    reduce_all(config(X,Env),config(V,Env1)), write(V), !.

reduce_single_stmt(config(call(writeStrLn,[X]),Env),Env1) :-
	reduce_all(config(X,Env),config(V,Env1)), write(V), nl, !.

reduce_single_stmt(config(call(writeLn,[]),Env),Env) :- nl, !.

reduce_single_stmt(config(call(Name,Params),Env),Env3) :-
	reduce_params(Params,Env,ReducedParams,Env0),
	lookup(Env0,Name,T), lookup_to_type(T,TY), type_to_stmts(TY,Stmts), 
	type_to_params(TY,P), params_to_ids(P,ReducedParams,Ids), 
	get_global_env_length(Length), get_global_env(Env0,Length,GlobalEnv), prepend(Ids,GlobalEnv,Env1),
	reduce_stmt(config(Stmts,Env1),Env2),
	env_to_list(Env,EnvList), env_to_list(Env2,EnvList2),
	update_env_proc_list(EnvList,EnvList2,EnvList3),
	update_env_proc(Env,EnvList3,Env3),!.

params_to_ids([],[],[]).
params_to_ids([par(Name,Type)|Tail],[VH|VT],[id(Name,par,Type,VH)|Rest]) :- params_to_ids(Tail,VT,Rest).

prepend([], Env, Env).
prepend([H|T], env(X,Y,Z), Result) :- prepend(T, env([H|X],Y,Z), Result).

env_to_list(env(X,_,_),X).
update_env_proc_list([], _, []).
update_env_proc_list([id(Name,var,Type,_)|RestEnv], Env2, [id(Name,var,Type,NewValue)|RestEnv3]) :-
    member(id(Name,var,Type,NewValue),Env2),
    update_env_proc_list(RestEnv,Env2,RestEnv3).
update_env_proc_list([id(Name,func,Type,_)|RestEnv], Env2, [id(Name,func,Type,NewValue)|RestEnv3]) :-
	member(id(Name,func,Type,NewValue),Env2),
    update_env_proc_list(RestEnv,Env2,RestEnv3).
update_env_proc_list([id(Name,proc,X,Y)|RestEnv], Env2, [id(Name,proc,X,Y)|RestEnv3]) :-
    update_env_proc_list(RestEnv,Env2,RestEnv3).
update_env_proc_list([_|RestEnv], Env2, RestEnv3) :-
    update_env_proc_list(RestEnv,Env2,RestEnv3).

update_env_proc(env(_,Y,Z), List, env(List,Y,Z)).

reduce_array_literal(array(Elements), Result) :- maplist(reduce_array_literal_helper, Elements, Result).
reduce_array_literal_helper(array(SubElements), Reduced) :- reduce_array_literal(array(SubElements), Reduced).
reduce_array_literal_helper(Element, Element) :- \+ is_array(Element).
is_array(array(_)).


