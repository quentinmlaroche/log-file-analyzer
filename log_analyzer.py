def count_lines(file_path):
    count = 0
    with open(file_path, "r") as file:
        for line in file:
            count += 1
    return count


def main():
    file_path = "sample.log"
    total_lines = count_lines(file_path)
    print(f"Total number of lines: {total_lines}")


if __name__ == "__main__":
    main()
