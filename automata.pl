% Author: Grezia Trujillo
% Date: 24 March, 2026
% Project: DFA in Prolog
% Purpose of the project: Create and validate the automata 
% generated using prolog, which must only accept the chosen language.


%defined as transit(initial_state,next_state,input).

%simple database for domin.
transit(a,b,d).
transit(b,c,o).
transit(c,d,m).
transit(d,e,i).
transit(e,f,n).

%simple database for mater.
transit(a,g,m).
transit(g,h,a).
transit(h,i_state,t).
transit(i_state,j,e).
transit(j,k,r).

%any necessary fallbacks.
transit(b,b,d).
transit(g,g,m).
transit(d,h,a).

%accepting states.
accept(f). %domin
accept(k). %mater 

%recursively check if string is accepted by automata.

%the first state in the automata is always a. Remember to change the string into a list in order to parse it.
parseThru(Word):-
    atom_chars(Word,List),
    readString(a,List).

%base case: if we are in an accepting state, string is accepted into language whether there are letters left to read.
readString(State,_) :-    
    accept(State).

%There are still characters to read. Recursively process the string to determine the next transition established in the automaton.
readString(State,[Char|Rest]) :-
    transit(State,NextState,Char), 
    readString(NextState,Rest). 

%character does not start with root. Retry from start state.
readString(a,[_|Rest]) :-
    readString(a,Rest).



