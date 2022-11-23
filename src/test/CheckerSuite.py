import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *

from main.bkool.utils.AST import *


class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     input = "class io extends TestParent {}"
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_2(self):
    #     input = "class Test extends TestParent {}"
    #     expect = "Undeclared Class: TestParent"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_3(self):
    #     input = """
    #     class Ex
    #     {
    #         int my1Var = 2 + 3;
    #         static float my1Var;
    #         int a() {}
    #     }"""
    #     expect = "Redeclared Attribute: my1Var"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_4(self):
    #     """If Expr: return `ClassType(C)`"""
    #     input = """
    #     class A {}
    #     class B extends A {}
    #     class C {
    #         A v;
    #         B x = v + v;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x),BinaryOp(+,Id(v),Id(v)))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_5(self):
    #     """If Expr: return `FloatType()`"""
    #     input = """
    #     class C {
    #         int a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_6(self):
    #     """If Expr: return `FloatType()` (check if not the same type)"""
    #     input = """
    #     class C {
    #         string a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_7(self):
    #     """If Expr: return `FloatType()` (check if not the same type)"""
    #     input = """
    #     class C {
    #         final string a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),StringType,BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_8(self):
    #     """If Expr: return `FloatType()` (check if not the same type) [conerce error only int assign to float]"""
    #     input = """
    #     class C {
    #         final int a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_9(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 \\ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(\\,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_10(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(^,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_11(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(^,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_12(self):
    #     input = """
    #     class C {
    #         final float a = "van" ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,BinaryOp(^,StringLit(van),StringLit(loc)))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
        class C {
            string x = 2;
            final float a = x + 3;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(^,Id(x),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 412))