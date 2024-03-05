from prefect import flow


@flow(log_prints=True)
def hello():
    print("Hello from Project 1!")
    print("This change is still in development.")


if __name__ == "__main__":
    hello()