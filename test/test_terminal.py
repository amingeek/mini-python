import time
from termcolor import cprint
import ast

# def check_main(file):
#     with open(file, 'r') as f:
#         tree = ast.parse(f.read())
#     mains = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == 'main']
#     return len(mains) > 0

def check_file(file):
    try:
        with open(file, 'r') as f:
            content = f.read()
        return True
    except FileNotFoundError:
        return False

def check_variable(file, number = 1):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    variables = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)]
    return len(variables) >= number

def check_function(file, func_name = 'main'):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.name == func_name]
    return len(functions) > 0

def check_import(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    imports = [node for node in ast.walk(tree) if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)]
    return len(imports) > 0

def check_comment(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    comments = [line for line in lines if line.strip().startswith('#')]
    return len(comments) > 0

def check_print(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    prints = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print']
    return len(prints) > 0

def check_input(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    inputs = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'input']
    return len(inputs) > 0

def check_loop(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    loops = [node for node in ast.walk(tree) if isinstance(node, ast.For) or isinstance(node, ast.While)]
    return len(loops) > 0

def check_condition(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    conditions = [node for node in ast.walk(tree) if isinstance(node, ast.If)]
    return len(conditions) > 0

def check_list(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    lists = [node for node in ast.walk(tree) if isinstance(node, ast.List)]
    return len(lists) > 0

def check_dictionary(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    dictionaries = [node for node in ast.walk(tree) if isinstance(node, ast.Dict)]
    return len(dictionaries) > 0

def check_tuple(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    tuples = [node for node in ast.walk(tree) if isinstance(node, ast.Tuple)]
    return len(tuples) > 0

def check_set(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    sets = [node for node in ast.walk(tree) if isinstance(node, ast.Set)]
    return len(sets) > 0

def check_exception(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    exceptions = [node for node in ast.walk(tree) if isinstance(node, ast.Try)]
    return len(exceptions) > 0

def check_file_operation(file):
    with open(file, 'r') as f:
        content = f.read()
    operations = ['open', 'read', 'write', 'close']
    return any(op in content for op in operations)

def check_class(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return len(classes) > 0

def check_module(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    modules = [node for node in ast.walk(tree) if isinstance(node, ast.Module)]
    return len(modules) > 0

def check_package(file):
    with open(file, 'r') as f:
        content = f.read()
    return 'import' in content or 'from' in content

def check_lambda(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    lambdas = [node for node in ast.walk(tree) if isinstance(node, ast.Lambda)]
    return len(lambdas) > 0

def check_map(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    maps = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'map']
    return len(maps) > 0

def check_filter(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    filters = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'filter']
    return len(filters) > 0

def check_reduce(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    reduces = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'reduce']
    return len(reduces) > 0

def check_list_comprehension(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    list_comps = [node for node in ast.walk(tree) if isinstance(node, ast.ListComp)]
    return len(list_comps) > 0

def check_dictionary_comprehension(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    dict_comps = [node for node in ast.walk(tree) if isinstance(node, ast.DictComp)]
    return len(dict_comps) > 0

def check_set_comprehension(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    set_comps = [node for node in ast.walk(tree) if isinstance(node, ast.SetComp)]
    return len(set_comps) > 0

def check_generator(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    generators = [node for node in ast.walk(tree) if isinstance(node, ast.GeneratorExp)]
    return len(generators) > 0

def check_decorator(file):
    with open(file, 'r') as f:
        tree = ast.parse(f.read())
    decorators = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and node.decorator_list]
    return len(decorators) > 0


filename = 'test/example.py'


tests = {
    'File created': check_file(filename),
    'File has 3 variables': check_variable(filename),
    'File has at least one function': check_function(filename),
    'File has at least one import': check_import(filename),
    'File has at least one comment': check_comment(filename),
    'File has at least one print statement': check_print(filename),
    'File has at least one input statement': check_input(filename),
    'File has at least one loop': check_loop(filename),
    'File has at least one condition': check_condition(filename),
    'File has at least one list': check_list(filename),
    'File has at least one dictionary': check_dictionary(filename),
    'File has at least one tuple': check_tuple(filename),
    'File has at least one set': check_set(filename),
    'File has at least one exception handling': check_exception(filename),
    'File has at least one file operation': check_file_operation(filename),
    'File has at least one class': check_class(filename),
    'File has at least one module': check_module(filename),
    'File has at least one package': check_package(filename),
    'File has at least one lambda': check_lambda(filename),
    'File has at least one map': check_map(filename),
    'File has at least one filter': check_filter(filename),
    'File has at least one reduce': check_reduce(filename),
    'File has at least one list comprehension': check_list_comprehension(filename),
    'File has at least one dictionary comprehension': check_dictionary_comprehension(filename),
    'File has at least one set comprehension': check_set_comprehension(filename),
    'File has at least one generator': check_generator(filename),
    'File has at least one decorator': check_decorator(filename)
}

for test_name, result in tests.items():
    if result:
        cprint(f":) {test_name} : pass", 'green', end="\n")
    else:
        cprint(f":( {test_name} : fail", 'red', end="\n")