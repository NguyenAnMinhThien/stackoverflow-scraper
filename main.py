import sys
import utils
import os


def welcome():
    print("Welcome.")
    print("What tag name do you want to extract from Stackoverflow ? e.x 'windows' or 'windows javascript'")
    tag = input()
    print("The number of pages ? (each page contains 50 results)")
    pages = input()

    return tag, pages


if __name__ == '__main__':
    tag, pages = welcome()
    # Get all the questions follow up the number of votes
    my_df = utils.extract_all_page(tag=tag, page_nums=pages)
    # Save file
    filename, filepath = utils.get_file_name(tag, pages)
    if os.name == "nt":
        # window
        my_df.to_csv(f".\output\\{filename}")
    else:
        # other
        my_df.to_csv(f"./output/{filename}")

    print(my_df)
    print(f"The file has been saved at: \n{filepath}")
