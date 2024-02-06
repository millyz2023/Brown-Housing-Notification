import pandas

testing_data = {
    "day": ["Sunday", "Monday", "Tuesday"],
    "weather": ["cloudy", "windy", "rainny"]
}

testing_dataframe = pandas.DataFrame(testing_data)
testing_dataframe.to_csv("testing-data.csv")

new_piece_of_data = {
    "day": ['Wednesday'],
    "weather": ['sunny'],
}

new_df = pandas.DataFrame(new_piece_of_data)
new_df.to_csv("testing-data.csv", mode="a", header=False)
