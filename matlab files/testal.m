function [] = testal(y,al,d,n)

nj= al(:,n)+d*randn(35,1)  ;
a2=sim(y,nj);
a3=compet(a2);
ans=find(a3==1)
figure,subplot(1,2,1);
plotchar(nj)
subplot(1,2,2);
plotchar(al(:,ans))

end

