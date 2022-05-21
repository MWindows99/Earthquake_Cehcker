# Earthquake Cehcker
A Simple Python library to get the latest earthquake information.

### Acknowledgement
This library uses this API.

[p2pquake.net](https://p2pquake.net)

## Introduction
✅ You can easily get the latest one earthquake information in this library.<br>
✅ An internet connection is required to use this library.<br>
⚠️ This library is currently **ONLY** available in Japanese.

## Object
This library returns **dictionary** object.

 - ```status``` : success / error
 - ```point``` : Epicenter
 - ```time``` : Date and time of the earthquake
 - ```magnitude``` : The magnitude of the earthquake
 - ```scale``` : Maximum seismic intensity
 - ```tsunami``` : Tsunami information

**[Cause of Error]**
 - API Error
 - Connection timeout, etc.

### Object Example
```
{'point': '石川県能登地方', 'time': '2022/05/20 20:14:00', 'magnitude': '2', 'scale': '1.0', 'tsunami': 'この地震による、津波の心配はありません。'}
```

## Usage
This library requires a ```requests``` library. Please install it first.
```shell
pip install requests
```

***You can get earthquake data just by calling a function.***

1. Import this library.
2. Call the ```earthquake``` function.
3. Object returned.

### Code Example
```python
from earthquake import earthquake

result = earthquake()
print(result)
```
