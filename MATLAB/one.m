clc,clear
close all
[a,b,c,d,e,f,g,h,M,j] = textread('/Users/apple/Desktop/2019_python/txt/H-TXT/WV-H.txt','%n%n%n%n%n%n%n%n%s%s',45);
%   KY   OH    PA    VA    WV
%H  111  88    67    127   45
%Q  120  88    67    131   55
for k = 1:length(a)
    m(k,1) = a(k)
    m(k,2) = b(k)
    m(k,3) = c(k)
    m(k,4) = d(k)
    m(k,5) = e(k)
    m(k,6) = f(k)
    m(k,7) = g(k) 
    m(k,8) = h(k)
end

for i = 1:length(a)
    onetest = m(i,:)
    for j = 1:length(onetest)-1
        twosub = abs(onetest(1,j)-onetest(1,j+1))
        rate(i,j) = twosub
    rate(i,8) = onetest(1,1)
    %rate(i,8) = onetest(1,8)
    sumrate = 0
    for k = 1:7
        sumrate = rate(i,k)+ sumrate
    end
    rate(i,9) = sumrate/7
    rate(i,10) = std(rate(i,1:7)./100)
    end
end
     

%n = mapminmax(m,3,5)
meana = mean(m(1,:))  %3.516
x = [0:10]
lenrate = length(rate)
brate = mapminmax(rate,0.1,1)
%t = [2010,2011,2012,2013,2014,2015,2016,2017]
syms A I T U I0
%dsolve('Di=-A*I*I+a*I*(1-1/k)','i(0) = i0','t')
%D = dsolve('Di = -A*I(I-(1-1/K))','i(0) = i0','t')
%I = dsolve('DI = A*I*(1-I)-U*I','I(0) = I0','t')
%I = dsolve('DI = -A*I*(1+I)-U*I','I(0) = I0','t')
I = dsolve('DI = A*I*(1+I)+U*I','I(0) = I0','t')
K = (tanh((x + (2.*atanh((2.*A.*I0)./(A+U)-1))./(A + U)).*(A./2+U./2))+1).*(A + U)./(2.*A)
for  k = 3
    %lenrate
    %rate9 = brate(k,9)
    %rate8 = brate(k,8)
    %rate10 = brate(k,10)
    U = brate(k,9)
    I0 = brate(k,8)
    A = brate(k,10)
    %y = subs(I,{A,U,I0},{rate9,rate10,rate8})
    Y = (tanh((x + (2.*atanh((2.*A.*I0)./(A+U)-1))./(A + U)).*(A./2+U./2))+1).*(A + U)./(2.*A)
    Ii = [0:0.01:1]
    Di = A.*Ii.*(1-Ii)-U.*Ii
    %plot(Ii,Di)
    county(k,1) = Y(8)
    %county(k,2) = Y(6)
    %county(k,3) = Y(7)
    plot(x,Y)
    title(' ¦Ò <= 1')
    xlabel('i')
    ylabel('di/dt')
    hold on
end


lab = county()

for index = 1:5        
    minc = max(lab(:,1))
    shibu = real(minc)
    [co,mn] = find(lab==minc)
    countyall(index,1) = M(co)
    countyall(index,2) = {shibu}
    lab(co) = []
end

% xlswrite('/Users/apple/Desktop/2019_python/source/WV-Q.xlsx', lab)












