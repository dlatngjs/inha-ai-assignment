import argparse
import csv
from pathlib import Path


def load_csv(csv_path: Path):
    dates = []
    values = []

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {"date", "value"}
        if not required.issubset(set(reader.fieldnames or [])):
            raise ValueError("CSV에는 'date'와 'value' 컬럼이 필요합니다.")

        for row in reader:
            dates.append(row["date"])
            values.append(float(row["value"]))

    if not dates:
        raise ValueError("CSV 데이터가 비어 있습니다.")

    return dates, values


def plot_and_save(dates, values, output_path: Path, title: str):
    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        raise RuntimeError(
            "matplotlib가 설치되어 있지 않습니다. `pip install matplotlib` 후 다시 실행하세요."
        ) from e

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker="o", linewidth=2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="CSV(date,value) 데이터를 읽어 추이 그래프(PNG)를 생성합니다.")
    parser.add_argument("csv_path", help="입력 CSV 파일 경로")
    parser.add_argument("--output", default="trend_plot.png", help="출력 PNG 파일명 (기본값: trend_plot.png)")
    parser.add_argument("--title", default="Trend Graph", help="그래프 제목")
    args = parser.parse_args()

    csv_path = Path(args.csv_path)
    output_path = Path(args.output)

    if not csv_path.exists():
        raise SystemExit(f"입력 CSV 파일이 존재하지 않습니다: {csv_path}")

    try:
        dates, values = load_csv(csv_path)
        plot_and_save(dates, values, output_path, args.title)
    except Exception as e:
        raise SystemExit(f"오류: {e}")

    print(f"그래프 생성 완료: {output_path.resolve()}")


if __name__ == "__main__":
    main()
