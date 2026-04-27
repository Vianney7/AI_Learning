def get_student_name():
    """Prompt until a non-empty student name is entered."""
    while True:
        name = input("Enter student's name: ").strip()
        if name:
            return name
        print("Invalid input. Name cannot be empty.")


def get_score(test_number):
    """Prompt until a valid score (0-100) is entered."""
    while True:
        raw_value = input(f"Enter test score {test_number} (0-100): ").strip()
        try:
            score = float(raw_value)
            if 0 <= score <= 100:
                return score
            print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def ask_to_continue():
    """Ask user whether they want to enter another student."""
    while True:
        answer = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Invalid input. Please enter yes or no.")


def main():
    students = []

    while True:
        name = get_student_name()
        scores = [get_score(i) for i in range(1, 4)]
        average = sum(scores) / len(scores)
        result = "Pass" if average >= 70 else "Fail"

        students.append({"name": name, "average": average, "result": result})

        print(f"\nStudent: {name}")
        print(f"Average score: {average:.2f}")
        print(result)

        if not ask_to_continue():
            break

    print("\nAll student results:")
    name_width = max(len("Name"), max(len(student["name"]) for student in students))
    avg_width = len("Average")
    result_width = len("Result")

    header = f"{'Name':<{name_width}}  {'Average':>{avg_width}}  {'Result':<{result_width}}"
    separator = f"{'-' * name_width}  {'-' * avg_width}  {'-' * result_width}"

    print(header)
    print(separator)
    for student in students:
        print(
            f"{student['name']:<{name_width}}  "
            f"{student['average']:>{avg_width}.2f}  "
            f"{student['result']:<{result_width}}"
        )


if __name__ == "__main__":
    main()
