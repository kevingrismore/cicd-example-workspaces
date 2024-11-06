from prefect import flow


@flow(log_prints=True)
def hello():
    print("Hello from Project 1! :)")
    print("new addition to project 1")


if __name__ == "__main__":
    hello()