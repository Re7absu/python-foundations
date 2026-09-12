import pandas as pd
import typer

app = typer.Typer()


@app.command()
def main(file: str, flag: str) -> None:

    df = pd.read_csv(file)
    df = df.dropna()
    df = df[df["status"] == flag]
    print(df)

    summary = pd.DataFrame(
        {"Metric": ["Total Rows", "Average Age"], "Value": [len(df), df["age"].mean()]}
    )

    print(summary)


# متغير داخل بايثون  في حال شغلت الملف مباشرة كدا يكون ترو
# في حال تك استرداده يكون false

if __name__ == "__main__":
    app()
