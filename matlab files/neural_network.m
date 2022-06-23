[al , t]=prprob();
[r ,q]=size(al);
p=al;
tt=t;

y=feedforwardnet(70,'traingdx'); %creat network
y.perfossreewwrmFcn='sse';
y.trainParam.goal=0.1;
net.trainParam.lr = 0.05;
net.trainParam.lr_inc = 1.05;
net.trainParam.lr_dec = 0.7;
y.trainParam.epochs=5000;
y.trainParam.show=20;
y.trainParam.mc=0.95;
y=train(y,p,tt); %training without noise

%training with noise
y.trainParam.goal=0.6 ;
y.trainParam.epochs=300 ;

tt=[t t t t] ;
for oo=1:50
    p=[al, (al+randn(r,q)*0.1), al ,(al+randn(r,q)*0.2)];
    % create 4 matrixes //2 with noise +2 without
    y=train(y,p,tt);
end
p=al;
tt=t;
y.performFcn='sse';
y.trainParam.goal=0.1;
y.trainParam.epochs=5000;
y.trainParam.show=20;
y.trainParam.mc=0.95;
y=train(y,p,tt);

for i=26:-1:1
 testal(y,al,0.1,i);
 end
