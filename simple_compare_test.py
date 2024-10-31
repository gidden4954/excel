# 간단히 엑셀 파일을 저장해보는 코드
try:
    with pd.ExcelWriter(output_file_path) as writer:
        old_df.to_excel(writer, sheet_name='Original', index=False)
    print("Temporary Excel file saved successfully at", output_file_path)
except Exception as e:
    print("Error while saving Excel file:", e)
