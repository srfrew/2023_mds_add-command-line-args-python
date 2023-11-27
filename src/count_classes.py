import pandas as pd
import click 

@click.command()
@click.argument('file_path')
@click.argument('class_col')
@click.argument('output_file')
def main(file_path, class_col, output_file):
    # read in wisconsin breast cancer data
    data = pd.read_csv(file_path)

    result = data.groupby(class_col).size().reset_index(name='Count')
    result = result.rename(columns={class_col: 'Class'})

    result.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()
