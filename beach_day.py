'''Beach Day
Konstantinos is planning his summer vacation in Greece and has the projected weather scores for
every day of the summer. He plans to visit different beaches, each one for zero or more days. In
past years he would grade the satisfaction of a beach visit as the sum of the scores of the days
spent there, this year however, he decided to go with a more sophisticated system. If $x$ is the
sum of the scores for a beach visit, then the adjusted score will be $x' = \\alpha x^2 + \\beta x +
\\gamma$, where $\\alpha$, $\\beta$, $\\gamma \\in R$ and $\\alpha < 0$. After leaving a beach,
Konstantinos is not going to return back to it. He turns to you to find chunks of consecutive days
for each beach visit. For example if the coefficients are $\\alpha=-1$, $\\beta=10$, $\\gamma=-20$
and the four vacation days have projected scores $x_1 = 2$, $x_2 = 2$, $x_3 = 3$, $x_4 = 4$, then
the best solution is to go to three beaches, the first on the days one and two, the second on day
three and the third one on day four. The adjusted scores are $4, 1$ and $4$ respectively for a
total score of $9$.

Input: in the first line there is a single integer, $N$, the number of vacation days. In the next
line there are three integers, $\\alpha$, $\\beta$ and $\\gamma$. In the final line there are $N$
integers, the projected scores for each day.

Output: One line with a single integer, the maximum adjusted cost achievable.
'''


def solve(N, a, b, c, scores):
    dp = [quadratic_exp(a, b, c, scores[0])]
    for i in range(1, N):
        max_value = float('-inf')
        sum_scores = 0
        for j in range(-1, i):
            sum_scores+=scores[j + 1]
        for k in range(0, i+1):
            if k == 0:
                if quadratic_exp(a, b, c, sum_scores) > max_value:
                    max_value = quadratic_exp(a, b, c, sum_scores)
            else:
                sum_scores -= scores[k - 1]
                if dp[k - 1] + quadratic_exp(a, b, c, sum_scores) > max_value:
                    max_value = dp[k-1] + quadratic_exp(a, b, c, sum_scores)
        dp.append(max_value)

    return dp[-1]
        

def quadratic_exp(a, b, c, x):
    return a*(x**2) + b*x + c


def read_input():
    N = int(input())
    a, b, c = [int(i) for i in input().split()]
    scores = [int(i) for i in input().split()]
    return N, a, b, c, scores


def main():
    N, a, b, c, scores = read_input()
    best = solve(N, a, b, c, scores)
    print(best)


if __name__ == '__main__':
    main()
