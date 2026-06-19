import pandas as pd
from pathlib import Path

def parse_asc_file(file_path):
    """Read .asc file"""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            parts = line.strip().split()
            if len(parts) >= 7:
                try:
                    x = float(parts[1])
                    y = float(parts[2])
                    z = float(parts[3])
                    nx = float(parts[4])
                    ny = float(parts[5])
                    nz = float(parts[6])
                    data.append([i, x, y, z, nx, ny, nz])
                except:
                    continue
    return pd.DataFrame(data, columns=['point_id', 'x', 'y', 'z', 'nx', 'ny', 'nz'])

# === MAIN PART ===
def main():
    # Change this path if your files are somewhere else
    input_folder = Path("attachments")   # ← put your .asc files here
    output_folder = Path("output_data")
    output_folder.mkdir(exist_ok=True)

    files = {
        "BLUE_CT": input_folder / "Surface comparison BLUE CT.asc",
        "BLUE_HS": input_folder / "Surface comparison BLUE HS.asc",
        "DARK_GREY_CT": input_folder / "surface comparison dark grey ct.asc",
        "DARK_GREY_HS": input_folder / "Surface comparison DARK GREY HS.asc",
        "LIGHT_GREY_CT": input_folder / "Surface comparison LIGHT GREY CT.asc",
        "LIGHT_GREY_HS": input_folder / "Surface comparison LIGHT GREY HS.asc",
    }

    for name, filepath in files.items():
        if filepath.exists():
            print(f"Processing {name} ...")
            df = parse_asc_file(filepath)
            print(f"   → Found {len(df):,} points")
            
            if len(df) > 1_000_000:
                # Save big files as CSV
                df.to_csv(output_folder / f"{name}.csv", index=False)
                print(f"   → Saved as CSV (very large file)")
            else:
                df.to_excel(output_folder / f"{name}.xlsx", index=False)
                print(f"   → Saved as Excel")
        else:
            print(f"File not found: {filepath.name}")

    print("\n🎉 All done! Check the 'output_data' folder.")

if __name__ == "__main__":
    main()
