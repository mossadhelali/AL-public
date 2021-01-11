from src.traces.traces import main as traces_main
import pandas as pd

def main():
    db_path = '/Users/mossad/personal_projects/AL-public/src/crawler/crawled_kaggle.db'
    traces_path = '/Users/mossad/personal_projects/AL-public/src/traces/extracted-traces.pkl'
    clean_traces_path = '/Users/mossad/personal_projects/AL-public/src/traces/clean-traces.pkl'

    # language = 'IPython Notebook'
    language = 'Python'

    traces_main(db_path, traces_path, language)

    tr = pd.read_pickle(traces_path)
    print()

if __name__ == '__main__':
    main()