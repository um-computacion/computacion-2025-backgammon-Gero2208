# Automated Reports

## Coverage Report
```text
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
cli/__init__.py          0      0   100%
cli/cli.py              87      4    95%   127-128, 134-135
core/__init__.py         0      0   100%
core/board.py           82      0   100%
core/checkers.py       181      5    97%   193, 210, 307-309
core/dice.py            17      0   100%
core/exceptions.py       4      0   100%
core/game.py            79      2    97%   143, 238
core/player.py          11      0   100%
--------------------------------------------------
TOTAL                  461     11    98%

```

## Pylint Report
```text
************* Module pygame_ui.ui
pygame_ui/ui.py:529:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/ui.py:644:0: C0301: Line too long (101/100) (line-too-long)
pygame_ui/ui.py:154:0: R0914: Too many local variables (21/15) (too-many-locals)
pygame_ui/ui.py:203:0: R0914: Too many local variables (21/15) (too-many-locals)
pygame_ui/ui.py:526:0: R0911: Too many return statements (8/6) (too-many-return-statements)
pygame_ui/ui.py:585:0: R0913: Too many arguments (6/5) (too-many-arguments)
pygame_ui/ui.py:585:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
pygame_ui/ui.py:592:22: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
pygame_ui/ui.py:585:0: R0911: Too many return statements (7/6) (too-many-return-statements)
pygame_ui/ui.py:618:0: R0914: Too many local variables (16/15) (too-many-locals)
pygame_ui/ui.py:648:0: R0913: Too many arguments (7/5) (too-many-arguments)
pygame_ui/ui.py:648:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
pygame_ui/ui.py:668:22: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
pygame_ui/ui.py:669:25: E1101: Module 'pygame' has no 'K_RETURN' member (no-member)
pygame_ui/ui.py:680:27: E1101: Module 'pygame' has no 'K_BACKSPACE' member (no-member)
pygame_ui/ui.py:694:0: R0913: Too many arguments (8/5) (too-many-arguments)
pygame_ui/ui.py:694:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
pygame_ui/ui.py:725:4: E1101: Module 'pygame' has no 'init' member (no-member)
pygame_ui/ui.py:747:30: E1101: Module 'pygame' has no 'QUIT' member (no-member)
pygame_ui/ui.py:783:4: E1101: Module 'pygame' has no 'quit' member (no-member)
************* Module core.board
core/board.py:93:4: R0914: Too many local variables (23/15) (too-many-locals)
************* Module tests.tests_cli
tests/tests_cli.py:140:37: W0613: Unused argument 'mock_input' (unused-argument)
************* Module tests.tests_checkers
tests/tests_checkers.py:107:0: C0303: Trailing whitespace (trailing-whitespace)
tests/tests_checkers.py:275:0: C0303: Trailing whitespace (trailing-whitespace)
tests/tests_checkers.py:291:0: C0303: Trailing whitespace (trailing-whitespace)
tests/tests_checkers.py:303:0: C0303: Trailing whitespace (trailing-whitespace)
tests/tests_checkers.py:316:0: W0311: Bad indentation. Found 13 spaces, expected 12 (bad-indentation)

-----------------------------------
Your code has been rated at 9.59/10


```
