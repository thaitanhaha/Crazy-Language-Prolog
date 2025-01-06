import unittest
from TestUtils import TestPreGen


class PreGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """program abc;
# 					begin
# 					end."""
#         expect = "[[],[],[]]. "
#         self.assertTrue(TestPreGen.test(input, expect, 301))
#     def test_program_with_const(self):
#         input = """program abc;
# 					const i = 30.0E3;
# 					begin
# 					end."""
#         expect = "[[const(i,30.0E3)],[],[]]. "
#         self.assertTrue(TestPreGen.test(input, expect, 302))
#     def test_program_with_assign(self):
#         input = """program abc;
# 					var i: string;
# 					begin
# 					 i:= 'af''sf';
# 					end."""
#         expect = """[[var(i,string)],[],[assign(i,str("af\\'sf"))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 303))
#     def test_program_with_if(self):
#         input = """program abc;
# 					begin
# 					var i:integer;
# 					    if true then
# 					        a:=10;
# 					    else
# 					        i:=i-1;
# 					end."""
#         expect = "[[],[],[var(i,integer),if(true,assign(a,10),assign(i,sub(i,1)))]]. "
#         self.assertTrue(TestPreGen.test(input, expect, 304))

#     def test_long_program(self):
#         input = """program sel;
# 					var i, j, min, t: integer;
# 					var k:integer;
# 					var a:array [10] of integer;
# 					         procedure fibonacci(i,k,l:integer;j,m:real);
# 					                begin
# 					                        const max = 25;
# 					                        var i: integer;
# 					                        var f: array [25] of integer;
# 					                        f[0]:= 1;
# 					                        f[1]:= 1;
# 					                        loop max do f[i]:= f[i-1] + f[i-2];
# 					                end;
# 					begin
# 					k:=1;
# 					do
					
# 					        a[k]:=readInt();
# 					        if k <10 then begin
# 					                k:=k-1;
# 					                continue;
# 					        end
# 					        while k < 100+1 do while k >= 100 do continue;
# 					        k:=k+1;
					
# 					while (k>10) ;
# 					loop 10 do
# 					begin
# 					        min:=i;
# 					        loop 10 do
# 					                if a[j]<a[min] then min:=j;
# 					        t:=a[min];
# 					        a[min]:=a[i];
# 					        a[i]:=t;
# 					end 
# 					loop 1 do
# 					        write(a[i],' ');
# 					end."""						
#         expect = """[[var(i,integer),var(j,integer),var(min,integer),var(t,integer),var(k,integer),var(a,arr([10],integer))],[proc(fibonacci,[par(i,integer),par(k,integer),par(l,integer),par(j,real),par(m,real)],[const(max,25),var(i,integer),var(f,arr([25],integer)),assign(ele(f,[0]),1),assign(ele(f,[1]),1),loop(max,assign(ele(f,[i]),add(ele(f,[sub(i,1)]),ele(f,[sub(i,2)]))))])],[assign(k,1),do([assign(ele(a,[k]),call(readInt,[])),if(less(k,10),[assign(k,sub(k,1)),continue(null)]),while(add(less(k,100),1),while(ge(k,100),continue(null))),assign(k,add(k,1))],greater(k,10)),loop(10,[assign(min,i),loop(10,if(less(ele(a,[j]),ele(a,[min])),assign(min,j))),assign(t,ele(a,[min])),assign(ele(a,[min]),ele(a,[i])),assign(ele(a,[i]),t)]),loop(1,call(write,[ele(a,[i]),str(" ")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 305))

#     def test_306(self):
#         input = """
# program test2;
# var a,b:integer;
# begin
# a := 1;
# b := 2;
# writeIntLn(a+b);
# end."""
#         expect = """[[var(a,integer),var(b,integer)],[],[assign(a,1),assign(b,2),call(writeIntLn,[add(a,b)])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 306))
        
#     def test_307(self):
#         input = """
# program test2;
# var a,b,c:real;
# var d:integer;
# var e:array[5][6] of real;
# var f:string;
# begin
# end."""
#         expect = """[[var(a,real),var(b,real),var(c,real),var(d,integer),var(e,arr([5,6],real)),var(f,string)],[],[]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 307))
        
#     def test_308(self):
#         input = """
# program test3;
# procedure foo(a:integer);
# 	begin
# 		var b:integer;
# 		b := a + 1;
# 		writeInt(b);
# 	end;
# begin
# 	foo(1);
# end."""
#         expect = """[[],[proc(foo,[par(a,integer)],[var(b,integer),assign(b,add(a,1)),call(writeInt,[b])])],[call(foo,[1])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 308))
        
#     def test_309(self):
#         input = """
# program test4;
# 	function foo(a:integer):integer ;
# 	begin
# 		foo := a + 1;
# 	end;
# begin
# 	foo(1);
# end."""
#         expect = """[[],[func(foo,[par(a,integer)],integer,[assign(foo,add(a,1))])],[call(foo,[1])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 309))

#     def test_310(self):
#         input = """
# program example;
# var childShare:integer;
# function child1():real;
# begin
# 	childShare := 1;
# 	child1 := childShare;
# end;

# procedure child2();
# begin
# 	childShare := 2;
# end;

# begin
# 	child1();
# 	writeIntLn(childShare);
# end."""
#         expect = """[[var(childShare,integer)],[func(child1,[],real,[assign(childShare,1),assign(child1,childShare)]),proc(child2,[],[assign(childShare,2)])],[call(child1,[]),call(writeIntLn,[childShare])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 310))

#     def test_311(self):
#         input = """
# program example;
# var a:integer;

# begin
# 	if a=1 then a := a+1;
# end."""
#         expect = """[[var(a,integer)],[],[if(eql(a,1),assign(a,add(a,1)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 311))

#     def test_312(self):
#         input = """
# program example;
# var a:integer;

# begin
# 	if a=1 then a := a+1; else a := a+2;
# end."""
#         expect = """[[var(a,integer)],[],[if(eql(a,1),assign(a,add(a,1)),assign(a,add(a,2)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 312))
        
#     def test_313(self):
#         input = """
# program example;
# var a:integer;
# procedure f();
# begin
# 	if a=1 then a := a+1; else a := a+2;
# end;
# begin
# 	if a=1 then a := a+1; else a := a+2;
# end."""
#         expect = """[[var(a,integer)],[proc(f,[],[if(eql(a,1),assign(a,add(a,1)),assign(a,add(a,2)))])],[if(eql(a,1),assign(a,add(a,1)),assign(a,add(a,2)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 313))
        
#     def test_314(self):
#         input = """
# program example;
# begin
# 	var i:integer;
#     i := (i+1) * (i-1) + (i+i+i-i);
# end."""
#         expect = """[[],[],[var(i,integer),assign(i,add(times(add(i,1),sub(i,1)),sub(add(add(i,i),i),i)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 314))

#     def test_315(self):
#         input = """
# program example;
# begin
#     writeInt((1+2) * (3+4) + (5+6+7-8));
# end."""
#         expect = """[[],[],[call(writeInt,[add(times(add(1,2),add(3,4)),sub(add(add(5,6),7),8))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 315))

#     def test_316(self):
#         input = """
# program example;
# begin
#     writeInt(1 + 2/3*4 + 5 mod 6 div 7-8);
# end."""
#         expect = """[[],[],[call(writeInt,[sub(add(add(1,times(rdiv(2,3),4)),idiv(imod(5,6),7)),8)])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 316))
        
#     def test_317(self):
#         input = """
# program example;
# begin
#     writeBool(not not (not not a));
# end."""
#         expect = """[[],[],[call(writeBool,[bnot(bnot(bnot(bnot(a))))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 317))
        
#     def test_318(self):
#         input = """
# program example;
# begin
#     writeInt(---1);
# end."""
#         expect = """[[],[],[call(writeInt,[sub(sub(sub(1)))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 318))
        
#     def test_319(self):
#         input = """
# program example;
# begin
#     writeBool((1 > 2) or (1 < 2) or (1 >= 2) or (1 <= 2) or (1 = 2) or (1 <> 2));
# end."""
#         expect = """[[],[],[call(writeBool,[bor(bor(bor(bor(bor(greater(1,2),less(1,2)),ge(1,2)),le(1,2)),eql(1,2)),ne(1,2))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 319))

#     def test_320(self):
#         input = """
# program example;
# begin
# 	var a,b,c:boolean;
#     writeBool(a or b and c);
# end."""
#         expect = """[[],[],[var(a,boolean),var(b,boolean),var(c,boolean),call(writeBool,[bor(a,band(b,c))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 320))

#     def test_321(self):
#         input = """
# program example;
# begin
# 	var a:integer;
#     a := 1;
#     loop (a+1) do a := a+1;
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),loop(add(a,1),assign(a,add(a,1)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 321))

#     def test_322(self):
#         input = """
# program example;
# begin
# 	var a:integer;
#     a := 1;
#     loop a+1 do a := a+1;
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),loop(add(a,1),assign(a,add(a,1)))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 322))

#     def test_323(self):
#         input = """
# program example;
# procedure foo(a:integer);
# begin
#     loop a+1 do a := a+1;
# end;
# begin
# 	foo(10);
# end."""
#         expect = """[[],[proc(foo,[par(a,integer)],[loop(add(a,1),assign(a,add(a,1)))])],[call(foo,[10])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 323))

#     def test_324(self):
#         input = """
# program example;
# begin
# 	var a:integer;
#     a := 1;
#     loop a+10 do 
#     begin
#         loop a+9 do foo(a);
#     end
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),loop(add(a,10),[loop(add(a,9),call(foo,[a]))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 324))

#     def test_325(self):
#         input = """
# program example;
# begin
#     loop -10 do 
#     begin
#         foo(-10+a*b);
#     end
# end."""
#         expect = """[[],[],[loop(sub(10),[call(foo,[add(sub(10),times(a,b))])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 325))

#     def test_326(self):
#         input = """
# program example;
# begin
#     var a: integer;
#     a := 1;
#     while a < 10 do foo(a);
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),while(less(a,10),call(foo,[a]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 326))

#     def test_327(self):
#         input = """
# program example;
# begin
#     var a: integer;
#     a := 1;
#     while (a < 10) do foo(a);
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),while(less(a,10),call(foo,[a]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 327))

#     def test_328(self):
#         input = """
# program example;
# begin
#     var a: integer;
#     a := 1;
#     while (a < 10) do 
#     begin
#         while (a < 10) do foo(a);
#     end
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),while(less(a,10),[while(less(a,10),call(foo,[a]))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 328))

#     def test_329(self):
#         input = """
# program example;
# procedure foo(a:integer);
# begin
#     while (a < (10-a*a)) do foo(a);
# end;
# begin
#     while (2 < (10-1*1)) do foo(a);
# end."""
#         expect = """[[],[proc(foo,[par(a,integer)],[while(less(a,sub(10,times(a,a))),call(foo,[a]))])],[while(less(2,sub(10,times(1,1))),call(foo,[a]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 329))

#     def test_330(self):
#         input = """
# program example;
# procedure foo(a:integer);
# begin
#     while (a < 10) do foo(a);
# end;
# begin
#     foo(10);
# end."""
#         expect = """[[],[proc(foo,[par(a,integer)],[while(less(a,10),call(foo,[a]))])],[call(foo,[10])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 330))

#     def test_331(self):
#         input = """
# program example;
# begin
#     do 
#         var a:integer;
#         a := 1;
#         a := a+1+2;
#         foo(a);
#     while 1 > (2-3*-3);
# end."""
#         expect = """[[],[],[do([var(a,integer),assign(a,1),assign(a,add(add(a,1),2)),call(foo,[a])],greater(1,sub(2,times(3,sub(3)))))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 331))

#     def test_332(self):
#         input = """
# program example;
# begin
#     do 
#         begin
#             var a:integer;
#             a := 1;
#             a := a+1+2;
#         end
#         foo(a);
#     while 1 > (2-3*-3);
# end."""
#         expect = """[[],[],[do([[var(a,integer),assign(a,1),assign(a,add(add(a,1),2))],call(foo,[a])],greater(1,sub(2,times(3,sub(3)))))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 332))

#     def test_333(self):
#         input = """
# program example;
# procedure foo();
# begin
#     do 
#         var a:integer;
#         a := 1;
#         a := a+1+2;
#         foo(a);
#     while 1 > (2-3*-3);
# end;
# begin
#     foo();
# end."""
#         expect = """[[],[proc(foo,[],[do([var(a,integer),assign(a,1),assign(a,add(add(a,1),2)),call(foo,[a])],greater(1,sub(2,times(3,sub(3)))))])],[call(foo,[])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 333))

#     def test_334(self):
#         input = """
# program example;
# begin
#     var a:integer;
#     a := 1;
#     do
#         do 
#             foo(a);
#             a := a+-1*-2;
#         while a < 10;
#     while false;
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),do([do([call(foo,[a]),assign(a,add(a,times(sub(1),sub(2))))],less(a,10))],false)]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 334))

#     def test_335(self):
#         input = """
# program example;
# begin
#     var a:integer;
#     a := 1;
#     do
#         do 
#             foo(a);
#             a := a+-1*-2;
#         while (a < 10);
#     while ((((false))));
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),do([do([call(foo,[a]),assign(a,add(a,times(sub(1),sub(2))))],less(a,10))],false)]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 335))

#     def test_336(self):
#         input = """
# program example;
# begin
# 	var a:integer;
#     a := 1;
#     loop 10 do 
#     begin 
#         a := a+1;
#         if a = 5 then break;
#         else continue;
#     end
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),loop(10,[assign(a,add(a,1)),if(eql(a,5),break(null),continue(null))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 336))

#     def test_337(self):
#         input = """
# program example;
# procedure foo();
# begin
# 	var a:integer;
#     a := 1;
#     loop 10 do 
#     begin 
#         a := a+1;
#         if a = 5 then break;
#         else continue;
#     end
# end;
# begin
#     foo();
# end."""
#         expect = """[[],[proc(foo,[],[var(a,integer),assign(a,1),loop(10,[assign(a,add(a,1)),if(eql(a,5),break(null),continue(null))])])],[call(foo,[])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 337))

#     def test_338(self):
#         input = """
# program example;
# begin
#     var a: integer;
#     a := 1;
#     while a < 10 do 
#     begin
#         if a = 5+1 then break;
#         else continue;
#         a := -a + 2*a + 1;
#     end
# end."""
#         expect = """[[],[],[var(a,integer),assign(a,1),while(less(a,10),[if(add(eql(a,5),1),break(null),continue(null)),assign(a,add(add(sub(a),times(2,a)),1))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 338))

#     def test_339(self):
#         input = """
# program example;
# procedure foo();
# begin
#     var a: integer;
#     a := 1;
#     while a < 10 do 
#     begin
#         if a = (5+1) then break;
#         else continue;
#         a := -a + 2*a + 1;
#     end
# end;
# begin
#     foo();
# end."""
#         expect = """[[],[proc(foo,[],[var(a,integer),assign(a,1),while(less(a,10),[if(eql(a,add(5,1)),break(null),continue(null)),assign(a,add(add(sub(a),times(2,a)),1))])])],[call(foo,[])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 339))

#     def test_340(self):
#         input = """
# program example;
# begin
#     do 
#         var a:integer;
#         a := 1;
#         writeIntLn(a);
#         if a=1 then break;
#         else continue;
#     while 1 < (2-3*-3);
# end."""
#         expect = """[[],[],[do([var(a,integer),assign(a,1),call(writeIntLn,[a]),if(eql(a,1),break(null),continue(null))],less(1,sub(2,times(3,sub(3)))))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 340))

#     def test_341(self):
#         input = """
# program example;
# procedure foo();
# begin
#     do 
#         var a:integer;
#         a := 1;
#         writeIntLn(a);
#         if a=1 then break;
#         else continue;
#     while 1 < (2-3*-3);
# end;
# begin
#     foo();
# end."""
#         expect = """[[],[proc(foo,[],[do([var(a,integer),assign(a,1),call(writeIntLn,[a]),if(eql(a,1),break(null),continue(null))],less(1,sub(2,times(3,sub(3)))))])],[call(foo,[])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 341))

#     def test_342(self):
#         input = """
# program example;
# begin
#     // start of declaration part
#     var r,s: real;
#     const myPI = 3.14;
#     // list of statements
#     r := 2.0;
#     s := r*r*myPI;
# end."""
#         expect = """[[],[],[var(r,real),var(s,real),const(myPI,3.14),assign(r,2.0),assign(s,times(times(r,r),myPI))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 342))

#     def test_343(self):
#         input = """
# program declDemo;

# var a: array[5] of integer; // global variable

# procedure fill(x:array[5] of integer);
# begin
#     var a:real; // hiding global var. a
#     var x:real; // WRONG because parameter x has the same name
#     a:=5.9;
#     init(x);
# end;

# procedure init(x:array[5] of integer);
# begin
#     var i:integer; //block variable
#     i:=0;
#     x[i]:=a[i]; // a is global var.
# end;
# begin
#     fill(a);
# end."""
#         expect = """[[var(a,arr([5],integer))],[proc(fill,[par(x,arr([5],integer))],[var(a,real),var(x,real),assign(a,5.9),call(init,[x])]),proc(init,[par(x,arr([5],integer))],[var(i,integer),assign(i,0),assign(ele(x,[i]),ele(a,[i]))])],[call(fill,[a])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 343))

#     def test_344(self):
#         input = """
# program example;
# begin
#     const myIntConst = 5;
#     var my1stVar: integer;
#     var myArrayVar: array[5] of real;
#     var my2ndVar, my3rdVar: boolean;
#     var my2ndArray, my3rdArray: array[6][8] of real;
#     const myRealConst = 5.3e4;
#     writeInt(my1stVar * myIntConst);
# end."""
#         expect = """[[],[],[const(myIntConst,5),var(my1stVar,integer),var(myArrayVar,arr([5],real)),var(my2ndVar,boolean),var(my3rdVar,boolean),var(my2ndArray,arr([6,8],real)),var(my3rdArray,arr([6,8],real)),const(myRealConst,5.3e4),call(writeInt,[times(my1stVar,myIntConst)])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 344))

#     def test_345(self):
#         input = """
# program example;
# const myIntConst = 5;
# var my1stVar: integer;
# var myArrayVar: array[5] of real;
# var my2ndVar, my3rdVar: boolean;
# var my2ndArray, my3rdArray: array[6][8] of real;
# const myRealConst = 5.3e4;
# begin
#     writeInt(my1stVar * myIntConst);
# end."""
#         expect = """[[const(myIntConst,5),var(my1stVar,integer),var(myArrayVar,arr([5],real)),var(my2ndVar,boolean),var(my3rdVar,boolean),var(my2ndArray,arr([6,8],real)),var(my3rdArray,arr([6,8],real)),const(myRealConst,5.3e4)],[],[call(writeInt,[times(my1stVar,myIntConst)])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 345))

#     def test_346(self):
#         input = """
# program example;
# begin
#     var arr: array[1][2][3] of integer;
#     arr[0][0][0] := 1;
#     arr[0][0][1] := arr[0][0][0] + 1;
#     writeInt(arr[0][0][1]);
# end."""
#         expect = """[[],[],[var(arr,arr([1,2,3],integer)),assign(ele(arr,[0,0,0]),1),assign(ele(arr,[0,0,1]),add(ele(arr,[0,0,0]),1)),call(writeInt,[ele(arr,[0,0,1])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 346))

#     def test_347(self):
#         input = """
# program example;
# begin
#     var arr: array[1][2][3] of boolean;
#     arr[0][0][0] := (1+2) < ((3*4) - 10);
#     arr[0][0][1] := not(arr[0][0][0]);
#     writeBool(arr[0][0][1]);
# end."""
#         expect = """[[],[],[var(arr,arr([1,2,3],boolean)),assign(ele(arr,[0,0,0]),less(add(1,2),sub(times(3,4),10))),assign(ele(arr,[0,0,1]),bnot(ele(arr,[0,0,0]))),call(writeBool,[ele(arr,[0,0,1])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 347))

#     def test_348(self):
#         input = """
# program example;
# procedure foo(arr:array[1][2][3] of integer);
# begin
#     writeInt(arr[0][0][0] + arr[0][0][1]);
# end;
# begin
#     var arr: array[1][2][3] of integer;
#     arr[0][0][0] := 1;
#     arr[0][0][1] := arr[0][0][0] + 1;
#     foo(arr);
# end."""
#         expect = """[[],[proc(foo,[par(arr,arr([1,2,3],integer))],[call(writeInt,[add(ele(arr,[0,0,0]),ele(arr,[0,0,1]))])])],[var(arr,arr([1,2,3],integer)),assign(ele(arr,[0,0,0]),1),assign(ele(arr,[0,0,1]),add(ele(arr,[0,0,0]),1)),call(foo,[arr])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 348))

#     def test_349(self):
#         input = """
# program example;
# procedure foo(arr1:array[1][2][3] of integer; arr2:array[1][2][3] of integer);
# begin
#     var i,j,k:integer;
#     i := 0;
#     j := 0;
#     k := 0;
#     while i<1 do
#     begin
#         while j<2 do
#         begin
#             while k<3 do
#                 begin
#                     writeInt(arr1[i][j][k] + arr2[i][j][k]);
#                     k:=k+1;
#                 end
#             j:=j+1;
#         end
#         i:=i+1;
#     end
# end;
# begin
#     var arr1,arr2: array[1][2][3] of integer;
#     foo(arr1,arr2);
# end."""
#         expect = """[[],[proc(foo,[par(arr1,arr([1,2,3],integer)),par(arr2,arr([1,2,3],integer))],[var(i,integer),var(j,integer),var(k,integer),assign(i,0),assign(j,0),assign(k,0),while(less(i,1),[while(less(j,2),[while(less(k,3),[call(writeInt,[add(ele(arr1,[i,j,k]),ele(arr2,[i,j,k]))]),assign(k,add(k,1))]),assign(j,add(j,1))]),assign(i,add(i,1))])])],[var(arr1,arr([1,2,3],integer)),var(arr2,arr([1,2,3],integer)),call(foo,[arr1,arr2])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 349))

#     def test_350(self):
#         input = """
# program example;
# function foo(arr1:array[1][2][3] of integer; arr2:array[1][2][3] of integer):integer;
# begin
#     var i,j,k,sum:integer;
#     i := 0;
#     j := 0;
#     k := 0;
#     sum := 0;
#     while i<1 do
#     begin
#         while j<2 do
#         begin
#             while k<3 do
#                 begin
#                     sum := sum + arr1[i][j][k] + arr2[i][j][k];
#                     k:=k+1;
#                 end
#             j:=j+1;
#         end
#         i:=i+1;
#     end
# end;
# begin
#     var arr1,arr2: array[1][2][3] of integer;
#     foo(arr1,arr2);
# end."""
#         expect = """[[],[func(foo,[par(arr1,arr([1,2,3],integer)),par(arr2,arr([1,2,3],integer))],integer,[var(i,integer),var(j,integer),var(k,integer),var(sum,integer),assign(i,0),assign(j,0),assign(k,0),assign(sum,0),while(less(i,1),[while(less(j,2),[while(less(k,3),[assign(sum,add(add(sum,ele(arr1,[i,j,k])),ele(arr2,[i,j,k]))),assign(k,add(k,1))]),assign(j,add(j,1))]),assign(i,add(i,1))])])],[var(arr1,arr([1,2,3],integer)),var(arr2,arr([1,2,3],integer)),call(foo,[arr1,arr2])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 350))

#     def test_351(self):
#         input = """
# program example; // comment
# /*
# comment
# comment
# */
# begin
#     var arr1, arr2: array[2][3] of integer;
#     arr1 := [[1,2,3], [5,6,7]];
#     arr2 := [[10,20,30], [50,60,70]];
# end."""
#         expect = """[[],[],[var(arr1,arr([2,3],integer)),var(arr2,arr([2,3],integer)),assign(arr1,array([array([1,2,3]),array([5,6,7])])),assign(arr2,array([array([10,20,30]),array([50,60,70])]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 351))

#     def test_352(self):
#         input = """
# program example;
# procedure foo(s:string);
# begin
#     loop 3 do writeStr(s);
# end;
# begin
#     foo('abc');
# end."""
#         expect = """[[],[proc(foo,[par(s,string)],[loop(3,call(writeStr,[s]))])],[call(foo,[str("abc")])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 352))

#     def test_353(self):
#         input = """
# program example;
# const str = 'abc';
# begin
#     writeStr(str);
# end."""
#         expect = """[[const(str,str("abc"))],[],[call(writeStr,[str])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 353))

#     def test_354(self):
#         input = """
# program example;
# var arr: array[3] of boolean;
# begin
#     arr := [true, false, false];
# end."""
#         expect = """[[var(arr,arr([3],boolean))],[],[assign(arr,array([true,false,false]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 354))

#     def test_355(self):
#         input = """
# program example;
# var arr: array[3] of string;
# begin
#     arr := ['abc', 'abcd', 'abcde'];
# end."""
#         expect = """[[var(arr,arr([3],string))],[],[assign(arr,array([str("abc"),str("abcd"),str("abcde")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 355))

#     def test_356(self):
#         input = """
# program example;
# begin
#     var arr: array[3] of integer;
#     arr[0] := 3;
#     arr[1] := 2;
#     arr[2] := 3;
#     loop arr[0] do 
#     begin
#         while arr[1] < 6 do
#         begin 
#             arr[1] := 2 - -arr[1];
#             do 
#                 writeIntLn(arr[0] * arr[1] * arr[2]);
#                 writeIntLn(-arr[0] * -arr[1] * -arr[2]);
#                 arr[2] := arr[2] + 1;
#             while arr[2] < 4;
#         end
#     end
# end."""
#         expect = """[[],[],[var(arr,arr([3],integer)),assign(ele(arr,[0]),3),assign(ele(arr,[1]),2),assign(ele(arr,[2]),3),loop(ele(arr,[0]),[while(less(ele(arr,[1]),6),[assign(ele(arr,[1]),sub(2,sub(ele(arr,[1])))),do([call(writeIntLn,[times(times(ele(arr,[0]),ele(arr,[1])),ele(arr,[2]))]),call(writeIntLn,[times(times(sub(ele(arr,[0])),sub(ele(arr,[1]))),sub(ele(arr,[2])))]),assign(ele(arr,[2]),add(ele(arr,[2]),1))],less(ele(arr,[2]),4))])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 356))

#     def test_357(self):
#         input = """
# program example;
# begin
#     begin
#     end
#     begin
#     end
#     begin
#     end
#     begin
#     end
# end."""
#         expect = """[[],[],[[],[],[],[]]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 357))

#     def test_358(self):
#         input = """
# program example;
# begin
#     begin
#         begin
#             begin
#                 begin
#                 end
#             end
#         end
#     end
# end."""
#         expect = """[[],[],[[[[[]]]]]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 358))

#     def test_359(self):
#         input = """
# program example;
# begin
#     var a:integer;
#     begin
#         var a:integer;
#         begin
#             var a:integer;
#         end
#     end
# end."""
#         expect = """[[],[],[var(a,integer),[var(a,integer),[var(a,integer)]]]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 359))

#     def test_360(self):
#         input = """
# program example;
# function foo(a,b,c:integer):integer;
# begin
#     foo := a+b+c;
# end;
# begin
#     var a:string;
#     a := readStr();
#     begin
#         var a,b,c:integer;
#         a := readInt();
#         b := readInt();
#         c := readInt();
#         writeInt(foo(a,b,c));
#     end
#     writeStr(a);
# end."""
#         expect = """[[],[func(foo,[par(a,integer),par(b,integer),par(c,integer)],integer,[assign(foo,add(add(a,b),c))])],[var(a,string),assign(a,call(readStr,[])),[var(a,integer),var(b,integer),var(c,integer),assign(a,call(readInt,[])),assign(b,call(readInt,[])),assign(c,call(readInt,[])),call(writeInt,[call(foo,[a,b,c])])],call(writeStr,[a])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 360))

#     def test_361(self):
#         input = """
# program example;
# function sum(n:integer):integer;
# begin
#     var m,res:integer;
#     m := n;
#     res := 0;
#     while m <> 0 do
#     begin
#         res := res + m mod 10;
#         m := m div 10;
#     end
#     sum := res;
# end;
# begin
#     var n:integer;
#     n := readInt();
#     writeInt(sum(n));
# end."""
#         expect = """[[],[func(sum,[par(n,integer)],integer,[var(m,integer),var(res,integer),assign(m,n),assign(res,0),while(ne(m,0),[assign(res,add(res,imod(m,10))),assign(m,idiv(m,10))]),assign(sum,res)])],[var(n,integer),assign(n,call(readInt,[])),call(writeInt,[call(sum,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 361))

#     def test_362(self):
#         input = """
# program example;
# function foo(n:integer):real;
# begin
#     var res:real;
#     var i:integer;
#     i := 1;
#     loop n do 
#     begin
#         res := res + 1/i;
#         i := i+1;
#     end
#     foo := res;
# end;
# begin
#     var n:integer;
#     n := readInt();
#     writeInt(foo(n));
# end."""
#         expect = """[[],[func(foo,[par(n,integer)],real,[var(res,real),var(i,integer),assign(i,1),loop(n,[assign(res,add(res,rdiv(1,i))),assign(i,add(i,1))]),assign(foo,res)])],[var(n,integer),assign(n,call(readInt,[])),call(writeInt,[call(foo,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 362))

#     def test_363(self):
#         input = """
# program example;
# function factorial(n:integer): integer;
# begin
#     if n <= 1 then factorial := 1;
#     else factorial := n * factorial(n - 1);
# end;
# begin
#     writeInt(factorial(1+1+1+1));
# end."""
#         expect = """[[],[func(factorial,[par(n,integer)],integer,[if(le(n,1),assign(factorial,1),assign(factorial,times(n,call(factorial,[sub(n,1)]))))])],[call(writeInt,[call(factorial,[add(add(add(1,1),1),1)])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 363))

#     def test_364(self):
#         input = """
# program example;
# function isPrime(n:integer): boolean;
# begin
#     var i:integer;
#     if n <= 1 then
#         isPrime := false;
#     else
#     begin
#         isPrime := true;
#         loop n div 2 do
#         begin
#             if i = 1 then continue;
#             if n mod i = 0 then
#             begin
#                 isPrime := false;
#                 break;
#             end
#             i := i+1;
#         end
#     end
# end;
# begin
#     if isPrime(5) then writeStr('Prime');  // Prime
#     else writeStr('NotPrime');  // Not Prime
# end.
# """
#         expect = """[[],[func(isPrime,[par(n,integer)],boolean,[var(i,integer),if(le(n,1),assign(isPrime,false),[assign(isPrime,true),loop(idiv(n,2),[if(eql(i,1),continue(null)),if(imod(n,eql(i,0)),[assign(isPrime,false),break(null)]),assign(i,add(i,1))])])])],[if(call(isPrime,[5]),call(writeStr,[str("Prime")]),call(writeStr,[str("NotPrime")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 364))

#     def test_365(self):
#         input = """
# program example;
# function fibonacci(n: integer): integer;
# begin
#     if n = 0 then fibonacci := 0;
#     if n = 1 then fibonacci := 1;
#     fibonacci := fibonacci(n - 1) + fibonacci(n - 2);
# end;
# begin
#     writeInt(fibonacci(2*2*2-4));
# end.
# """
#         expect = """[[],[func(fibonacci,[par(n,integer)],integer,[if(eql(n,0),assign(fibonacci,0)),if(eql(n,1),assign(fibonacci,1)),assign(fibonacci,add(call(fibonacci,[sub(n,1)]),call(fibonacci,[sub(n,2)])))])],[call(writeInt,[call(fibonacci,[sub(times(times(2,2),2),4)])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 365))

#     def test_366(self):
#         input = """
# program example;
# var res: array[3] of integer;
# procedure multiplyMatrix(a, b: array[3] of integer);
# begin
#     var i, j, k: integer;
#     i := 0;
#     j := i;
#     k := j;
#     loop 3 do
#     begin
#         loop 3 do
#         begin
#             res[i][j] := 0;
#             loop 3 do
#             begin
#                 res[i][j] := res[i][j] + a[i][k] * b[k][j];
#                 k := k + 1;
#             end
#             j := j + 1;
#         end
#         i := i + 1;
#     end
# end;
# begin
    
# end.
# """
#         expect = """[[var(res,arr([3],integer))],[proc(multiplyMatrix,[par(a,arr([3],integer)),par(b,arr([3],integer))],[var(i,integer),var(j,integer),var(k,integer),assign(i,0),assign(j,i),assign(k,j),loop(3,[loop(3,[assign(ele(res,[i,j]),0),loop(3,[assign(ele(res,[i,j]),add(ele(res,[i,j]),times(ele(a,[i,k]),ele(b,[k,j])))),assign(k,add(k,1))]),assign(j,add(j,1))]),assign(i,add(i,1))])])],[]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 366))

#     def test_367(self):
#         input = """
# program example;
# procedure printMatrix(m: array[3] of integer);
# begin
#     var i, j: integer;
#     i := 0;
#     j := i;
#     loop 3 do
#     begin
#         loop 3 do
#         begin
#             writeInt(m[i][j]);
#             j := j + 1;
#         end
#         writeStrLn('');
#         i := i + 1;
#     end
# end;
# begin
    
# end."""
#         expect = """[[],[proc(printMatrix,[par(m,arr([3],integer))],[var(i,integer),var(j,integer),assign(i,0),assign(j,i),loop(3,[loop(3,[call(writeInt,[ele(m,[i,j])]),assign(j,add(j,1))]),call(writeStrLn,[str("")]),assign(i,add(i,1))])])],[]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 367))

#     def test_368(self):
#         input = """
# program example;
# var res: array[3] of integer;
# procedure multiplyMatrix(a,b: array[3] of integer);
# begin
#     var i, j, k: integer;
#     i := 0;
#     j := i;
#     k := j;
#     loop 3 do
#     begin
#         loop 3 do
#         begin
#             res[i][j] := 0;
#             loop 3 do
#             begin
#                 res[i][j] := res[i][j] + a[i][k] * b[k][j];
#                 k := k + 1;
#             end
#             j := j + 1;
#         end
#         i := i + 1;
#     end
# end;
# procedure printMatrix(m: array[3] of integer);
# begin
#     var i, j: integer;
#     i := 0;
#     j := i;
#     loop 3 do
#     begin
#         loop 3 do
#         begin
#             writeInt(m[i][j]);
#             j := j + 1;
#         end
#         writeStrLn('');
#         i := i + 1;
#     end
# end;
# begin
#     var a,b: array[3] of integer;
#     // Initialize A and B with some values (can be read from user input)
#     a := [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
#     b := [[9, 8, 7], [6, 5, 4], [3, 2, 1]];
#     multiplyMatrix(a,b);
#     printMatrix(res);
# end."""
#         expect = """[[var(res,arr([3],integer))],[proc(multiplyMatrix,[par(a,arr([3],integer)),par(b,arr([3],integer))],[var(i,integer),var(j,integer),var(k,integer),assign(i,0),assign(j,i),assign(k,j),loop(3,[loop(3,[assign(ele(res,[i,j]),0),loop(3,[assign(ele(res,[i,j]),add(ele(res,[i,j]),times(ele(a,[i,k]),ele(b,[k,j])))),assign(k,add(k,1))]),assign(j,add(j,1))]),assign(i,add(i,1))])]),proc(printMatrix,[par(m,arr([3],integer))],[var(i,integer),var(j,integer),assign(i,0),assign(j,i),loop(3,[loop(3,[call(writeInt,[ele(m,[i,j])]),assign(j,add(j,1))]),call(writeStrLn,[str("")]),assign(i,add(i,1))])])],[var(a,arr([3],integer)),var(b,arr([3],integer)),assign(a,array([array([1,2,3]),array([4,5,6]),array([7,8,9])])),assign(b,array([array([9,8,7]),array([6,5,4]),array([3,2,1])])),call(multiplyMatrix,[a,b]),call(printMatrix,[res])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 368))

#     def test_369(self):
#         input = """
# program example;
# function gcd(a: integer; b: integer): integer;
# begin
#     while b <> 0 do
#     begin
#         var temp: integer;
#         temp := b;
#         b := a mod b;
#         a := temp;
#     end
#     gcd := a;
# end;
# begin
#     var a, b: integer;
#     a := 10;
#     b := 8;
#     writeInt(gcd(a, b));
# end."""
#         expect = """[[],[func(gcd,[par(a,integer),par(b,integer)],integer,[while(ne(b,0),[var(temp,integer),assign(temp,b),assign(b,imod(a,b)),assign(a,temp)]),assign(gcd,a)])],[var(a,integer),var(b,integer),assign(a,10),assign(b,8),call(writeInt,[call(gcd,[a,b])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 369))

#     def test_370(self):
#         input = """
# program example;
# procedure foo(a: array[3] of string);
# begin
#     var i:integer;
#     i := 0;
#     loop 3 do
#     begin
#         writeStr(a[i]);
#         i := i+1;
#     end
# end;
# begin
#     var a:array[3] of string;
#     a := ['abc', 'def', 'ghi'];
#     foo(a);
# end."""
#         expect = """[[],[proc(foo,[par(a,arr([3],string))],[var(i,integer),assign(i,0),loop(3,[call(writeStr,[ele(a,[i])]),assign(i,add(i,1))])])],[var(a,arr([3],string)),assign(a,array([str("abc"),str("def"),str("ghi")])),call(foo,[a])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 370))

#     def test_371(self):
#         input = """
# program example;
# function power(base: integer; exp: integer): integer;
# begin
#     var result: integer;
#     result := 1;
#     while exp > 0 do
#     begin
#         if exp mod 2 = 1 then
#             result := result * base;
#         base := base * base;
#         exp := exp div 2;
#     end
#     power := result;
# end;
# begin
#     var base, exp: integer;
#     base := 2;
#     exp := 10;
#     writeInt(power(base, exp));
# end."""
#         expect = """[[],[func(power,[par(base,integer),par(exp,integer)],integer,[var(result,integer),assign(result,1),while(greater(exp,0),[if(imod(exp,eql(2,1)),assign(result,times(result,base))),assign(base,times(base,base)),assign(exp,idiv(exp,2))]),assign(power,result)])],[var(base,integer),var(exp,integer),assign(base,2),assign(exp,10),call(writeInt,[call(power,[base,exp])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 371))

#     def test_372(self):
#         input = """
# program example;
# procedure bubbleSort(arr: array[4] of integer; n: integer);
# begin
#     var i, j, temp: integer;
#     i := 0;
#     loop n - 1 do
#     begin
#         j := 0;
#         loop n - i - 1 do
#         begin
#             if arr[j] > arr[j + 1] then
#             begin
#                 temp := arr[j];
#                 arr[j] := arr[j + 1];
#                 arr[j + 1] := temp;
#             end
#             j := j + 1;
#         end
#         i := i + 1;
#     end
# end;
# begin
#     var arr: array[4] of integer;
#     arr := [4,3,2,1];
#     bubbleSort(arr, 5);
#     i := 0;
#     loop 4 do
#     begin
#         writeInt(arr[i]);
#         i := i + 1;
#     end
# end."""
#         expect = """[[],[proc(bubbleSort,[par(arr,arr([4],integer)),par(n,integer)],[var(i,integer),var(j,integer),var(temp,integer),assign(i,0),loop(sub(n,1),[assign(j,0),loop(sub(sub(n,i),1),[if(greater(ele(arr,[j]),ele(arr,[add(j,1)])),[assign(temp,ele(arr,[j])),assign(ele(arr,[j]),ele(arr,[add(j,1)])),assign(ele(arr,[add(j,1)]),temp)]),assign(j,add(j,1))]),assign(i,add(i,1))])])],[var(arr,arr([4],integer)),assign(arr,array([4,3,2,1])),call(bubbleSort,[arr,5]),assign(i,0),loop(4,[call(writeInt,[ele(arr,[i])]),assign(i,add(i,1))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 372))

#     def test_373(self):
#         input = """
# program example;
# function sumOfEvens(arr: array[4] of integer; n: integer): integer;
# begin
#     var sum, i: integer;
#     sum := 0;
#     i := 0;
#     loop n do
#     begin
#         if arr[i] mod 2 = 0 then
#             sum := sum + arr[i];
#         i := i + 1;
#     end
#     sumOfEvens := sum;
# end;
# begin
#     var arr: array[4] of integer;
#     arrr := [1,2,3,4];
#     writeInt(sumOfEvens(arr, 4));
# end."""
#         expect = """[[],[func(sumOfEvens,[par(arr,arr([4],integer)),par(n,integer)],integer,[var(sum,integer),var(i,integer),assign(sum,0),assign(i,0),loop(n,[if(imod(ele(arr,[i]),eql(2,0)),assign(sum,add(sum,ele(arr,[i])))),assign(i,add(i,1))]),assign(sumOfEvens,sum)])],[var(arr,arr([4],integer)),assign(arrr,array([1,2,3,4])),call(writeInt,[call(sumOfEvens,[arr,4])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 373))

#     def test_374(self):
#         input = """
# program example;
# function findMax(arr: array[5] of integer; n: integer): integer;
# begin
#     var max, i: integer;
#     max := arr[0];
#     i := 1;
#     loop n do
#     begin
#         if arr[i] > max then
#             max := arr[i];
#         i := i + 1;
#     end
#     findMax := max;
# end;
# begin
#     var arr: array[5] of integer;
#     arr := [3,5,7,2,4];
#     writeInt(findMax(arr, 5));
# end."""
#         expect = """[[],[func(findMax,[par(arr,arr([5],integer)),par(n,integer)],integer,[var(max,integer),var(i,integer),assign(max,ele(arr,[0])),assign(i,1),loop(n,[if(greater(ele(arr,[i]),max),assign(max,ele(arr,[i]))),assign(i,add(i,1))]),assign(findMax,max)])],[var(arr,arr([5],integer)),assign(arr,array([3,5,7,2,4])),call(writeInt,[call(findMax,[arr,5])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 374))

#     def test_375(self):
#         input = """
# program example;
# function countOdds(arr: array[6] of integer; n: integer): integer;
# begin
#     var count, i: integer;
#     count := 0;
#     i := 0;
#     loop n do
#     begin
#         if arr[i] mod 2 <> 0 then
#             count := count + 1;
#         i := i + 1;
#     end
#     countOdds := count;
# end;
# begin
#     var arr: array[6] of integer;
#     arr := [1,2,3,4,5,6];
#     writeInt(countOdds(arr, 6));
# end."""
#         expect = """[[],[func(countOdds,[par(arr,arr([6],integer)),par(n,integer)],integer,[var(count,integer),var(i,integer),assign(count,0),assign(i,0),loop(n,[if(imod(ele(arr,[i]),ne(2,0)),assign(count,add(count,1))),assign(i,add(i,1))]),assign(countOdds,count)])],[var(arr,arr([6],integer)),assign(arr,array([1,2,3,4,5,6])),call(writeInt,[call(countOdds,[arr,6])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 375))

#     def test_376(self):
#         input = """
# program example;
# function multiplyArray(arr: array[4] of integer): integer;
# begin
#     var product, i: integer;
#     product := 1;
#     i := 0;
#     loop n do
#     begin
#         product := product * arr[i];
#         i := i + 1;
#     end
#     multiplyArray := product;
# end;
# begin
#     var arr: array[4] of integer;
#     arr := [2,4,6,8];
#     writeInt(multiplyArray(arr));
# end."""
#         expect = """[[],[func(multiplyArray,[par(arr,arr([4],integer))],integer,[var(product,integer),var(i,integer),assign(product,1),assign(i,0),loop(n,[assign(product,times(product,ele(arr,[i]))),assign(i,add(i,1))]),assign(multiplyArray,product)])],[var(arr,arr([4],integer)),assign(arr,array([2,4,6,8])),call(writeInt,[call(multiplyArray,[arr])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 376))

#     def test_377(self):
#         input = """
# program example;
# function fibonacci(n: integer): integer;
# begin
#     var a, b, i, temp: integer;
#     a := 0;
#     b := 1;
#     i := 2;
#     if n = 0 then
#         fibonacci := 0;
#     if n = 1 then
#         fibonacci := 1;
#     else
#     begin
#         while i <= n do
#         begin
#             temp := b;
#             b := a + b;
#             a := temp;
#             i := i + 1;
#         end
#         fibonacci := b;
#     end
# end;
# begin
#     var n: integer;
#     n := 5;
#     writeInt(fibonacci(n));
# end."""
#         expect = """[[],[func(fibonacci,[par(n,integer)],integer,[var(a,integer),var(b,integer),var(i,integer),var(temp,integer),assign(a,0),assign(b,1),assign(i,2),if(eql(n,0),assign(fibonacci,0)),if(eql(n,1),assign(fibonacci,1),[while(le(i,n),[assign(temp,b),assign(b,add(a,b)),assign(a,temp),assign(i,add(i,1))]),assign(fibonacci,b)])])],[var(n,integer),assign(n,5),call(writeInt,[call(fibonacci,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 377))

#     def test_378(self):
#         input = """
# program example;
# function reverseNumber(n: integer): integer;
# begin
#     var reversed, digit: integer;
#     reversed := 0;
#     while n > 0 do
#     begin
#         digit := n mod 10;
#         reversed := reversed * 10 + digit;
#         n := n div 10;
#     end
#     reverseNumber := reversed;
# end;
# begin
#     var n: integer;
#     n := 1234;
#     writeInt(reverseNumber(n));
# end."""
#         expect = """[[],[func(reverseNumber,[par(n,integer)],integer,[var(reversed,integer),var(digit,integer),assign(reversed,0),while(greater(n,0),[assign(digit,imod(n,10)),assign(reversed,add(times(reversed,10),digit)),assign(n,idiv(n,10))]),assign(reverseNumber,reversed)])],[var(n,integer),assign(n,1234),call(writeInt,[call(reverseNumber,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 378))

#     def test_379(self):
#         input = """
# program example;
# function greatest(a,b,c: integer): integer;
# begin
#     if (a >= b) and (a >= c) then
#         greatest := a;
#     else 
#         if (b >= a) and (b >= c) then
#             greatest := b;
#         else
#             greatest := c;
# end;
# begin
#     var a, b, c: integer;
#     a := 4;
#     b := 8;
#     c := 6;
#     writeInt(greatest(a, b, c));
# end."""
#         expect = """[[],[func(greatest,[par(a,integer),par(b,integer),par(c,integer)],integer,[if(band(ge(a,b),ge(a,c)),assign(greatest,a),if(band(ge(b,a),ge(b,c)),assign(greatest,b),assign(greatest,c)))])],[var(a,integer),var(b,integer),var(c,integer),assign(a,4),assign(b,8),assign(c,6),call(writeInt,[call(greatest,[a,b,c])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 379))

#     def test_380(self):
#         input = """
# program example;
# function sumNaturalNumbers(n: integer): integer;
# begin
#     var sum, i: integer;
#     sum := 0;
#     i := 1;
#     while i <= n do
#     begin
#         sum := sum + i;
#         i := i + 1;
#     end
#     sumNaturalNumbers := sum;
# end;

# begin
#     var n: integer;
#     n := 6;
#     writeInt(sumNaturalNumbers(n));
# end."""
#         expect = """[[],[func(sumNaturalNumbers,[par(n,integer)],integer,[var(sum,integer),var(i,integer),assign(sum,0),assign(i,1),while(le(i,n),[assign(sum,add(sum,i)),assign(i,add(i,1))]),assign(sumNaturalNumbers,sum)])],[var(n,integer),assign(n,6),call(writeInt,[call(sumNaturalNumbers,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 380))

#     def test_381(self):
#         input = """
# program example;
# function isPerfectSquare(n: integer): boolean;
# begin
#     var i: integer;
#     i := 1;
#     while i * i <= n do
#     begin
#         if i * i = n then
#         begin
#             isPerfectSquare := true;
#             break;
#         end
#         i := i + 1;
#     end
#     if i * i > n then isPerfectSquare := false;
# end;
# begin
#     var n: integer;
#     n := 16;
#     if isPerfectSquare(n) then
#         writeStr('Perfect Square');
#     else
#         writeStr('Not a Perfect Square');
# end."""
#         expect = """[[],[func(isPerfectSquare,[par(n,integer)],boolean,[var(i,integer),assign(i,1),while(times(i,le(i,n)),[if(times(i,eql(i,n)),[assign(isPerfectSquare,true),break(null)]),assign(i,add(i,1))]),if(times(i,greater(i,n)),assign(isPerfectSquare,false))])],[var(n,integer),assign(n,16),if(call(isPerfectSquare,[n]),call(writeStr,[str("Perfect Square")]),call(writeStr,[str("Not a Perfect Square")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 381))

#     def test_382(self):
#         input = """
# program example;
# function isArmstrong(n: integer): boolean;
# begin
#     var original, sum, digit, numDigits: integer;
#     sum := 0;
#     original := n;
#     numDigits := 0;
    
#     // Calculate number of digits
#     var temp: integer;
#     temp := n;
#     while temp > 0 do
#     begin
#         temp := temp div 10;
#         numDigits := numDigits + 1;
#     end

#     // Calculate sum of each digit raised to numDigits
#     while n > 0 do
#     begin
#         digit := n mod 10;
#         var power, i: integer;
#         power := 1;
#         i := 1;
#         while i <= numDigits do
#         begin
#             power := power * digit;
#             i := i + 1;
#         end
#         sum := sum + power;
#         n := n div 10;
#     end
#     isArmstrong := (sum = original);
# end;

# begin
#     var n: integer;
#     n := 153;
#     if isArmstrong(n) then writeStr('Armstrong');
#     else writeStr('Not Armstrong');
# end."""
#         expect = """[[],[func(isArmstrong,[par(n,integer)],boolean,[var(original,integer),var(sum,integer),var(digit,integer),var(numDigits,integer),assign(sum,0),assign(original,n),assign(numDigits,0),var(temp,integer),assign(temp,n),while(greater(temp,0),[assign(temp,idiv(temp,10)),assign(numDigits,add(numDigits,1))]),while(greater(n,0),[assign(digit,imod(n,10)),var(power,integer),var(i,integer),assign(power,1),assign(i,1),while(le(i,numDigits),[assign(power,times(power,digit)),assign(i,add(i,1))]),assign(sum,add(sum,power)),assign(n,idiv(n,10))]),assign(isArmstrong,eql(sum,original))])],[var(n,integer),assign(n,153),if(call(isArmstrong,[n]),call(writeStr,[str("Armstrong")]),call(writeStr,[str("Not Armstrong")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 382))

#     def test_383(self):
#         input = """
# program example;
# // Palindrome number check program example
# function isPalindrome(n: integer): boolean;
# begin
#     var original, reversed, digit: integer;
#     original := n;
#     reversed := 0;

#     while n > 0 do
#     begin
#         digit := n mod 10;
#         reversed := reversed * 10 + digit;
#         n := n div 10;
#     end

#     isPalindrome := (original = reversed);
# end;

# begin
#     var n: integer;
#     n := 373;
#     if isPalindrome(n) then writeStr('Palindrome');
#     else writeStr('Not Palindrome');
# end."""
#         expect = """[[],[func(isPalindrome,[par(n,integer)],boolean,[var(original,integer),var(reversed,integer),var(digit,integer),assign(original,n),assign(reversed,0),while(greater(n,0),[assign(digit,imod(n,10)),assign(reversed,add(times(reversed,10),digit)),assign(n,idiv(n,10))]),assign(isPalindrome,eql(original,reversed))])],[var(n,integer),assign(n,373),if(call(isPalindrome,[n]),call(writeStr,[str("Palindrome")]),call(writeStr,[str("Not Palindrome")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 383))

#     def test_384(self):
#         input = """
# program example;
# function numDivisors(n: integer): integer;
# begin
#     var count, i: integer;
#     count := 0;
#     i := 1;
#     while i <= n do
#     begin
#         if n mod i = 0 then
#             count := count + 1;
#         i := i + 1;
#     end
#     numDivisors := count;
# end;

# begin
#     var n: integer;
#     n := 12;
#     writeInt(numDivisors(n));
# end."""
#         expect = """[[],[func(numDivisors,[par(n,integer)],integer,[var(count,integer),var(i,integer),assign(count,0),assign(i,1),while(le(i,n),[if(imod(n,eql(i,0)),assign(count,add(count,1))),assign(i,add(i,1))]),assign(numDivisors,count)])],[var(n,integer),assign(n,12),call(writeInt,[call(numDivisors,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 384))

#     def test_385(self):
#         input = """
# program example;
# procedure printMultiples(n: integer; count: integer);
# begin
#     var i: integer;
#     i := 1;
#     while i <= count do
#     begin
#         writeInt(n * i);
#         i := i + 1;
#     end
# end;
# begin
#     var n, count: integer;
#     n := 4;
#     count := 4;
#     printMultiples(n, count);
# end."""
#         expect = """[[],[proc(printMultiples,[par(n,integer),par(count,integer)],[var(i,integer),assign(i,1),while(le(i,count),[call(writeInt,[times(n,i)]),assign(i,add(i,1))])])],[var(n,integer),var(count,integer),assign(n,4),assign(count,4),call(printMultiples,[n,count])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 385))

#     def test_386(self):
#         input = """
# program example;
# function isAbundant(n: integer): boolean;
# begin
#     var sum, i: integer;
#     sum := 0;
#     i := 1;
#     while i < n do
#     begin
#         if n mod i = 0 then
#             sum := sum + i;
#         i := i + 1;
#     end
#     isAbundant := (sum > n);
# end;

# begin
#     var n: integer;
#     n := 12;
#     if isAbundant(n) then writeStr('Abundant');
#     else writeStr('Not Abundant');
# end."""
#         expect = """[[],[func(isAbundant,[par(n,integer)],boolean,[var(sum,integer),var(i,integer),assign(sum,0),assign(i,1),while(less(i,n),[if(imod(n,eql(i,0)),assign(sum,add(sum,i))),assign(i,add(i,1))]),assign(isAbundant,greater(sum,n))])],[var(n,integer),assign(n,12),if(call(isAbundant,[n]),call(writeStr,[str("Abundant")]),call(writeStr,[str("Not Abundant")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 386))

#     def test_387(self):
#         input = """
# program example;
# function triangularNumber(n: integer): integer;
# begin
#     var sum, i: integer;
#     sum := 0;
#     i := 1;
#     while i <= n do
#     begin
#         sum := sum + i;
#         i := i + 1;
#     end
#     triangularNumber := sum;
# end;
# begin
#     var n: integer;
#     n := 5;
#     writeInt(triangularNumber(n));
# end."""
#         expect = """[[],[func(triangularNumber,[par(n,integer)],integer,[var(sum,integer),var(i,integer),assign(sum,0),assign(i,1),while(le(i,n),[assign(sum,add(sum,i)),assign(i,add(i,1))]),assign(triangularNumber,sum)])],[var(n,integer),assign(n,5),call(writeInt,[call(triangularNumber,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 387))

#     def test_388(self):
#         input = """
# program example;
# function gcd(a,b: integer): integer;
# begin
#     while b <> 0 do
#     begin
#         var temp: integer;
#         temp := b;
#         b := a mod b;
#         a := temp;
#     end
#     gcd := a;
# end;
# function lcm(a,b: integer): integer;
# begin
#     lcm := (a * b) div gcd(a, b);
# end;
# begin
#     var a, b: integer;
#     a := 12;
#     b := 15;
#     writeInt(lcm(a, b));
# end."""
#         expect = """[[],[func(gcd,[par(a,integer),par(b,integer)],integer,[while(ne(b,0),[var(temp,integer),assign(temp,b),assign(b,imod(a,b)),assign(a,temp)]),assign(gcd,a)]),func(lcm,[par(a,integer),par(b,integer)],integer,[assign(lcm,idiv(times(a,b),call(gcd,[a,b])))])],[var(a,integer),var(b,integer),assign(a,12),assign(b,15),call(writeInt,[call(lcm,[a,b])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 388))

#     def test_389(self):
#         input = """
# program example;
# function isPrime(n:integer): boolean;
# begin
#     var i:integer;
#     if n <= 1 then
#         isPrime := false;
#     else
#     begin
#         isPrime := true;
#         loop n div 2 do
#         begin
#             if i = 1 then continue;
#             if n mod i = 0 then
#             begin
#                 isPrime := false;
#                 break;
#             end
#             i := i+1;
#         end
#     end
# end;
# function countPrimes(upTo: integer): integer;
# begin
#     var count, i: integer;
#     count := 0;
#     i := 2;
#     while i <= upTo do
#     begin
#         if isPrime(i) then
#             count := count + 1;
#         i := i + 1;
#     end
#     countPrimes := count;
# end;

# begin
#     var n: integer;
#     n := 10;
#     writeInt(countPrimes(n));
# end."""
#         expect = """[[],[func(isPrime,[par(n,integer)],boolean,[var(i,integer),if(le(n,1),assign(isPrime,false),[assign(isPrime,true),loop(idiv(n,2),[if(eql(i,1),continue(null)),if(imod(n,eql(i,0)),[assign(isPrime,false),break(null)]),assign(i,add(i,1))])])]),func(countPrimes,[par(upTo,integer)],integer,[var(count,integer),var(i,integer),assign(count,0),assign(i,2),while(le(i,upTo),[if(call(isPrime,[i]),assign(count,add(count,1))),assign(i,add(i,1))]),assign(countPrimes,count)])],[var(n,integer),assign(n,10),call(writeInt,[call(countPrimes,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 389))


#     def test_390(self):
#         input = """
# program example;
# function isPowerOfTwo(n: integer): boolean;
# begin
#     if n <= 0 then isPowerOfTwo := false;
#     else
#     begin
#         while n mod 2 = 0 do
#             n := n div 2;
#         isPowerOfTwo := (n = 1);
#     end
# end;
# begin
#     var n: integer;
#     n := 32;
#     if isPowerOfTwo(n) then
#         writeStr('Power of Two');
#     else
#         writeStr('Not Power of Two');
# end.
# """
#         expect = """[[],[func(isPowerOfTwo,[par(n,integer)],boolean,[if(le(n,0),assign(isPowerOfTwo,false),[while(imod(n,eql(2,0)),assign(n,idiv(n,2))),assign(isPowerOfTwo,eql(n,1))])])],[var(n,integer),assign(n,32),if(call(isPowerOfTwo,[n]),call(writeStr,[str("Power of Two")]),call(writeStr,[str("Not Power of Two")]))]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 390))

#     def test_391(self):
#         input = """
# program example;
# function factorial(n: integer): integer;
# begin
#     var res, i: integer;
#     res := 1;
#     i := 1;
#     while i <= n do
#     begin
#         res := res * i;
#         i := i + 1;
#     end
#     factorial := res;
# end;
# function catalanNumber(n: integer): integer;
# begin
#     catalanNumber := factorial(2 * n) div (factorial(n + 1) * factorial(n));
# end;
# begin
#     var n: integer;
#     n := 4;
#     writeInt(catalanNumber(n));
# end."""
#         expect = """[[],[func(factorial,[par(n,integer)],integer,[var(res,integer),var(i,integer),assign(res,1),assign(i,1),while(le(i,n),[assign(res,times(res,i)),assign(i,add(i,1))]),assign(factorial,res)]),func(catalanNumber,[par(n,integer)],integer,[assign(catalanNumber,idiv(call(factorial,[times(2,n)]),times(call(factorial,[add(n,1)]),call(factorial,[n]))))])],[var(n,integer),assign(n,4),call(writeInt,[call(catalanNumber,[n])])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 391))

#     def test_392(self):
#         input = """
# program example;
# function double(n:integer):integer;
# begin
#     double := n * 2;
# end;
# function triple(n:integer):integer;
# begin
#     triple := n * 3;
# end;
# function square(n:integer):integer;
# begin
#     square := n * n;
# end;
# function cube(n:integer):integer;
# begin
#     cube := n * n * n;
# end;
# begin
#     var n:integer;
#     n := 2;
#     writeInt(double(triple(square(cube(n)))) + 10 ---2);
# end."""
#         expect = """[[],[func(double,[par(n,integer)],integer,[assign(double,times(n,2))]),func(triple,[par(n,integer)],integer,[assign(triple,times(n,3))]),func(square,[par(n,integer)],integer,[assign(square,times(n,n))]),func(cube,[par(n,integer)],integer,[assign(cube,times(times(n,n),n))])],[var(n,integer),assign(n,2),call(writeInt,[sub(add(call(double,[call(triple,[call(square,[call(cube,[n])])])]),10),sub(sub(2)))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 392))

#     def test_393(self):
#         input = """
# program example;
# begin
#     var a,b:integer;
#     a := 2;
#     b := 3;
#     writeInt((a * b + a) mod (b - 1) + (b * 3 mod a));
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),assign(a,2),assign(b,3),call(writeInt,[add(imod(add(times(a,b),a),sub(b,1)),imod(times(b,3),a))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 393))

#     def test_394(self):
#         input = """
# program example;
# begin
#     var a,b,c:integer;
#     a := 2;
#     b := 3;
#     c := 5;
#     writeInt(a*a*a + b*(a*-c) + -c*-(a) ----- (b*(-2+a)));
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),var(c,integer),assign(a,2),assign(b,3),assign(c,5),call(writeInt,[sub(add(add(times(times(a,a),a),times(b,times(a,sub(c)))),times(sub(c),sub(a))),sub(sub(sub(sub(times(b,add(sub(2),a)))))))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 394))

#     def test_395(self):
#         input = """
# program example;
# begin
#     var a,b,c:integer;
#     a := 2;
#     b := 3;
#     c := 5;
#     writeBool( (not ((a>b) and (a > b-c))) or (not (a <> 0 and b <> 0 and c = 0)));
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),var(c,integer),assign(a,2),assign(b,3),assign(c,5),call(writeBool,[bor(bnot(band(greater(a,b),sub(greater(a,b),c))),bnot(eql(ne(ne(a,band(0,b)),band(0,c)),0)))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 395))

#     def test_396(self):
#         input = """
# program example;
# begin
#     var a,b,c:integer;
#     a := 2;
#     b := 3;
#     c := 5;
#     writeBool( (not ((a>b) and (a > b-c))) or (not ((a <> 0) and (b <> 0) and (c = 0))));
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),var(c,integer),assign(a,2),assign(b,3),assign(c,5),call(writeBool,[bor(bnot(band(greater(a,b),sub(greater(a,b),c))),bnot(band(band(ne(a,0),ne(b,0)),eql(c,0))))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 396))

#     def test_397(self):
#         input = """
# program example;
# begin
#     var a,b,c:integer;
#     a := 2;
#     b := 3;
#     c := 5;
#     var arr: array[3] of integer;
#     arr[0] := a+b+c;
#     arr[1] := a*b*c;
#     arr[2] := a-b-c;
#     writeInt(arr[0] ----- arr[1] + ---arr[2]);
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),var(c,integer),assign(a,2),assign(b,3),assign(c,5),var(arr,arr([3],integer)),assign(ele(arr,[0]),add(add(a,b),c)),assign(ele(arr,[1]),times(times(a,b),c)),assign(ele(arr,[2]),sub(sub(a,b),c)),call(writeInt,[add(sub(ele(arr,[0]),sub(sub(sub(sub(ele(arr,[1])))))),sub(sub(sub(ele(arr,[2])))))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 397))

#     def test_398(self):
#         input = """
# program example;
# begin
#     var a,b,c:integer;
#     a := 2;
#     b := 3;
#     c := 5;
#     var arr: array[3] of integer;
#     arr[0] := a+b+c;
#     arr[1] := a*b*c;
#     arr[2] := a-b-c;
#     writeBool(((arr[0] ----- arr[1] + ---arr[2]) > 0) or (arr[0] <> 0));
# end."""
#         expect = """[[],[],[var(a,integer),var(b,integer),var(c,integer),assign(a,2),assign(b,3),assign(c,5),var(arr,arr([3],integer)),assign(ele(arr,[0]),add(add(a,b),c)),assign(ele(arr,[1]),times(times(a,b),c)),assign(ele(arr,[2]),sub(sub(a,b),c)),call(writeBool,[bor(greater(add(sub(ele(arr,[0]),sub(sub(sub(sub(ele(arr,[1])))))),sub(sub(sub(ele(arr,[2]))))),0),ne(ele(arr,[0]),0))])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 398))

#     def test_399(self):
#         input = """
# program example;
# begin
#     var a,b,c:string;
#     a := 'abc';
#     b := 'def';
#     c := 'ghi';
#     writeStr('a');
#     writeStr(c);
# end."""
#         expect = """[[],[],[var(a,string),var(b,string),var(c,string),assign(a,str("abc")),assign(b,str("def")),assign(c,str("ghi")),call(writeStr,[str("a")]),call(writeStr,[c])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 399))

#     def test_400(self):
#         input = """
# program example;
# begin
#     const a = 'abc';
#     const b = 'ab''cd';
#     const c = 'ab"cd''ef"g';
#     const d = 'abc \\\\ \\n \\t';
#     const e = '''';
#     writeStr(a);
# end."""
#         expect = """[[],[],[const(a,str("abc")),const(b,str("ab\\'cd")),const(c,str("ab\\"cd\\'ef\\"g")),const(d,str("abc \\\\ \\n \\t")),const(e,str("\\'")),call(writeStr,[a])]]. """
#         self.assertTrue(TestPreGen.test(input, expect, 400))

    def test_400(self):
        input = """
program example;
var arr: array[4] of string;
begin
    arr[0] := 'abc';
    arr[1] := 'def';
    arr[2] := 'ghi';
    arr[3] := 'xyz';
    var i: integer;
    i := 0;
    loop 4 do 
    begin
        writeString(arr[i]);
        i := i+1;
    end
end."""
        expect = """[[var(arr,arr([4],string))],[],[assign(ele(arr,[0]),str("abc")),assign(ele(arr,[1]),str("def")),assign(ele(arr,[2]),str("ghi")),assign(ele(arr,[3]),str("xyz")),var(i,integer),assign(i,0),loop(4,[call(writeString,[ele(arr,[i])]),assign(i,add(i,1))])]]. """
        self.assertTrue(TestPreGen.test(input, expect, 400))