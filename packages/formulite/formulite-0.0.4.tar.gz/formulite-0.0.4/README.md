# formulite

## Simple formula parser

<img src="https://raw.githubusercontent.com/Tom-game-project/formulite/e540bf0dc3b6858d99d71d20f7df76028be8419b/icon/formulite.svg">

FormuLite is the simple formula parser.

## INSTALL

```bash
pip install formulite
```

## HOW TO USE

```python
from formulite.calc_parser import parser

text="f(x)+g(x,y,z)*5"

par = parser(text)
print(
    par.resolve()
)

# polish notation
# return <function name>[<args>,[,]]
# return +[f['x'], *[g['x', 'y', 'z'], '5']]

```

## LICENSE

[MIT](https://github.com/Tom-game-project/formulite/blob/master/LICENSE.MIT)
