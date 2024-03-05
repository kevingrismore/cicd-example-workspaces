from prefect import flow


@flow(log_prints=True)
def hello():
    print("Hello from Project 2!")


if __name__ == "__main__":
    hello()