from datasets import Dataset


def main():
    for dataset in Dataset.list_all():
        print(dataset.summary)


if __name__ == '__main__':
    main()
