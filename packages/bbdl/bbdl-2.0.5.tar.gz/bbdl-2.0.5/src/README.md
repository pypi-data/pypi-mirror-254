# BBDL

Downloads BB Newspaper for offline reading.

## Usage

Can be used after importing

```py
from bbdl import BBDL
```

Then init an object and get a target date.

```py
app = BBDL()
year = "2023"
month = "09"
day = "18"
```

We need to identify how many pages the news has covered for that day.

```py
app.max_page_check(year, month, day)
```

This would store the value in the app object as `max_pages`

```py
print(app.max_pages) # E.g. 31
```

Lastly, call `bb_dl_full()` function. Set `download=False` to not download the pages. The pages will be stored in `data/BB-<YEAR><MONTH><DAY>` folder if `download=True` (default)

To view a list of image URLs it downloaded from, check its attribute `list_of_urls`

```py
print(app.list_of_urls)
```
