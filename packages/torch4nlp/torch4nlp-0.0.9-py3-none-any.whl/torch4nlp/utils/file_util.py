import os
import pandas as pd
import pyarrow.parquet as pq
import json


def read_txt(infile, delimeter=None, maxsplit=-1, remove_newline=True, cols=None, line_limit=None):
    """read text file
    Args:
        infile: input file
        delimiter
        maxsplit
        remove_newline
        cols: int or list of int
        line_limit: number of lines that returned
    """

    if cols is not None and type(cols) != list and type(cols) != int:
        raise RuntimeError('cols must be a list or an integer')
    if not os.path.exists(infile):
        raise RuntimeError('file not existed: {}'.format(infile))

    content = []
    for l in open(infile, 'r', encoding='utf8'):
        if line_limit is not None and len(content) >= line_limit:
            break
        if remove_newline:
            l = l.rstrip('\n')
        if delimeter is not None:
            l = l.split(delimeter, maxsplit=maxsplit)
            if cols is not None:
                if type(cols) == list:
                    l = [l[index] for index in cols]
                else:  # integer
                    l = l[cols]
        content.append(l)
    return content


def read_jsonl(infile, cols=None, line_limit=None):
    """read jsonl file

    args:
        cols: str or list of string
    """
    
    if cols is not None and type(cols) != list and type(cols) != str:
        raise RuntimeError('cols must be string or list of string')
    if not os.path.exists(infile):
        raise RuntimeError('file not existed: {}'.format(infile))
    
    content = []
    for l in open(infile, 'r', encoding='utf8'):
        if line_limit is not None and len(content) >= line_limit:
            break
        lj = json.loads(l.rstrip('\n'))
        if cols is not None:
            if type(cols) == list:
                lj = {c: lj.get(c) for c in cols}
            else:  # string
                lj = {c: lj.get(c)}
        content.append(lj)
    return content


def load_txt(infile, delimeter='\t', maxsplit=-1, batch_size=10000, remove_newline=True, cols=None):
    """load text file
    """

    if cols is not None and type(cols) != list and type(cols) != int:
        raise RuntimeError('cols must be a list or integer')
    if not os.path.exists(infile):
        raise RuntimeError('file not existed: {}'.format(infile))
        
    chunk = []
    for l in open(infile, 'r', encoding='utf8'):
        if remove_newline:
            l = l.rstrip('\n')
        if delimeter is not None:
            l = l.split(delimeter, maxsplit=maxsplit)
            if cols is not None:
                if type(cols) == list:
                    l = [l[index] for index in cols]
                else:  # integer
                    l = l[cols]
        chunk.append(l)
        if len(chunk) >= batch_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def load_parquet(infile):
    data = []
    df = pq.read_table(infile).to_pandas()
    for index, row in df.iterrows():
        json_row = row.to_json(force_ascii=False)
        data.append(json.loads(json_row))
    return data
    

def dump_to_file(data, outfile, **kwargs):
    if outfile.endswith('.xlsx'):
        with pd.ExcelWriter(outfile) as writer:
            pd.DataFrame(data).to_excel(writer, **kwargs)
    elif outfile.endswith('.jsonl') or outfile.endswith('.json'):
        with open(outfile, 'w') as fout:
            for x in data:
                fout.write(json.dumps(x, ensure_ascii=False) + '\n')
    elif outfile.endswith('.data') or outfile.endswith('.txt'):
        with open(outfile, 'w') as fout:
            for x in data:
                fout.write(x + '\n')
    elif outfile.endswith('.csv'):
        pd.DataFrame(data).to_csv(outfile, **kwargs)
    else:
        raise RuntimeError('file type not support')


if __name__ == '__main__':
    data = [[1,2,3], ['a', 'b', 'c']]
    dump_to_file(data, 'a.csv', index=None)