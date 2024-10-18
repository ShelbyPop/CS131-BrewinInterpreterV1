from brewparse import parse_program
from intbase import *

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)   # call InterpreterBase's constructor

    def run(self, program):

        ast = parse_program(program) # returns list of function nodes
        self.variable_name_to_value = {} # dict to hold vars
        main_func_node = self.get_main_func_node(ast)
        #self.output(main_func_node)
        self.run_func(main_func_node)

    # returns 'main' func node from the dict input.
    def get_main_func_node(self, ast):

        # returns functions sub-dict, 'functions' is a value
        func_list = ast.dict['functions'] 

        # checks for function whose name is 'main'
        for i in range(0,len(func_list)):
            if func_list[i].dict['name'] == "main":
                return func_list[i]
        
        # define error for 'main' not found.
        super().error(ErrorType.NAME_ERROR, "No main() function was found")


    # self explanatory
    def run_func(self, func_node):
        # statements key for sub-dict.
        for statement_node in func_node.dict['statements']:
            self.run_statement(statement_node)
    

    def run_statement(self, statement_node):
        if self.is_definition(statement_node):
            self.do_definition(statement_node)
        elif self.is_assignment(statement_node):
            self.do_assignment(statement_node)
        elif self.is_func_call(statement_node):
            self.do_func_call(statement_node)
    
    def is_definition(self, statement_node):
        raise NotImplementedError

    def is_assignment(self, statement_node):
        raise NotImplementedError
    
    def is_func_call(self, statement_node):
        raise NotImplementedError

    def do_definition(self, statement_node):
        raise NotImplementedError

    def do_assignment(self, statement_node):
        raise NotImplementedError
    
    def do_func_call(self, statement_node):
        raise NotImplementedError
    

    def evaluate_expression(expression_node):
        raise NotImplementedError
    
    # + or -
    def evaluate_binary_operator(expression_node):
        raise NotImplementedError

    # Several more functions remain


program = """
            func main() {
             var x;
             x = 5 + 6;
             print("The sum is: ", x);
            }"""

interpreter = Interpreter()
interpreter.run(program)