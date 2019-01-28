b = [0	0.004273437	0.000548895]
a = [1,2,3]
p = polyfit(a,b,2);
Z=polyval(p,a);
plot(a,Z)