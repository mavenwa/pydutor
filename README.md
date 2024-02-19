# PyDutor

`É inútil pra quem sabe Python, mas caso vocâ não saiba, pode te ajudar um pouco a entender o que cada coisa faz e ainda ter um código funcional.`

O PyDutor é uma biblioteca Python que permite que você escreva códigos Python em português. Ele traduz palavras-chave e funções principais do Python para o português, facilitando a escrita de código para falantes de língua portuguesa.

## Como usar

1. Baixe o arquivo `tradutor.py` e coloque-o na mesma pasta que seus scripts Python.
2. Copie e cole essa linha no inicio do seu código ```from tradutor import Tradutor```
3. Copie o conteúdo do `content.py` e cole no seu arquivo.
4. Escreva seu código dentro da variável `codigo_portugues`.

Exemplo de uso:

```python
from pydutor import PyDutor

pydutor = PyDutor()

codigo_portugues = '''
se idade >= 18:
    mostre("Maior de idade")
senao:
    mostre("Menor de idade")
'''

pydutor.interpretar_codigo_portugues(codigo_portugues)
```

Isso executará o código Python traduzido para português.

## Palavras-chave suportadas

Atualmente, o PyDutor suporta as seguintes palavras-chave e funções principais do Python:

- `se`: `if`
- `senao`: `else`
- `mostre`: `print`

## Contribuindo

Sinta-se à vontade para contribuir com novas traduções, melhorias ou correções de bugs. Basta abrir uma issue ou enviar um pull request para o repositório do PyDutor no GitHub.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
