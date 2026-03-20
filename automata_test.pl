
%tests for mater
?- parseThru(mater).
true.

?- parseThru(maternal).
true.

?- parseThru(matriarch).
false.

?- parseThru(immaterial).
true.

?- parseThru(matrix).
false.

?- parseThru(hello).
false.

?- parseThru(worming).
false.

?- parseThru(materialize).
true.

?- parseThru(abdicate).
false.


%tests for domin
?- parseThru(domin).
true.

?- parseThru(dominate).
true.

?- parseThru(abdominal).
true.

?- parseThru(doming).
true.

?- parseThru(mathematics).
false.

?- parseThru(denominator).
false.

?- parseThru(predominately).
true.

?- parseThru(zoom).
false.
