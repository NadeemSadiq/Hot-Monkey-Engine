# Hot-Monkey-Engine

Python pipelined webscraping library that revolves around handling JavaScript scraping alongside HTML scraping. This wraps around the selenium driver to give an easier to use framework for webscraping. This library handles each pipeline item as a 'map-reduce' like sequence where you can 'map' UI data into an object and 'reduce' the data from it. However, unlike other webscraping libraries, this handles the pipeline in a more functional approach which removes a lot of the boiler plate code and complexity you get from building classes in larger pipelines as well making it much easier for people to dive into this library.

## About this library

This library is designed to allow a pipeline to webscraping enforcing scraping logic to be separated from the core application logic. This allows integration with date from multiple sites/pages to be handled to return a list of objects which you can use at the other end without the need to merge together.

This library also tries to tackle pages where certain features are hidden behind JavaScript allowing more data to be accessed. This allows even more data to be accessed and allows even more access to automated webscraping without the need to know which URL endpoints to hit.

Lastly, this library  tries to tackle the ever changing nature of website UI. This library is designed to be able to identify such changes and allows you to resolve it quickly. Since this library is designed to be separated from the application logic, this means that.

## Installation

To Install the application,use the following pip command

```bash
pip instal hot-monkey-engine
```

Once installed, you can call it as shown in the example below which will simply count the unquie tags sent down:

```python
import hot-monkey-engine as hme

hme.config( browser = "$PathToHeadlessBrowser")

await hme.request('https://example.com')

unquie_tag_count = hme.scrape_elements() \
    .map(lambda tagname: (tagname, 1)) \
    .reduceBykey(lambda a, b: a + b)

print(unquie_tag_count)
```

## Configuration

pass

## Examples

pass

## Troubleshooting

pass
