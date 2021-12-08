def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
       return 0

# If weight of the nth item > W, exclude.
    if (wt[n - 1] > W):
       return knapSack(W, wt, val, n - 1)

    else:

         inc = val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1)
         exc = knapSack(W, wt, val, n - 1)
         print("Profit including item", n, ":", inc, sep=" ")
         print("Profit excluding item", n, ":", exc, sep=" ")
         return max(inc, exc)
n = int(input("Enter no. of items: "))
wt = []
val = []
for i in range(n):
    wt.append(int(input("Item " + str(i + 1) + " weight: ")))
    val.append(int(input("Item " + str(i + 1) + " value: ")))
W = int(input("Enter max capacity of knapsack: "))
print("Maximum Profit: ", knapSack(W, wt, val, n))
