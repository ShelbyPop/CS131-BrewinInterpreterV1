from brewparse import parse_program
from intbase import *

class Interpreter(InterpreterBase):
    def __init__(self, console_output=True, inp=None, trace_output=False):
        super().__init__(console_output, inp)   # call InterpreterBase's constructor

    def run(self, program):

        ast = parse_program(program) # returns list of function nodes
        self.variable_name_to_value = {} # dict to hold vars
        main_func_node = self.get_main_func_node(ast)

    
    def get_main_func_node(self, ast):
        # returns 'main' func node from the dict input.

        # returns functions sub-dict, 'functions' is a value
        func_list = ast.dict['functions'] 

        # checks for function whose name is 'main'
        for i in range(0,len(func_list)):
            if func_list[i].dict['name'] == "main":
                return func_list[i]
        
        # define error for 'main' not found.
        super().error(ErrorType.NAME_ERROR, "No main() function was found")



    def run_func(self, func_node):
        raise NotImplementedError
    

    def run_statement(self, statement_node):
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