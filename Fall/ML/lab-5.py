def compute_errors(x,y,w,b):
    m = len(x)
    cost_sum = 0

    for i in range(m):
        f_wb = w*x[i]+b
        cost = (f_wb - y[i])**2
        cost_sum = cost + cost_sum

    total_cost = (cost_sum) / (2*m)

    return total_cost

def compute_gradients(x,y,w,b):
    m = len(x)
    b_wa = 0
    w_ba = 0

    for i in range(m):

