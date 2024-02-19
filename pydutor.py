# Para utilizar, mantenha o arquivo tradutor.py e o arquivo que contém o código em português na mesma pasta.
# Execute o arquivo que contém o código em português e veja a saída em inglês.
# Créditos: https://github.com/onlyversus2

import re

class PyDutor:
    def __init__(self):
        self.keywords = {
            'se': 'if',
            'senao': 'else',
            'mostre': 'print',
            'para': 'for',
            'enquanto': 'while',
            'em': 'in',
            'intervalo': 'range',
            'classe': 'class',
            'def': 'def',
            'importa': 'import',
            'de': 'from',
            'retorna': 'return',
            'global': 'global',
            'exceto': 'except',
            'passar': 'pass',
            'continua': 'continue',
            'pausa': 'break',
            'com': 'with',
            'atribui': '=',
            'igual': '==',
            'isso': 'self',
            'Nenhum': 'None',
            'Verdadeiro': 'True',
            'Falso': 'False',
            'caso': 'case',
            'quando': 'when',
            'selecionar': 'select',
            'senão se': 'elif',
            'mais': 'elif',
            'recebe': 'input',
            'abre': 'open',
            'como': 'as',
            'tente': 'try',
            'finalmente': 'finally',
            'lance': 'raise',
            'passar': 'pass',
            'exec': 'exec',
            'função': 'lambda',
            'mapa': 'map',
            'filtro': 'filter',
            'reduzir': 'reduce',
            'enumerar': 'enumerate',
            'somar': 'sum',
            'tamanho': 'len',
            'mínimo': 'min',
            'máximo': 'max',
            'ordem': 'sorted',
            'reverter': 'reversed',
            'apagar': 'del',
            'iterar': 'iter',
            'próximo': 'next',
            'formato': 'format',
            'abrir': 'open',
            'gravar': 'write',
            'leitura': 'read',
            'fechar': 'close',
            'apagar': 'clear',
            'pop': 'pop',
            'conjunto': 'set',
            'adicionar': 'add',
            'remover': 'remove',
            'descartar': 'discard',
            'copiar': 'copy',
            'unir': 'union',
            'interseção': 'intersection',
            'diferença': 'difference',
            'diferença_simétrica': 'symmetric_difference',
            'issubset': 'issubset',
            'issuperset': 'issuperset',
            'procurar': 'find',
            'substituir': 'replace',
            'conte': 'count',
            'minúsculo': 'lower',
            'maiúsculo': 'upper',
            'capitalizar': 'capitalize',
            'juntar': 'join',
            'dividir': 'split',
            'partir': 'partition',
            'começa_com': 'startswith',
            'termina_com': 'endswith',
            'encontrar': 'find',
            'índice': 'index',
            'formatar': 'format',
            'contar': 'count',
            'acrescentar': 'append',
            'estender': 'extend',
            'inserir': 'insert',
            'reverter': 'reverse',
            'index': 'index',
            'sorte': 'sort',
            'count': 'count',
            'pop': 'pop',
            'remove': 'remove',
            'remove': 'remove',
            'clear': 'clear',
            'update': 'update',
        }

    def interpret_portuguese_code(self, code):
        for portuguese_keyword, english_keyword in self.keywords.items():
            code = re.sub(r'\b{}\b'.format(portuguese_keyword), english_keyword, code)
        
        try:
            exec(code)
            print('Creditos: @onlyversus2 - https://github.com/onlyversus2')
            print('PyDutor 1.0.0a')
            print('Caso haja algum erro ou bug, entre em contato diretamente pelo GitHub. Caracteres especiais podem causar problemas. Licenca MIT. Aproveite! :)')
        except SyntaxError as e:
            print("Erro de sintaxe:", e)
            print('Creditos: @onlyversus2 - https://github.com/onlyversus2')
            print('PyDutor 1.0.0a')
            print('Caso haja algum erro ou bug, entre em contato diretamente pelo GitHub. Caracteres especiais podem causar problemas. Licenca MIT. Aproveite! :)')