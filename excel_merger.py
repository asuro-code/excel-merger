import pandas as pd
import os

# 対象フォルダ（同じディレクトリに "excel_files" フォルダを作っておく）
folder_path = "excel_files"
output_file = "merged_output.xlsx"

# 空のDataFrameで初期化
all_data = pd.DataFrame()

# フォルダ内のすべてのExcelファイルを結合
for file in os.listdir(folder_path):
    if file.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)

# 結合結果を出力
all_data.to_excel(output_file, index=False)
print(f"✅ 結合完了！ → {output_file}")
