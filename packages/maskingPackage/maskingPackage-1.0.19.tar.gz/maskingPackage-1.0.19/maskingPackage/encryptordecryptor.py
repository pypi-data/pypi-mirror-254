import pandas as pd
from cryptography.fernet import Fernet
import json
from pyspark.sql.types import StringType
from pyspark.sql.functions import col, udf
from pyspark.sql import functions as F
import re



class DataEncryptorDecryptor:
    def __init__(self, decryptionkey,data,generated_json):
        self.decryptionkey = decryptionkey
        self.data = data
        self.generated_json = generated_json

    def encrypt_data(self):
        data1 = self.data
        if  isinstance(data1, pd.DataFrame):
            data = data1
        else:
            data = data1.toPandas()
        key = self.decryptionkey
        init_result = self.generated_json
        cipher_suite = Fernet(key)
        sensitive_columns = []
        masking_functions = {}

        for column_info in init_result["content"]:
            if column_info["sensitivity"] == 1:
                column_name = column_info["columnName"]
                masking_function = column_info["function"]
                sensitive_columns.append(column_name)
                masking_functions[column_name] = masking_function
        if sensitive_columns:
            for column in sensitive_columns:
                # data[column] = data[column].apply(lambda x: cipher_suite.encrypt(x.encode()).decode())
                data[column] = data[column].apply(lambda x: cipher_suite.encrypt(str(x).encode()).decode() if isinstance(x, (str, int, float)) else x)
            result_df = data
        else:
            result_df = data.copy()
        return result_df# This function is designed for Pandas DataFrames; it requires the data to be in that format for processing
    def decrypt_data(self, sensitive_columns, dataset):
        # dataset = pd.read_csv(masked_encrypted_csv_path, low_memory=False)

        decryption_key = self.decryptionkey
        if decryption_key:
            cipher_suite = Fernet(decryption_key)
            for sensitive_column in sensitive_columns:
                dataset[sensitive_column] = dataset[sensitive_column].apply(
                    lambda x: cipher_suite.decrypt(x.encode()).decode()
                )
        else:
            print("Decryption key not valid")

        return dataset
# masks the data
    def masking_all_column(self, encrypted_dataset):
        init_result= self.generated_json
        def mask_column_with_function(pd_column, function):
            exec(function, globals())
            masked_column = pd_column.apply(maskInfo)
            return masked_column

        # init_result = self.generated_json
        maskeddata = encrypted_dataset.copy()

        for col_info in init_result['content']:
            col_name = col_info['columnName']
            if col_info.get('sensitivity') == 1:
                print(f"Applying masking to sensitive column: {col_name}...")
                maskeddata[col_name] = mask_column_with_function(maskeddata[col_name], col_info['function'])
            else:
                print(f"Skipping non-sensitive column: {col_name}")

        return maskeddata
# This handles both encryption and masking logic together 
    def encryption_masking(self):
        data1 = self.data
        if  isinstance(data1, pd.DataFrame):
            data = data1
        else:
            data = data1.toPandas()

        def mask_column_with_function(pd_column, function):
            exec(function, globals())
            # masked_column = pd_column.apply(maskInfo)
            masked_column = pd_column.astype(str).apply(maskInfo)
            # masked_column = pd_column.apply(lambda x: maskInfo(x))
            return masked_column
        key = self.decryptionkey
        cipher_suite = Fernet(key)
        init_result = self.generated_json
        sensitive_columns = []
        masking_functions = {}

        for column_info in init_result["content"]:
            if column_info["sensitivity"] == 1:
                column_name = column_info["columnName"]
                masking_function = column_info["function"]
                sensitive_columns.append(column_name)
                masking_functions[column_name] = masking_function
            
        if sensitive_columns:
            key = self.decryptionkey
            for column in sensitive_columns:
                new_column_name = f"{column}_encrypted"
                cipher_suite = Fernet(key)
                data[new_column_name] = data[column].apply(lambda x: cipher_suite.encrypt(str(x).encode()).decode() if isinstance(x, (str, int, float)) else x)
                duplicate_mask = data[column_name].notna()  
                duplicated_rows = data[duplicate_mask]
                duplicated_df = pd.concat([data, duplicated_rows], ignore_index=True)
                
                result_df = pd.concat([data, duplicated_df], ignore_index=True)
                maskeddata = result_df
                for col_info in init_result['content']:
                    col_name = col_info['columnName']
                    
                    if col_info.get('sensitivity') == 1:          
                        maskeddata[col_name] = mask_column_with_function(maskeddata[col_name],col_info['function'])          
                    else:
                        pass
            maskeddata.sort_index(axis=1, inplace=True)
            # maskeddata = spark.createDataFrame(maskeddata)
            return maskeddata
    def decryption(self,sensitive_columns,dataset):
        for sensitive_column in sensitive_columns:
            decryption_key = self.decryptionkey
            if decryption_key:
                cipher_suite = Fernet(decryption_key)

                # Define a UDF for decryption
                def decrypt_udf(value):
                    if value is not None:
                        return cipher_suite.decrypt(value.encode()).decode()
                    else:
                        return None

                dataset = dataset.withColumn(
                    sensitive_column,
                    F.udf(decrypt_udf, StringType())(dataset[sensitive_column])
                )
            else:
                print("Decryption key not valid")
        for column in dataset.columns:
            if column.endswith('_encrypted') and column in sensitive_columns:
                    new_column_name = column.replace('_encrypted', '_decrypted')
                    dataset = dataset.withColumnRenamed(column,new_column_name)
        return dataset
            # for sensitive_column in sensitive_columns:
            #     decryption_key = self.decryptionkey
            #     if decryption_key:
            #         cipher_suite = Fernet(decryption_key)

            #         # Define a UDF for decryption
            #         def decrypt_udf(value):
            #             if value is not None:
            #                 return cipher_suite.decrypt(value.encode()).decode()
            #             else:
            #                 return None
            #         dataset = dataset.withColumn(
            #             sensitive_column,
            #             F.udf(decrypt_udf, StringType())(dataset[sensitive_column])
            #         )
            #     else:
            #         print("Decryption key not valid")
            # for columnrename in dataset:
                
            # return dataset

