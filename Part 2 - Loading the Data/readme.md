# Part 2 - Loading the Data
In this part, I generated data about the whisky restail shop, designed a Central RDBMS, applied normalization to the data and loaded it.

## Applying the code
1. Generate Random Data

```
python generate_store_data.py
```

2. Design the Database

- Current Schema:

![current_schema](https://user-images.githubusercontent.com/65648983/200842768-8f03b391-cea9-44bf-9296-26abadefccf8.png)


- Run this to design the data
```
python normalize_data.py
```

- Finished Schema:
![1 TJ76ouNmK-vH2-3P_GI9aQ](https://user-images.githubusercontent.com/65648983/200844488-806fc02c-6632-414b-a3ec-1853898f1818.png)

3. Load the Data to MySQL
```
Python load_data.py
```

## End Result
