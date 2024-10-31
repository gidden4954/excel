import pandas as pd
from tkinter import Tk, filedialog
import os

def compare_excel_files(old_file_path, new_file_path, output_file_path):
    # Load the old and new Excel files
    old_df = pd.read_excel(old_file_path)
    new_df = pd.read_excel(new_file_path)

    # Check if both files have the same structure
    if old_df.shape != new_df.shape:
        print("Files have different shapes. Comparison may not be valid.")
        return

    # Compare values
    comparison_df = old_df == new_df
    differences = old_df[~comparison_df]

    # Create a result file showing mismatches
    result_df = old_df.copy()
    result_df['Match'] = comparison_df.all(axis=1)

        # Debugging: Print output file path
    print("Output file will be saved at:", output_file_path)
    
    with pd.ExcelWriter(output_file_path) as writer:
        result_df.to_excel(writer, sheet_name='Comparison_Results', index=False)
        differences.to_excel(writer, sheet_name='Differences', index=False)

    print("Comparison complete. Results saved in", output_file_path)

def main():
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Prompt the user to select the old and new Excel files
    print("Select the old version Excel file")
    old_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    
    print("Select the new version Excel file")
    new_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])

    if not old_file_path or not new_file_path:
        print("Both files need to be selected.")
        return

    # Prompt the user to choose a location and name for the output file
    print("Choose a location to save the comparison result")
    output_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                    filetypes=[("Excel files", "*.xlsx")],
                                                    initialfile="comparison_result.xlsx")

    if not output_file_path:
        print("Output file path was not specified.")
        return

    # Run the comparison
    compare_excel_files(old_file_path, new_file_path, output_file_path)

 #예외 처리 추가 부분
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
