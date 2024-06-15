from SingletonPattern.singleton.DB import DB


def write(n: int):
    for i in range(n):
        DB().set(i, i * 10)


def read(n: int):
    for i in range(n):
        print(DB().get(i))


def main():
    write(10)
    read(10)


if __name__ == "__main__":
    main()
