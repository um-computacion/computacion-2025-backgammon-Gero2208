# Automated Reports

## Coverage Report
```text
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
cli/__init__.py        0      0   100%
cli/cli.py            88     88     0%   1-112
core/__init__.py       0      0   100%
core/board.py         80     62    22%   50-150
core/checkers.py     273    273     0%   1-377
core/dice.py          13      3    77%   38-41
core/game.py          34     23    32%   43-54, 63-75
core/player.py        11     11     0%   1-30
------------------------------------------------
TOTAL                499    460     8%

```

## Pylint Report
```text
************* Module cli.cli
cli/cli.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:55:0: C0301: Line too long (105/100) (line-too-long)
cli/cli.py:81:0: C0301: Line too long (114/100) (line-too-long)
cli/cli.py:83:0: C0301: Line too long (109/100) (line-too-long)
cli/cli.py:84:0: C0301: Line too long (114/100) (line-too-long)
cli/cli.py:108:0: C0301: Line too long (132/100) (line-too-long)
cli/cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/cli.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
cli/cli.py:7:0: R0914: Too many local variables (24/15) (too-many-locals)
cli/cli.py:105:19: W0718: Catching too general exception Exception (broad-exception-caught)
cli/cli.py:7:0: R0912: Too many branches (20/12) (too-many-branches)
cli/cli.py:7:0: R0915: Too many statements (82/50) (too-many-statements)
cli/cli.py:37:8: W0612: Unused variable 'resultado' (unused-variable)
************* Module core.checkers
core/checkers.py:21:0: C0301: Line too long (109/100) (line-too-long)
core/checkers.py:22:0: C0303: Trailing whitespace (trailing-whitespace)
core/checkers.py:54:0: C0303: Trailing whitespace (trailing-whitespace)
core/checkers.py:63:0: C0303: Trailing whitespace (trailing-whitespace)
core/checkers.py:132:0: C0301: Line too long (119/100) (line-too-long)
core/checkers.py:140:0: C0301: Line too long (107/100) (line-too-long)
core/checkers.py:227:0: C0303: Trailing whitespace (trailing-whitespace)
core/checkers.py:243:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/checkers.py:247:0: C0325: Unnecessary parens after 'not' keyword (superfluous-parens)
core/checkers.py:358:0: C0303: Trailing whitespace (trailing-whitespace)
core/checkers.py:378:0: C0304: Final newline missing (missing-final-newline)
core/checkers.py:378:0: C0301: Line too long (102/100) (line-too-long)
core/checkers.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checkers.py:3:4: W0107: Unnecessary pass statement (unnecessary-pass)
core/checkers.py:5:0: C0115: Missing class docstring (missing-class-docstring)
core/checkers.py:7:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:40:8: W0612: Unused variable 'color' (unused-variable)
core/checkers.py:42:8: W0612: Unused variable 'puntos' (unused-variable)
core/checkers.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
core/checkers.py:91:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/checkers.py:169:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/checkers.py:172:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:173:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:174:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:175:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:176:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:179:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:180:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:181:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:182:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:185:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:186:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:187:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:190:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:191:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:194:60: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:201:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:202:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:203:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:204:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:205:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:208:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:209:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:210:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:211:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:214:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:215:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:216:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:219:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:220:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:223:58: C0321: More than one statement on a single line (multiple-statements)
core/checkers.py:160:4: R0911: Too many return statements (42/6) (too-many-return-statements)
core/checkers.py:160:4: R0912: Too many branches (42/12) (too-many-branches)
core/checkers.py:249:15: E1101: Class 'Checkers' has no '_all_in_home' member (no-member)
core/checkers.py:253:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/checkers.py:264:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:272:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:280:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:288:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:296:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:316:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:324:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:332:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:340:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:348:31: E1101: Class 'Checkers' has no '_hay_mas_lejos_en_home_if' member (no-member)
core/checkers.py:229:4: R0911: Too many return statements (42/6) (too-many-return-statements)
core/checkers.py:229:4: R0912: Too many branches (42/12) (too-many-branches)
core/checkers.py:366:15: E1101: Class 'Checkers' has no 'puede_bear_off_con_dado' member (no-member)
************* Module core.game
core/game.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:75:0: C0304: Final newline missing (missing-final-newline)
core/game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/game.py:43:8: C0415: Import outside toplevel (random) (import-outside-toplevel)
core/game.py:47:12: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
************* Module core.board
core/board.py:5:0: C0301: Line too long (111/100) (line-too-long)
core/board.py:6:0: C0301: Line too long (101/100) (line-too-long)
core/board.py:11:0: C0301: Line too long (103/100) (line-too-long)
core/board.py:150:0: C0301: Line too long (117/100) (line-too-long)
core/board.py:151:0: C0305: Trailing newlines (trailing-newlines)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:42:4: R0914: Too many local variables (23/15) (too-many-locals)
core/board.py:52:8: C0103: Variable name "VACIO" doesn't conform to snake_case naming style (invalid-name)
core/board.py:73:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/board.py:84:16: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.player
core/player.py:25:0: C0303: Trailing whitespace (trailing-whitespace)
core/player.py:28:0: C0303: Trailing whitespace (trailing-whitespace)
core/player.py:30:0: C0304: Final newline missing (missing-final-newline)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/player.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
core/player.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
core/player.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module core.dice
core/dice.py:12:0: C0301: Line too long (105/100) (line-too-long)
core/dice.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:36:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:39:42: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:41:0: C0304: Final newline missing (missing-final-newline)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/dice.py:37:4: C0116: Missing function or method docstring (missing-function-docstring)
core/dice.py:38:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module tests.tests_dice
tests/tests_dice.py:27:0: C0304: Final newline missing (missing-final-newline)
tests/tests_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/tests_dice.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/tests_dice.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_dice.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_dice.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_dice.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.tests_board
tests/tests_board.py:31:0: C0304: Final newline missing (missing-final-newline)
tests/tests_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/tests_board.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/tests_board.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_board.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_board.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_board.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.tests_game
tests/tests_game.py:33:0: C0304: Final newline missing (missing-final-newline)
tests/tests_game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/tests_game.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/tests_game.py:4:0: R0903: Too few public methods (0/2) (too-few-public-methods)
tests/tests_game.py:8:0: C0115: Missing class docstring (missing-class-docstring)
tests/tests_game.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_game.py:19:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/tests_game.py:24:4: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 6.83/10


```
