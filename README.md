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

## Findings
The first run of the gradient-descend function had the following properties:

|    Property     | Value |
|-----------------|-------|
| Starting Point  | 2.405 |
| Gamma           | 0.001 |
| Precision       | 1E-7  |
| Max. Iterations | 2E+6  |
| Iterations      | 1727  |

In the numeric approximations of integral and derivative the following variables were used:

|      Variable     | Value |
|-------------------|-------|
| Integral Min.     |   -3  |
| Integral Max.     |   +3  |
| Δx for derivative | 1E-7  |
| Δx for integral   | 5E-4  |

The function produced an approximation of b and an average error :

|    Result     |        Value        |
|---------------|---------------------|
| b             | 2.4086376806430434  |
| Average Error | 0.0105561117608605  |
