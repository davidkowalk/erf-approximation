# ERF Approximation via streched sigmoid functions
This project aims at approximating the mathematical error function with a simple sigmoid function:

```
erf(x) ~= 2 / (1+e^(-bx²))-1
```

This approximation is strong around zero, with x>1, and x<-1. In this project I aim at finding the value b with the smalles average error by gradient decend.
