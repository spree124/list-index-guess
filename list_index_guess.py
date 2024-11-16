import random
import traceback as tb

k = []
def randomize_list(list1: list, range1: int = 11) -> list[int]:
    for i in range(range1):
        list1.append(i)
    random.shuffle(list1)
    return list1

def start_round(ans: list) -> None:
    """Starts the round.
    If you imported this, use the main() function instead.
    Args:
        ans (list): list of shuffled integers.
    Returns:
        None
    """
    for index, answer in enumerate(ans, 1):
        while True:
            try:
                user_guess = int(input(f"What is your guess for index {index}? "))
                if user_guess != answer:
                    print("Incorrect. Try again.")
                else:
                    print("Correct!")
                    break
            except ValueError:
                print("Please type a valid number.")
            except Exception as e:
                with open("error_log_list_guess.txt", 'a') as file:
                    file.write("An error occurred:\n")
                    tb.print_exc(file=file)


def main(k: list) -> None:
    """The main part for lè game."""
    k = randomize_list(k)
    start_round(k)

if __name__ == "__main__":
    main(k)
