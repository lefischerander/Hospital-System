from test_analyse import Analyse
import pandas as pd

def main():
    analyse = Analyse()
    try:
        df = pd.read_csv(analyse.omr_csv_path)
        print(df.head(10))
    except FileNotFoundError:
        print(f"File not found: {analyse.omr_csv_path}")
    except pd.errors.EmptyDataError:
        print(f"No data: {analyse.omr_csv_path}")
    except pd.errors.ParserError:
        print(f"Parse error: {analyse.omr_csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()