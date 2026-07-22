# Python Data Loading Report

## Objective

Load the dataset into Python using Pandas and inspect its structure.

---

## Tasks Performed

- Loaded CSV file
- Displayed first five rows
- Checked dataset dimensions
- Listed column names
- Checked data types
- Checked missing values
- Checked duplicate rows
- Generated summary statistics

---

## Observations

### Dataset Shape

(5000, 12)

### Missing Values

order_id            0
order_date          0
customer_id         0
product_category    0
region              0
quantity            0
unit_price          0
discount            0
payment_method      0
delivery_days       0
customer_rating     0
revenue             0
dtype: int64

### Duplicate Rows

0


### Summary Statistics


order_id  customer_id     quantity   unit_price     discount  delivery_days  customer_rating      revenue
count   5000.000000  5000.000000  5000.000000  5000.000000  5000.000000    5000.000000      5000.000000  5000.000000
mean   12500.500000  1505.701200     4.044800   308.418774     0.179984       6.118800         2.973980  1021.955148
std     1443.520003   290.836902     2.020398   169.259369     0.101404       3.153264         1.157722   825.584219
min    10001.000000  1000.000000     1.000000    15.150000     0.000000       1.000000         1.000000    11.210000
25%    11250.750000  1253.000000     2.000000   161.895000     0.090000       3.000000         2.000000   354.527500
50%    12500.500000  1510.000000     4.000000   309.890000     0.180000       6.000000         3.000000   796.650000
75%    13750.250000  1761.000000     6.000000   455.557500     0.270000       9.000000         4.000000  1515.690000
max    15000.000000  1999.000000     7.000000   599.960000     0.350000      11.000000         5.000000  4119.330000

### Data Types

Data Types
order_id              int64
order_date              str
customer_id           int64
product_category        str
region                  str
quantity              int64
unit_price          float64
discount            float64
payment_method          str
delivery_days         int64
customer_rating     float64
revenue             float64
dtype: object


### Data columns (total 12 columns):


#   Column            Non-Null Count  Dtype  

---  ------            --------------  -----  
 0   order_id          5000 non-null   int64  
 1   order_date        5000 non-null   str    
 2   customer_id       5000 non-null   int64  
 3   product_category  5000 non-null   str    
 4   region            5000 non-null   str    
 5   quantity          5000 non-null   int64  
 6   unit_price        5000 non-null   float64
 7   discount          5000 non-null   float64
 8   payment_method    5000 non-null   str    
 9   delivery_days     5000 non-null   int64  
 10  customer_rating   5000 non-null   float64
 11  revenue           5000 non-null   float64
dtypes: float64(4), int64(4), str(4)

---

## Conclusion

The dataset was successfully loaded and inspected. It is ready for data cleaning.