import csv


def read_checkout_data():

    data = []

    with open(
        "test-data/checkout_data.csv",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            data.append(
                (
                    row["first_name"],
                    row["last_name"],
                    row["zip_code"]
                )
            )

    return data