def fib(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # This will take longer than you are willing to wait.
    print(fib(53))
