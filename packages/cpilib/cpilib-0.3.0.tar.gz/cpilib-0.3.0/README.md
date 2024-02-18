## **CPI-Lib**

Python Library to handle CPI data.

### **Installation**

```bash
pip install cpilib
```

### **Usage**

```python
from cpilib import HICP

# Will fetch new data if the data from cache (if any)
# is older than 1 week (time_limit in days)
hicp = HICP.from_cache(time_limit=7) 

# COICOP code
node = 'CP01'
# Country code
country = 'DE'

# DataFrame of the prices of the children of (node, country)
price_children = hicp.prices.children(node, country)

# DataFrame of the weights of the children of (node, country)
weight_children = hicp.weights.children(node, country)

# Series of the weights of (node, country)
total_weight = hicp.weights.node(node, country) # Yearly (int)
```