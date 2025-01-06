import unittest
from TestUtils import TestVM


class VMSuite(unittest.TestCase):
    # def test_400(self):
    #     input = """[[],[],[var(a,integer),var(b,real),var(c,boolean),assign(a,call(readInt,[])),assign(b,call(readReal,[])),assign(c,call(readBool,[])),call(writeInt,[a]),call(writeReal,[b]),call(writeBool,[c])]]."""
    #     expect = "21.0"
    #     self.assertTrue(TestVM.test(input, expect, 400))

    def test_simple_program(self):
        input = """[[],[],[call(writeInt,[3])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 401))

    def test_simple_expression(self):
        input = """[[],[],[call(writeInt,[add(3,1)])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 402))

    def test_redeclaration(self):
        input = """[[var(a,integer),var(b,integer),var(a,real)],[],[call(writeInt,[1])]]."""
        expect = "Redeclared identifier: var(a,real)"
        self.assertTrue(TestVM.test(input, expect, 403))

    def test_minus_expression(self):
        input = """[[],[],[call(writeInt,[sub(3,1)])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 404))

    def test_405(self):
        input = """[[],[],[
        call(writeLn,[]),
        call(writeRealLn,[add(1.2,0.8)]),call(writeRealLn,[rdiv(1.6,0.8)]),
        call(writeIntLn,[idiv(2,1)]),call(writeIntLn,[imod(7,3)]),
        call(writeBoolLn,[bnot(false)]),
        call(writeBoolLn,[band(true,true)]),call(writeBoolLn,[bor(false,true)]),
        call(writeBoolLn,[greater(2,1)]),call(writeBoolLn,[less(2,1)]),
        call(writeBoolLn,[ge(2,1)]),call(writeBoolLn,[le(2,1)]),
        call(writeBoolLn,[eql(2,2)]),call(writeBoolLn,[ne(2,2)])]]."""
        expect = """
2.0
2.0
2
1
true
true
true
true
false
true
false
true
false
"""
        self.assertTrue(TestVM.test(input, expect, 405))

    def test_406(self):
        input = """[[var(a,integer),var(b,integer)],[],[assign(a,1),call(writeInt,[a])]]."""
        expect = "1"
        self.assertTrue(TestVM.test(input, expect, 406))

    def test_407(self):
        input = """[[],[],[var(a,integer),var(b,integer),assign(a,20),call(writeInt,[a])]]."""
        expect = "20"
        self.assertTrue(TestVM.test(input, expect, 407))

    def test_408(self):
        input = """[[],[],[var(a,integer),var(b,integer),assign(a,10),assign(b,30),call(writeInt,[add(a,b)])]]."""
        expect = "40"
        self.assertTrue(TestVM.test(input, expect, 408))

    def test_409(self):
        input = """[[],[],[var(a,integer),assign(a,10),call(writeInt,[add(a,true)])]]."""
        expect = "Type mismatch: add(a,true)"
        self.assertTrue(TestVM.test(input, expect, 409))

    def test_410(self):
        input = """[[],[],[var(a,real),call(writeReal,[a])]]."""
        expect = "Invalid expression: a"
        self.assertTrue(TestVM.test(input, expect, 410))

    def test_411(self):
        input = """[[],[],[var(a,real),call(writeReal,[a,a])]]."""
        expect = "Wrong number of arguments: call(writeReal,[a,a])"
        self.assertTrue(TestVM.test(input, expect, 411))

    def test_412(self):
        input = """[[var(a,integer)],[proc(foo,[],[call(writeInt,[a])])],[assign(a,3),call(foo,[])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 412))

    def test_413(self):
        input = """[[var(a,integer)],[proc(foo,[],[call(writeInt,[a])])],[assign(a,3),call(foo,[10])]]."""
        expect = "Wrong number of arguments: call(foo,[10])"
        self.assertTrue(TestVM.test(input, expect, 413))

    def test_414(self):
        input = """[[],[proc(foo,[par(a,integer)],[call(writeInt,[a])])],[var(b,integer),assign(b,3),call(foo,[b])]]. """
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 414))

    def test_415(self):
        input = """[[],[proc(foo,[par(a,integer),par(b,integer)],[call(writeInt,[a])])],[var(c,real),assign(c,1.5),call(foo,[1,c])]]. """
        expect = "Type mismatch: call(foo,[1,c])"
        self.assertTrue(TestVM.test(input, expect, 415))

    def test_416(self):
        input = """[[],[],[var(i,integer),assign(i,10),if(eql(i,10),call(writeInt,[i]))]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 416))

    def test_417(self):
        input = """[[],[],[var(i,integer),assign(i,10),if(add(i,10),call(writeInt,[i]))]]."""
        expect = "Type mismatch: if(add(i,10),call(writeInt,[i]))"
        self.assertTrue(TestVM.test(input, expect, 417))

    def test_418(self):
        input = """[[var(a,integer)],[],[assign(a,10),if(eql(a,5),assign(a,11),assign(a,12)),call(writeInt,[a])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 418))

    def test_419(self):
        input = """[[var(a,integer)],[],[assign(a,10),if(eql(a,10),assign(a,11),assign(a,12)),call(writeInt,[a])]]."""
        expect = "11"
        self.assertTrue(TestVM.test(input, expect, 419))

    def test_420(self):
        input = """[[var(a,integer)],[],[assign(a,10),while(add(a,10),assign(a,11))]]."""
        expect = "Type mismatch: while(add(a,10),assign(a,11))"
        self.assertTrue(TestVM.test(input, expect, 420))

    def test_421(self):
        input = """[[var(a,integer)],[],[assign(a,10),while(eql(a,10),assign(a,11))]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 421))

    def test_422(self):
        input = """[[var(a,integer)],[],[assign(a,11),do([assign(a,9),call(writeInt,[a])],add(a,10))]]."""
        expect = "Type mismatch: do([assign(a,9),call(writeInt,[a])],add(a,10))"
        self.assertTrue(TestVM.test(input, expect, 422))

    def test_423(self):
        input = """[[var(a,integer)],[],[assign(a,11),do([assign(a,9),call(writeInt,[a])],eql(a,10))]]."""
        expect = "9"
        self.assertTrue(TestVM.test(input, expect, 423))

    def test_424(self):
        input = """[[var(a,integer)],[],[assign(a,1),while(less(a,4),[call(writeInt,[a]),assign(a,add(a,1))])]]."""
        expect = "123"
        self.assertTrue(TestVM.test(input, expect, 424))

    def test_425(self):
        input = """[[var(a,integer)],[],[assign(a,10),if(ne(a,10),assign(a,11),[assign(a,12),call(writeInt,[a])])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 425))

    def test_426(self):
        input = """[[var(a,integer)],[],[assign(a,1),loop(eql(a,1),call(writeInt,[2]))]]."""
        expect = "Type mismatch: loop(eql(a,1),call(writeInt,[2]))"
        self.assertTrue(TestVM.test(input, expect, 426))

    def test_427(self):
        input = """[[var(a,integer)],[],[assign(a,1),loop(add(a,1),call(writeInt,[2]))]]."""
        expect = "22"
        self.assertTrue(TestVM.test(input, expect, 427))

    def test_428(self):
        input = """[[var(a,integer)],[],[assign(a,1),loop(add(a,1),[assign(a,10),call(writeInt,[a])])]]."""
        expect = "1010"
        self.assertTrue(TestVM.test(input, expect, 428))

    def test_429(self):
        input = """[[var(a,integer)],[],[assign(a,1),while(less(a,4),[call(writeInt,[a]),assign(a,add(a,2))])]]."""
        expect = "13"
        self.assertTrue(TestVM.test(input, expect, 429))

    def test_430(self):
        input = """[[var(a,integer)],[],[assign(a,1),while(less(a,10),[if(eql(imod(a,2),0),call(writeInt,[a])),assign(a,add(a,1))])]]."""
        expect = "2468"
        self.assertTrue(TestVM.test(input, expect, 430))

    def test_431(self):
        input = """[[var(a,arr([2],integer))],[],[assign(ele(a,[add(1,2)]),true)]]."""
        expect = "Type mismatch: assign(ele(a,[add(1,2)]),true)"
        self.assertTrue(TestVM.test(input, expect, 431))

    def test_432(self):
        input = """[[var(a,arr([2],integer))],[],[assign(ele(a,[true]),0)]]."""
        expect = "Type mismatch: ele(a,[true])"
        self.assertTrue(TestVM.test(input, expect, 432))

    def test_433(self):
        input = """[[var(a,arr([2],integer))],[],[assign(ele(a,[0]),0),call(writeInt,[ele(a,[0])])]]."""
        expect = "0"
        self.assertTrue(TestVM.test(input, expect, 433))

    def test_434(self):
        input = """[[var(a,arr([2],integer))],[],[assign(ele(a,[0]),0),assign(ele(a,[0]),10),assign(ele(a,[1]),20),call(writeInt,[add(ele(a,[0]),ele(a,[1]))])]]."""
        expect = "30"
        self.assertTrue(TestVM.test(input, expect, 434))

    def test_435(self):
        input = """[[var(a,arr([2],integer))],[],[call(writeInt,[ele(a,[0])])]]."""
        expect = "Invalid expression: ele(a,[0])"
        self.assertTrue(TestVM.test(input, expect, 435))

    def test_436(self):
        input = """[[var(a,arr([2],integer)),var(b,integer)],[],[assign(b,ele(a,[0]))]]."""
        expect = "Invalid expression: ele(a,[0])"
        self.assertTrue(TestVM.test(input, expect, 436))

    def test_437(self):
        input = """[[var(a,arr([2],integer))],[],[call(writeInt,[ele(a,[2])])]]."""
        expect = "Index out of bound: ele(a,[2])"
        self.assertTrue(TestVM.test(input, expect, 437))

    def test_438(self):
        input = """[[var(a,arr([2],integer))],[],[assign(ele(a,[2]),0)]]."""
        expect = "Index out of bound: ele(a,[2])"
        self.assertTrue(TestVM.test(input, expect, 438))

    def test_439(self):
        input = """[[var(a,arr([2],integer))],[],[call(writeInt,[ele(a,[-1])])]]."""
        expect = "Index out of bound: ele(a,[-1])"
        self.assertTrue(TestVM.test(input, expect, 439))

    def test_440(self):
        input = """[[var(b,integer)],[func(foo,[],integer,[assign(foo,2)])],[assign(b,call(foo,[])),call(writeInt,[b])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 440))

    def test_441(self):
        input = """[[var(b,integer)],[func(foo,[par(a,integer)],integer,[assign(foo,add(a,1))])],[assign(b,call(foo,[3])),call(writeInt,[b])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 441))

    def test_442(self):
        input = """[[],[func(foo,[par(a,integer)],integer,[assign(foo,add(a,1))])],[call(writeInt,[add(call(foo,[3]),call(foo,[4]))])]]."""
        expect = "9"
        self.assertTrue(TestVM.test(input, expect, 442))

    def test_443(self):
        input = """[[],[func(foo,[par(a,integer),par(b,integer)],integer,[assign(foo,times(a,b))])],[call(writeInt,[call(foo,[3,4])])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 443))

    def test_444(self):
        input = """[[],[proc(foo,[par(a,integer),par(b,integer)],[call(writeInt,[a]),call(writeInt,[b])])],[var(c,integer),assign(c,3),call(foo,[2,c])]]."""
        expect = "23"
        self.assertTrue(TestVM.test(input, expect, 444))

    def test_445(self):
        input = """[[],[proc(foo,[par(a,arr([2],integer))],[call(writeInt,[add(ele(a,[0]),ele(a,[1]))])])],[var(arr,arr([2],integer)),assign(ele(arr,[0]),1),assign(ele(arr,[1]),add(ele(arr,[0]),1)),call(foo,[arr])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 445))

    def test_446(self):
        input = """[[],[func(foo,[par(a,arr([2],integer))],integer,[assign(foo,add(ele(a,[0]),ele(a,[1])))])],[var(arr,arr([2],integer)),assign(ele(arr,[0]),1),assign(ele(arr,[1]),add(ele(arr,[0]),1)),call(writeInt,[call(foo,[arr])])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 446))

    def test_447(self):
        input = """[[],[],[var(arr,arr([1,2,3],integer)),assign(ele(arr,[0,0,0]),1),assign(ele(arr,[0,0,1]),add(ele(arr,[0,0,0]),1)),call(writeInt,[ele(arr,[0,0,1])])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 447))

    def test_448(self):
        input = """[[],[func(findMax,[par(a,arr([3],integer)),par(n,integer)],integer,[var(max,integer),var(i,integer),assign(max,ele(a,[0])),assign(i,1),loop(sub(n,1),[if(greater(ele(a,[i]),max),assign(max,ele(a,[i]))),assign(i,add(i,1))]),assign(findMax,max)])],[var(arr,arr([3],integer)),assign(ele(arr,[0]),1),assign(ele(arr,[1]),7),assign(ele(arr,[2]),3),call(writeInt,[call(findMax,[arr,3])])]]."""
        expect = "7"
        self.assertTrue(TestVM.test(input, expect, 448))

    def test_449(self):
        input = """[[],[proc(foo,[par(arr,arr([1,2,3],integer))],[call(writeInt,[add(ele(arr,[0,0,0]),ele(arr,[0,0,1]))])])],[var(arr,arr([1,2,3],integer)),assign(ele(arr,[0,0,0]),1),assign(ele(arr,[0,0,1]),add(ele(arr,[0,0,0]),1)),call(foo,[arr])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 449))

    def test_450(self):
        input = """[[var(a,integer)],[proc(foo,[par(a,integer)],[assign(a,4),call(writeInt,[a])])],[assign(a,3),call(foo,[a])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 450))

    def test_451(self):
        input = """[[var(a,integer)],[proc(foo,[par(a,integer)],[assign(a,4),call(writeInt,[a])])],[assign(a,3),call(foo,[a]),call(writeInt,[a])]]."""
        expect = "43"
        self.assertTrue(TestVM.test(input, expect, 451))

    def test_452(self):
        input = """[[var(a,integer)],[],[var(a,integer),assign(a,3),call(writeInt,[a])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 452))

    def test_453(self):
        input = """[[var(a,integer)],[proc(foo1,[par(a,integer)],[]),proc(foo2,[par(a,integer)],[])],[]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 453))

    def test_454(self):
        input = """[[var(a,integer)],[proc(foo,[par(a,integer)],[var(a,integer)])],[]]."""
        expect = "Redeclared identifier: var(a,integer)"
        self.assertTrue(TestVM.test(input, expect, 454))

    def test_455(self):
        input = """[[var(a,integer)],[proc(foo,[par(a,integer)],[call(writeInt,[b])])],[var(b,integer),call(foo,[1])]]."""
        expect = "Undeclared identifier: b"
        self.assertTrue(TestVM.test(input, expect, 455))

    def test_456(self):
        input = """[[var(a,integer),var(b,integer)],[proc(foo,[par(a,integer)],[call(writeInt,[b])])],[]]."""
        expect = ""
        self.assertTrue(TestVM.test(input, expect, 456))

    def test_457(self):
        input = """[[var(a,integer),var(b,integer)],[proc(foo,[par(a,integer)],[call(writeInt,[b])])],[call(foo,[1])]]."""
        expect = "Invalid expression: b"
        self.assertTrue(TestVM.test(input, expect, 457))

    def test_458(self):
        input = """[[var(a,integer),var(b,integer)],[proc(foo,[par(a,integer)],[call(writeInt,[b])])],[var(b,integer),assign(b,1),call(foo,[1])]]."""
        expect = "Invalid expression: b"
        self.assertTrue(TestVM.test(input, expect, 458))

    def test_459(self):
        input = """[[],[func(findMax,[par(arr,arr([5],integer)),par(n,integer)],integer,[var(max,integer),var(i,integer),assign(max,ele(arr,[0])),assign(i,1),loop(sub(n,1),[if(greater(ele(arr,[i]),max),assign(max,ele(arr,[i]))),assign(i,add(i,1))]),assign(findMax,max)])],[var(arr,arr([5],integer)),assign(ele(arr,[0]),3),assign(ele(arr,[1]),5),assign(ele(arr,[2]),7),assign(ele(arr,[3]),2),assign(ele(arr,[4]),4),call(writeInt,[call(findMax,[arr,5])])]]."""
        expect = "7"
        self.assertTrue(TestVM.test(input, expect, 459))

    def test_460(self):
        input = """[[var(arr,arr([4],integer))],[],[var(i,integer),assign(ele(arr,[0]),1),assign(ele(arr,[1]),2),assign(ele(arr,[2]),3),assign(ele(arr,[3]),4),loop(2,[assign(i,0),loop(4,[call(writeInt,[ele(arr,[i])]),assign(i,add(i,1))])])]]. """
        expect = "12341234"
        self.assertTrue(TestVM.test(input, expect, 460))
    
    def test_461(self):
        input = """[[var(a,arr([4],integer))],[proc(bubbleSort,[par(n,integer)],[var(i,integer),var(j,integer),var(temp,integer),assign(i,0),loop(sub(n,1),[assign(j,0),loop(sub(sub(n,i),1),[if(greater(ele(a,[j]),ele(a,[add(j,1)])),[assign(temp,ele(a,[j])),assign(ele(a,[j]),ele(a,[add(j,1)])),assign(ele(a,[add(j,1)]),temp)]),assign(j,add(j,1))]),assign(i,add(i,1))])])],[var(i,integer),assign(ele(a,[0]),4),assign(ele(a,[1]),3),assign(ele(a,[2]),2),assign(ele(a,[3]),1),call(bubbleSort,[4]),assign(i,0),loop(4,[call(writeInt,[ele(a,[i])]),assign(i,add(i,1))])]]."""
        expect = "1234"
        self.assertTrue(TestVM.test(input, expect, 461))

    def test_462(self):
        input = """[[],[func(gcd,[par(a,integer),par(b,integer)],integer,[var(temp,integer),while(ne(b,0),[assign(temp,b),assign(b,imod(a,b)),assign(a,temp)]),assign(gcd,a)])],[var(a,integer),var(b,integer),assign(a,10),assign(b,8),call(writeInt,[call(gcd,[a,b])])]]."""
        expect = "2"
        self.assertTrue(TestVM.test(input, expect, 462))

    def test_463(self):
        input = """[[],[func(power,[par(base,integer),par(exp,integer)],integer,[var(result,integer),assign(result,1),while(greater(exp,0),[if(eql(imod(exp,2),1),assign(result,times(result,base))),assign(base,times(base,base)),assign(exp,idiv(exp,2))]),assign(power,result)])],[var(base,integer),var(exp,integer),assign(base,2),assign(exp,5),call(writeInt,[call(power,[base,exp])])]]."""
        expect = "32"
        self.assertTrue(TestVM.test(input, expect, 463))

    def test_464(self):
        input = """[[],[func(sum,[par(n,integer)],integer,[var(m,integer),var(res,integer),assign(m,n),assign(res,0),while(ne(m,0),[assign(res,add(res,imod(m,10))),assign(m,idiv(m,10))]),assign(sum,res)])],[var(n,integer),assign(n,987),call(writeInt,[call(sum,[n])])]]."""
        expect = "24"
        self.assertTrue(TestVM.test(input, expect, 464))

    def test_465(self):
        input = """[[],[],[var(a,string),var(b,string),var(c,string),assign(a,str("abc")),assign(b,str("def")),assign(c,str("ghi")),call(writeStr,[str("a")]),call(writeStr,[c])]]."""
        expect = "aghi"
        self.assertTrue(TestVM.test(input, expect, 465))

    def test_466(self):
        input = """[[var(a,string),var(b,string),var(c,string)],[],[assign(a,str("abc")),assign(b,str("def")),assign(c,str("ghi")),call(writeStr,[str("a")]),call(writeStr,[c])]]."""
        expect = "aghi"
        self.assertTrue(TestVM.test(input, expect, 466))

    def test_467(self):
        input = """[[var(arr,arr([4],string))],[],[var(i,integer),assign(ele(arr,[0]),str("abc")),assign(ele(arr,[1]),str("def")),assign(ele(arr,[2]),str("ghi")),assign(ele(arr,[3]),str("xyz")),assign(i,0),loop(4,[call(writeStr,[ele(arr,[i])]),assign(i,add(i,1))])]]."""
        expect = "abcdefghixyz"
        self.assertTrue(TestVM.test(input, expect, 467))

    def test_468(self):
        input = """[[],[],[var(a,boolean),var(b,boolean),var(c,boolean),assign(a,true),assign(b,false),assign(c,bor(true,b)),call(writeBool,[c]),call(writeBool,[false])]]."""
        expect = "truefalse"
        self.assertTrue(TestVM.test(input, expect, 468))

    def test_469(self):
        input = """[[var(a,boolean),var(b,boolean),var(c,boolean)],[],[assign(a,true),assign(b,false),assign(c,bor(true,b)),call(writeBool,[c]),call(writeBool,[false])]]."""
        expect = "truefalse"
        self.assertTrue(TestVM.test(input, expect, 469))

    def test_470(self):
        input = """[[var(arr,arr([4],boolean))],[],[var(i,integer),assign(ele(arr,[0]),true),assign(ele(arr,[1]),false),assign(ele(arr,[2]),bor(ele(arr,[0]),ele(arr,[1]))),assign(ele(arr,[3]),band(ele(arr,[0]),ele(arr,[1]))),assign(i,0),loop(4,[call(writeBool,[ele(arr,[i])]),assign(i,add(i,1))])]]. """
        expect = "truefalsetruefalse"
        self.assertTrue(TestVM.test(input, expect, 470))

    def test_471(self):
        input = """[[const(i,3)],[],[call(writeInt,[i])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 471))

    def test_472(self):
        input = """[[],[],[const(i,3),call(writeInt,[i])]]."""
        expect = "3"
        self.assertTrue(TestVM.test(input, expect, 472))

    def test_473(self):
        input = """[[],[],[const(i,3),assign(i,4),call(writeInt,[i])]]."""
        expect = "Cannot assign to a constant: assign(i,4)"
        self.assertTrue(TestVM.test(input, expect, 473))

    def test_474(self):
        input = """[[],[],[const(i,3),var(i,integer),assign(i,4),call(writeInt,[i])]]."""
        expect = "Redeclared identifier: var(i,integer)"
        self.assertTrue(TestVM.test(input, expect, 474))

    def test_475(self):
        input = """[[const(i,3)],[],[var(i,integer),assign(i,4),call(writeInt,[i])]]."""
        expect = "4"
        self.assertTrue(TestVM.test(input, expect, 475))

    def test_476(self):
        input = """[[],[],[break(null)]]."""
        expect = "Break not in a loop: break(null)"
        self.assertTrue(TestVM.test(input, expect, 476))

    def test_477(self):
        input = """[[],[],[continue(null)]]."""
        expect = "Continue not in a loop: continue(null)"
        self.assertTrue(TestVM.test(input, expect, 477))

    def test_478(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(5,[assign(a,add(a,1)),if(eql(a,3),break(null),call(writeInt,[a]))])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 478))

    def test_479(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(5,[assign(a,add(a,1)),if(eql(a,3),continue(null),call(writeInt,[a]))])]]."""
        expect = "1245"
        self.assertTrue(TestVM.test(input, expect, 479))

    def test_480(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(5,[assign(a,add(a,1)),if(eql(a,3),break(null),call(writeInt,[a]))]),assign(a,0),loop(5,[assign(a,add(a,1)),call(writeInt,[a])])]]."""
        expect = "1212345"
        self.assertTrue(TestVM.test(input, expect, 480))

    def test_481(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(5,[assign(a,add(a,1)),if(eql(a,3),continue(null),call(writeInt,[a]))]),assign(a,0),loop(5,[assign(a,add(a,1)),call(writeInt,[a])])]]."""
        expect = "124512345"
        self.assertTrue(TestVM.test(input, expect, 481))

    def test_482(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(3,[loop(5,[assign(a,add(a,1)),if(eql(a,4),break(null),call(writeInt,[a]))])])]]."""
        expect = "123567891011121314"
        self.assertTrue(TestVM.test(input, expect, 482))

    def test_483(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(3,[loop(5,[assign(a,add(a,1)),if(eql(a,2),continue(null),call(writeInt,[a]))])])]]."""
        expect = "13456789101112131415"
        self.assertTrue(TestVM.test(input, expect, 483))

    def test_484(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(3,[assign(a,add(a,1)),loop(3,[assign(a,add(a,1)),if(eql(a,4),break(null),call(writeInt,[a]))]),call(writeInt,[a])])]]."""
        expect = "234678810111212"
        self.assertTrue(TestVM.test(input, expect, 484))

    def test_485(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(5,[if(eql(a,2),continue(null),assign(a,add(a,1))),call(writeInt,[a])])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 485))

    def test_486(self):
        input = """[[],[],[var(a,integer),assign(a,0),loop(2,[loop(3,[assign(a,add(a,1)),if(eql(a,2),continue(null),loop(2,[assign(a,add(a,1)),if(eql(a,5),break(null),call(writeInt,[a]))]))])])]]."""
        expect = "2378101113141617"
        self.assertTrue(TestVM.test(input, expect, 486))

    def test_487(self):
        input = """[[],[],[var(a,integer),assign(a,0),while(less(a,5),[assign(a,add(a,1)),if(eql(a,3),break(null),call(writeInt,[a]))])]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 487))

    def test_488(self):
        input = """[[],[],[var(a,integer),assign(a,0),while(less(a,5),[assign(a,add(a,1)),if(eql(a,3),continue(null),call(writeInt,[a]))])]]."""
        expect = "1245"
        self.assertTrue(TestVM.test(input, expect, 488))

    def test_489(self):
        input = """[[],[],[var(a,integer),var(b,integer),assign(a,0),while(less(a,3),[assign(b,0),assign(a,add(a,1)),while(less(b,2),[assign(b,add(b,1)),call(writeInt,[a]),call(writeInt,[b])])])]]."""
        expect = "111221223132"
        self.assertTrue(TestVM.test(input, expect, 489))

    def test_490(self):
        input = """[[],[],[var(a,integer),assign(a,0),while(true,[assign(a,add(a,1)),call(writeInt,[a]),if(eql(a,3),break(null))])]]."""
        expect = "123"
        self.assertTrue(TestVM.test(input, expect, 490))

    def test_491(self):
        input = """[[],[],[var(a,integer),assign(a,0),do([assign(a,add(a,1)),if(eql(a,3),break(null),call(writeInt,[a]))],less(a,5))]]."""
        expect = "12"
        self.assertTrue(TestVM.test(input, expect, 491))

    def test_492(self):
        input = """[[],[],[var(a,integer),assign(a,0),do([assign(a,add(a,1)),if(eql(a,3),continue(null),call(writeInt,[a]))],less(a,5))]]."""
        expect = "1245"
        self.assertTrue(TestVM.test(input, expect, 492))

    def test_493(self):
        input = """[[],[],[var(a,integer),assign(a,0),do([do([assign(a,add(a,1)),if(eql(a,2),continue(null),call(writeInt,[a]))],less(a,4)),if(eql(a,3),break(null))],less(a,5))]]."""
        expect = "1345"
        self.assertTrue(TestVM.test(input, expect, 493))

    def test_494(self):
        input = """[[],[],[var(a,integer),assign(a,0),[var(a,integer),assign(a,1),call(writeInt,[a])],call(writeInt,[a])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 494))

    def test_495(self):
        input = """[[var(a,integer)],[],[assign(a,0),[var(a,integer),assign(a,1),call(writeInt,[a])],call(writeInt,[a])]]."""
        expect = "10"
        self.assertTrue(TestVM.test(input, expect, 495))

    def test_496(self):
        input = """[[],[
        func(findMax,[par(arr,arr([3],integer)),par(n,integer)],integer,[var(max,integer),var(i,integer),assign(max,ele(arr,[0])),assign(i,1),loop(sub(n,1),[if(greater(ele(arr,[i]),max),assign(max,ele(arr,[i]))),assign(i,add(i,1))]),assign(findMax,max)])],
        [var(arr,arr([3],integer)),assign(ele(arr,[0]),1),assign(ele(arr,[1]),7),assign(ele(arr,[2]),3),
        call(writeInt,[call(findMax,[arr,3])])]]."""
        expect = "7"
        self.assertTrue(TestVM.test(input, expect, 496))

    def test_497(self):
        input = """[[var(a,integer)],[],[[var(a,integer),assign(a,1),call(writeInt,[a])],call(writeInt,[a])]]."""
        expect = "1Invalid expression: a"
        self.assertTrue(TestVM.test(input, expect, 497))

    def test_498(self):
        input = """[[var(a,integer)],[],[[assign(a,1),call(writeInt,[a])],call(writeInt,[a])]]."""
        expect = "11"
        self.assertTrue(TestVM.test(input, expect, 498))

    def test_499(self):
        input = """[[],[],[var(a,integer),[var(b,integer),assign(b,1),call(writeInt,[b])],call(writeInt,[b])]]."""
        expect = "Undeclared identifier: b"
        self.assertTrue(TestVM.test(input, expect, 499))

    def test_500(self):
        input = """[[var(a,arr([5],integer))],[proc(init,[par(x,arr([5],integer))],[var(i,integer),assign(i,0),assign(ele(x,[i]),ele(a,[i]))]),proc(fill,[par(x,arr([5],integer))],[var(a,real),var(x,real),assign(a,5.9),call(init,[x])])],[call(fill,[a])]]."""
        expect = "Redeclared identifier: var(x,real)"
        self.assertTrue(TestVM.test(input, expect, 500))

    def test_501(self):
        input = """[[var(a,arr([5],integer))],[proc(init,[par(x,arr([5],integer))],[var(i,integer),assign(i,0),assign(ele(x,[i]),ele(a,[i]))]),proc(fill,[par(x,arr([5],integer))],[var(a,real),assign(a,5.9),call(init,[x])])],[call(fill,[a])]]."""
        expect = "Invalid expression: ele(a,[i])"
        self.assertTrue(TestVM.test(input, expect, 501))

    def test_502(self):
        input = """[[var(a,arr([5],integer))],[
proc(init,[par(x,arr([5],integer))],[
    var(i,integer),assign(i,0),loop(5,[assign(ele(x,[i]),add(i,1)),assign(i,add(i,1))]),assign(i,0),loop(5,[call(writeInt,[ele(x,[i])]),assign(i,add(i,1))])]),
proc(fill,[par(x,arr([5],integer))],[
    var(a,real),assign(a,5.9),call(init,[x])])
        ],
        [call(fill,[a]),call(writeInt,[ele(a,[0])])]]."""
        expect = "12345Invalid expression: ele(a,[0])"
        self.assertTrue(TestVM.test(input, expect, 502))

    def test_503(self):
        input = """[[var(a,arr([5],integer))],[
proc(init,[par(x,arr([5],integer))],[
    var(i,integer),assign(i,0),loop(5,[assign(ele(a,[i]),add(i,1)),assign(i,add(i,1))]),assign(i,0),loop(5,[call(writeInt,[ele(a,[i])]),assign(i,add(i,1))])]),
proc(fill,[par(x,arr([5],integer))],[
    var(a,real),assign(a,5.9),call(init,[x])])
        ],
        [call(fill,[a]),call(writeInt,[ele(a,[0])])]]."""
        expect = "123451"
        self.assertTrue(TestVM.test(input, expect, 503))

    def test_504(self):
        input = """[[var(arr,arr([4],integer))],[],[var(i,integer),assign(i,0),assign(arr,array([1,2,3,4])),loop(4,[call(writeInt,[ele(arr,[i])]),assign(i,add(i,1))])]]."""
        expect = "1234"
        self.assertTrue(TestVM.test(input, expect, 504))

    def test_505(self):
        input = """[[var(arr,arr([2,2],integer))],[],[assign(arr,array([array([2,3]),array([3,4])])),call(writeInt,[ele(arr,[0,0])]),call(writeInt,[ele(arr,[0,1])]),call(writeInt,[ele(arr,[1,0])]),call(writeInt,[ele(arr,[1,1])])]]."""
        expect = "2334"
        self.assertTrue(TestVM.test(input, expect, 505))

    def test_506(self):
        input = """[[],[func(readInt,[],real,[])],[]]."""
        expect = "Redeclared function: readInt"
        self.assertTrue(TestVM.test(input, expect, 506))

    def test_507(self):
        input = """[[],[func(foo,[],integer,[]),proc(foo,[a],[])],[]]."""
        expect = "Redeclared procedure: foo"
        self.assertTrue(TestVM.test(input, expect, 507))

    def test_508(self):
        input = """[[var(foo,integer)],[proc(foo,[a],[])],[]]."""
        expect = "Redeclared procedure: foo"
        self.assertTrue(TestVM.test(input, expect, 508))

    def test_509(self):
        input = """[[var(a,integer)],[],[assign(a,call(foo,[]))]]."""
        expect = "Undeclared function: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 509))

    def test_510(self):
        input = """[[],[],[call(foo,[])]]."""
        expect = "Undeclared procedure: call(foo,[])"
        self.assertTrue(TestVM.test(input, expect, 510))

    def test_511(self):
        input = """[[],[func(power,[par(base,integer),par(exp,integer)],integer,[var(result,integer),assign(result,1),while(greater(exp,0),[if(eql(imod(exp,2),1),assign(result,times(result,base))),assign(base,times(base,base)),assign(exp,idiv(exp,2))]),assign(power,result)])],[var(base,integer),var(exp,integer),assign(base,2),assign(exp,5),call(writeInt,[call(power,[base,exp])]),call(writeStr,[str("abc")]),call(writeInt,[add(1,1)])]]."""
        expect = "32abc2"
        self.assertTrue(TestVM.test(input, expect, 511))

    def test_512(self):
        input = """[[const(myIntConst,5),var(my1stVar,integer),var(myArrayVar,arr([5],real)),var(my2ndVar,boolean),var(my3rdVar,boolean),var(my2ndArray,arr([6,8],real)),var(my3rdArray,arr([6,8],real)),const(myRealConst,5.3e4)],[],[call(writeInt,[times(my1stVar,myIntConst)])]]."""
        expect = "Invalid expression: my1stVar"
        self.assertTrue(TestVM.test(input, expect, 512))

    def test_513(self):
        input = """[[],[func(foo,[par(arr1,arr([1,2,3],integer)),par(arr2,arr([1,2,3],integer))],integer,[var(i,integer),var(j,integer),var(k,integer),var(sum,integer),assign(i,0),assign(j,0),assign(k,0),assign(sum,0),while(less(i,1),[while(less(j,2),[while(less(k,3),[assign(sum,add(add(sum,ele(arr1,[i,j,k])),ele(arr2,[i,j,k]))),assign(k,add(k,1))]),assign(j,add(j,1))]),assign(i,add(i,1))]),assign(foo,sum)])],
        [var(arr1,arr([1,2,3],integer)),var(arr2,arr([1,2,3],integer)),
        assign(ele(arr1,[0,0,0]),1),assign(ele(arr1,[0,0,1]),1),assign(ele(arr1,[0,0,2]),1),
        assign(ele(arr1,[0,1,0]),1),assign(ele(arr1,[0,1,1]),1),assign(ele(arr1,[0,1,2]),1),
        assign(ele(arr2,[0,0,0]),1),assign(ele(arr2,[0,0,1]),1),assign(ele(arr2,[0,0,2]),1),
        assign(ele(arr2,[0,1,0]),1),assign(ele(arr2,[0,1,1]),1),assign(ele(arr2,[0,1,2]),1),
        call(writeInt,[call(foo,[arr1,arr2])])]]."""
        expect = "6"
        self.assertTrue(TestVM.test(input, expect, 513))




