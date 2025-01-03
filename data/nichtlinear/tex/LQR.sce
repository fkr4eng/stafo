\begin{minipage}[t]{\textwidth}\color{blue}
\begin{verbatim}
A=[0 1 0;0 0 1;0 0 0];
b=[0 0 1]';
Q=eye(3,3);
R=1;
P=ricc(A,b*inv(R)*b',Q,'cont');
k=(b'*P/R);
\end{verbatim}
\end{minipage}
