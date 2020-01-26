from engine import integrate_error as get_error
from pandas import DataFrame
#def get_error(min, max, step, b):
#    return b**2-2*b+2

def main():

    global r, drv, step

    # initialization
    r = 3 # radius of error function
    drv = 0.0000001 # Step in derivative approximation
    step = 0.0005 # Step size of the integration function

    next_b = 2.405 # Through experimental data we knowm that b idealy lies somewhere between 2.40 and 2.41
    gamma = 0.001 # Step size multiplier
    precision = 0.0000001 # Desired precision of result
    max_iter = 200000

    # Data for change analysis
    data = []

    optimize(next_b, gamma, precision, max_iter, data)
    print("done")

    #export data
    df = DataFrame(data)
    df.to_csv("./data/gradient_descend.csv", header=["b", "error", "step"], index = False)

    #for line in data:
    #    print(line)

def optimize(next_b, gamma, precision, max_iter, data):

    #Gradient descend
    for i in range(max_iter):
        if i%10 ==0:
            print(f"{i}/{max_iter}")
        current_b = next_b
        error, derror = delta_error(current_b)
        next_b = current_b - gamma * derror/drv

        b_step = next_b - current_b
        data.append([next_b, error, b_step])
        if abs(b_step) <= precision:
            break


def delta_error(b):

    current_error = get_error(-r, r, step, b)
    return (current_error, get_error(-r, r, step, b+drv)-current_error)

if __name__ == "__main__":
    main()
