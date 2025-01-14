import sys
import utils
import os


def welcome():
    print("Welcome.")




if __name__ == '__main__':
    # Get all the questions follow up the number of votes
    my_df = utils.extract_all_page()
    # Save file
    filename, filepath = utils.get_file_name()
    if os.name == "nt":
        # window
        my_df.to_csv(f".\\output\\{filename}")
    else:
        # other
        my_df.to_csv(f"./output/{filename}")

    print(my_df)
    print(f"The file has been saved at: \n{filepath}")
