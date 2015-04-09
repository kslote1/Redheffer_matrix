n=6;
A=zeros(n);

for i=1:n; for j=2:n; if j==i*floor(j/i), A(i,j)=1;end,end,end

for i=1:n; A(i,1)=1; end

