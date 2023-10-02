# LL1 Parser

```
program    -> stmt_list
stmt_list  -> stmt stmt_list'
stmt_list' -> $ \varepsilon $
            | stmt_list
stmt        -> assign
            | for_stmt
assign      -> ID '=' expr ';'
expr        -> term expr'
expr'       -> '+' term expr'
            | '-' term expr'
            | '>' term expr'
            | '<' term expr'
            | '==' term expr'
            | $ \varepsilon $
term        -> '!' factor term'
            | factor term'
term'       -> '*' factor term'
            | '/' factor term'
            | $ \varepsilon $
factor      -> '(' expr ')'
            | ID
            | INT
for_dir    -> 'to'
            | 'downto'
for_body   -> stmt
            | 'begin' stmt_list 'end'
for_stmt   -> 'for' assign for_dir expr 'do' for_body
```