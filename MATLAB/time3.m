clc,clear
[a,b,c,d,e,f,g,h,i,j]=textread('/Users/apple/Desktop/math/WV-H.txt','%n%n%n%n%n%n%n%n%s%s',45);
%   KY   OH    PA    VA    WV
%H  111  88    67    127   45
%Q  120  88    67    131   55
A=[a b c d e f g h];
D=[];
for index=1:45
    B=A(index,:);
    B=B';
    dy = diff(B,2,1);
    m=armax(dy,[1,1]);
    ythat=forecast(m,dy,5)
    xthat=B(end)+cumsum(ythat)
    for q=1:5
        if xthat(q)<0
            xthat(q)=0;
        end
    end
    B=[B;xthat];
    B=B';
    D=[D;B];
end
xlswrite('/Users/apple/Desktop/math/WV-H.xlsx',D)
xlswrite('/Users/apple/Desktop/math/WV-H.xlsx',i,1,'N1')
xlswrite('/Users/apple/Desktop/math/WV-H.xlsx',j,1,'O1')

% B=A(68,:);
% B=B';
% t=2010:2017;
% 
% figure
% plot(t,B)
% 
% figure
% subplot(211),autocorr(B);
% subplot(212),parcorr(B);
% 
% figure
% dy = diff(B,2,1);
% subplot(211),autocorr( dy );
% subplot(212),parcorr( dy );
% 
% m=armax(dy,[1,1]);
% ythat=forecast(m,dy,3)
% xthat=B(end)+cumsum(ythat)
% for q=1:3
%     if ythat(q)<0
%     ythat(q)=0.01;
%     end
% end
% for q=1:3
%     if xthat(q)<0
%     xthat(q)=0;
%     end
% end
% UB=xthat+0.2*sqrt(ythat)
% LB=xthat-0.2*sqrt(ythat)
% 
% figure
% h4 = plot(t,B,'b');
% hold on
% h5 = plot(2018:2020,xthat,'r','LineWidth',2);
% h6 = plot(2018:2020,UB,'k--','LineWidth',1.5);
% h7 = plot(2018:2020,LB,'k--','LineWidth',1.5);
% hold off