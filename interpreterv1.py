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
        for func in func_list:
            if func.dict['name'] == "main":
                return func
        
        # define error for 'main' not found.
        super().error(ErrorType.NAME_ERROR, "No main() function was found")


    # self explanatory
    def run_func(self, func_node):
        # statements key for sub-dict.
        for statement_node in func_node.dict['statements']:
            # self.output(statement_node)
            self.run_statement(statement_node)
    

    def run_statement(self, statement_node):
        if self.is_definition(statement_node):
            self.do_definition(statement_node)
        elif self.is_assignment(statement_node):
            self.do_assignment(statement_node)
        elif self.is_func_call(statement_node):
            self.do_func_call(statement_node)
    
    def is_definition(self, statement_node):
        return (True if statement_node.elem_type == "vardef" else False)
    def is_assignment(self, statement_node):
        return (True if statement_node.elem_type == "=" else False)
    def is_func_call(self, statement_node):
        return (True if statement_node.elem_type == "fcall" else False)



    def do_definition(self, statement_node):
        # just add to var name

        target_var_name = self.get_target_variable_name(statement_node)
        self.variable_name_to_value[target_var_name] = None
        

    def do_assignment(self, statement_node):
        pass
        target_var_name = self.get_target_variable_name(statement_node)
        # self.output(target_var_name)
        if not self.var_name_exists(target_var_name):
            super().error(ErrorType.NAME_ERROR, "variable used and not declared", )
        source_node = self.get_expression_node(statement_node)
        resulting_value = self.evaluate_expression(source_node)
        self.variable_name_to_value[target_var_name] = resulting_value
        
        self.output(source_node.elem_type)
    
    def get_target_variable_name(self, statement_node):
        return statement_node.dict['name']
    def var_name_exists(self, varname):
        return True if varname in self.variable_name_to_value.keys() else False
    
    def get_expression_node(self, statement_node):
        return statement_node.dict['expression']
    
    def do_func_call(self, statement_node):
        pass
    

    def evaluate_expression(self, expression_node):

        pass
        # raise NotImplementedError
    
    # + or -
    def evaluate_binary_operator(self, expression_node):
        raise NotImplementedError

    # Several more functions remain


program = """
            func main() {
             var x;
             x = 5 + 6 - 7;
             print("The sum is: ", x);
            }"""

interpreter = Interpreter()
interpreter.run(program)