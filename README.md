# ERF Approximation via streched sigmoid functions
This project aims at approximating the mathematical error function with a simple sigmoid function:

```
erf(x) ~= 2 / (1+e^(-bx))-1
```

This approximation is strong around zero, with x>1, and x<-1. In this project I aim at finding the value b with the smalles average error by gradient decend. This project compares it's predictions to the known values provided by math.erf().

Even though less accurate, this approximation can be inverted to a inverse error function:
```
erfinv(y) = -ln(2/(1+y)-1)/b
```
