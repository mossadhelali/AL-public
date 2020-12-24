from src.traces.traces import main as traces_main
import pandas as pd

def main():
    db_path = '/home/mosemos/projects/al-public/src/crawler/crawled_kaggle.db'
    traces_path = '/home/mosemos/projects/al-public/src/traces/extracted-traces.pkl'
    clean_traces_path = '/home/mosemos/projects/al-public/src/traces/clean-traces.pkl'

    language = 'IPython Notebook'

    traces_main(db_path, traces_path, language)

    tr = pd.read_pickle('extracted-traces.pkl')
    print()

if __name__ == '__main__':
    main()