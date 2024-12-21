data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

ans1 = sorted(data, key=abs, reverse=True)
print(ans1)

ans2_with_lambda = sorted(data, key=lambda x: -abs(x))
print(ans2_with_lambda)
