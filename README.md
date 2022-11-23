- Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
- Change current directory to initial/src where there is file run.py
- Type: python run.py gen
- Then type: python run.py test LexerSuite
- Then type: python run.py test ParserSuite
- Then type: python run.py test ASTGenSuite

# SUPPORT METHODS

## getASTName()
```python
    ### `getASTName` function used to get name of AST object
    ## @param targetObj can be type of MemDecl(AttributeDecl, MethodDecl) or StoreDecl(ConstDecl, VarDecl)
    ## @return name type str
    def getASTName(self, targetObj):
```

## checkClassExist()

```python
    ### `checkClassExist` function used to check if class exist or not
    ## @param classname name of the class to check (type: str)
    ## @param classDecls list of class existed
    ## @return True/False
    def checkClassExist(self, classname: str, classDecls: List[ClassDecl]):
```

## checkMemberExist()

```python
    ### `checkMemberExist` function used to check if member (can be attribute or method) exist within a class
    ## @param targetMem name of member need to check (type: MemDecl)
    ## @param memlist list of members need to check (type: List[MemDecl])
    ## @return True/False
    def checkMemberExist(self, targetMem: MemDecl, memlist: List[MemDecl]):
```

## checkIsKidOf()

```python
    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    ## @param targetChildName is the child's name need to check (type: str)
    ## @param targetParentName is the parent's name need to check (type: str)
    ## @return True/False
    def checkIsKidOf(self, targetChildName: str, targetParentName: str):
```

## checkStoreExist()

```python
    ### `checkStoreExist` function used to check if variable is declared within a block scope
    ## @param variable is the name to check
    ## @param varDecls is list of decl type StoreDecl that may contain variable
    ## @return True/False
    def checkStoreExist(self, variable: str, decls: List[StoreDecl]):
```
## searchClass()

```python
    ### `searchClass` function used to find existed class
    ## @param classname type str
    ## @param ClassDecl (None if not found)
    def searchClass(self, classname: str):
```

## searchVarDecl()

```python
    ### `searchVarDecl` function used to search a varDecl through name
    ## @param targetname name to search
    ## @param varDecls is list of varDecl that may contain varDecl with targetname
    ## @return VarDecl
    def searchVarDecl(self, variable: targetname, varDecls: List[VarDecl]):
```

# CHECK ASSIGNMENT

## visitId
> `additional param` varDecls: List[VarDecl] (can be list of `StoreDecl`[VarDecl, ConstDecl] or list of `MemDecl`[AttributeDecl,MethodDecl]) 

> `return` Type() can be `IntType()`, `StringType()`, `FloatType()`, `BoolType()`, `VoidType()`
- check error `Undeclared(Identifier(), ast.name)` check if `id` exist

## visitBinaryOp

> `additional param` varDecls: List[VarDecl]

> `return` Type() can be `IntType()`, `StringType()`, `FloatType()`, `BoolType()`

## visitVarDecl

> `additional param` varDecls: List (can be list of `StoreDecl` or list of `MemDecl`)

- check error `Redeclared(Variable(), variable)` if `varDecls` is the list of `StoreDecl`
- check error `TypeMismatchInStatement(Assign(lhs,exp))` **dunno what the exactly error type (just sure that TypeMismatch)**

## visitBlock



## visitConstDecl

> `additional param` varDecls: List (can be list of `StoreDecl` or list of `MemDecl`)

- check error `Redeclared(Constant(), constant)` if `varDecls` is the list of `StoreDecl`
- check error `TypeMismatchInConstant(ast)` the same to TypeMismatch in visitVarDecl

## visitClassDecl

- check error `Redeclared(Class(), classname)` the new class
- check error `Undeclared(Class(), parentname)` the parent of new class

## visitMethodDecl

> `additional param` memList: List[MemDecl]

- check error `Redeclared(Method(), methodName)` of the new method
- check error `Redeclared(Parameter(),paramName)` in list of params

## visitAttributeDecl

> `additional param` memList: List[MemDecl]

- check error `Redeclared(Attribute(), attributeName)` of the new attribute

## visitProgram

- add one existed class `io` to the completely new program
