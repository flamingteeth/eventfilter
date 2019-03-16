from pathlib import Path
import click
import pandas as pd
import pendulum
import xmltodict


def parse_epoch(t):
    ''' parse epoch to ADT datetime string'''
    dt = pendulum.from_timestamp(t / 1000)
    dt = pendulum.timezone('Canada/Atlantic').convert(dt)
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z')


def process(path_csv, path_json, path_xml):
    ''' combine and process three source files'''
	# csv source file import 
    df_csv = pd.read_csv(path_csv)
    
	# JSON source file import 
    df_json = pd.read_json(path_json)
    df_json['request-time'] = df_json['request-time'].apply(parse_epoch)
    
	# XML source file import 
    with path_xml.open('rb') as f:
        df_xml= pd.DataFrame.from_records(xmltodict.parse(f)['records']['report'])

    df = pd.concat((df_csv, df_json, df_xml), sort=False, ignore_index=True)
    df = df.astype({'packets-serviced': int})
    df = df[df['packets-serviced'] != 0].sort_values('request-time')
    # Summary and print
    summary = df.groupby('service-guid').size()
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(summary)

    return df


@click.command()
@click.argument('output')
def main(output):
    df = process(
        Path(__file__).parent / 'reports.csv',
        Path(__file__).parent / 'reports.json',
        Path(__file__).parent / 'reports.xml',
    )
    with open(output, 'w') as f:
        df.to_csv(f, index=False)


if __name__ == '__main__':
    main()
