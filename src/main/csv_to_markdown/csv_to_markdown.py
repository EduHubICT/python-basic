import pandas as pd


class CSVToMarkdown:
    def __init__(self, file=None):
        if file is None:
            raise Exception("CSV file can't be None")

        self.df = pd.read_csv(file)
        self.headers = self.df.columns.values.tolist()
        with open("markdown.md", "w") as md:
            line = "|"
            for header in self.headers:
                line += header
                line += "|"
            md.write(line)
            md.write("\n")

        with open("markdown.md", "a") as md:
            line = "|"
            for _ in self.headers:
                line += ":---:|"
            md.write(line)
            md.write("\n")

    def csv_to_markdown(self):
        with open("markdown.md", "a") as md:
            for i in range(self.df.shape[0]):
                line = "|"
                for column in self.df.columns.values.tolist():
                    line += self.df[column][i]
                    line += "|"
                md.write(line)
                md.write("\n")


if __name__ == "__main__":
    df = CSVToMarkdown("demo.csv")
    df.csv_to_markdown()
