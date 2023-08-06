from argparse import ArgumentParser, RawTextHelpFormatter
import subprocess


def main():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "-s",
        choices=["d", "m", "t"],
        default="t",
        help="Positional values to represent starting point\n"
        " d : Download dataset\n"
        " m : Train machine learning model\n"
        " t : Predict on test input\n",
    )

    stage = parser.parse_args()

    if stage.s == "d":
        subprocess.call(["python", "data_downloader.py"])

    elif stage.s == "m":
        subprocess.call(["python", "data_modeler.py"])

    elif stage.s == "t":
        subprocess.call(["python", "predict.py"])


if __name__ == "__main__":
    main()
