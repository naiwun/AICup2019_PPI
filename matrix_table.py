import pandas as pd
import numpy as np


def calculate(source, target):
    source_df = pd.DataFrame(source,
                             columns=["PMID", "Sentence_ID", "Gene1|Gene1_ID", "Gene1_Index(start|end)",
                                      "Gene2|Gene2_ID", "Gene2_Index(start|end)", "RE_Type"])

    target_df = pd.DataFrame(target,
                             columns=["PMID", "Sentence_ID", "Gene1|Gene1_ID", "Gene1_Index(start|end)",
                                      "Gene2|Gene2_ID", "Gene2_Index(start|end)", "RE_Type"])

    column_list = target_df[target_df.columns[len(target_df.columns) - 1]].drop_duplicates()
    column_dict = dict(zip(column_list[::], column_list[::]))
    df = pd.DataFrame(np.zeros((21, 21)), columns=column_dict, index=column_dict, dtype=int)

    TP = 0
    FP = 0
    FN = 0
    for source_index, source_row in source_df.iterrows():
        for target_index, target_row in target_df.iterrows():
            if ((source_row['PMID'] == target_row['PMID']) and (
                    source_row['Sentence_ID'] == target_row['Sentence_ID']) and (
                    (source_row['Gene1|Gene1_ID'] == target_row['Gene1|Gene1_ID']) and (
                    source_row['Gene1_Index(start|end)'] == target_row['Gene1_Index(start|end)']) and (
                            source_row['Gene2|Gene2_ID'] == target_row['Gene2|Gene2_ID']) and (
                            source_row['Gene2_Index(start|end)'] == target_row['Gene2_Index(start|end)']) or (
                            source_row['Gene1|Gene1_ID'] == target_row['Gene2|Gene2_ID']) and (
                            source_row['Gene1_Index(start|end)'] == target_row['Gene2_Index(start|end)']) and (
                            source_row['Gene2|Gene2_ID'] == target_row['Gene1|Gene1_ID']) and (
                            source_row['Gene2_Index(start|end)'] == target_row['Gene1_Index(start|end)']))):

                if source_row['RE_Type'] == target_row['RE_Type']:
                    # Exact match with question and answer
                    TP += 1
                    df.xs(source_row['RE_Type'])[target_row['RE_Type']] = df.loc[source_row['RE_Type'], target_row[
                        'RE_Type']] + 1
                    break
                else:
                    # Partial match with question but not answer
                    if source_row['RE_Type'] == "NoRE":
                        FN += 1
                    else:
                        df.xs(source_row['RE_Type'])[target_row['RE_Type']] = df.loc[source_row['RE_Type'], target_row[
                            'RE_Type']] + 1
                        FP += 1
                    break

    print("TP: " + str(TP))
    print("FP: " + str(FP))
    print("FN: " + str(FN))
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1_score = 2 * ((precision * recall) / (precision + recall))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1-Score: " + str(F1_score))


def read_file(source, target):
    source_data = pd.read_csv(source, delimiter='\t', encoding='utf-8')
    target_data = pd.read_csv(target, delimiter='\t', encoding='utf-8')
    return source_data, target_data

source_data, target_data = read_file("./data/predict_3.tsv", "./data/gold.tsv")
calculate(source_data, target_data)
